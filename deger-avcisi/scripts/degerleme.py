import requests
import pandas as pd
import math
import datetime
import yfinance as yf
import json
import os
from openpyxl.styles import Alignment, PatternFill, Font

# ==============================================================================
# ⚙️ AYARLAR
# ==============================================================================
KRITERLER = {
    "MAX_SERMAYE_LOT": 600_000_000,
    "MIN_ROE": 25,
    "MAX_PD_DD": 2.50,          
    "RSI_SINIR": 65,
    "RSI_UYARI": 60,
    "MAX_LYNCH_BUYUME": 45,
    "GRAHAM_CARPAN": 22.5,
    "MAX_FORMUL_ROE": 100,
    
    "UYARI_PD_DD": 5.00,        
    "VETO_PD_DD": 10.00,        
    "MIN_GRAHAM_POT": 30        
}

COLUMNS = [
    "name", "close", "price_book_ratio", "price_earnings_ttm",
    "return_on_equity_fq", "debt_to_equity_fq", "RSI",
    "earnings_per_share_basic_ttm", "book_value_per_share_fq",
    "total_shares_outstanding_current", "net_income_ttm"
]

print(f"🚀 BIST Yönetim Paneli V33 (Terminoloji Birliği) Çalıştırılıyor... ({datetime.datetime.now().strftime('%H:%M:%S')})")

# ==============================================================================
# 1. VERİ ÇEKME
# ==============================================================================
url = "https://scanner.tradingview.com/turkey/scan"
payload = {
    "filter": [{"left": "exchange", "operation": "equal", "right": "BIST"}],
    "options": {"lang": "tr"},
    "symbols": {"query": {"types": []}, "tickers": []},
    "columns": COLUMNS,
    "sort": {"sortBy": "name", "sortOrder": "asc"},
    "range": [0, 1000]
}
headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data_json = response.json()
    clean_data = []
    for item in data_json['data']:
        clean_data.append(dict(zip(COLUMNS, item['d'])))
    df = pd.DataFrame(clean_data)
    
    df = df.rename(columns={
        'name': 'Hisse', 'close': 'Fiyat', 'price_book_ratio': 'PD/DD',
        'return_on_equity_fq': 'ROE %', 'debt_to_equity_fq': 'Borç/Öz',
        'RSI': 'RSI', 'earnings_per_share_basic_ttm': 'EPS',
        'book_value_per_share_fq': 'Defter Degeri',
        'total_shares_outstanding_current': 'Sermaye', 'net_income_ttm': 'Net Kar'
    })
    print(f"✅ TradingView'dan {len(df)} hisse çekildi. Analiz Başlıyor...\n")

except Exception as e:
    print(f"❌ Ana Veri Hatası: {e}")
    exit()

# ==============================================================================
# 2. HESAPLAMA MOTORU
# ==============================================================================
def yfinance_ile_tamamla(hisse_kodu):
    try:
        ticker = yf.Ticker(f"{hisse_kodu}.IS")
        info = ticker.info 
        fiyat = info.get('currentPrice', 0)
        yf_eps = info.get('trailingEps', 0)
        yf_dd = info.get('bookValue', 0)
        yf_roe = info.get('returnOnEquity', 0)

        if (yf_eps is None or yf_eps == 0) and fiyat > 0:
            fk = info.get('trailingPE', 0)
            if fk: yf_eps = fiyat / fk
        
        if (yf_dd is None or yf_dd == 0) and fiyat > 0:
            pddd = info.get('priceToBook', 0)
            if pddd: yf_dd = fiyat / pddd

        if yf_roe: yf_roe = yf_roe * 100
        return yf_eps, yf_dd, yf_roe
    except: return 0, 0, 0

list_firsatlar = []
list_buyukler = []
list_pahali = []
list_digerleri = [] 

print("⏳ Veriler işleniyor, TERA ve CCOLA etiketleri uyumlu hale getiriliyor...")

for index, row in df.iterrows():
    sermaye = row['Sermaye'] if row['Sermaye'] is not None else 999_999_999_999
    pd_dd = row['PD/DD'] if row['PD/DD'] is not None else 999
    rsi = row['RSI'] if row['RSI'] is not None else 100
    fiyat = row['Fiyat']
    borc = row['Borç/Öz'] if row['Borç/Öz'] is not None else 999
    
    eps = row['EPS'] if row['EPS'] is not None else 0
    dd = row['Defter Degeri'] if row['Defter Degeri'] is not None else 0
    roe = row['ROE %'] if row['ROE %'] is not None else 0

    if (eps == 0 or dd == 0) and fiyat > 0:
        yf_eps, yf_dd, yf_roe = yfinance_ile_tamamla(row['Hisse'])
        if yf_eps != 0: eps = yf_eps
        if yf_dd != 0: dd = yf_dd
        if yf_roe != 0 and roe == 0: roe = yf_roe

    graham_deger = 0
    lynch_deger = 0
    ort_deger = 0
    dd_hedef = dd
    durum_notu = "" 

    if eps > 0:
        try:
            if dd > 0: graham_deger = math.sqrt(KRITERLER["GRAHAM_CARPAN"] * eps * dd)
        except: pass
        try:
            if roe > 0:
                hesap_roe = min(roe, KRITERLER["MAX_FORMUL_ROE"])
                efektif_buyume = min(hesap_roe, KRITERLER["MAX_LYNCH_BUYUME"])
                lynch_deger = eps * efektif_buyume
        except: pass
        
        bilesenler = [d for d in [graham_deger, lynch_deger, dd_hedef] if d > 0]
        if bilesenler:
            ort_deger = sum(bilesenler) / len(bilesenler)
    else:
        durum_notu = "⚠️ ZARAR AÇIKLADI"
        ort_deger = dd_hedef

    # Potansiyel Hesapla
    def pot_hesapla(hedef, fiyat):
        return ((hedef - fiyat) / fiyat) * 100 if fiyat > 0 and hedef > 0 else 0

    dd_pot = pot_hesapla(dd_hedef, fiyat)
    graham_pot = pot_hesapla(graham_deger, fiyat)
    ort_pot = pot_hesapla(ort_deger, fiyat)
    lynch_pot = pot_hesapla(lynch_deger, fiyat)

    # --- SİNYAL SİSTEMİ (V33 - DÜZELTİLMİŞ) ---
    sinyal_notu = ""
    veto_yedi = False
    
    # 1. ZARAR KONTROLÜ
    if eps < 0:
        sinyal_notu = "⚠️ ZARAR (İzleme)"
        veto_yedi = True

    # 2. BALON KONTROLÜ (PD/DD > 10)
    elif pd_dd > KRITERLER["VETO_PD_DD"]:
        if graham_pot > 0:
            # TERA BURAYA DÜŞER: Graham +10% (Pozitif), ama PD/DD 100
            # Eski: "MAKUL - AŞIRI PD/DD"
            sinyal_notu = "🟠 BÜYÜME ODAKLI - 🚫 AŞIRI PD/DD"
        else:
            sinyal_notu = f"🚫 BALON RİSKİ"
        veto_yedi = True
    
    # 3. YÜKSEK PRİM (5 < PD/DD < 10)
    elif pd_dd > KRITERLER["UYARI_PD_DD"]:
        if graham_pot > 0:
            if ort_pot > 50:
                sinyal_notu = "🟢 UCUZ - ⚠️ YÜKSEK PD/DD"
            else:
                sinyal_notu = "🟠 BÜYÜME ODAKLI - ⚠️ YÜKSEK PD/DD" # Makul yerine Büyüme Odaklı
        else:
            sinyal_notu = "🟠 YÜKSEK PRİMLİ"
        veto_yedi = True 

    # 4. NORMAL DEĞERLEME (Veto yok)
    if not veto_yedi:
        if ort_pot > 200:
            if graham_pot < KRITERLER["MIN_GRAHAM_POT"]: 
                sinyal_notu = "🟠 PRİMLİ (BÜYÜME ODAKLI)"
            else:
                sinyal_notu = "💎 ÇOK UCUZ"
        
        elif ort_pot > 50:
            if graham_pot < KRITERLER["MIN_GRAHAM_POT"]: 
                sinyal_notu = "🟠 PRİMLİ (BÜYÜME ODAKLI)"
            else:
                sinyal_notu = "🟢 UCUZ"
        
        elif ort_pot >= -10:
            # CCOLA BURAYA DÜŞER: Ort Pot > 0 ama Graham Pot < 0
            if graham_pot < 0:
                 sinyal_notu = "🟠 PRİMLİ (BÜYÜME ODAKLI)"
            else:
                 sinyal_notu = "⚪ MAKUL (EDERİNDE)"

        elif ort_pot >= -40:
            sinyal_notu = "🟠 PAHALI"
        else:
            sinyal_notu = "🔴 ÇOK PAHALI"

    veri_satiri = {
        "Hisse": row['Hisse'],
        "Fiyat": row['Fiyat'],
        "Sinyal": sinyal_notu,
        "DD Hedef": round(dd_hedef, 2),
        "DD Pot.%": round(dd_pot, 0),
        "G.Hedef": round(graham_deger, 2),
        "G.Pot.%": round(graham_pot, 0),
        "L.Hedef": round(lynch_deger, 2),
        "L.Pot.%": round(lynch_pot, 0),
        "Ort.Hedef": round(ort_deger, 2),
        "Ort.Pot.%": round(ort_pot, 0),
        "ROE %": round(roe, 1),
        "PD/DD": round(pd_dd, 2),
        "RSI": round(rsi, 0),
        "Sermaye (M)": round(sermaye / 1_000_000, 1),
        "Özel Not": durum_notu,
        "Ham_Ort_Pot": ort_pot
    }

    if graham_deger > 0 and fiyat > (graham_deger * 1.20):
        veri_satiri["Aşırı Fiyat %"] = round(((fiyat - graham_deger) / graham_deger) * 100, 0)
        list_pahali.append(veri_satiri)

    if sermaye > KRITERLER["MAX_SERMAYE_LOT"]:
        list_buyukler.append(veri_satiri)
        continue 

    puan = 0
    notlar = []
    if eps < 0: notlar.append("ZARAR")
    else:
        if roe >= KRITERLER["MIN_ROE"]: puan += 1
        else: notlar.append(f"Düşük ROE (%{roe:.1f})")
        if pd_dd <= KRITERLER["MAX_PD_DD"]: puan += 1
        else: notlar.append(f"Yüksek PD/DD ({pd_dd:.2f})")
    if rsi <= KRITERLER["RSI_UYARI"]: puan += 1
    elif rsi <= KRITERLER["RSI_SINIR"]:
        puan += 1
        notlar.append("RSI Sınırda")
    else: notlar.append(f"RSI Şişik ({rsi:.0f})")
    if borc < 1: puan += 1
    
    if puan >= 2 and eps > 0:
        row_firsat = veri_satiri.copy()
        row_firsat["Durum"] = "⭐ TAM UYUM" if not notlar else "⚠️ " + ", ".join(notlar)
        row_firsat["Oncelik"] = 0 if not notlar else 1
        list_firsatlar.append(row_firsat)
    else:
        row_diger = veri_satiri.copy()
        if not notlar: notlar.append("Yetersiz Puan")
        row_diger["Elenme Nedeni"] = ", ".join(notlar)
        list_digerleri.append(row_diger)

# ==============================================================================
# 3. BİLGİ VE AYARLAR
# ==============================================================================
bilgi_verileri = []
try:
    with open('bilgi_notlari.json', 'r', encoding='utf-8') as f:
        bilgi_verileri = json.load(f)
    print("✅ 'bilgi_notlari.json' dosyası okundu.")
except FileNotFoundError:
    print("⚠️ UYARI: 'bilgi_notlari.json' bulunamadı.")

bilgi_verileri.append({"Konu": "----------------", "Açıklama": "--------------------------------"})
bilgi_verileri.append({"Konu": "YENİ SİNYAL: BÜYÜME ODAKLI", "Açıklama": "Fiyatı, Graham'a (Varlık) göre primli ama Lynch'e (Büyüme) göre ucuz."})
bilgi_verileri.append({"Konu": "GÜNCEL FİLTRELER", "Açıklama": "Otomatik Rapor"})
bilgi_verileri.append({"Konu": " SERMAYE", "Açıklama": f"Max {KRITERLER['MAX_SERMAYE_LOT']/1_000_000:.0f} Milyon Lot"})
bilgi_verileri.append({"Konu": " KARLILIK", "Açıklama": f"Min %{KRITERLER['MIN_ROE']}"})
bilgi_verileri.append({"Konu": " UCUZLUK", "Açıklama": f"Max {KRITERLER['MAX_PD_DD']}"})
bilgi_verileri.append({"Konu": "TARİH", "Açıklama": datetime.datetime.now().strftime("%d.%m.%Y %H:%M")})

# ==============================================================================
# 4. EXCEL ÇIKTISI
# ==============================================================================
dosya_adi = f"Borsaci_Dede_Panel_V33_{datetime.datetime.now().strftime('%Y%m%d')}.xlsx"

df_firsat = pd.DataFrame(list_firsatlar)
df_buyuk = pd.DataFrame(list_buyukler)
df_pahali = pd.DataFrame(list_pahali)
df_diger = pd.DataFrame(list_digerleri)
df_bilgi = pd.DataFrame(bilgi_verileri)

if not df_firsat.empty:
    df_firsat = df_firsat.sort_values(by=['Oncelik', 'Ham_Ort_Pot'], ascending=[True, False]).drop(columns=['Oncelik', 'Ham_Ort_Pot'])
if not df_buyuk.empty:
    df_buyuk = df_buyuk.sort_values(by='Ham_Ort_Pot', ascending=False).drop(columns=['Ham_Ort_Pot'])
if not df_pahali.empty:
    df_pahali = df_pahali.sort_values(by='Hisse', ascending=True).drop(columns=['Ham_Ort_Pot'])
if not df_diger.empty:
    df_diger = df_diger.sort_values(by='Hisse', ascending=True).drop(columns=['Ham_Ort_Pot'])

turuncu_dolgu = PatternFill(start_color='FFC000', end_color='FFC000', fill_type='solid')

try:
    with pd.ExcelWriter(dosya_adi, engine='openpyxl') as writer:
        if not df_firsat.empty: df_firsat.to_excel(writer, index=False, sheet_name='FIRSATLAR')
        if not df_buyuk.empty: df_buyuk.to_excel(writer, index=False, sheet_name='BUYUK_SIRKETLER')
        if not df_diger.empty: df_diger.to_excel(writer, index=False, sheet_name='DIGERLERI_IZLEME')
        if not df_pahali.empty: df_pahali.to_excel(writer, index=False, sheet_name='G.PAHALI_RISKLI')
        df_bilgi.to_excel(writer, index=False, sheet_name='BILGI_VE_AYARLAR')
        
        for sheetname in writer.sheets:
            worksheet = writer.sheets[sheetname]
            for col in worksheet.columns:
                max_length = 0
                column_letter = col[0].column_letter
                header_val = str(col[0].value) if col[0].value else ""
                
                is_percentage_col = "%" in header_val
                is_dd_pot_col = header_val == "DD Pot.%"
                
                for cell in col:
                    if is_percentage_col and isinstance(cell.value, (int, float)):
                        cell.number_format = '#,##0 "%"'
                        cell.alignment = Alignment(horizontal='right')
                    
                    if sheetname == 'DIGERLERI_IZLEME' and is_dd_pot_col:
                        if isinstance(cell.value, (int, float)) and cell.value < 0:
                            cell.fill = turuncu_dolgu

                    try:
                        if len(str(cell.value)) > max_length: max_length = len(str(cell.value))
                    except: pass
                
                worksheet.column_dimensions[column_letter].width = (max_length + 3)

    print("="*100)
    print(f"🎉 V33 PANEL HAZIR! (Terminoloji Tamamlandı)")
    print(f"📂 Dosya: {dosya_adi}")
    print("="*100)

except Exception as e:
    print(f"❌ Kayıt Hatası: {e}")