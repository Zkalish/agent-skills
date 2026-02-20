from tradingview_screener import Query, Column
import pandas as pd

def taramayi_calistir():
    # Sütun İsimleri
    cols = [
        'name', 'close', 'change', 'volume', 'typespecs', 'market_cap_basic',
        'relative_volume_10d_calc', 'change|1W', 
        'ADX', 'P.SAR'
    ]

    # Sorgu
    qry = Query().set_markets('turkey')\
                 .select(*cols)\
                 .where(
                     # --- ANAYASA: GÜVENLİK DUVARLARI ---
                     Column('market_cap_basic') > 1200000000,
                     Column('volume') > 5000,

                     # --- GÖRSELDEKİ FİLTRELER ---
                     Column('change') < 9.5,                    # Tavan olmayan
                     Column('change|1W') < 10,                  # Haftalıkta şişmemiş
                     
                     # 1. GÜÇLÜ HACİM (Rel Vol > 1.8)
                     # Görselde 1.8 seçili, bu oldukça yüksek bir oran.
                     Column('relative_volume_10d_calc') > 1.8, 

                     # 2. TREND VAR (ADX > 20)
                     Column('ADX') > 20,      

                     # 3. DÖNÜŞ SİNYALİ (Fiyat P.SAR'ı YUKARI Kesiyor)
                     # Görselde "SAR Crosses Price" var. Yükseliş için Fiyat > SAR olmalı.
                     Column('close').crosses_above(Column('P.SAR'))
                 )\
                 .get_scanner_data()

    # Veri Kontrolü
    if not qry or len(qry) < 2: return pd.DataFrame()
    df = pd.DataFrame(data=qry[1], columns=cols)

    # --- ANAYASA: PAZAR FİLTRESİ ---
    allowed = ['stock', 'reit', 'common']
    forbidden = ['submarket', 'poip', 'preference', 'watch_list', 'fund']
    
    def pazar_kontrolu(specs):
        s_str = [str(s).lower() for s in specs] if specs else []
        if any(f in s for f in forbidden for s in s_str): return False
        return any(a in s for a in allowed for s in s_str)

    df_filtered = df[df['typespecs'].apply(pazar_kontrolu)].copy()
    
    # Formatlama
    if not df_filtered.empty:
        df_filtered['Piyasa_Degeri_Milyar'] = df_filtered['market_cap_basic'] / 1_000_000_000
        df_filtered.reset_index(drop=True, inplace=True)
        df_filtered.index += 1
        
    return df_filtered

# --- MANUEL MOD ---
if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    print("P.Sar + ADX Stratejisi Çalıştırılıyor...")
    
    df = taramayi_calistir()
    
    if not df.empty:
        print(f"\n--- PSAR+ADX SONUÇLARI ({len(df)} Hisse) ---")
        goster = ['name', 'close', 'change', 'relative_volume_10d_calc', 'ADX', 'P.SAR']
        print(df[goster].to_string())
    else:
        print("Kriterlere uyan hisse bulunamadı.")