
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[32]:

dt = pd.read_csv("C:\\Users\\Shijie Wang\\Desktop\\Data Scientist\\GitWeb\\Data till 20180130.csv")
dt = dt[:-2]
dt['Date'] =  pd.to_datetime(dt['Date'])
dt.dtypes


# In[33]:

plt.plot(dt['Date'],dt['Close Price'])
plt.show()
#dt.loc[dt['Date'] > '2017-01-01']


# In[64]:

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


# In[53]:

list([dict(count=1,label='1m',step='month',stepmode='backward'), dict(random="yes")])


# In[54]:

[dict(count=1,label='1m',step='month',stepmode='backward'), dict(random="yes")]


# In[ ]:



