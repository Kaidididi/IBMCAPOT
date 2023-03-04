#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd

# Define input
data = {'id': [1,2,3,4,5],
        'isValid': ['false','true','false','true','true'],
        'errorMessage':['ERR_OOM','','ERR_TIME_OUT','','']}

df_in = pd.DataFrame(data)

# Build error list and isValid indicator
error = []
isValid = 'Yes'

for i in range(0,len(df_in)):
    if df_in.loc[i,'isValid'] == 'false':
        error.append(df_in.loc[i,'errorMessage'])
        isValid = 'No'

# Print output
print(isValid)
print(error)

