def label_peaks(prices, window):
    """
    株価の時系列データから「山（ピーク）」と「谷（ボトム）」を判定し、
    ラベル（1：山、-1：谷、0：その他）を返す関数。
    
    Parameters:
        prices (list or array): 株価などの時系列データ（例：終値）
        window (int): 判定に使う前後の日数（3なら前後3日と比較）

    Returns:
        list: ラベル配列（1：山、-1：谷、0：その他）
    """

    # 各時点に対するラベルを初期化（すべて「0（その他）」）
    labels = [0] * len(prices)

    # 判定は、前後window日分のデータがある範囲でのみ実施
    for i in range(window, len(prices) - window):

        # --- 山（ピーク）の判定 ---
        # 現在の価格が「前のwindow日すべてより高い」かつ「後のwindow日すべてより高い」場合
        if all(prices[i] > prices[i - j] for j in range(1, window + 1)) and \
           all(prices[i] > prices[i + j] for j in range(1, window + 1)):
            labels[i] = 1  # 山（ピーク）とラベリング

        # --- 谷（ボトム）の判定 ---
        # 現在の価格が「前のwindow日すべてより低い」かつ「後のwindow日すべてより低い」場合
        elif all(prices[i] < prices[i - j] for j in range(1, window + 1)) and \
             all(prices[i] < prices[i + j] for j in range(1, window + 1)):
            labels[i] = -1  # 谷（ボトム）とラベリング

    # ラベル配列を返す（例：[0, 0, 1, 0, -1, 0, ...]）
    return labels
