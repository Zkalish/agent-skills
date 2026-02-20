from tradingview_screener import Query, Column
import pandas as pd

def taramayi_calistir():
    # Sütun İsimleri
    cols = [
        'name', 'close', 'change', 'volume', 'typespecs', 'market_cap_basic',
        'relative_volume_10d_calc', 'change|1W', 'change|1M',
        'RSI', 'Mom', 
        'SMA5', 'SMA10', 'SMA200'
    ]

    # Sorgu
    qry = Query().set_markets('turkey')\
                 .select(*cols)\
                 .where(
                     # --- ANAYASA: HACİM ---
                     Column('volume') > 5000,

                     # --- DRIEHAUS FİLTRELERİ ---
                     Column('change') < 9.5,                    # Tavan olmayan
                     Column('change|1W') < 10,                  # Haftalık şişmemiş
                     Column('relative_volume_10d_calc') > 1,    # Hacim desteği

                     # 1. DEVLER LİGİ (Market Cap >= 10 Milyar TL) [DÜZELTİLDİ]
                     # Artık 10 Milyar sınırındakileri de kapsar.
                     Column('market_cap_basic') >= 10000000000, 

                     # 2. AYLIK PERFORMANS POZİTİF
                     Column('change|1M') > 0.7,

                     # 3. MOMENTUM GÖSTERGELERİ
                     Column('RSI') > 50,
                     Column('Mom') > 1,

                     # 4. TREND TAKİBİ (Fiyat > Ortalamalar)
                     Column('close') > Column('SMA5'),
                     Column('close') > Column('SMA10'),
                     Column('close') > Column('SMA200')
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
    print("Driehaus Momentum Stratejisi (>= 10 Milyar) Çalıştırılıyor...")
    
    df = taramayi_calistir()
    
    if not df.empty:
        print(f"\n--- DRIEHAUS SONUÇLARI ({len(df)} Hisse) ---")
        goster = ['name', 'close', 'Piyasa_Degeri_Milyar', 'RSI', 'Mom', 'SMA200']
        print(df[goster].to_string())
    else:
        print("Kriterlere uyan hisse bulunamadı.")