import pandas as pd
import numpy as np
import os
import warnings
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

warnings.simplefilter(action='ignore')

# --- GPS SİSTEMİ ---
if os.path.exists("Hisse_Verileri"):
    VERI_KLASORU = "Hisse_Verileri"
    GRAFIK_KLASORU = "Grafikler_DIPDK"
elif os.path.exists("../Hisse_Verileri"):
    VERI_KLASORU = "../Hisse_Verileri"
    GRAFIK_KLASORU = "../Grafikler_DIPDK"
else:
    VERI_KLASORU = "Hisse_Verileri"
    GRAFIK_KLASORU = "Grafikler_DIPDK"

if not os.path.exists(GRAFIK_KLASORU):
    os.makedirs(GRAFIK_KLASORU)

# ═══════════════════════════════════════════════════════════════
# GÜVENLİK VE SINIFLANDIRMA (YENİ MODÜL)
# ═══════════════════════════════════════════════════════════════

def hisse_siniflandir(df):
    """
    Hissenin 10 günlük ortalama işlem hacmine (TL) göre sınıfını belirler.
    """
    try:
        # Son 10 gün
        son_10 = df.tail(10).copy()
        # Günlük Hacim (TL) = Kapanış Fiyatı * Hacim (Lot)
        son_10['Hacim_TL'] = son_10['Close'] * son_10['Volume']
        ort_hacim = son_10['Hacim_TL'].mean()
        
        limit_milyon = ort_hacim / 1_000_000
        
        if limit_milyon >= 100:
            return "🟢 YILDIZ", limit_milyon
        elif limit_milyon >= 20:
            return "🟡 ANA", limit_milyon
        elif limit_milyon >= 5:
            return "🟠 YAN", limit_milyon
        else:
            return "🔴 SPEK", limit_milyon
    except:
        return "⚪ BELİRSİZ", 0

# ═══════════════════════════════════════════════════════════════
# GRAFİK MOTORU (V4 - Aynen Korundu)
# ═══════════════════════════════════════════════════════════════

def en_yakin_dibi_bul(series, idx, range_val=2):
    try:
        start = max(0, idx - range_val)
        end = min(len(series), idx + range_val + 1)
        local_min_idx = np.argmin(series.iloc[start:end])
        global_idx = start + local_min_idx
        return global_idx
    except: return idx

def grafik_ciz_ve_kaydet(df, hisse_adi, dk_params, dip_params, sinif_bilgisi):
    try:
        plot_df = df.tail(150).copy().reset_index(drop=True)
        offset = len(df) - len(plot_df)
        
        egim, intercept, dk_pivots = dk_params
        dip_p1, dip_p2 = dip_params
        
        dip_p1_loc = dip_p1 - offset
        dip_p2_loc = dip_p2 - offset
        
        if 0 <= dip_p1_loc < len(plot_df): dip_p1_loc = en_yakin_dibi_bul(plot_df['Low'], dip_p1_loc)
        if 0 <= dip_p2_loc < len(plot_df): dip_p2_loc = en_yakin_dibi_bul(plot_df['Low'], dip_p2_loc)

        fig = plt.figure(figsize=(14, 9), facecolor='white')
        gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1], hspace=0.08)
        
        ax1 = plt.subplot(gs[0])
        ax2 = plt.subplot(gs[1])
        
        # --- 1. MUM GRAFİĞİ ---
        width = 0.6
        up_color, down_color = '#00b746', '#ff3131'
        
        for i in range(len(plot_df)):
            open_p, close_p = plot_df['Open'].iloc[i], plot_df['Close'].iloc[i]
            high_p, low_p = plot_df['High'].iloc[i], plot_df['Low'].iloc[i]
            
            color = up_color if close_p >= open_p else down_color
            lower = open_p if close_p >= open_p else close_p
            height = abs(close_p - open_p) if abs(close_p - open_p) > 0 else 0.01 * close_p
            
            ax1.add_patch(mpatches.Rectangle((i - width/2, lower), width, height, facecolor=color, edgecolor=color, zorder=2))
            ax1.plot([i, i], [low_p, high_p], color='black', linewidth=0.8, zorder=1)

        ax1.set_xlim(-1, len(plot_df) + 1)
        ax1.set_ylim(plot_df['Low'].min() * 0.98, plot_df['High'].max() * 1.02)

        # DK Çizgisi
        dk_pivots_loc = [p - offset for p in dk_pivots if p >= offset]
        start_x = min(dk_pivots_loc) if dk_pivots_loc else 0
        x_vals = np.arange(start_x, len(plot_df))
        trend_vals = [(egim * (x + offset)) + intercept for x in x_vals]
        ax1.plot(x_vals, trend_vals, color='blue', linewidth=2.5, linestyle='--', label='Düşen Trend', zorder=5)
        
        for p in dk_pivots_loc:
            if 0 <= p < len(plot_df): ax1.scatter(p, plot_df['High'].iloc[p], color='blue', s=40, zorder=6)

        # DIP Çizgisi
        if dip_p1_loc >= 0 and dip_p2_loc >= 0:
            y1, y2 = plot_df['Low'].iloc[dip_p1_loc], plot_df['Low'].iloc[dip_p2_loc]
            label_text = 'Yatay Dip / Uyumsuzluk' if y2 >= y1 * 0.99 else 'Pozitif Uyumsuzluk'
            ax1.plot([dip_p1_loc, dip_p2_loc], [y1, y2], color='#00FF00', linewidth=3, label=label_text, zorder=10)
            ax1.scatter([dip_p1_loc, dip_p2_loc], [y1, y2], color='#00FF00', s=80, edgecolors='black', zorder=11)

        # BAŞLIKTA SINIF BİLGİSİ
        sinif_adi, hacim_milyon = sinif_bilgisi
        title_text = f"{hisse_adi} - DIPDK | {sinif_adi} ({hacim_milyon:.1f} Milyon TL)"
        ax1.set_title(title_text, fontsize=14, fontweight='bold')
        ax1.legend(loc='upper right', framealpha=0.8)
        ax1.grid(True, alpha=0.2, linestyle='--')
        ax1.set_xticklabels([])

        # --- 4. RSI PANELİ ---
        rsi_vals = plot_df['RSI']
        ax2.plot(plot_df.index, rsi_vals, color='purple', linewidth=1.5, label='RSI (14)')
        ax2.axhline(30, color='green', linestyle='--', alpha=0.5)
        ax2.axhline(70, color='red', linestyle='--', alpha=0.5)
        ax2.fill_between(plot_df.index, rsi_vals, 30, where=(rsi_vals < 30), color='green', alpha=0.1)

        rsi_p1_loc, rsi_p2_loc = dip_p1 - offset, dip_p2 - offset
        if rsi_p1_loc >= 0 and rsi_p2_loc >= 0:
            rsi1, rsi2 = rsi_vals.iloc[rsi_p1_loc], rsi_vals.iloc[rsi_p2_loc]
            ax2.plot([rsi_p1_loc, rsi_p2_loc], [rsi1, rsi2], color='#00FF00', linewidth=3, zorder=10)
            ax2.scatter([rsi_p1_loc, rsi_p2_loc], [rsi1, rsi2], color='#00FF00', s=60, edgecolors='black', zorder=11)

        ax2.legend(loc='upper left', framealpha=0.8)
        ax2.grid(True, alpha=0.2, linestyle='--')
        ax2.set_ylim(0, 100)

        plt.tight_layout()
        plt.savefig(os.path.join(GRAFIK_KLASORU, f"{hisse_adi}_DIPDK.png"), dpi=100)
        plt.close()
    except: plt.close()

# ═══════════════════════════════════════════════════════════════
# ... (HESAPLAMA MODÜLLERİ - AYNI) ...
# ═══════════════════════════════════════════════════════════════

def pivot_tepeleri_bul_dk(highs, window=10):
    peaks = []
    for i in range(window, len(highs) - window):
        if highs[i] == np.max(highs[i-window:i+window+1]): peaks.append(i)
    return peaks

def duseni_kiran_analiz(df):
    try:
        df_dk = df.tail(400).copy().reset_index(drop=True)
        if len(df_dk) < 100: return False, 0, None
        highs = df_dk['High'].values; closes = df_dk['Close'].values
        pivots = pivot_tepeleri_bul_dk(highs, window=10)
        if len(pivots) < 2: return False, 0, None
        bugun_idx = len(df_dk) - 1; son_kapanis = closes[-1]; onceki_kapanis = closes[-2]
        en_iyi_trend = None; en_cok_dokunus = 0; en_iyi_params = None

        for i in range(len(pivots)-1, 0, -1):
            idx_b = pivots[i]
            if idx_b >= bugun_idx - 5: continue
            for j in range(i-1, -1, -1):
                idx_a = pivots[j]
                if (idx_b - idx_a) < 30: continue
                fiyat_a = highs[idx_a]; fiyat_b = highs[idx_b]
                if fiyat_b >= fiyat_a: continue
                egim = (fiyat_b - fiyat_a) / (idx_b - idx_a)
                intercept = fiyat_a - (egim * idx_a)
                bugun_trend = (egim * bugun_idx) + intercept
                if son_kapanis <= bugun_trend: continue 
                dun_trend = (egim * (bugun_idx - 1)) + intercept
                if onceki_kapanis > dun_trend: continue
                gecerli_mi = True
                aralik_idx = np.arange(idx_a, bugun_idx)
                trend_vals = (egim * aralik_idx) + intercept
                real_highs = highs[idx_a:bugun_idx]
                ihlal_mask = real_highs > (trend_vals * 1.02)
                if np.sum(ihlal_mask) > (len(real_highs) * 0.05): continue
                dokunus_sayisi = 0
                for p_idx in pivots:
                    if p_idx < idx_a or p_idx >= bugun_idx: continue
                    p_val = highs[p_idx]; p_tr = (egim * p_idx) + intercept
                    if 0.985 * p_tr <= p_val <= 1.02 * p_tr: dokunus_sayisi += 1
                if dokunus_sayisi >= 3 and dokunus_sayisi > en_cok_dokunus:
                    en_cok_dokunus = dokunus_sayisi
                    en_iyi_trend = bugun_trend
                    en_iyi_params = (egim, intercept, pivots)
        if en_iyi_trend: return True, en_cok_dokunus, en_iyi_params
        return False, 0, None
    except: return False, 0, None

def hesapla_rsi(close, period=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def pivot_low_bul(series, left=5, right=5):
    pivots = []
    values = series.values
    for i in range(left, len(values) - right):
        if values[i] == np.min(values[i-left:i+right+1]): pivots.append(i)
    return pivots

def divergence_tespit(df, indikator_col, check_idx):
    try:
        ind = df[indikator_col]
        lows = df['Low']
        df_slice = df.iloc[max(0, check_idx-300):check_idx+1]
        offset = df_slice.index[0]
        pivots_rel = pivot_low_bul(df_slice[indikator_col], 5, 5)
        pivots = [p + offset for p in pivots_rel]
        relevant_pivots = [p for p in pivots if p <= check_idx]
        if len(relevant_pivots) < 2: return False, None
        p2 = relevant_pivots[-1]; p1 = relevant_pivots[-2]
        if (check_idx - p2) > 5: return False, None
        rsi_yukseliyor = ind.loc[p2] > ind.loc[p1]
        fiyat_dusuyor_veya_esit = lows.loc[p2] <= (lows.loc[p1] * 1.01)
        if rsi_yukseliyor and fiyat_dusuyor_veya_esit: return True, (p1, p2)
        return False, None
    except: return False, None

def dip_avcisi_gecmis_tara(df, gun_sayisi=25):
    df['RSI'] = hesapla_rsi(df['Close'])
    son_idx = len(df) - 1
    for i in range(gun_sayisi):
        kontrol_idx = son_idx - i
        if kontrol_idx < 50: break
        var_mi, noktalar = divergence_tespit(df, 'RSI', kontrol_idx)
        if var_mi: return True, noktalar
    return False, None

# ═══════════════════════════════════════════════════════════════
# ANA TARAMA (GÜNCELLENDİ)
# ═══════════════════════════════════════════════════════════════

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
            
            dk_sinyali, dokunus, dk_params = duseni_kiran_analiz(df)
            
            if dk_sinyali:
                dip_sinyali, dip_params = dip_avcisi_gecmis_tara(df, gun_sayisi=25)
                
                if dip_sinyali:
                    son = df['Close'].iloc[-1]
                    prev = df['Close'].iloc[-2]
                    change = ((son - prev) / prev) * 100
                    
                    # --- SPEK KONTROLÜ (YENİ) ---
                    sinif, hacim = hisse_siniflandir(df)
                    
                    sonuclar.append({
                        'name': hisse_adi,
                        'close': round(son, 2),
                        'change': round(change, 2),
                        'Dokunus': dokunus,
                        'Sinif': sinif, # Raporda görünecek
                        'Hacim(M)': round(hacim, 1),
                        'Skor': 100
                    })
                    
                    plt.ioff()
                    # Grafiği çizerken sınıf bilgisini de gönder
                    grafik_ciz_ve_kaydet(df.tail(400).copy().reset_index(drop=True), hisse_adi, dk_params, dip_params, (sinif, hacim))
        except: pass

    if sonuclar:
        return pd.DataFrame(sonuclar).sort_values(by='Dokunus', ascending=False)
    return pd.DataFrame()

if __name__ == "__main__":
    import time
    print("🧬 DIPDK (Spek Dedektörlü) Test Ediliyor...")
    basla = time.time()
    df = taramayi_calistir()
    sure = time.time() - basla
    print(f"\n⏱️ Süre: {sure:.2f} sn")
    if not df.empty:
        # Çıktıda Sınıfı da göster
        print(f"✅ BULUNANLAR:\n{df[['name', 'close', 'change', 'Dokunus', 'Sinif', 'Hacim(M)']].to_string()}")
        print(f"\n🖼️ Grafikler '{GRAFIK_KLASORU}' içine kaydedildi.")
    else: print("❌ Kesişim bulunamadı.")