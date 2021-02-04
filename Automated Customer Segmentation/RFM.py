import matplotlib as plt
import numpy as np
import pandas as pd

# %matplotlib inline  
# import warnings
# warnings.filterwarnings('ignore')
# url = 'https://github.com/tristanga/Data-Analysis/raw/master/Global%20Superstore.xls'
# df = pd.read_excel(url)
# df = df[(df.Segment == 'Consumer') & (df.Country == 'United States')]
# df.head()

class  rfm:
    def __init__(self):
        
        # data = pd.read_csv('data.csv')
        # df = pd.DataFrame(data)
        df = pd.read_excel('GlobalSuperstore.xls')
        self.df = df
        
    def dataframe(self,f_stream):
        df = pd.read_csv(f_stream)
        # df = df[(df.Segment == 'Consumer') & (df.Country == 'United States')]
        
        return df
    
    def data(self):
        # data = pd.read_csv('data.csv')
        # df = pd.DataFrame(data)
        # url = 'https://github.com/tristanga/Data-Analysis/raw/master/Global%20Superstore.xls'
        # df = pd.read_excel(url)
        return self.df

    def rfm_features(self,df,Customer_ID,Order_date,orderID,Sales):
        df_RFM = df.groupby(Customer_ID).agg({Order_date: lambda y: (df[Order_date].max().date() - y.max().date()).days,
                                        orderID: lambda y: len(y.unique()),  
                                        Sales: lambda y: round(y.sum(),2)})
        
        df_RFM.columns = ['Recency', 'Frequency', 'Monetary']
        df_RFM = df_RFM.sort_values('Monetary', ascending=False)
        return df_RFM

    def automate_segmentation(self,df_RFM):
        
        quantiles = df_RFM.quantile(q=[0.8])
        df_RFM['R']=np.where(df_RFM['Recency']<=int(quantiles.Recency.values), 2, 1)
        df_RFM['F']=np.where(df_RFM['Frequency']>=int(quantiles.Frequency.values), 2, 1)
        df_RFM['M']=np.where(df_RFM['Monetary']>=int(quantiles.Monetary.values), 2, 1)
    
        return df_RFM
    
    def RFM_score(self,df_RFM, select_1):
        df_RFM['RMScore'] = df_RFM.M.map(str)+df_RFM.R.map(str)
        df_RFM = df_RFM.reset_index()
        df_RFM_SUM = df_RFM.groupby('RMScore').agg({str(select_1): lambda y: len(y.unique()),
                                                'Frequency': lambda y: round(y.mean(),0),
                                                'Recency': lambda y: round(y.mean(),0),
                                                'R': lambda y: round(y.mean(),0),
                                                'M': lambda y: round(y.mean(),0),
                                                'Monetary': lambda y: round(y.mean(),0)})
        df_RFM_SUM = df_RFM_SUM.sort_values('RMScore', ascending=False)
        return df_RFM_SUM

    def Value_Matrix(self,df_RFM_SUM):
        
        df_RFM_M = df_RFM_SUM.pivot(index='M', columns='R', values='Monetary')
        df_RFM_M= df_RFM_M.reset_index().sort_values(['M'], ascending = False).set_index(['M'])

        df_RFM_C = df_RFM_SUM.pivot(index='M', columns='R', values='Customer ID')
        df_RFM_C= df_RFM_C.reset_index().sort_values(['M'], ascending = False).set_index(['M'])

        df_RFM_R = df_RFM_SUM.pivot(index='M', columns='R', values='Recency')
        df_RFM_R= df_RFM_R.reset_index().sort_values(['M'], ascending = False).set_index(['M'])
        
        return df_RFM_M, df_RFM_C, df_RFM_R