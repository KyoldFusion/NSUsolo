#!/usr/bin/env python
# coding: utf-8

# ### Pymaceuticals Skill Drill - Day 1

# Congratulations, you are hired by Pymaceuticals Inc., one of the leading imaginary pharmaceutical companies that specializes in anti-cancer pharmaceuticals, to assist their senior scientist team in the effort to begin screening for potential treatments for squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.
# 
# In this study, 249 mice identified with SCC tumor growth were treated through a variety of drug regimens. Over the course of 45 days, tumor development was observed and measured. The purpose of this study was to compare the performance of Pymaceuticals' drug of interest, Capomulin, versus the other treatment regimens. You have been tasked by the senior scientist team to generate an initial drug regimens comparison and generate a summary of your findings. 
# 
# For this skill drill, you will walk through the steps of a basic analysis and visualize our dataset using a new type of visualization - a box and whisker plot. Although we have provided all of the steps required to produce each output, there may be some new concepts and/or terminology in this skill drill you may not have seen before. If you are ever stuck or confused, try googling some of the terms or check out the resource links we provide throughout the activity. You got this!

# ### Data Cleaning 

# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


# Import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[12]:


# Read the mouse data and the study results
mousePD = pd.read_csv('../Resources/mouse_metadata.csv')


# In[13]:


# Display the mouse data
mousePD


# In[11]:


# Display the study data
studyPD = pd.read_csv('../Resources/Study_results.csv')
studyPD


# In[8]:


# Combine the data into a single dataset and display it
MSpd = pd.merge(studyPD, mousePD, how="left", on="Mouse ID")
MSpd


# In[31]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
Dupes = MSpd.loc[MSpd.duplicated(subset=['Mouse ID', 'Timepoint']),'Mouse ID'].unique()
Dupes


# In[8]:


# Optional: Get all the data for the duplicate mouse ID. 


# In[40]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID and display it
CleanPD = MSpd[MSpd['Mouse ID'].isin(Dupes)==False]
CleanPD


# ### Generating the Boxplot

# In[53]:


# Determine the final timepoint for each mouse.
mouse = CleanPD.groupby(['Mouse ID', 'Timepoint'])
# Start by getting the greatest timepoint for each mouse
MaxStat = mouse.max()


# In[43]:


# Join the newly created `.max()` dataframe to the dataframe from Part 1
SSdf = pd.merge(MaxStat, CleanPD)
SSdf


# In[55]:


# Create a list with all 10 drug regimens.
Dlist = list(SSdf['Drug Regimen'].unique())
# Create a empty list to fill with the tumor vol data
Tlist = []
# Isolate (filter) each mice on each drug to collect their tumor volume.
# Locate the rows which match the drug and get the final tumor volumes of all mice
# Append the outcome to the empty list previously created.
for i in Dlist:
    v = MaxStat.loc[MaxStat['Drug Regimen'] == i]['Tumor Volume (mm3)']
    Tlist.append(v)


# In[63]:


# Create a boxplot that visualizes the final tumor volume of all mice in the study across all drug regimens.
plt.title("Tumor Volume")
plt.boxplot(Tlist, 1, 'o', showfliers=True, labels=Dlist)
plt.show()
# Define a custom shape for all outliers in the visualization


# In[61]:


# Create horizontal box and whisker plot
plt.title("Tumor Volume")
plt.boxplot(Tlist, 1, 'rD', showfliers=True, labels=Dlist, vert=False)
plt.show()


# In[ ]:




