from data_acquisition.download_stock_data import download_stock_data
from data_preprocessing.clean_stock_data import clean_stock_data
from labeling.target_label_make import label_peaks

def main():

    stock_name = 'NVDA'  # 企業名

    # 企業名,期間
    raw_data = download_stock_data(stock_name, '2020-01-01', '2025-07-01')

    clean_data = clean_stock_data(raw_data)
    clean_data.to_csv(f'data/clean/clean_{stock_name}_data.csv', index=False)
    print(clean_data.dtypes)

    # 目的関数のラベルの作成
    clean_data['Peaklabel'] = label_peaks(clean_data['Close'], window=3)
    peak_data = clean_data
    peak_data.to_csv(f'data/target_label_data/label_{stock_name}_data.csv', index=False)

if __name__ == "__main__":
    main()