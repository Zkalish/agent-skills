from tradingview_screener import Query, Column
import pandas as pd

def taramayi_calistir():
    cols = ['name', 'close', 'change|1W', 'volume', 'P.SAR', 'P.SAR|1W', 'Stoch.RSI.K', 'Stoch.RSI.D', 'typespecs', 'market_cap_basic', 'relative_volume_10d_calc']

    qry = Query().set_markets('turkey')\
                 .select(*cols)\
                 .where(
                     # --- ANAYASA ---
                     Column('market_cap_basic') > 1200000000,
                     Column('volume') > 5000,

                     # --- STRATEJİ ---
                     Column('relative_volume_10d_calc') > 1,
                     Column('change|1W') < 10,
                     Column('close|1W') > Column('P.SAR|1W'),
                     Column('close') < Column('P.SAR'),
                     Column('Stoch.RSI.K').crosses_above(Column('Stoch.RSI.D'))
                 )\
                 .get_scanner_data()

    if not qry or len(qry) < 2: return pd.DataFrame()
    df = pd.DataFrame(data=qry[1], columns=cols)

    allowed = ['stock', 'reit', 'common']
    forbidden = ['submarket', 'poip', 'preference', 'watch_list', 'fund']
    def pazar_kontrolu(specs):
        s_str = [str(s).lower() for s in specs] if specs else []
        if any(f in s for f in forbidden for s in s_str): return False
        return any(a in s for a in allowed for s in s_str)

    df_filtered = df[df['typespecs'].apply(pazar_kontrolu)].copy()
    
    if not df_filtered.empty:
        df_filtered.reset_index(drop=True, inplace=True)
        df_filtered.index += 1
        
    return df_filtered

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    print("Sar Düzeltmesi (Manuel)...")
    df = taramayi_calistir()
    if not df.empty:
        print(df[['name', 'close', 'change|1W', 'Stoch.RSI.K']].to_string())
    else:
        print("Sonuç Yok.")