import pandas as pd
import numpy as np
from zipfile import ZipFile
from Helper import pandas_column_utilities as pcu
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from Helper import FeatureTransformer as ft

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
        #Begin : Creating categorical pipeline
        # create encoder object
        encode = ft.HotEncoder()
        impute = Imputer(strategy='most_frequent')
        pipeline = Pipeline([('encode',encode),('impute',impute)])
        pipeline.fit(df[categorical])
        print pipeline.transform(df[categorical])
        #END : Creating categorical pipeline

        return df

    def select_features(self, df):
        print "select features"
        return df

    def get_data(self, df, continuous_columns, ordinal_columns, date_columns, categorical) :
        # df = self.load_csv_to_df()
        df = self.feature_engineer(df, continuous_columns, ordinal_columns, date_columns, categorical)
        df = self.select_features(df)
        return df

# continuous_columns = ['Undercarriage_Pad_Width']
categorical_columns = ['Steering_Controls','Pad_Type']
#  'Differential_Type', 'Blade_Type', \
# 'Travel_Controls', 'Grouser_Type', 'Coupler', 'Tip_Control', 'Ripper', \
# 'Hydraulics', 'Engine_Horsepower', 'Transmission', 'Pad_Type', 'Stick', \
# 'ModelID' , 'datasource',  'fiModelDesc' ,'fiBaseModel', 'fiSecondaryDesc', \
# 'fiModelSeries', 'fiModelDescriptor' , 'state', 'ProductGroup', \
# 'ProductGroupDesc', 'Drive_System',  'Enclosure' ,

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
data_class = DataClass('../data/Train.csv')
df = data_class.load_csv_to_df()
#
#EDA
# pcu.info(df)
df = data_class.get_data(df, [], [], [], categorical_columns)
