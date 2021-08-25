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

ParaSet=bb.buildmodel(Xdata,Ydata,40)
Ynew=bb.usemodel(Xnew,ParaSet)

plt.plot(Xdata,Ydata,'*')
plt.plot(Xnew,Ynew)
plt.show()
