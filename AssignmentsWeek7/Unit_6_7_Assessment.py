#!/usr/bin/env python
# coding: utf-8

# 1. Which is the best schema for creating a new database table called weather_history?
# 
# a. 
# ```
# CREATE TABLE weatherhistory (
#   date VARCHAR NOT NULL,
#   temperature VARCHAR,
#   rainfall_amount VARCHAR,
# );
# ```
# 
# b. 
# 
# ```
# CREATE TABLE weather_history (
#   date VARCHAR,
#   temperature VARCHAR,
#   rainfall_amount VARCHAR,
# );
# ```
# 
# c. 
# ```
# CREATE TABLE weather_history (
#   date DATE NOT NULL,
#   temperature FLOAT,
#   rainfall_amount INT,
# );
# ```
# 
# d. 
# ```
# CREATE TABLE weather_history (
#   date DATE NOT NULL,
#   temperature FLOAT,
#   rainfall_amount FLOAT,
# );
# ```

# In[ ]:


# Please provide answer below.
D


# 2. Which is the best way to select all from weather_history?
# 
# a. 
# 
# ```
# SELECT ALL FROM weather_history;
# ```
# 
# b. 
# 
# ```
# SELECT date, temperature, rainfall_amount FROM weather_history;
# ```
# 
# c. 
# 
# ```
# SELECT * FROM weather_history;
# ```
# 
# d. 
# 
# ```
# SELECT ALL(*) FROM weather_history;
# ```

# In[ ]:


# Please provide your answer below.
C


# 3. Which is the best way to select temperature and rainfall_amount, then group by date?
# 
# a. 
# 
# ```
# select * FROM weather_history GROUP BY date;
# ```
# 
# b. 
# 
# ```
# select temperature, rainfall_amount FROM weather_history GROUP BY date;
# ```
# 
# c. 
# 
# ```
# select temperature, rainfall_amount FROM weather_history;
# ```
# 
# d. 
# 
# ```
# select * FROM weather_history GROUP BY temperature, rainfall_amount, date;
# ```

# In[ ]:


# Please provide your answer below.
B


# 4. Which is the best way to find the number of rows in the weather_history database table?
# 
# a. 
# ```
# select count(date) FROM weather_history;
# ```
# 
# b. 
# ```
# select * FROM weather_history;
# ```
# 
# c.
# ```
# select count(*) FROM weather_history;
# ```
# 
# d. 
# ```
# select *, count(*) FROM weather_history;
# ```

# In[ ]:


# Please provide your answer below.
C


# 5. Which CTE is the best example of returning the number of days where the temperature is over 50 degrees?
# 
# a. 
# ```
# WITH greater_than_50 AS (
#   SELECT *
#   FROM weather_history
# )
# SELECT *
# FROM greater_than_50
# WHERE temperature > 50;
# ```
# 
# b.
# ```
# WITH greater_than_50 AS (
#   SELECT *
#   FROM weather_history
#   WHERE temperature > 50
# )
# SELECT *
# FROM greater_than_50
# ```
# 
# c.
# ```
# WITH greater_than_50 AS (
#   SELECT *
#   FROM weather_history
#   WHERE temperature > 50
# )
# ```
# 
# d.
# ```
# SELECT *
# FROM weather_history
# WHERE temperature > 50
# ```

# In[ ]:


# Please provide your answer below.
A


# 6. What is the difference between AWS RDS and AWS S3?
# 
# a. RDS is a file storage service. S3 is a database service.
# 
# b. RDS is a server that can run PySpark code. S3 is a database service.
# 
# c. RDS is a database service. S3 is also a database service.
# 
# d. RDS is a database service. S3 is a file storage service.

# In[ ]:


# Please provide your answer below.
D


# 7. Which method should be used to change the data type of a DataFrame column in PySpark?
# 
# a. 
# ```
# dataType()
# ```
# 
# b. 
# ```
# withType()
# ```
# 
# c.
# ```
# withColumn()
# ```
# 
# d. 
# ```
# changeColumn()
# ```

# In[ ]:


# Please provide your answer below.
C


# 8. Which standard parameters are needed to insert into an RDS Postgres database table?
# 
# a.
# ```
# database_table, username, password, url, column_count
# ```
# 
# b.
# ```
# database_table, username, password
# ```
# 
# c. 
# ```
# username, password, url
# ```
# 
# d.
# ```
# username, password, driver
# ```

# In[ ]:


# Please provide your answer below.
B


# 9. Suppose you had a dataframe with columns called transaction_id, item_id, and item_cost. What is the correct way to group all of the item_id’s together using PySpark such that it creates a new dataframe?
# 
# a. 
# ```
# transaction_df.groupBy('item_id')
# ```
# 
# b. 
# ```
# transaction_df.groupBy('item_cost')
# ```
# 
# c. 
# ```
# transactionGroups = transaction_df.groupBy('item_id')
# ```
# 
# d. 
# ```
# transaction_df['item_id']
# ```

# In[ ]:


# Please provide your answer below.
A


# 10. What is the correct way to filter the dataframe such that we create a new dataframe with only items that cost more than $50?
# 
# a.
# ```
# transaction_df = transaction_df['item_cost>50']
# ```
# 
# b. 
# ```
# transaction_df = transaction_df['item_cost' > 50]
# ```
# 
# c.
# ```
# transaction_df = transaction_df['item_cost'] > 50
# ```
# 
# d.
# ```
# transaction_df = transaction_df.filter('item_cost>50').show()
# ```

# In[ ]:


# Please provide your answer below.
B

