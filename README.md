# 株価予測AIシステム仕様書

## 🧭 プロジェクトの目的

- 主に**スイングトレード（7日以内）向けの株価トレンド予測**を行うAIを構築
- 目的は**ガクチカ・趣味**であり、いずれ**クラウド上でWeb公開**する予定
- トレンド予測（上がる/下がる）を中心に、将来的に**値段予測（回帰）も対応**

---

## 🔍 予測モデルの構成方針

### 🧠 予測対象

| 種類         | 内容                                         |
|--------------|----------------------------------------------|
| トレンド予測 | 1時間後の株価が上がるか下がるか（2値分類）  |
| 値段予測     | 1時間後の株価そのもの（回帰）               |

---

### ⏱ 予測粒度

- 1時間ごとに最新データを取得し、1時間後の動きを予測
- スイングトレードに活かせるタイムスケールを想定

---

## 📊 使用するデータ

### 株価データ

| 項目 | 内容 |
|------|------|
| ソース | [Finnhub API](https://finnhub.io/) |
| 粒度 | 1時間足 |
| 取得銘柄 | 当面は1銘柄（例：AAPL）に絞って開発 |
| 保存形式 | CSV（ローカル） / Cloud Storage（クラウド）予定 |

### ニュースデータ

| 項目 | 内容 |
|------|------|
| ソース | Finnhub API |
| 内容 | 銘柄ごとのニュース記事・速報・SNS |
| 取得方法 | APIからJSONで取得、スコア化（TF-IDF/BERTなど予定） |

---

## 🏗 システム構成（案③：推論クラウド + 再学習1日1回）

| 項目 | 内容 |
|------|------|
| 特徴量生成・推論 | **Cloud Run（Flask API）で毎時実行** |
| モデル再学習 | **Vertex AI** で **毎日1回のみ実行**（分類モデル） |
| モデル保存 | Cloud Storage に `.pkl` モデル保存（バージョン管理も） |
| 値段予測モデル | **ローカルで再学習・手動更新**（低頻度） |

---

## 🧩 モデル設計方針

### トレンド予測（上がる/下がる）

| 項目 | 内容 |
|------|------|
| アルゴリズム | LightGBM（scikit-learn ラッパー）予定 |
| タスク | 2値分類 |
| 評価指標 | Accuracy, F1スコア, AUCなど |

### 値段予測（株価そのもの）

| 項目 | 内容 |
|------|------|
| アルゴリズム | LightGBM or Linear Regression |
| タスク | 回帰 |
| 評価指標 | RMSE, MAE, MAPEなど |
| 更新頻度 | 手動（週〜月1回程度） |

---

## 📁 ディレクトリ構成（案）

```plaintext
stock_ml_project/
├── data/                   # データ関連
│   ├── raw/                # 生データ（CSVやJSONなど）
│   ├── processed/          # 前処理後データ
│   └── external/           # 外部データ（経済指標やSNSデータなど）
│       └── twitter_sentiment.csv # SNS感情分析結果データ
├── notebooks/              # Jupyter Notebook
│   ├── EDA.ipynb           # Exploratory Data Analysis（データ探索）
│   ├── Model_Training.ipynb # モデル学習と検証
│   └── Evaluation.ipynb    # 評価指標の検証や可視化
├── src/                    # ソースコード
│   ├── main.py
│   ├── data_acquisition/   # データ収集
│   │   └── download_twitter_data.py # Twitterデータの収集スクリプト
│   ├── data_preprocessing/ # データ前処理
│   │   ├── load_data.py    # 欠損値や異常値の処理
│   │   ├── split_data.py   # 生データをtrainとtestデータに分割
│   │   └── normalize.py    # 正規化や標準化
│   ├── feature_engineering/ # 特徴量エンジニアリング
│   │   ├── technical_indicators.py # テクニカル指標生成（MACD, RSIなど）
│   │   ├── date_features.py # 日付関連特徴量（曜日、月末など）
│   │   └── twitter_sentiment.py # SNS感情スコアの特徴量エンジニアリング
│   ├── models/             # モデル定義と学習
│   │   ├── xgboost_model.py # XGBoostモデル
│   │   └── lstm_model.py    # LSTMモデル
│   ├── evaluation/         # モデル評価
│   │   ├── metrics.py      # 評価指標の計算（MSE, MAE, AUCなど）
│   │   └── visualization.py # 結果の可視化（グラフ生成）
│   └── utils/              # ユーティリティ関数
│       ├── data_loader.py  # データ読み込み関数
│       └── config.py       # 設定ファイル読み込み
├── config/                 # 設定ファイル
│   ├── xgboost_config.yaml # XGBoost用のパラメータ
│   ├── lstm_config.yaml    # LSTM用のパラメータ
│   └── paths.yaml          # データやモデルのパス設定
├── experiments/            # 実験結果とログ
│   ├── logs/               # 実行ログ
│   ├── results/            # 評価結果
│   └── models/             # 学習済みモデル
├── outputs/                # モデル予測結果やグラフ
│   ├── predictions/        # モデルの予測結果
│   └── plots/              # グラフ出力
├── tests/                  # テストコード
│   ├── test_data_preprocessing.py # 前処理のテスト
│   ├── test_models.py          # モデル動作確認
│   └── test_utils.py           # ユーティリティ関数のテスト
└── README.md               # プロジェクト概要
