import pandas as pd
from zipfile import ZipFile

class DataClass :

    def __init__(self, path) :
        self.path = path

    #getdata
    #feature engineering
        # cleanup
        # date, ordinal, categorical
        # scaling
        # imputing
    # select features

    def load_csv_to_df(self):
        print "loading csv"
        df = pd.read_csv(self.path)
        return df

    def feature_engineer(self, df, continuous_columns, ordinal_columns, date_columns, categorical) :
        print "feature engineering"
        return df

    def select_features(self, df):
        print "select features"
        return df

    def get_data(self, df, continuous_columns, ordinal_columns, date_columns, categorical) :
        # df = self.load_csv_to_df()
        df = self.feature_engineer(df, continuous_columns, ordinal_columns, date_columns, categorical)
        df = self.select_features(df)
        return df

#
# zf = ZipFile('data/Train.zip')
#
# df = pd.read_csv('data/Train.csv')
#
# year = df['YearMade']
# year = year[year != 1000]
#
# price_v_year = df[['SalePrice', 'YearMade']]
#
data_class = DataClass('data/Train.csv')
df = data_class.load_csv_to_df()
#EDA
df = data_class.get_data(df, [], [], [], [])
