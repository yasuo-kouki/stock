from data_acquisition.download_stock_data import download_stock_data
from data_preprocessing.clean_stock_data import clean_stock_data

def main():

    stock_name = 'NVDA'  # 企業名

    # 企業名,期間
    raw_data = download_stock_data(stock_name, '2020-01-01', '2023-10-01')
    #raw_data.to_csv('data/raw_{stock_name}_data.csv', index=False)

    clean_data = clean_stock_data(raw_data)
    clean_data.to_csv(f'data/clean/clean_{stock_name}_data.csv', index=False)
    # print(clean_data.dtypes)

if __name__ == "__main__":
    main()