from tradingview_screener import Query, Column
import pandas as pd

def taramayi_calistir():
    # Sütun İsimleri
    cols = [
        'name', 'close', 'change', 'volume', 'typespecs', 'market_cap_basic',
        'relative_volume_10d_calc', 'change|1W', 
        'Volatility.W', 'Volatility.M', # Haftalık ve Aylık Volatilite
        'BB.basis' # Bollinger Orta Bant (Basis)
    ]

    # Sorgu
    qry = Query().set_markets('turkey')\
                 .select(*cols)\
                 .where(
                     # --- ANAYASA: GÜVENLİK DUVARLARI ---
                     Column('market_cap_basic') > 1200000000,
                     Column('volume') > 5000,

                     # --- GÖRSELDEKİ STRATEJİ FİLTRELERİ ---
                     Column('change') < 9.5,                    # Tavan olmayanlar
                     Column('change|1W') < 10,                  # Haftalıkta henüz patlamamış
                     
                     # 1. SESSİZLİK (Düşük Volatilite - Sıkışma)
                     # Görselde 0-5% ve -5-5% istenmiş. Volatilite mutlak değerdir, 0-5 arası güvenlidir.
                     Column('Volatility.W').between(0, 5),      
                     Column('Volatility.M').between(0, 5),      
                     
                     # 2. HACİM DESTEĞİ (Rel Vol > 1.7)
                     Column('relative_volume_10d_calc') > 1.7, 

                     # 3. UYANIŞ (Fiyat Bollinger Basis'i KESİYOR)
                     # Görselde: Price Crosses BB(20) Basis
                     Column('close').crosses_above(Column('BB.basis'))
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
    pd.set_option('display.width', 1000)
    print("Volatilite Kırılımı Stratejisi Çalıştırılıyor...")
    
    df = taramayi_calistir()
    
    if not df.empty:
        print(f"\n--- VOLATİLİTE KIRILIMI SONUÇLARI ({len(df)} Hisse) ---")
        # Önemli sütunları gösterelim
        goster = ['name', 'close', 'change', 'relative_volume_10d_calc', 'Volatility.W', 'BB.basis']
        print(df[goster].to_string())
    else:
        print("Kriterlere uyan hisse bulunamadı.")