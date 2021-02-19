#!/usr/bin/env python
# coding: utf-8

# ### Pymaceuticals Skill Drill - Day 1

# Congratulations, you are hired by Pymaceuticals Inc., one of the leading imaginary pharmaceutical companies that specializes in anti-cancer pharmaceuticals, to assist their senior scientist team in the effort to begin screening for potential treatments for squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.
# 
# In this study, 249 mice identified with SCC tumor growth were treated through a variety of drug regimens. Over the course of 45 days, tumor development was observed and measured. The purpose of this study was to compare the performance of Pymaceuticals' drug of interest, Capomulin, versus the other treatment regimens. You have been tasked by the senior scientist team to generate an initial drug regimens comparison and generate a summary of your findings. 
# 
# For this skill drill, you will walk through the steps of a basic analysis and visualize our dataset using a new type of visualization - a box and whisker plot. Although we have provided all of the steps required to produce each output, there may be some new concepts and/or terminology in this skill drill you may not have seen before. If you are ever stuck or confused, try googling some of the terms or check out the resource links we provide throughout the activity. You got this!

# ### Data Cleaning 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


# Import dependencies
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


# Read the mouse data and the study results
mouse = pd.read_csv('../Resources/Mouse_metadata.csv')
study = pd.read_csv('../Resources/Study_results.csv')


# In[4]:


# Display the mouse data
mouse.head()


# In[5]:


# Display the study data
study.head()


# In[6]:


# Combine the data into a single dataset and display it
study_data_complete = pd.merge(study, mouse, how="left", on="Mouse ID")
study_data_complete.head()


# In[7]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
duplicate_mouse_ids = study_data_complete.loc[study_data_complete.duplicated(subset=['Mouse ID', 'Timepoint']),'Mouse ID'].unique()
duplicate_mouse_ids


# In[8]:


# Optional: Get all the data for the duplicate mouse ID. 
duplicate_mouse_data = study_data_complete.loc[study_data_complete["Mouse ID"] == "g989"]
duplicate_mouse_data


# In[9]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID and display it
clean_study_data_complete = study_data_complete[study_data_complete['Mouse ID'].isin(duplicate_mouse_ids)==False]
clean_study_data_complete.head()


# In[10]:


def sex_to_num(sex):
    if sex == "Male":
        return 0
    if sex == "Female":
        return 1


# In[11]:


clean_study_data_complete["Sex_num"] = clean_study_data_complete["Sex"].map(sex_to_num)


# In[12]:


clean_study_data_complete.head()


# ### Quartiles, Outliers and Boxplots

# In[13]:


# Determine the final timepoint for each mouse.

# Start by getting the greatest timepoint for each mouse
max_tumor = clean_study_data_complete.groupby(['Mouse ID'])['Timepoint'].max()
max_tumor = max_tumor.reset_index()
max_tumor.head()


# In[14]:


# Join the newly created `.max()` dataframe to the dataframe from Part 1
merged_data = max_tumor.merge(clean_study_data_complete, on=['Mouse ID', 'Timepoint'], how='left')
merged_data.head()


# In[15]:


# Create a list with all 10 drug regimens.
treatment_list = ['Infubinol', 'Placebo', 'Ceftamin', 'Stelasyn', 'Zoniferol',
       'Ramicane', 'Ketapril', 'Propriva', 'Naftisol', 'Capomulin']

# Create a empty list to fill with the tumor vol data
tumor_vol_list = []

# Isolate (filter) each mice on each drug to collect their tumor volume.
for drug in treatment_list:

    # Locate the rows which match the drug and get the final tumor volumes of all mice
    final_tumor_vol = merged_data.loc[merged_data['Drug Regimen'] == drug]['Tumor Volume (mm3)']
        
    # Append the outcome to the empty list previously created.
    tumor_vol_list.append(final_tumor_vol)


# In[16]:


# Create a boxplot that visualizes the final tumor volume of all mice in the study across all drug regimens.

# Define a custom shape for all outliers in the visualization
red_circle = dict(markerfacecolor='r', marker='o')

# Create horizontal box and whisker plot
plt.boxplot(tumor_vol_list, labels = treatment_list, flierprops=red_circle)
plt.xlabel('Final Tumor Volume (mm3)')
plt.show()


# In[17]:


# Assign drugs into a list
treatment_list = ['Infubinol', 'Placebo', 'Ceftamin', 'Stelasyn', 'Zoniferol',
       'Ramicane', 'Ketapril', 'Propriva', 'Naftisol', 'Capomulin']

# create a empty list to fill with the tumor vol data
tumor_vol_list = []

##Calculate the IQR and quantitatively determine if there are any potential outliers. 
for drug in treatment_list:

    # Locate the rows which contain mice on each drug and get the tumor volumes
    final_tumor_vol = merged_data.loc[merged_data['Drug Regimen'] == drug]['Tumor Volume (mm3)']
    # Append to tumor_vol_list
    tumor_vol_list.append(final_tumor_vol)
    
    # Determine outliers using upper and lower bounds
    quartiles = final_tumor_vol.quantile([.25,.5,.75])
    q_one = quartiles[0.25]
    q_three = quartiles[0.75]
    iqr = q_three - q_one
    lower_bound = q_one - (1.5*iqr)
    upper_bound = q_three + (1.5*iqr)
    outliers = final_tumor_vol.loc[(final_tumor_vol < lower_bound) | (final_tumor_vol > upper_bound)]
    print(f"{drug}'s potential outliers: {outliers}")


# ### Analysis

# In[18]:


Caster = []
for x in treatment_list:
    Keys = merged_data.loc[merged_data['Drug Regimen'] == x]['Tumor Volume (mm3)'].max()
    #Keys = merged_data.loc[merged_data['Drug Regimen'] == x][['Drug Regimen', 'Tumor Volume (mm3)']]
    Caster.append(Keys)
Caster


# In[ ]:





# In[19]:


GG = pd.DataFrame()
for drug in treatment_list:
    final_tumor_vol1 = merged_data.loc[merged_data['Drug Regimen'] == drug][['Sex_num', 'Tumor Volume (mm3)', 'Drug Regimen', 'Age_months']].max()
    final_tumor_df = pd.DataFrame(final_tumor_vol1)
    GG = GG.append(final_tumor_df.transpose(), ignore_index=True)
GG
    # Append to tumor_vol_list


# In[20]:


GG = GG.append(final_tumor_df.transpose(), ignore_index=True)
GG


# In[21]:


TempGG = list(GG['Tumor Volume (mm3)'])
GGmax = merged_data[merged_data['Tumor Volume (mm3)'].isin(TempGG)]
GGmax[['Sex_num', 'Tumor Volume (mm3)', 'Drug Regimen']]


# In[ ]:





# In[22]:


fig, axs = plt.subplots(2,2)


# In[23]:


colors = [(1,0,0),(0,1,0),(0,0,1)]


# In[24]:


im4 = axs[1,1]
axs[0,0].boxplot(tumor_vol_list, labels=treatment_list)
axs[0, 0].set_title('Axis [0, 0]')
axs[0,1].set_title('Axis [0, 1]')
#y = np.arange(len(treatment_list))
axs[0, 1].barh(treatment_list, Caster)
axs[1,0].set_title('Axis [1,0]')
axs[1,1].set_title('Axis [1,1]')
axs[1,0].scatter(GGmax['Drug Regimen'], GGmax['Tumor Volume (mm3)'], c=GGmax['Sex_num'])
axs[1,1].scatter(GGmax['Drug Regimen'], GGmax['Tumor Volume (mm3)'], c=GGmax['Age_months'],cmap='twilight')

