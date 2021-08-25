# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:10:56 2021

@author: npkn
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file='DataCSV.csv'
dataIN = pd.read_csv(file)
Xdata=dataIN['Xdata']
Ydata=dataIN['Ydata']
file='DataCSV_Xnew.csv'
dataIN = pd.read_csv(file)
Xnew=dataIN['Xnew']

from buildingblocks import bb
Ynew=bb.interpolate(Xdata,Ydata,Xnew,40)

plt.figure()
# fig1=plt.plot(Xdata,Ydata,'*')
plt.plot(Xdata,Ydata,'*')
# plt.figure()
plt.plot(Xnew,Ynew)

