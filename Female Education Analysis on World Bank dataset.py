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
