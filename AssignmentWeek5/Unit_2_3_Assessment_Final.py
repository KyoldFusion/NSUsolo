#!/usr/bin/env python
# coding: utf-8

# # Instructions

# Read each question carefully and provide an appropriate answer in the following cells. Depending on the question, you may need to provide code or a text submission. **Be sure to label your answers with the question number for easy identification!**

# **Question 1: Which of the following statements is the correct way to import a csv into a Pandas DataFrame? (2 points)** 
# 
# A. 
# ```python
# import pandas as pd
# infile = pd.read_csv(file_name)
# ```
# 
# 
# B. 
# 
# ```python
# import pandas as pd
# infile = pd.readCSV(file_name)
# ```
# 
# 
# C. 
# 
# ```python
# import pandas as pd
# infile = read_file(file_name)
# ```
# 
# 
# D. 
# 
# ```python
# import pandas as pd
# df.read_file(file_name)
# ```
# 

# In[1]:


# Answer 1
#A


# **Question 2: Create a code block that first imports the `student.json` file into a Pandas dataframe named `grades`, then creates a new dataframe named `passing` that contains only the students whose `Pass/Fail` status equals `PASS`. (5 points)**

# In[2]:


# Answer 2
import pandas as pd


# In[12]:


grades = pd.read_json('student.json')
passing = student[student['Pass/Fail'] == 'PASS']
passing


# **Question 3: Create a code block that creates a Pandas dataframe with the following columns and values: (5 points)**
# 
# * `Stock_Symbol`: AAPL, GOOG, TSLA, KO, MSFT
# * `Company_Name`: Apple, Google, Tesla, Coca-Cola, Microsoft
# * `52_Week_High`: 145.09, 1934.86, 900.40, 60.13, 242.64

# In[32]:


# Answer 3
Info = {
'Stock_Symbol': ['AAPL','GOOG','TSLA','KO','MSFT'],
'Company_Name': ['Apple', 'Google', 'Tesla', 'Coca-Cola', 'Microsoft'],
'52_Week_High': [145.09, 1934.86, 900.40, 60.13, 242.64]
}
Stocks = pd.DataFrame(Info)
Stocks


# **Question 4: Which of the following `git` commands creates a new branch in your local repository? (2 points):**
# 
# A. `git clone`
# 
# B. `git pull <branch name>` 
# 
# C. `git checkout -b <branch name>`
# 
# D. `git push -b <branch name>`

# In[4]:


# Answer 4
#A


# **Question 5: Create a code block that performs the following operations: (10 points)**
# 
#    1. Import the `bitcoin_cash_price.csv` file into a Pandas dataframe called `bitcoin`.
#    
#    2. Import the `dash_price.csv` file into a Pandas dataframe called `dash`.
#    
#    3. Merge the `bitcoin` and `dash` dataframes using the `Date` column as the identifier column. Name this new merged dataframe `crypto`. 
#    
#    4. Create a new `Delta_Volume` column in the `crypto` dataframe that calculates the largest **absolute** difference between the bitcoin `Volume` versus dash `Volume`.
#    
#      * **Hint:** Use `abs()` to calculate absolute value.
#    
#    
#    5. Find the row in the `crypto` dataframe that contains the maximum `Delta_Volume` value. Print the row out. 

# In[134]:


# Answer 5
import pandas as pd
bitcoin = pd.read_csv('bitcoin_cash_price.csv')
dash = pd.read_csv('dash_price.csv')
crypto = bitcoin.merge(dash, how='left', on='Date',)
crypto['Delta_Volume'] = abs(bitcoin['Volume']) - abs(dash['Volume'])
#crypto['Delta_Volume'] = crypto
#bitcoin['Volume']
#dash['Volume']
#crypto
print(max(crypto['Delta_Volume']))


# **Question 6: Which of the following statements adjusts the upper and lower limits on a Matplotlib visualization? (2 points)**
# 
# A. 
# 
# ```python
# import matplotlib.pyplot as plt
# plt.hlines(0,25,0, alpha=0.25)
# ```
# 
# B.
# 
# ```python
# import matplotlib.pyplot as plt
# plt.xlim(0,25)
# plt.ylim(0,25)
# ```
# 
# C.
# ```python
# import matplotlib.pyplot as plt
# plt.grid(0,25,0,25)
# ```
# 
# D.
# ```python
# import matplotlib.pyplot as plt
# plt.upper(0,25)
# plt.lower(0,25)
# ```

# In[6]:


# Answer 6
#B


# **Question 7: Generate a bar plot that visualizes the following Netflix show IMDB ratings: (5 points)**
# 
# `{"Series":["The Witcher","Disenchantment","Tiger King","Ozark","Stranger Things"],"User Ratings":[8.2,7.2,7.6,8.4,8.7]}`

# In[58]:


# Answer 7
import matplotlib.pyplot as plt
data = {
    "Series":["The Witcher","Disenchantment","Tiger King","Ozark","Stranger Things"],
    "User Ratings":[8.2,7.2,7.6,8.4,8.7]
}
df = pd.DataFrame(data)
df.plot.barh(x = 'Series', y='User Ratings', color=['C1','C2','C3','C4','C5'], legend='Series')


# **Question 8: Which of the following statements corretly creates a Matplotlib visualization with four subplots? (2 points)**
# 
# A. `plt.subplot()`
# 
# B. `plt.subplot(1,2,3,4)`
# 
# C. `plt.subplot(1,4)`
# 
# D. `plt.subplot(2,2,1)`

# In[8]:


# Answer 8
#C


# **Question 9: Which of the following Matplotlib methods would you use to add a label to your plot with an arrow pointing to the value? (2 points)**
# 
# A. `plt.annotate()`
# 
# B. `plt.label()`
# 
# C. `plt.show()`
# 
# D. `plt.arrow()`

# In[9]:


# Answer 9
#D


# **Question 10: Create a code block that performs the following operations: (15 points)**
# 
# 1. Import the `earthquakes_database.csv` file into a Pandas dataframe named `earthquakes`
# 
# 2. Retrieve the names of the unique data sources found in the `Source` column within your `earthquakes` dataframe.
# 
#     * **Hint:** There should be 13 data sources.
# 
# 
# 3. Create a Matplotlib scatterplot for each data source that visualizes the `Magnitude` (y-axis) versus `Depth` (x-axis). Be sure to add axis labels to your axes and title each plot with the name of the data source.
# 
#     * **Note:** You will need to filter the `earthquakes` dataframe for each category type.
# 

# In[132]:


# Answer 10
import pandas as pd
import matplotlib.pyplot as plt
earthquakes = pd.read_csv('earthquakes_database.csv')
#Create Unique Array of Sources from Earthquakes
SourceUQ = earthquakes['Source'].unique

#Create DataFrames

ISCGEM = pd.DataFrame(earthquakes[earthquakes['Source'] == 'ISCGEM'])
ISCGEMSUP = pd.DataFrame(earthquakes[earthquakes['Source'] == 'ISCGEMSUP'])
OFFICIAL = pd.DataFrame(earthquakes[earthquakes['Source'] == 'OFFICIAL'])
CI = pd.DataFrame(earthquakes[earthquakes['Source'] == 'CI'])
US = pd.DataFrame(earthquakes[earthquakes['Source'] == 'US'])
NC = pd.DataFrame(earthquakes[earthquakes['Source'] == 'NC'])
GCMT = pd.DataFrame(earthquakes[earthquakes['Source'] == 'GCMT'])
UW = pd.DataFrame(earthquakes[earthquakes['Source'] == 'UW'])
ATLAS = pd.DataFrame(earthquakes[earthquakes['Source'] == 'ATLAS'])
NN = pd.DataFrame(earthquakes[earthquakes['Source'] == 'NN'])
SE = pd.DataFrame(earthquakes[earthquakes['Source'] == 'SE'])
AK = pd.DataFrame(earthquakes[earthquakes['Source'] == 'AK'])
PR = pd.DataFrame(earthquakes[earthquakes['Source'] == 'PR'])

#PlotDataFrames

ISCGEM.plot.scatter(x='Depth',y='Magnitude', colormap='Blues', title='ISCGEM' )
ISCGEMSUP.plot.scatter(x='Depth', y='Magnitude', title='ISCGEMSUP')
OFFICIAL.plot.scatter(x='Depth', y='Magnitude', title='OFFICIAL')
CI.plot.scatter(x='Depth', y='Magnitude', title='CI')
US.plot.scatter(x='Depth', y='Magnitude', title='US')
NC.plot.scatter(x='Depth', y='Magnitude', title='NC')
GCMT.plot.scatter(x='Depth', y='Magnitude', title='GCMT')
UW.plot.scatter(x='Depth', y='Magnitude', title='UW')
ATLAS.plot.scatter(x='Depth', y='Magnitude', title='ATLAS')
NN.plot.scatter(x='Depth', y='Magnitude', title='NN')
SE.plot.scatter(x='Depth', y='Magnitude', title='SE')
AK.plot.scatter(x='Depth', y='Magnitude', title='AK')
PR.plot.scatter(x='Depth', y='Magnitude', title='PR')


# In[101]:


print(SourceUQ)


# In[ ]:




