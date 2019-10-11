#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:36:16 2019

@author: rahul
"""
import matplotlib.pyplot as plt 
import pandas as pd

data = pd.read_excel('datafile1.xls')
ds=data.loc[:, ['Category','Accounts-2000-01','Accounts-2001-02']]
df=ds['Category'].unique().tolist()
x1=[]
y1=[]
print(df)
for x in df:
	df1=ds.loc[ds['Category']==x]
	x2=sum(df1['Accounts-2000-01'])
	x3=sum(df1['Accounts-2001-02'])
	x1.append(x2)
	y1.append(x3)
print(x1)
plt.figure()

plt.barh(df,x1,align='edge')
plt.xlabel('Accounts-2000-01')
plt.ylabel('Accounts-2001-02')
plt.title('Revenue and Expenditure')

plt.figure()
plt.scatter(x1,y1)
plt.xlabel('Accounts-2000-01')
plt.ylabel('Accounts-2001-02')
plt.title('Revenue and Expenditure')

plt.figure()
ax = data.loc[:, ['Category','Accounts-2000-01','Accounts-2001-02']].boxplot()
ax.set_title('Category wise revenue and expenditure in year 2001-02')
plt.show()