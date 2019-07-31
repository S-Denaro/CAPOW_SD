# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:44:59 2019

@author: sdenaro
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

N=200 #number of years

prices_d=pd.read_csv('PNW_daily_prices_merged.csv', usecols=[1])
prices_d=pd.DataFrame(np.reshape(prices_d.values, (364,N)))
prices_d.loc[364,:]=prices_d.loc[363,:]
prices_d=pd.DataFrame(np.reshape(prices_d.values, (N*365,-1)),columns=['MidC'])
#prices_d.to_csv('PNW_prices_200.csv')


n_=10 # number of years you want to plot
plt.figure()
plt.plot(prices_d.loc[0:364*n_,'MidC'])
plt.title('Synthetic MidC prices')
plt.xticks(np.arange(0,364*n_ ,365))


#######
# fix slack variable
SLACK=700 # slack price value

prices_h=pd.read_csv('PNW_hourly_prices_merged.csv',usecols=[1])
prices_h[prices_h==SLACK]=178.583229
prices_h=pd.DataFrame(np.reshape(prices_h.values, (364*24,N)))
last_days=prices_h.loc[24*364-24:24*364,:]
prices_h=prices_h.append(last_days)
prices_h=pd.DataFrame(np.reshape(prices_h.values, (N*365*24,-1)),columns=['MidC'])

no_days=365*N
daily_prices_fix = np.zeros((no_days,1))
for i in range(0,no_days):  
          daily_prices_fix[i] = np.mean(prices_h[i*24:i*24+24])


plt.plot(daily_prices_fix[0:364*n_])

plt.figure()
plt.plot(daily_prices_fix)

plt.figure()
plt.plot(daily_prices_fix[0:364*10])
plt.xticks(np.arange(0,364*10 ,365))

daily_prices_fix=pd.DataFrame(daily_prices_fix, columns=['MidC'])

daily_prices_fix.to_csv('PNW_prices_N_FIX.csv')