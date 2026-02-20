from tradingview_screener import Query, Column
import pandas as pd

def taramayi_calistir():
    """
    STRATEJİ: MİNİ RALLİ (Revize Edildi)
    
    GÜNCELLEMELER:
    - ISGSY gibi GSYO'ları yakalamak için 'fund' yasağı kalktı.
    - Sınırda kalanları yakalamak için Haftalık değişim < 12 yapıldı.
    """

    cols = [
        'name', 'close', 'change', 'volume', 'typespecs', 'market_cap_basic',
        'relative_volume_10d_calc', 'change|1W', 
        'EMA50', 'BB.basis'
    ]

    qry = Query().set_markets('turkey')\
                 .select(*cols)\
                 .where(
                     # === ANAYASA KURALLARI ===
                     Column('market_cap_basic') > 1200000000,
                     Column('volume') > 5000,

                     # === GÖRSELDEKİ KRİTERLER ===
                     Column('relative_volume_10d_calc') > 1,
                     Column('change') < 9.5,

                     # GÜNCELLEME: RTALB gibi sert yükselenleri kaçırmamak için %10 -> %12 esnetildi
                     Column('change|1W') < 12,

                     # === KIRILIM (CROSSOVER) ===
                     Column('close').crosses_above(Column('EMA50')),
                     Column('close').crosses_above(Column('BB.basis'))
                 )\
                 .get_scanner_data()

    if not qry or len(qry) < 2: return pd.DataFrame()
    
    df = pd.DataFrame(data=qry[1], columns=cols)

    # --- 4. ANAYASA: PAZAR FİLTRESİ (GÜNCELLENDİ) ---
    # ISGSY (CEF) gibi kağıtları kaçırmamak için 'fund' yasağını kaldırdık.
    # Ancak 'mutual fund' (yatırım fonu) gelirse diye 'fund'u kontrollü çıkarıyoruz.
    
    allowed = ['stock', 'reit', 'common', 'cef', 'fund'] # 'fund' ve 'cef' eklendi
    forbidden = ['submarket', 'poip', 'preference', 'watch_list'] # 'fund' buradan çıkarıldı
    
    def pazar_kontrolu(specs):
        s_str = [str(s).lower() for s in specs] if specs else []
        # Eğer 'mutual' varsa (gerçek yatırım fonu) yine de eleyelim
        if any('mutual' in s for s in s_str): return False
        
        if any(f in s for f in forbidden for s in s_str): return False
        return any(a in s for a in allowed for s in s_str)

    df_filtered = df[df['typespecs'].apply(pazar_kontrolu)].copy()
    
    if not df_filtered.empty:
        df_filtered['Piyasa_Degeri_Milyar'] = df_filtered['market_cap_basic'] / 1_000_000_000
        df_filtered = df_filtered[['name', 'close', 'change', 'change|1W', 'relative_volume_10d_calc', 'Piyasa_Degeri_Milyar']]
        df_filtered.reset_index(drop=True, inplace=True)
        df_filtered.index += 1
        
    return df_filtered

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print("🚀 Mini Ralli (Düzeltilmiş Versiyon)...")
    sonuc = taramayi_calistir()
    if not sonuc.empty:
        print(f"\n✅ BULUNANLAR ({len(sonuc)}):")
        print(sonuc.to_string())
    else:
        print("❌ Sonuç Yok.")