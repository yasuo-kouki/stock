import pandas as pd
import datetime


def clean_stock_data(data):

    """株価データをクリーンアップする""" 
    raw_data = data.copy()

    # 1行目を削除，インデックスのリセット
    raw_data = raw_data.iloc[1:].reset_index(drop=True)

    # データ形式の変更
    raw_data.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

    # 日付をdatetime型に変換
    raw_data['Date'] = pd.to_datetime(raw_data['Date'],errors='coerce')
    # データのソート
    #raw_data = raw_data.sort_values('Date')

    return raw_data



