from tradingview_screener import Query, Column
import pandas as pd

def taramayi_calistir():
    cols = ['name', 'close', 'change|1W', 'volume', 'price_sales_ratio', 'return_on_equity_fq', 'RSI', 'TechRating_1D', 'P.SAR', 'earnings_per_share_diluted_yoy_growth_ttm', 'typespecs', 'market_cap_basic', 'relative_volume_10d_calc']

    qry = Query().set_markets('turkey')\
                 .select(*cols)\
                 .where(
                     # --- ANAYASA ---
                     Column('market_cap_basic') > 1200000000,
                     Column('volume') > 5000,
                     
                     # --- STRATEJİ ---
                     Column('relative_volume_10d_calc') > 1.5,
                     Column('change|1W') < 10,
                     Column('average_volume_10d_calc') > 1000000,
                     Column('price_sales_ratio') <= 10,
                     Column('return_on_equity_fq') > 15,
                     Column('debt_to_equity_fq') < 1,
                     Column('current_ratio_fq') > 1,
                     Column('RSI').between(30, 80),
                     Column('ADX+DI') > Column('ADX-DI'),
                     Column('Mom') > -0.1,
                     Column('Stoch.K') > Column('Stoch.D'),
                     Column('MACD.macd') > Column('MACD.signal'),
                     Column('P.SAR') < Column('close'),
                     Column('MoneyFlow') > 50,
                     Column('earnings_per_share_diluted_yoy_growth_ttm') > 15
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
    print("Temel Teknik 2 (Manuel)...")
    df = taramayi_calistir()
    if not df.empty:
        print(df[['name', 'close', 'price_sales_ratio', 'return_on_equity_fq']].to_string())
    else:
        print("Sonuç Yok.")