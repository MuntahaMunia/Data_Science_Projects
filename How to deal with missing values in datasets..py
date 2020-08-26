#!/usr/bin/env python
# coding: utf-8

# # Data Wrangling:
# Data wrangling is the process of cleaning, structuring and enriching raw data into a desired format for better decision making in less time.

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pylab as plt


# In[8]:


path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()


# Identify Missing Value:

# In[9]:


import numpy as np


# In[10]:


df.replace("?",np.nan, inplace = True)


# In[11]:


df.head(5)


# Evaluting for Missing Data:

# In[12]:


missing_data = df.isnull()
missing_data.head(5)


# Count Missing values in each column:

# In[13]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# Calculate the average of the column:

# In[16]:


avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)


# # How to obtain the dataset with no missing value:

# In[17]:


avg_stroke = df["stroke"].astype("float").mean(axis = 0)
print("Average of stroke:", avg_stroke)


# In[18]:


df["stroke"].replace(np.nan, avg_stroke, inplace = True)


# In[19]:


avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)


# In[20]:


df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)


# In[21]:


avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)


# In[22]:


df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)


# In[23]:


df['num-of-doors'].value_counts()


# In[24]:


df['num-of-doors'].value_counts().idxmax()


# In[25]:


df["num-of-doors"].replace(np.nan, "four", inplace=True)


# In[26]:


df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)


# In[27]:


df.head()


# In[ ]:




