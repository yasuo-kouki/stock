import yfinance as yf

def download_stock_data(symbol: str,start_date: str, end_date: str):
    """指定した株式コードのデータを取得し保存する"""

    try:
        # 株価データを取得
        #data = yf.download(symbol, start=start_date, end=end_date)
        data = yf.download(symbol, period='max')  # 最大期間のデータを取得

        if data.empty:
            print(f"警告:データが取得できませんでした ({symbol})")
            return

        # インデックスをリセットして日付を列に変換
        data.reset_index(inplace=True)

        print("データの収得ができました")  # デバッグ用

    except Exception as e:
        print(f"エラーが発生しました: {e}")

    return data