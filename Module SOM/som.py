
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom as minisom
from pylab import bone, pcolor,colorbar,plot,show,close

from sklearn.preprocessing import LabelEncoder

class class_som:
    def __init__(self):
        
        data = pd.read_csv('Data.csv')
        # df = pd.DataFrame(data)
        # df = pd.read_excel('Data.xls')
        self.df = data
        
    def dataframe(self,f_stream):
        df = pd.read_csv(f_stream)
        # df = df[(df.Segment == 'Consumer') & (df.Country == 'United States')]
        
        return df

    def func_som(self):
        self.df.drop(["Unnamed: 0","Purpose"],axis=1,inplace=True)
        self.df_null=self.df.columns[self.df.isnull().any()]
        self.df[self.df_null].isnull().sum()
        self.df["Saving accounts"].fillna(method='bfill',inplace=True)
        self.df["Checking account"].fillna(method='ffill',inplace=True)
        self.df_categ = list(self.df.select_dtypes(exclude = ["number"]).columns)
        
        le = LabelEncoder()
        for i in self.df_categ:
            print(self.df[i].unique())
            self.df[i] = le.fit_transform(self.df[i])
        X=self.df.iloc[:, :].values
        y= np.genfromtxt('Data.csv', delimiter=',', usecols=(9), dtype=str)
        t = np.zeros(len(y), dtype=int)
        t[y == 'radio/TV'] = 0
        t[y == 'education'] = 1
        t[y == 'furniture/equipment'] = 2
        t[y == 'car'] = 3
        t[y == 'business'] = 4
        t[y == 'repairs'] = 5
        t[y == 'vacation/others'] = 6
        t[y == 'domestics appliances'] = 7
        
        scaler = MinMaxScaler(feature_range=(0,1))
        X = scaler.fit_transform(X)
        return X
        
    def color_map(self,func_som):
        X= func_som()
        som= minisom(x=10,y=10,input_len=8,sigma=1.0,learning_rate=0.5)
        som.random_weights_init(X)
        som.train_random(data=X, num_iteration=100)
        
        bone()
        pcolor(som.distance_map().T)
        colorbar()
        markers=['o','s','+','-','*','D','p','-s']
        colors=['C0','C1','C2','C3','C4','C5','C6','C7']
        
        # plt.figure(figsize=(10, 10))
        # for i,x in enumerate(X):
        #     w=som.winner(x)
        #     plt.plot(w[0]+0.5,
        #         w[1]+0.5,
        #         markers[t[i]],
        #         markeredgecolor=colors[t[i]],markerfacecolor='None',markersize=10,markeredgewidth=2)
        # # show()
        
        plt.savefig('static/images/plot2.png')
        
        plt.close()
        close()
    
    def color_map2(self,func_som):
        X= func_som()
        som= minisom(x=10,y=10,input_len=8,sigma=1.0,learning_rate=0.5)
        som.random_weights_init(X)
        som.train_random(data=X, num_iteration=100)
        
        # bone()
        # pcolor(som.distance_map().T)
        # colorbar()
        markers=['o','s','+','-','*','D','p','-s']
        colors=['C0','C1','C2','C3','C4','C5','C6','C7']
        
        plt.figure(figsize=(10, 10))
        for i,x in enumerate(X):
            w=som.winner(x)
            plt.plot(w[0]+0.5,
                w[1]+0.5,
                markers[t[i]],
                markeredgecolor=colors[t[i]],markerfacecolor='None',markersize=10,markeredgewidth=2)
        # show()
        
        plt.savefig('static/images/plot2.png')
        
        plt.close()
        close()
        

