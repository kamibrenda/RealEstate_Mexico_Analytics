#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


#importing the libraries and modules
import pandas as pd
import numpy as np


# In[3]:


#importing the dataset in csv format
df1 = pd.read_csv ("Housing-in-Mexico.csv")
df2 = pd.read_csv ("Housing-in-Mexico - 2.csv")
df3 = pd.read_csv ("Housing-in-Mexico - 3.csv")


# # Data Wrangling

# In[4]:


#Checking for the shape of the dataset i.e the number of observations and features
df1.shape
df2.shape
df3.shape


# In[5]:


#Checking for the datatypes of the dataset
df1.info()
df2.info()
df3.info()


# In[6]:


#Checking for the first 5 rows
df1.head()


# In[7]:


#Checking for the first 5 rows
df2.head()


# In[8]:


#Checking for the first 5 rows
df3.head()


# In[9]:


#Checking for the values in a particular column-shows frist and last 5
df1['price_usd'] 


# In[10]:


#Checking for the values between observations (50-60) in price.
df1.price_usd[0:10]


# In[11]:


# Ensure 'price' column is of string data type
df1['price_usd'] = df1['price_usd'].astype(str)

"""To drop a column that is not needed or in use then use the method
df.drop(columns=["price"] inplace=True)"""

df1["price_usd"]= (
    df1["price_usd"]
    .str.replace("$" , "", regex=False)
    .str.replace("," , "")
    .astype(float)
)
df1.info()
df1.head()


# In[12]:


# Ensure 'price' column is of string data type
#df2['price_mxn'] = df2['price_mxn'].astype(str)

#Convert pesos to usd
df2["price_usd"] = df2["price_mxn"] / 19
 
"""To drop a column that is not needed or in use then use the method"""
df2.drop(columns= ["price_mxn"], inplace=True)
df2.head()


# In[13]:


# Ensure 'price' column is of string data type
df3['price_usd'] = df3['price_usd'].astype(str)
df3.head()


# In[14]:


#Drop null values from dataframe 3
df3.dropna(inplace=True)

df3[["lat", "lon"]] = df3["lat-lon"].str.split(",", expand=True)

df3.head()


# In[15]:


#Create "state" column for df3
#df3["state"] = df3["place_with_parent_names"].str.split("|", expand =True)

#Drop the column "place_with_parent_names" and "lat-lon" from df3
#df3.drop(columns=["place_with_parent_names" , "lat-lon"], inplace=True)  ---highlighted out as the column is dropped 

df3.head()


# In[16]:


#Concatenation of the 3 cleaned datasets
final_df = pd.concat([df1, df2, df3])
final_df.info()


# In[17]:


#Saving the final dataframe to a CSV file
final_df.to_csv("C:\\Users\\admin\\Desktop\\Personal_stuff\\Datascience_Pandas_with_python\\Proj1_Housing.csv", index = False)


# # Exploratory Data Analysis

# In[18]:


#Loading the clean and conctenated dataset
final_df = pd.read_csv("Proj1_Housing.csv")


# In[19]:


final_df.shape


# In[20]:


final_df.info()


# In[21]:


final_df.head(20)


# In[22]:


#Importing the neccessary libraries for EDA
import matplotlib.pyplot as plt #visualisation
import plotly.express as px

#Plotting a heatmap to display realtime location of the houses using 'lon' and 'lat'
fig = px.scatter_mapbox(
    final_df,
    lat= "lat",
    lon= "lon",
    center={"lat": 19.43, "lon": -99.13}, #To center the map
    width= 600, #width of the map
    height=600, #height of the map
    hover_data = ["price_usd", "state"], #Display the price in USD and the state when hovering 
)

#Add a mapbox_style to figure layout
fig.update_layout(mapbox_style="open-street-map")

#Show the figure
fig.show()
    


# ### Categorical Data

# In[23]:


#Displaying the number of unique values in the "state" column
final_df["state"].nunique()


# In[24]:


#Displaying the unique value in the "state" column
final_df["state"].unique()


# In[25]:


#Displaying the value count of the unique values in the "state" column 
final_df["state"].value_counts().head(10)


# In[26]:


df3["State


# In[ ]:


df3copy = df3.copy()

