#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# Preprocessing Infected data
infected = pd.read_csv('time_series_covid19_confirmed_global.csv')
infected_aze = infected[infected['Country/Region'] == 'Azerbaijan']
infected_aze


# In[3]:


infected_aze = infected_aze.rename(index={17: 'infected'})
infected_aze


# In[4]:


# Preprocessing Input data
death = pd.read_csv('time_series_covid19_deaths_global.csv')
death_aze = death[death['Country/Region'] == 'Azerbaijan']
death_aze


# In[5]:


death_aze = death_aze.rename(index={17: 'death'})
death_aze


# In[6]:


# Preprocessing Input data
recovered = pd.read_csv('time_series_covid19_recovered_global.csv')
recovered_aze = recovered[recovered['Country/Region'] == 'Azerbaijan']
recovered_aze


# In[7]:


recovered_aze = recovered_aze.rename(index={17: 'recovered'})
recovered_aze


# In[8]:


result = [infected_aze, death_aze, recovered_aze]


# In[9]:


data = pd.concat(result)
data


# In[10]:


del data['Province/State']


# In[11]:


del data['Lat']


# In[12]:


del data['Long']


# In[13]:


del data['Country/Region']


# In[14]:


data


# In[ ]:





# In[15]:


data = data.T


# In[16]:


data


# In[17]:


data = data.tail(36)


# In[ ]:





# In[23]:


# Preprocessing Input data
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)


# In[19]:


X = data.iloc[:,0]
X


# In[20]:


Y = data.iloc[:,1]
Y


# In[21]:


Z = data.iloc[:,2]
Z


# In[24]:


plt.plot(X, label = 'Infected', linewidth=3.5)
plt.plot(Y, label = 'Death', linewidth=3.5)
plt.plot(Z, label = 'Recovered', linewidth=3.5)
plt.xlabel('Time', fontsize = 24)
plt.ylabel('Number of People', fontsize=24)
plt.title('COVID-19 Cases in Azerbaijan', fontsize=24)
plt.legend(fontsize = 17)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




