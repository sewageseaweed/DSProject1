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
# df = pd.read_csv(r"C:\Users\Clyde\Desktop\Crash_Reporting_-_Drivers_Data.csv")

# daniel
df =  pd.read_csv("/home/daniel/Documents/cst383/project/Crash_Reporting_-_Drivers_Data.csv")

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
# What are the most common distraction types in car accidents in Montgomery County?
df['Driver Distracted By'].value_counts().plot.bar()
plt.title("Most Common Distraction Types")
plt.ylabel("Count")
plt.xlabel("Distraction")


############# PLOT 2 #############

# Most of the column 'Driver Distracted By' is made up of a handful of values and many values can be combined into one.
def clean(val):
    if 'CELLULAR PHONE' in val:
      return 'DEVICE OR OBJECT'
    if val in ['LOOKED BUT DID NOT SEE', 'INATTENTIVE OR LOST IN THOUGHT']:
      return 'INATTENTIVE'
    if val in ['OTHER ELECTRONIC DEVICE (NAVIGATIONAL PALM PILOT)', 'USING DEVICE OBJECT BROUGHT INTO VEHICLE', 'SMOKING RELATED', 'BY MOVING OBJECT IN VEHICLE', 'EATING OR DRINKING', 'DEVICE']:
      return 'DEVICE OR OBJECT'
    if val in ['USING OTHER DEVICE CONTROLS INTEGRAL TO VEHICLE', 'ADJUSTING AUDIO AND OR CLIMATE CONTROLS']:
      return 'VEHICLE CONTROLS'
    if val =='DISTRACTED BY OUTSIDE PERSON OBJECT OR EVENT':
      return 'OUTSIDE'
    return val

df['Driver Distracted By'] = df['Driver Distracted By'].apply(clean)

df['Driver Distracted By'].value_counts().plot.bar()

plt.title("Most Common Distraction Types")
plt.ylabel("Count")
plt.xlabel("Distraction")
plt.xticks(rotation = 65);

############# PLOT 3 #############
# How does the distraction type relate to injury severity?
dist = df[~df['Driver Distracted By'].isin(['NOT DISTRACTED', 'UNKNOWN'])]

pd.crosstab(dist['Driver Distracted By'], dist['Injury Severity']).plot.bar(stacked=True);

####################################################################

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
