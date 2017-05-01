import pandas as pd
from zipfile import ZipFile
from Helper import pandas_column_utilities as pcu

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
        '''
        Steps :
            1. continuous_columns :
                    - impute,
                    - normalize
            2. ordinal_columns :
                    - get a map of the ordinal values to their numbers and cpply the map
                    e,g. {'L':1, 'M':2,'L':3, 'XL':4}
                    - impute
            4. date_columns
                    - convert the date columns from string to dates
                    - split them in to multiple columns for day, day of year, month, quarter, year etc.,
                    - impute
            5. categorical
                    - impute
                    - one hot encoding
            6. remove columns which are fully zero or have the same value throughout.
        '''


        return df

    def select_features(self, df):
        print "select features"
        return df

    def get_data(self, df, continuous_columns, ordinal_columns, date_columns, categorical) :
        # df = self.load_csv_to_df()
        df = self.feature_engineer(df, continuous_columns, ordinal_columns, date_columns, categorical)
        df = self.select_features(df)
        return df

continuous_columns = ['avg_dist','avg_rating_by_driver','avg_rating_of_driver','avg_surge','surge_pct','trips_in_first_30_days','weekday_pct']
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
pcu.info(df)
# df = data_class.get_data(df, [], [], [], [])
