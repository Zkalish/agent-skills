import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore')

# --- GPS SİSTEMİ ---
if os.path.exists("Hisse_Verileri"):
    VERI_KLASORU = "Hisse_Verileri"
    GRAFIK_KLASORU = "Grafikler"
elif os.path.exists("../Hisse_Verileri"):
    VERI_KLASORU = "../Hisse_Verileri"
    GRAFIK_KLASORU = "../Grafikler"
else:
    VERI_KLASORU = "Hisse_Verileri"
    GRAFIK_KLASORU = "Grafikler"

if not os.path.exists(GRAFIK_KLASORU): os.makedirs(GRAFIK_KLASORU)

def grafik_ciz_ve_kaydet(df, hisse_adi, egim, intercept, pivots):
    try:
        plot_df = df.tail(300).copy().reset_index(drop=True)
        plt.figure(figsize=(12, 6))
        plt.plot(plot_df.index, plot_df['Close'], label='Kapanış', color='black', linewidth=1.5)
        plt.plot(plot_df.index, plot_df['High'], label='Yüksek (High)', color='lightgray', linewidth=1, alpha=0.7)
        ilk_pivot = min(pivots) if len(pivots) > 0 else 0
        x_values = np.arange(ilk_pivot, len(plot_df))
        trend_values = (egim * x_values) + intercept
        plt.plot(x_values, trend_values, color='red', linewidth=2, linestyle='--', label='Düşen Trend')
        
        degen_x, degen_y = [], []
        for p_idx in pivots:
            if p_idx < len(plot_df):
                p_high = plot_df['High'].iloc[p_idx]
                p_trend = (egim * p_idx) + intercept
                if 0.98 * p_trend <= p_high <= 1.02 * p_trend:
                    degen_x.append(p_idx); degen_y.append(p_high)
        plt.scatter(degen_x, degen_y, color='blue', s=50, zorder=5, label='Dokunuşlar')
        plt.title(f"{hisse_adi} - Düşeni Kıran (Taze Kırılım)", fontsize=14)
        plt.legend(); plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(GRAFIK_KLASORU, f"{hisse_adi}_Kirim.png"))
        plt.close()
    except: plt.close()

def pivot_tepeleri_bul(highs, window=10):
    peaks = []
    for i in range(window, len(highs) - window):
        if highs[i] == np.max(highs[i-window:i+window+1]): peaks.append(i)
    return peaks

def en_iyi_trend_cizgisi(df):
    try:
        df = df.tail(400).copy().reset_index(drop=True)
        highs = df['High'].values
        closes = df['Close'].values
        opens = df['Open'].values
        
        if len(df) < 100: return None, 0, 0, 0, []

        pivots = pivot_tepeleri_bul(highs, window=10)
        if len(pivots) < 2: return None, 0, 0, 0, []

        bugun_idx = len(df) - 1
        son_kapanis = closes[-1]
        
        # --- TAZE KIRILIM KONTROLÜ (YENİ) ---
        # Önceki mumun kapanışı
        onceki_kapanis = closes[-2]
        
        en_iyi_trend = None
        en_cok_dokunus = 0
        best_params = (0, 0)

        for i in range(len(pivots)-1, 0, -1):
            idx_b = pivots[i]
            if idx_b >= bugun_idx - 5: continue

            for j in range(i-1, -1, -1):
                idx_a = pivots[j]
                if (idx_b - idx_a) < 30: continue

                fiyat_a = highs[idx_a]
                fiyat_b = highs[idx_b]
                if fiyat_b >= fiyat_a: continue

                egim = (fiyat_b - fiyat_a) / (idx_b - idx_a)
                intercept = fiyat_a - (egim * idx_a)
                
                bugun_trend = (egim * bugun_idx) + intercept
                
                # 1. Bugün üzerinde mi?
                if son_kapanis <= bugun_trend: continue 
                
                # 2. 🔥 Dün altında mıydı? (TAZE KIRILIM ŞARTI) 🔥
                # Dünkü trend değeri
                dun_trend = (egim * (bugun_idx - 1)) + intercept
                # Eğer dün de trendin üzerindeyse, bu eski bir sinyaldir -> ATLA
                if onceki_kapanis > dun_trend: continue

                # İhlal Kontrolü
                gecerli_mi = True
                aralik_idx = np.arange(idx_a, bugun_idx)
                trend_line_values = (egim * aralik_idx) + intercept
                real_highs = highs[idx_a:bugun_idx]
                
                ihlal_mask = real_highs > (trend_line_values * 1.02)
                if np.sum(ihlal_mask) > (len(real_highs) * 0.05): gecerli_mi = False
                if not gecerli_mi: continue

                dokunus_sayisi = 0
                for p_idx in pivots:
                    if p_idx < idx_a or p_idx >= bugun_idx: continue
                    p_fiyat = highs[p_idx]
                    p_trend_degeri = (egim * p_idx) + intercept
                    if 0.985 * p_trend_degeri <= p_fiyat <= 1.02 * p_trend_degeri:
                        dokunus_sayisi += 1
                
                if dokunus_sayisi >= 3:
                    if dokunus_sayisi > en_cok_dokunus:
                        en_cok_dokunus = dokunus_sayisi
                        en_iyi_trend = bugun_trend
                        best_params = (egim, intercept)

        if en_iyi_trend:
            if son_kapanis > opens[-1] and son_kapanis < en_iyi_trend * 1.10:
                return en_iyi_trend, en_cok_dokunus, best_params[0], best_params[1], pivots

        return None, 0, 0, 0, []

    except: return None, 0, 0, 0, []

def taramayi_calistir():
    sonuclar = []
    if not os.path.exists(VERI_KLASORU): return pd.DataFrame()
    dosyalar = [f for f in os.listdir(VERI_KLASORU) if f.endswith('.csv')]
    
    for dosya in dosyalar:
        hisse_adi = dosya.replace('.csv', '')
        dosya_yolu = os.path.join(VERI_KLASORU, dosya)
        try:
            df = pd.read_csv(dosya_yolu)
            if df.empty or len(df) < 100: continue
            
            trend, dokunus, egim, intercept, pivots = en_iyi_trend_cizgisi(df)
            
            if trend and dokunus >= 3:
                son = df['Close'].iloc[-1]
                prev = df['Close'].iloc[-2]
                change = ((son - prev) / prev) * 100
                
                sonuclar.append({
                    'name': hisse_adi,
                    'close': round(son, 2),
                    'change': round(change, 2),
                    'Trend_Destegi': round(trend, 2),
                    'Dokunus': dokunus
                })
                plt.ioff()
                grafik_ciz_ve_kaydet(df.tail(400).reset_index(drop=True), hisse_adi, egim, intercept, pivots)
        except: pass

    if sonuclar:
        return pd.DataFrame(sonuclar).sort_values(by='Dokunus', ascending=False)
    return pd.DataFrame()

if __name__ == "__main__":
    import time
    print(f"🎨 DÜŞENİ KIRANLAR (V16 - Taze Kırılım)...")
    basla = time.time()
    df = taramayi_calistir()
    sure = time.time() - basla
    print(f"\n⏱️ Tarama Süresi: {sure:.2f} saniye")
    if not df.empty: print(df[['name', 'close', 'Trend_Destegi', 'Dokunus']].to_string())
    else: print("❌ Yeni kırılım bulunamadı.")