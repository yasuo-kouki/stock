import pandas as pd

def add_date_features(data):
    """日付由来の特徴量（曜日、月末フラグなど）を追加"""

    # Date列をdatetimeに変換（必要なら）
    if not pd.api.types.is_datetime64_any_dtype(data['Date']):
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    # 曜日（0=月, 4=金）
    data['dayofweek'] = data['Date'].dt.dayofweek

    # 月末フラグ（1なら月末、0ならそれ以外）
    data['is_month_end'] = data['Date'].dt.is_month_end.astype(int)

    return data
