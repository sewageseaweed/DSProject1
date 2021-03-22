# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:58:59 2021

@author: Clyde
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# clyde
df = pd.read_csv(r"C:\Users\Clyde\Desktop\Crash_Reporting_-_Drivers_Data.csv")

# daniel
# df =  pd.read_csv("/home/daniel/Documents/cst383/project/Crash_Reporting_-_Drivers_Data.csv")

print(df.columns)
df['Driver Distracted By'].value_counts()
df['Driver Distracted By'].isna().sum()

df.shape

#121,400 Rows
#44 Columns



df.isna().sum().sum()
#703278 Rows that are NA

df.isna().sum() / len(df)
#This is the fraction of na values per column in a scale of 0-1.


#drop municipilaty, off road desc, related non motor, non-motorist substance abuse, Non-Motorist Substance Abuse Maybe? 

df['Non-Motorist Substance Abuse'].value_counts()

#Severity injury with distraction, equip problems with both.
#Vehicle year, make, model, with injury severity/equipment problems

#

############# PLOT 1 #############
# CHECKS IF DISTRACTED and Imputes if they are distracted or not 
def distracted(x):
    if x == 'NOT DISTRACTED':
        return False
    return True
# NEW COLUMN IN df
df['DISTRACTED'] = df['Driver Distracted By'].apply(distracted)

# PLOT 
plt.figure(figsize=(30,15))
for i in enumerate(df['Injury Severity'].unique()):
    plt.subplot(1,5, i[0]+1)
    plt.title(i[1])
    sns.countplot(x='DISTRACTED', data= df[ df['Injury Severity'] == i[1] ])
    plt.rc('xtick',labelsize=8)
    plt.ylabel("Events")
plt.suptitle("Distraction in Injury Severity", fontsize=20, weight = 'bold')

############# PLOT 2 #############

# Cleans 'Driver Distracted By'
def phone(x):
    if 'CELL PHONE' in x:
        return 'CELL PHONE'
    return x
df['Driver Distracted By'] = df['Driver Distracted By'].apply(phone)

# PLOT
plt.figure(figsize=(15,20))
for i in enumerate(df['Injury Severity'].unique()):
    plt.subplot(5,1, i[0]+1)
    sns.countplot(y='Driver Distracted By', data= df[ (df['Injury Severity'] == i[1]) & (df['Driver Distracted By'] != 'NOT DISTRACTED') ])
    plt.rc('xtick',labelsize=8)
    plt.xlabel("")
    plt.ylabel("Distraction")
    plt.title(i[1])
plt.suptitle("Distraction Type in Injury Severity", fontsize=15, weight = 'bold')


df.columns

#Cross tab of different injury types and if they were distracted or not
distract_injury_cross = pd.crosstab(df['DISTRACTED'], df['Injury Severity'])

distract_injury_cross.plot.bar()
##THIS DOESNT LOOK TOO USEFUL VVVV
#df['Vehicle Body Type'].value_counts()
#df['Vehicle Body Type'].isna().sum()

#Impute NA Data to Unknown
#df['Vehicle Body Type'].replace(to_replace = np.nan, value="UNKNOWN", inplace=True)

#carType_injury_cross = pd.crosstab(df['Vehicle Body Type'], df['Injury Severity'])
#carType_injury_cross.plot.bar()

#Drop columns we dont need

#df.drop(columns=['Report Number', 'Local Case Number', 'Agency Name', ], axis=1, inplace = True)

df['Collision Type'].value_counts()
df['Collision Type'].isna().sum()
df['Collision Type'].replace(to_replace = np.nan, value = "UNKNOWN", inplace=True)
collision_injury_cross = pd.crosstab(df['Collision Type'],df['Injury Severity'])
collision_injury_cross.plot.bar()

df['Vehicle Damage Extent'].value_counts()
df['Vehicle Damage Extent'].isna().sum()
damage_injury_cross = pd.crosstab(df['Vehicle Damage Extent'],df['Injury Severity'])
damage_injury_cross.plot.bar()
