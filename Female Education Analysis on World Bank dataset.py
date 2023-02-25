#!/usr/bin/env python
# coding: utf-8

# Name: Muhammad Tufail
# 
# ID: 22014806

# # Loading Modules & Data

# In[1]:


# Importing Modules
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading dataset
df = pd.read_csv("API_SE.PRM.CMPT.FE.ZS_DS2_en_csv_v2_4772234.csv", skiprows=4).iloc[:, :-1]
df.head()


# # Preparing Data

# In[ ]:


# FIlling missing values
df.fillna(0, inplace=True)


# In[2]:


# Extracting Valid counties
import pycountry
countries = list(pycountry.countries)
country_names = [country.name for country in countries]

df = df[df["Country Name"].isin(country_names)]


# In[3]:


# Dropping all world records
index = df[df["Country Name"] == "World"].index
df.drop(index, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# # Visualizations

# In[4]:


useless_cols = ["Country Code", "Indicator Name", "Indicator Code"]
df_edu = df.drop(useless_cols, axis=1).set_index("Country Name").iloc[:, :-2]
df_edu.iloc[:, 30:].mean().plot(kind="line", figsize=(14, 5))
plt.title("Average Female Primary Education Completion Rate in whole World", fontsize=18)
plt.show()


# In[5]:


temp = df_edu.iloc[:, 30:].mean(axis=1).sort_values(ascending=False)
temp = temp[temp > 0][9:29]
plt.figure(figsize=(16, 6))
sns.barplot(temp.index, temp.values)
plt.title("Top 20 Countries with Highest Female Primary Education Completion Rate", fontsize=18)
plt.xticks(rotation=90)
plt.show()


# In[42]:


temp = df_edu.mean()
temp = temp[temp>0]

plt.figure(figsize=(10,8))
plt.pie(temp.values, labels=temp.index)
plt.title("Education Completion rate per Year of whole world")
plt.show()
