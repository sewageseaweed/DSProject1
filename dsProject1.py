# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:58:59 2021

@author: Clyde
"""

import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Clyde\Desktop\Crash_Reporting_-_Drivers_Data.csv")

print(df.columns)
df['Driver Distracted By'].value_counts()
df['Driver Distracted By'].isna().sum()

df.shape

df.isna().sum()
#drop municipilaty, off road desc, related non motor, non-motorist substance abuse, Non-Motorist Substance Abuse Maybe? 

df['Non-Motorist Substance Abuse'].value_counts()

#Severity injury with distraction, equip problems with both.
#Vehicle year, make, model, with injury severity/equipment problems


df[]