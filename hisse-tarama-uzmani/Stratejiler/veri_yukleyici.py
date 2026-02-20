"""
BIST Hisse Veri Yükleyici
/root/Job/Bistdata/daily klasöründen veri yükler.
 Eksik/güncel olmayan hisseleri borsapy'den tamamlar.
"""

import os
import csv
from pathlib import Path
from datetime import datetime, timedelta
import borsapy as bp
import time

DATA_PATH = Path("/root/Job/Bistdata/daily")


def get_local_stocks():
    """Yerel hisseleri listele"""
    return [f.stem for f in DATA_PATH.glob("*.csv")]


def is_data_fresh(ticker, days=30):
    """Verinin taze olup olmadığını kontrol et"""
    csv_path = DATA_PATH / f"{ticker}.csv"
    if not csv_path.exists():
        return False

    try:
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if not rows:
                return False
            last_date = rows[-1]['Date'][:10]
            last_dt = datetime.strptime(last_date, "%Y-%m-%d")
            return (datetime.now() - last_dt).days <= days
    except:
        return False


def update_stock(ticker, period="2y"):
    """Tek hisseyi güncelle"""
    try:
        df = bp.Ticker(ticker).history(period=period)
        if len(df) > 100:
            df.to_csv(DATA_PATH / f"{ticker}.csv")
            return True
    except:
        pass
    return False


def load_stock_data(ticker, days=90):
    """Hisse verisini yükle (yerel veya güncelle)"""
    csv_path = DATA_PATH / f"{ticker}.csv"

    if not csv_path.exists():
        print(f"  📥 {ticker}: Yerel veri yok, indiriliyor...")
        if update_stock(ticker):
            pass
        else:
            return None
    elif not is_data_fresh(ticker, days):
        print(f"  🔄 {ticker}: Veri eski, güncelleniyor...")
        update_stock(ticker)

    # Oku
    try:
        df = pd.read_csv(csv_path, parse_dates=['Date'])
        df.set_index('Date', inplace=True)
        return df
    except:
        return None


def update_all_stocks(min_days=30, max_per_run=50):
    """Tüm eksik/eski hisseleri güncelle"""
    import pandas as pd

    # KAP verilerini oku
    ana_path = Path("/root/Job/Bistdata/ana_pazar.csv")
    yildiz_path = Path("/root/Job/Bistdata/yildiz_pazar.csv")

    if ana_path.exists() and yildiz_path.exists():
        with open(ana_path) as f:
            ana = set([r['ticker'] for r in csv.DictReader(f)])
        with open(yildiz_path) as f:
            yildiz = set([r['ticker'] for r in csv.DictReader(f)])
        all_tickers = ana | yildiz
    else:
        all_tickers = set(get_local_stocks())

    local = set(get_local_stocks())

    # Eksik olanlar
    eksik = list(all_tickers - local)

    # Güncelleme gerekenler
    guncel_gerek = []
    for t in local:
        if not is_data_fresh(t, min_days):
            guncel_gerek.append(t)

    to_update = eksik + guncel_gerek
    to_update = list(set(to_update))[:max_per_run]

    if not to_update:
        print("✅ Tüm veriler güncel!")
        return

    print(f"🔄 {len(to_update)} hisse güncelleniyor...")

    success = 0
    for i, t in enumerate(to_update):
        print(f"  {i+1}/{len(to_update)}: {t}...", end=" ")
        if update_stock(t):
            print("✅")
            success += 1
        else:
            print("❌")
        time.sleep(0.3)

    print(f"\n✅ Tamamlandı: {success}/{len(to_update)}")


def get_all_stocks():
    """Tüm yerel hisseleri DataFrame olarak yükle"""
    import pandas as pd

    stocks = {}
    for f in DATA_PATH.glob("*.csv"):
        ticker = f.stem
        try:
            df = pd.read_csv(f, parse_dates=['Date'])
            df.set_index('Date', inplace=True)
            stocks[ticker] = df
        except:
            pass
    return stocks


# Test
if __name__ == "__main__":
    print("=== BIST Veri Durumu ===")
    local = get_local_stocks()
    print(f"Yerel hisse: {len(local)}")

    # Güncelleme yap
    update_all_stocks(max_per_run=10)
