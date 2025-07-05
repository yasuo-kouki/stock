def add_technical_indicators(data):
    """テクニカル指標（RSI, MACD, ボリンジャーバンドなど）を追加"""

    # 移動平均と乖離率
    data['ma_5'] = data['Close'].rolling(window=5).mean()
    data['ma_10'] = data['Close'].rolling(window=10).mean()
    data['ma_ratio'] = data['Close'] / data['ma_5']

    # リターン（変化率）
    data['return_1'] = data['Close'].pct_change(1)
    data['return_5'] = data['Close'].pct_change(5)
    data['diff'] = data['Close'] - data['Open']

    # RSI（14日）
    delta = data['Close'].diff()
    gain = delta.clip(lower=0).rolling(window=14).mean()
    loss = -delta.clip(upper=0).rolling(window=14).mean()
    rs = gain / loss
    data['rsi'] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema26 = data['Close'].ewm(span=26, adjust=False).mean()
    data['macd'] = ema12 - ema26
    data['macd_signal'] = data['macd'].ewm(span=9, adjust=False).mean()

    # ボリンジャーバンド
    ma_20 = data['Close'].rolling(window=20).mean()
    std_20 = data['Close'].rolling(window=20).std()
    data['bb_upper'] = ma_20 + 2 * std_20
    data['bb_lower'] = ma_20 - 2 * std_20
    data['bb_width'] = data['bb_upper'] - data['bb_lower']

    # 出来高関連
    data['vol_ma_5'] = data['Volume'].rolling(window=5).mean()
    data['vol_change'] = data['Volume'].pct_change(1)

    return data
