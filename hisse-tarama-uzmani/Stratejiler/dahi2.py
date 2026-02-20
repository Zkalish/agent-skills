from tradingview_screener import Query, Column
import pandas as pd

def taramayi_calistir():
    # Sütun İsimleri (Yeni eklenenler: SMA50, SMA200, P.SAR, CMF)
    cols = [
        'name', 'close', 'change', 'volume', 'typespecs', 'market_cap_basic',
        'relative_volume_10d_calc', 'ADX', 'ADX+DI', 'ADX-DI', 
        'Aroon.Up', 'Aroon.Down', 'HullMA9', 
        'Ichimoku.BLine', 'Ichimoku.CLine', 
        'change|1W', 
        'SMA50', 'SMA200', 'P.SAR', 'ChaikinMoneyFlow'
    ]

    # Sorgu
    qry = Query().set_markets('turkey')\
                 .select(*cols)\
                 .where(
                     # --- ANAYASA: GÜVENLİK DUVARLARI ---
                     Column('market_cap_basic') > 1200000000,
                     Column('volume') > 5000,

                     # --- DAHI 1 ÇEKİRDEK FİLTRELERİ ---
                     Column('change') < 9.5,
                     Column('change|1W') < 10,
                     Column('relative_volume_10d_calc') > 1,
                     Column('ADX') > 20,
                     Column('ADX+DI') > Column('ADX-DI'),
                     Column('Aroon.Up') >= 99.9,
                     Column('Aroon.Up') > Column('Aroon.Down'),
                     Column('close') > Column('HullMA9'),
                     Column('Ichimoku.CLine') > Column('Ichimoku.BLine'), # Tenkan > Kijun

                     # --- DAHI 2: YENİ EKLENEN FİLTRELER ---
                     Column('SMA50') > Column('SMA200'),    # Trend yönü yukarı (Golden Cross bölgesi)
                     Column('close') > Column('P.SAR'),     # Fiyat SAR'ın üzerinde
                     Column('ChaikinMoneyFlow') > 0         # Para Girişi Var (Pozitif)
                 )\
                 .get_scanner_data()

    # Veri Kontrolü ve DataFrame Dönüşümü
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
    
    # Formatlama ve İndeksleme
    if not df_filtered.empty:
        df_filtered['Piyasa_Degeri_Milyar'] = df_filtered['market_cap_basic'] / 1_000_000_000
        df_filtered.reset_index(drop=True, inplace=True)
        df_filtered.index += 1
        
    return df_filtered

# --- MANUEL MOD (Tek Başına Çalıştırılırsa) ---
if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print("DAHI 2 Stratejisi (Manuel Mod) Çalıştırılıyor...")
    
    df = taramayi_calistir()
    
    if not df.empty:
        print(f"\n--- DAHI 2 SONUÇLARI ({len(df)} Hisse) ---")
        # Önemli sütunları gösterelim
        gosterilecekler = ['name', 'close', 'change', 'SMA50', 'SMA200', 'ChaikinMoneyFlow', 'typespecs']
        print(df[gosterilecekler].to_string())
    else:
        print("Kriterlere uyan hisse bulunamadı.")