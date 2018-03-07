
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import urllib.request
import datetime
import csv
import os
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
today


# In[2]:

def get_data(date):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    headers={'User-Agent':user_agent,} 
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2011-01-01&end=' + date
    request=urllib.request.Request(url,None,headers)
    obj = urllib.request.urlopen(request)
    data = json.loads(obj.read().decode('utf-8'))
    series = []
    for k,v in data['bpi'].items():
        series.append([k,v])

    series.sort()
    return series

series = get_data(today)


# In[3]:

series.sort()
series


# In[8]:


path ="C:\\Users\Shijie Wang\\Desktop\\Data Scientist"
filename = os.path.join(path,'Historical Price.csv')
with open(filename, "w",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(series)


# In[18]:

from pathlib import Path
import json
import urllib.request
import datetime
import csv
import os


def get_data(date):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    headers={'User-Agent':user_agent,} 
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2011-01-01&end=' + date
    request=urllib.request.Request(url,None,headers)
    obj = urllib.request.urlopen(request)
    data = json.loads(obj.read().decode('utf-8'))
    series = []
    for k,v in data['bpi'].items():
        series.append([k,v])

    series.sort()
    return series

def daily_data():
    path ="C:\\Users\Shijie Wang\\Desktop\\Data Scientist"
    filename = os.path.join(path,'Historical Price.csv')
    my_file = Path(filename)
    if my_file.is_file() == False:
        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d") 
        series = get_data(today)
        with open(filename, "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerows(series)
    else:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        headers={'User-Agent':user_agent,}
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        request=urllib.request.Request(url,None,headers)
        obj = urllib.request.urlopen(request)
        data = json.loads(obj.read().decode('utf-8'))
        today_date_obj = datetime.datetime.strptime(data['time']['updated'],"%b %d, %Y %H:%M:%S %Z")
        today_str = today_date_obj.strftime("%Y-%m-%d")
        today_series = [today_str,data['bpi']['USD']['rate_float']]
        with open(filename, "a") as f:
            wr = csv.writer(f)
            wr.writerow(today_series)
            f.close()
daily_data()



# In[2]:

dt = pd.read_csv("C:\\Users\\Shijie Wang\\Desktop\\Data Scientist\\GitWeb\\DianBlog\\Data till 20180218.csv")
dt = dt[:-2]
dt['Date'] =  pd.to_datetime(dt['Date'])
dt.dtypes


# #  We could use the basic plot function, but it doesn't look so pretty. We want to examine piecewise trend due to the volatility of price trend

# In[3]:


plt.plot(dt['Date'],dt['Close Price'])
plt.show()
dt


# In[4]:

# test
import plotly.plotly as py
import plotly.tools as tool
import plotly.graph_objs as go
price_idx = go.Scatter(
    x=dt.Date,
    y=dt['Close Price'],
    name = "Close Price",
    line = dict(color = '#17BECF'),
    opacity = 0.8)
data = [price_idx]

layout= dict(
    title = "Bitcoin Price with Slider for Inspection",
    xaxis = dict(
        rangeselector = dict(
            buttons = list([
                    dict(count = 3,
                        label = '3m',
                        step = 'month',
                        stepmode = 'backward'),
                    dict(count = 6,
                        label = '6m',
                        step = 'month',
                        stepmode = 'backward'),
                    dict(count = 12,
                        label = '12m',
                        step = 'month',
                        stepmode= 'backward'),
                    dict(count=2,
                        label = '2y',
                        step = 'year',
                        stepmode = 'backward'),
                    dict(count = 3,
                        label = '3y',
                        step = 'year',
                        stepmode = 'backward'),
                    dict(count = 5,
                        label = '5y',
                        step = 'year',
                        stepmode = 'backward'),
                    dict(step='all')
                ])
            ),
            rangeslider = dict(),
            type = 'date'
        
        )
    )
fig = dict(data = data, layout = layout)
tool.set_credentials_file(username='schwarzsakura', api_key='hGlwMTWkd2MWAuYdnoZK')
py.iplot(fig, filename = "Bitcoin Price with Slider for Inspection")


# # ARIMA: Test for structural breakpoint
# 
# There is no python package for structural breakpoint test and similar function as auto.arima yet. We install rpy2 which creates a framework that can translate Python objects into R objects and create R outputs. 
# 
# ## rpy2 installation guide: 
# 1. Download precomplied binary package at https://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2 based on your python version
# 2. Run ```python pip install \Location\rpy2‑2.8.6‑cp35‑cp35m‑win_amd64.whl``` 
# 3. Setting PATH variables for R_HOME and R_USER
# ```python
# import os
# os.environ['R_HOME'] ='c:\program files\r\r-3.4.3' #where R is insatlled 
# os.environ['R_USER'] = #path where your package rpy2 is installed. You can search rpy2 and open the file location. Also, add RStudio as a user C:\Users\Shijie Wang\Anaconda3\Lib\site-packages\rpy2;C:\Program Files\RStudio\bin
# ```
# 4. Intall any package you need by using ```python utils``` in  ```python imprort r``` 
# ```python 
# from rpy2.robjects.packages import importr
# utils = importr('utils')
# utils.install_packages('MASS')
# ```

# In[5]:

#import rpy2.tests
#import unittest


import os

import rpy2.robjects as robjects
import rpy2.tests
import unittest
from rpy2.robjects.packages import importr
# import R's "base" package
base = importr('base')

# import R's "utils" package
utils = importr('utils')

struc = importr('strucchange')
pi = robjects.r['pi']
pi[0]


# In[36]:



r = robjects.r
dt['tt'] = list(range(1,len(dt)+1))
dt

from rpy2.robjects import r,pandas2ri
pandas2ri.activate()

r_dt = pandas2ri.py2ri(dt)
r_dt.rx(2)


# In[81]:

from rpy2.robjects import r,pandas2ri
pandas2ri.activate()

r = robjects.r
dt['tt'] = list(range(1,len(dt)+1))
dt = dt[dt['Date'] > '2017-01-01']


fmla = robjects.Formula('Close.Price ~ tt')
env = fmla.environment
env['Close.Price'] = dt['Close Price']
env['tt'] = dt['tt']
stats = importr('stats')

lm_basic = stats.lm(fmla)
#brk = struc.breakpoints()
print(base.summary(lm_basic))
type(lm_basic)


# In[82]:

seg = rpackages.importr('segmented')
seg_m = seg.segmented(lm_basic)
#print(base.summary(seg_m))

print(seg_m.names)
print(seg.slope(seg_m))

#using all historical data makes it harder to detect breakpoints


# In[89]:

dt = pd.read_csv("C:\\Users\\Shijie Wang\\Desktop\\Data Scientist\\GitWeb\\DianBlog\\Data past year.csv")
dt = dt[:-2]
dt['Date'] =  pd.to_datetime(dt['Date'])
dt.dtypes
dt['tt'] = list(range(1,len(dt)+1))


fmla = robjects.Formula('Close.Price ~ tt')
env = fmla.environment
env['Close.Price'] = dt['Close Price']
env['tt'] = dt['tt']
stats = importr('stats')

lm_basic = stats.lm(fmla)
#brk = struc.breakpoints()
print(base.summary(lm_basic))
type(lm_basic)
psi_v = robjects.IntVector([250,360])
seg_m = seg.segmented(lm_basic, psi = psi_v)
#print(base.summary(seg_m))

print(seg_m.names)
print(seg.slope(seg_m))


# In[92]:

print(seg_m.rx2("psi"))


# In[ ]:



