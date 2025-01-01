#!/usr/bin/env python
# coding: utf-8

# In[23]:


import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "duckdb"])



# In[24]:


import pandas as pd
import glob
import time
import duckdb

conn = duckdb.connect() # create an in-memory database


# In[25]:


import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])



# In[26]:


# with pandas
cur_time = time.time()
df = pd.concat([pd.read_csv(f) for f in glob.glob('*.csv')])
print(f"time: {(time.time() - cur_time)}")
print(df.head(10))


# In[27]:


# with duckdb
cur_time = time.time()
df = conn.execute("""
	SELECT *
	FROM '*.csv'
	LIMIT 10
""").df()
print(f"time: {(time.time() - cur_time)}")
print(df)


# In[28]:


df = conn.execute("""
	SELECT *
	FROM '*.csv'
""").df()
conn.register("df_view", df)
conn.execute("DESCRIBE df_view").df() # doesn't work if you don't register df as a virtual table


# In[29]:


conn.execute("SELECT COUNT(*) FROM df_view").df()


# In[30]:


df.isnull().sum()
df = df.dropna(how='all')

# Notice we use df and not df_view
# With DuckDB you can run SQL queries on top of Pandas dataframes
conn.execute("SELECT COUNT(*) FROM df").df()


# In[31]:


df.isnull().sum()
df = df.dropna(how='all')

# Notice we use df and not df_view
# With DuckDB you can run SQL queries on top of Pandas dataframes
conn.execute("SELECT COUNT(*) FROM df").df()


# In[32]:


conn.execute("""SELECT * FROM df WHERE "Order ID"='295665'""").df()


# In[37]:


print(df.dtypes)
df["Price"] = df["Price"].str.replace(",", "").astype(float)


# In[38]:


conn.execute("""
CREATE OR REPLACE TABLE sales AS
SELECT
    "Order ID"::INTEGER AS order_id,
    Product AS product,
    "Quantity Ordered"::INTEGER AS quantity,
    "Price"::DECIMAL AS price_each,
    "Order Date"::DATE AS order_date,
    "Purchase Address" AS purchase_address
FROM df
WHERE
    TRY_CAST("Order ID" AS INTEGER) NOTNULL

""")


# In[39]:


# Fetch all rows from the 'sales' table
sales_data = conn.execute("SELECT * FROM sales").fetchdf()
print(sales_data)


# In[ ]:




