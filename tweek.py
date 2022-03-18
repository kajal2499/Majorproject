#!/usr/bin/env python
# coding: utf-8

# In[1]:


file= open("/ml/conf.txt", "r")
count=int(file.readline())

neuron=int(file.readline())
epoch=int(file.readline())
file.close()


# In[2]:


count+=1


# In[3]:





# In[4]:


epoch*=2


# In[5]:


file= open("/ml/conf.txt", "w")
file.write(str(count)+"\n"+str(neuron)+"\n"+str(epoch))
file.close()


# In[ ]:




