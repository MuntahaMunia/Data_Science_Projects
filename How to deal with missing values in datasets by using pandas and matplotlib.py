#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pylab as plt
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()


# Identify Missing Values:

# In[2]:


import numpy as np
df.replace("?", np.nan, inplace = True)
df.head(5)


# In[3]:


missing_data = df.isnull()
missing_data.head(5)


# Count missing values in each column:

# In[4]:


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  


# Calculate the average of the column:

# In[5]:


avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)


# In[6]:


df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)


# In[7]:


avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)


# In[8]:


df["bore"].replace(np.nan, avg_bore, inplace=True)


# In[9]:


# calculate the mean vaule for "stroke" column
avg_stroke = df["stroke"].astype("float").mean(axis = 0)
print("Average of stroke:", avg_stroke)

# replace NaN by mean value in "stroke" column
df["stroke"].replace(np.nan, avg_stroke, inplace = True)


# In[10]:


avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)


# In[11]:


df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)


# In[12]:


avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)


# In[13]:


df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)


# In[14]:


df['num-of-doors'].value_counts()


# In[15]:


df['num-of-doors'].value_counts().idxmax()


# In[16]:


#replace the missing 'num-of-doors' values by the most frequent 
df["num-of-doors"].replace(np.nan, "four", inplace=True)


# In[17]:


# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)


# In[18]:


df.head()


# And this is how we can obtain dataset with no missing values :D

# In[ ]:




