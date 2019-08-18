# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:32:53 2019

@author: Avisha
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
df = pd.read_csv('https://raw.githubusercontent.com/duanalytics/datasets/master/csv/mtcars.csv')
df.to_csv("mtcars")
#from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars