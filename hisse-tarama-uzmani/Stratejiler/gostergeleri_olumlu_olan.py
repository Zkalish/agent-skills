import pandas as pd
import pandas_ta as ta
import os
import warnings
import concurrent.futures
from datetime import datetime

# Uyarıları gizle
warnings.simplefilter(action='ignore')

# =============================================================================
# AYARLAR
# =============================================================================
STRATEJI_ADI = "GOO"

# --- ZAMAN AYARI ---
# -1: Dosyadaki EN SON SATIR
# -2: Sondan bir önceki
ANALIZ_GUNU_INDEKSI = -1 

# --- HIZ AYARI ---
MAX_ISLEM_SAYISI = 50 

# --- YOL AYARLARI ---
MEVCUT_YOL = os.path.dirname(os.path.abspath(__file__))
ANA_KLASOR = os.path.dirname(MEVCUT_YOL) 

if os.path.exists(os.path.join(ANA_KLASOR, "Hisse_Verileri")):
    VERI_KLASORU = os.path.join(ANA_KLASOR, "Hisse_Verileri")
    DOSYA_ADI = os.path.join(ANA_KLASOR, "Sinyal_Takip_Defteri.xlsx")
else:
    VERI_KLASORU = "Hisse_Verileri"
    DOSYA_ADI = "Sinyal_Takip_Defteri.xlsx"

# -----------------------------------------------------------------------------
# 🔍 ARASE DEDEKTÖRÜ (ÖZEL DEBUG - DÜZELTİLDİ)
# -----------------------------------------------------------------------------
def arase_kontrol():
    try:
        path = os.path.join(VERI_KLASORU, "ARASE.csv")
        if not os.path.exists(path):
            # print("\n🕵️ ARASE DEDEKTÖRÜ: ARASE.csv dosyası BULUNAMADI!")
            return

        df = pd.read_csv(path)
        # print(f"\n🕵️ ARASE DEDEKTÖRÜ: Dosya Okundu. Toplam Satır: {len(df)}")
        
        # Tarih Sütunu
        date_col = 'Date' if 'Date' in df.columns else 'Tarih'
        # last_date = df[date_col].iloc[-1]
        
    except Exception as e:
        print(f"🕵️ ARASE DEDEKTÖRÜ HATA: {e}")

# -----------------------------------------------------------------------------

def hisseleri_al():
    hisseler = []
    if not os.path.exists(VERI_KLASORU):
        return []
    dosyalar = os.listdir(VERI_KLASORU)
    for dosya in dosyalar:
        if dosya.endswith(".csv"):
            hisseler.append(dosya) 
    return sorted(hisseler)

def teknik_analiz(dosya_adi):
    try:
        dosya_yolu = os.path.join(VERI_KLASORU, dosya_adi)
        hisse_adi = dosya_adi.replace(".csv", "").replace(".IS", "")
        
        df = pd.read_csv(dosya_yolu)
        if df.empty or len(df) < 205: return None
        
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
        elif 'Tarih' in df.columns:
            df['Tarih'] = pd.to_datetime(df['Tarih'])
            df.set_index('Tarih', inplace=True)

        # --- İNDİKATÖRLER ---
        df['EMA_20'] = df.ta.ema(length=20)
        df['EMA_50'] = df.ta.ema(length=50)
        df['EMA_200'] = df.ta.ema(length=200)
        df['HMA_9'] = df.ta.hma(length=9)
        
        psar = df.ta.psar()
        df['SAR'] = psar.iloc[:, 0].ffill() if psar is not None else 0

        ichi = df.ta.ichimoku(tenkan=9, kijun=26, senkou=52)
        df['TENKAN'] = ichi[0].iloc[:, 0] if ichi is not None else 0

        df['RSI'] = df.ta.rsi(length=14)

        adx = df.ta.adx(length=14)
        if adx is not None:
            df['ADX'] = adx['ADX_14']; df['DMP'] = adx['DMP_14']; df['DMN'] = adx['DMN_14']
        else:
            df['ADX'] = 0

        macd = df.ta.macd(fast=12, slow=26, signal=9)
        if macd is not None:
            df['MACD'] = macd['MACD_12_26_9']; df['MACD_SIGNAL'] = macd['MACDs_12_26_9']
        else:
            df['MACD'] = 0

        stochrsi = df.ta.stochrsi(length=14, rsi_length=14, k=3, d=3)
        if stochrsi is not None:
            df['Srsi_K'] = stochrsi['STOCHRSIk_14_14_3_3']; df['Srsi_D'] = stochrsi['STOCHRSId_14_14_3_3']
        else:
            df['Srsi_K'] = 0

        df['MFI'] = df.ta.mfi(length=14)
        df['CMF'] = df.ta.cmf(length=20)

        vol_sma = df['Volume'].rolling(window=14).mean()
        df['RelVol'] = df['Volume'] / vol_sma

        # --- SEÇİLEN GÜN ---
        idx = ANALIZ_GUNU_INDEKSI
        son = df.iloc[idx]
        close_now = son['Close']
        try: sinyal_tarihi = df.index[idx].strftime('%Y-%m-%d')
        except: sinyal_tarihi = datetime.now().strftime('%Y-%m-%d')
        
        degisim_hafta = ((close_now - df['Close'].iloc[idx-6]) / df['Close'].iloc[idx-6]) * 100
        degisim_gun = ((close_now - df['Close'].iloc[idx-1]) / df['Close'].iloc[idx-1]) * 100

        # --- FİLTRELER ---
        if not (degisim_hafta < 15): return None
        if not (degisim_gun < 9.5):  return None
        if not (son['RelVol'] > 1):  return None

        if not (close_now > son['EMA_20']):  return None
        if not (close_now > son['EMA_50']):  return None
        if not (close_now > son['EMA_200']): return None
        if not (close_now > son['HMA_9']):   return None
        if not (son['SAR'] < close_now):     return None
        if not (close_now > son['TENKAN']):  return None

        if not (son['RSI'] > 50):        return None
        if not (son['ADX'] > 25):        return None
        if not (son['DMP'] > son['DMN']):return None
        if not (son['MACD'] > son['MACD_SIGNAL']): return None
        if not (son['Srsi_K'] > son['Srsi_D']): return None

        if not (son['MFI'] > 50):  return None
        if not (son['CMF'] > 0.2): return None

        return {
            'Tarih': sinyal_tarihi,
            'Strateji': STRATEJI_ADI,
            'Hisse': hisse_adi,
            'Giris_Fiyati': round(close_now, 2),
            'Durum': 'Aktif',
            'Detay': f"RSI:{son['RSI']:.0f} CMF:{son['CMF']:.2f}"
        }

    except Exception:
        return None

def excel_yaz(yeni_sinyaller):
    if not yeni_sinyaller: return
    print(f"\n💾 {len(yeni_sinyaller)} adet GOO sinyali KAYDEDİLİYOR...")
    
    try:
        df_mevcut = pd.read_excel(DOSYA_ADI, sheet_name='Sinyaller')
    except:
        df_mevcut = pd.DataFrame(columns=['Tarih', 'Strateji', 'Hisse', 'Giris_Fiyati', 'Durum'])

    kayit_listesi = [{k: v for k, v in s.items() if k != 'Detay'} for s in yeni_sinyaller]
    df_yeni = pd.DataFrame(kayit_listesi)
    
    df_tum = pd.concat([df_mevcut, df_yeni], ignore_index=True)
    df_tum.drop_duplicates(subset=['Tarih', 'Strateji', 'Hisse'], keep='last', inplace=True)

    with pd.ExcelWriter(DOSYA_ADI, engine='xlsxwriter') as writer:
        df_tum.to_excel(writer, sheet_name='Sinyaller', index=False)
    
    print("✅ Sinyaller ana veritabanına eklendi.")

def taramayi_baslat():
    # HATA DÜZELTME: arase_kontrol fonksiyonunun tanımlı olduğundan emin olunduktan sonra açıldı.
    arase_kontrol()
    
    dosyalar = hisseleri_al()
    print(f"🚀 {STRATEJI_ADI} Taraması Başlıyor ({len(dosyalar)} Dosya)...")
    
    sonuclar = []
    tamamlanan = 0
    toplam = len(dosyalar)

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_ISLEM_SAYISI) as executor:
        gelecek_islemler = {executor.submit(teknik_analiz, d): d for d in dosyalar}
        
        for future in concurrent.futures.as_completed(gelecek_islemler):
            try:
                sonuc = future.result()
                tamamlanan += 1
                if tamamlanan % 50 == 0:
                    print(f"\r⏳ İlerleme: %{int(tamamlanan/toplam*100)}", end="")

                if isinstance(sonuc, dict):
                    print(f"\n✅ BULUNDU: {sonuc['Hisse']} ({sonuc['Tarih']}) - {sonuc['Detay']}")
                    sonuclar.append(sonuc)
            except:
                pass
            
    print(f"\n🏁 Tarama Bitti.")
    return sonuclar

# --- BIST CEO BURAYI ÇAĞIRIR (EXCEL'E YAZAR) ---
def bist_ceo_calistir():
    sonuclar = taramayi_baslat()
    if sonuclar: 
        excel_yaz(sonuclar)
    else: 
        print("❌ Sonuç Yok.")

# --- MANUEL TEST MODU (EXCEL'E YAZMAZ - SADECE EKRANA BASAR) ---
if __name__ == "__main__":
    print(f"\n🧪 TEST MODU: {STRATEJI_ADI} (Excel'e Yazma KAPALI)\n" + "="*60)
    
    bulunanlar = taramayi_baslat()
    
    if bulunanlar:
        print(f"\n✨ TOPLAM {len(bulunanlar)} HİSSE BULUNDU (KAYDEDİLMEDİ):")
        for s in bulunanlar:
            print(f"   👉 {s['Hisse']} - Fiyat: {s['Giris_Fiyati']} - {s['Detay']}")
    else:
        print("\n❌ Sonuç Yok.")
    
    print("\n" + "="*60 + "\n(Not: Kaydetmek için Bist_Ceo üzerinden çalıştırın.)")