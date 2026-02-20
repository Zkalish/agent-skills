from tradingview_screener import Query, Column
import pandas as pd

# --- FONKSİYON: SADECE HESAPLAR VE LİSTEYİ DÖNDÜRÜR ---
def taramayi_calistir():
    column_names = [
        'name', 'close', 'change', 'volume', 'typespecs', 'market_cap_basic',
        'relative_volume_10d_calc', 'ADX', 'ADX+DI', 'ADX-DI', 
        'Aroon.Up', 'Aroon.Down', 'HullMA9', 'Ichimoku.BLine', 'Ichimoku.CLine', 'change|1W'
    ]

    qry = Query().set_markets('turkey')\
                 .select(*column_names)\
                 .where(
                     Column('market_cap_basic') > 1200000000,
                     Column('volume') > 5000,
                     Column('change') < 9.5,
                     Column('change|1W') < 10,
                     Column('relative_volume_10d_calc') > 1,
                     Column('ADX') > 20,
                     Column('ADX+DI') > Column('ADX-DI'),
                     Column('Aroon.Up') >= 99.9,
                     Column('Aroon.Up') > Column('Aroon.Down'),
                     Column('close') > Column('HullMA9'),
                     Column('Ichimoku.CLine') > Column('Ichimoku.BLine')
                 )\
                 .get_scanner_data()

    if not qry or len(qry) < 2: return pd.DataFrame()

    df = pd.DataFrame(data=qry[1], columns=column_names)

    # Pazar Filtresi
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
        df_filtered.index = df_filtered.index + 1
        
    return df_filtered

# --- MANUEL MOD: TEK BAŞINA ÇALIŞTIRILIRSA TABLO BASAR ---
if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print("DAHI Stratejisi (Manuel Mod)...")
    df = taramayi_calistir()
    if not df.empty:
        print(df[['name', 'close', 'change', 'change|1W', 'ADX', 'Piyasa_Degeri_Milyar', 'typespecs']]
              .to_string(justify='left', formatters={'name': '{:<8}'.format}))
    else:
        print("Sonuç Yok.")