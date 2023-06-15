#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Roll Number: 21KP1A44D0
Student Name: Y.Naga Sasi Kumar
Branch: CSD
Section: B
project Domain: Data Analytics


# In[56]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('dsdbx.xlsx')
df.fillna('Data Science',inplace = True)
print(df.BRANCH)
print(df.info())


# In[57]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loading data from Excel file
df = pd.read_excel('dsdbx.xlsx')

#Data PreProcessing
#print(df.isnull().sum())
df.fillna('Data Science',inplace = True)

#dropping EMAIL & Timestamp column
df.drop(['EMAIL','Timestamp'],axis=1,inplace = True)

#print(df.isnull().sum())
#print(df.shape)
#print(df.describe())

#Changing the Column Names
df.rename(columns = {'Email address':'Gmail','CURRENT SEMEISTER':'SEMISTER','AADHAAR NO':'UIDAI NO'},inplace=True)
print(df.columns)




# In[58]:


df.replace({'7O':70},inplace=True)
print(df) 


# In[59]:


df.info()


# In[60]:


df[(df['CGPA']>8.0)]


# In[61]:


df.nlargest(52,columns=['CGPA'])


# In[62]:


df.nsmallest(52,columns=['CGPA'])


# In[63]:


gr = df.groupby(['AGE','BRANCH'])
gr.first()


# In[64]:


ds_group = df.groupby('COURSE').get_group('DS')
ds_group


# In[65]:


df.replace(['18h'],18,inplace=True)
print(df)


# In[86]:


cse = df.groupby('COURSE').get_group('CSE')
cse


# In[74]:


age18 = df.groupby("AGE").get_group(18)
age18


# In[80]:


age19=df.groupby("AGE").get_group(19)
age19


# In[93]:


age20 = df.groupby("AGE").get_group(20)
age20


# In[69]:


age_21 = df.groupby("AGE").get_group(21)
age_21


# In[84]:


mech = df.groupby('COURSE').get_group('MECH')
mech


# In[75]:


age18.plot.bar(color=['blue','green','yellow'])
age18


# In[30]:





# In[49]:


df.AGE=df.AGE.astype('int16')
df.CGPA=df.CGPA.astype('float16')


# In[72]:


df.info()


# In[81]:


age19.plot.bar(color=['blue','green','yellow'])
age19


# In[54]:


cse_group.plot.bar(color=['blue','green','yellow'])
cse_group


# In[ ]:





# In[53]:





# In[77]:


age19 = age19.plot.bar(color=['blue','green','red'])
age19


# In[82]:


age20 = age20.plot.bar(color=['blue','green','yellow'])
age20


# In[83]:


age_21 = age_21.plot.bar(color=['blue','green','yellow'])
age_21


# In[85]:


mech = mech.plot.bar(color= ['blue','green','yellow'])
mech


# In[87]:


cse = cse.plot.bar(color=['green','red','black'])
cse


# In[95]:


y = age19.CGPA.value_counts()
y


# In[89]:


plt.pie(y,labels=['8.0%','73.0%','0.75%'])
plt.show()


# In[94]:


z = age20.CGPA.value_counts()
z


# In[96]:


plt.scatter(y.head(),y.tail())
plt.show()

