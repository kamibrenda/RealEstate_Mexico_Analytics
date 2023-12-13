#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


#importing the libraries and modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #for visualisation


# In[3]:


# importing the dataset in csv format
dfa = pd.read_csv("Mexico_dataset1.csv", encoding = "ISO-8859-1")
dfb = pd.read_csv("Mexico_dataset2.csv", encoding='ISO-8859-2')
dfc = pd.read_csv("Mexico_dataset3.csv", encoding='ISO-8859-3')


# In[4]:


dfa.head()


# In[5]:


dfb.head()


# In[6]:


dfc.head()


# ## Data Wrangling

# In[7]:


#Making a copy of the dataframe
dfacopy = dfa.copy()
dfacopy.info()


# In[8]:


#Making a copy of the dataframe and checking for its datatypes
dfbcopy = dfb.copy()
dfbcopy.info()


# In[9]:


dfccopy = dfc.copy()
dfccopy.info()


# In[10]:


#Checking for the shape of the dataset i.e the number of observations and features
dfacopy.shape


# In[11]:


dfbcopy.shape


# In[12]:


dfccopy.shape


# In[13]:


#Checking for the first 5 rows
dfacopy.head()


# In[14]:


#Checking for the first 5 rows
dfbcopy.head()


# In[15]:


#Checking for the first 5 rows
dfccopy.head()


# In[16]:


#Checking for the values in a particular column-shows frist and last 5
dfacopy['price_usd'] 


# In[17]:


#Checking for the values between observations (50-60) in price.
dfacopy.price_usd[0:10]


# In[18]:


#Dropping null values
dfacopy.dropna(inplace=True)


# In[19]:


dfacopy.info()


# In[20]:


# Ensure 'price' column is of string data type
dfacopy['price_usd'] = dfacopy['price_usd'].astype(str)

"""To drop a column that is not needed or in use then use the method
df.drop(columns=["price"] inplace=True)"""
dfacopy["price_usd"]= (
    dfacopy["price_usd"]
    .str.replace("$" , "", regex=False)
    .str.replace("," , "")
    .astype(float)
)
dfacopy.info()
dfacopy.head()


# In[21]:


dfbcopy.dropna(inplace=True)
dfbcopy.shape


# In[22]:


dfbcopy.head()


# In[23]:


#Convert pesos to usd
dfbcopy["price_usd"] = dfbcopy["price_mxn"] / 19
 
"""To drop a column that is not needed or in use then use the method"""
dfbcopy.drop(columns= ["price_mxn"], inplace=True)


# In[24]:


dfbcopy.head()


# In[25]:


dfccopy.info()
dfccopy.head()


# In[26]:


#Drop null values from dataframe 3
dfccopy.dropna(inplace=True)

dfccopy[["lat", "lon"]] = dfccopy["lat-lon"].str.split(",", expand=True)

dfccopy.head()


# In[27]:


#Create "state" column for dfccopy
dfccopy["state"] = dfccopy["place_with_parent_names"].str.split("|", expand =True)[2].head()

#Drop the column "place_with_parent_names" and "lat-lon" from df3---highlighted out as the column is dropped 
dfccopy.drop(columns=["place_with_parent_names" , "lat-lon"], inplace=True)  

dfccopy.head(5)


# In[28]:


#Concatenation of the 3 cleaned datasets
final_df = pd.concat([dfacopy, dfbcopy, dfccopy])
final_df.info()


# In[29]:


#Saving the final dataframe to a CSV file
final_df.to_csv("C:\\Users\\admin\\Desktop\\Personal_stuff\\Datascience_Pandas_with_python\\Proj1_Housing\\Mexico_clean_final.csv", index = False)


# In[30]:


#Creating a copy of the final Dataframe 
finalcpy_df = final_df.copy()

#Saving the copied dataframe 
finalcpy_df.to_csv("C:\\Users\\admin\\Desktop\\Personal_stuff\\Datascience_Pandas_with_python\\Proj1_Housing\\Mexico_cleancpy_final.csv", index = False)


# # Exploratory Data Analysis

# In[31]:


finalcpy_df.info()
finalcpy_df.head()


# In[32]:


#Loading the clean and conctenated dataset
finalcpy_df = pd.read_csv("Mexico_cleancpy_final.csv")


# In[33]:


finalcpy_df.shape


# In[34]:


finalcpy_df.info()


# In[35]:


final_df.head(20)


# In[36]:


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

# In[37]:


#Displaying the number of unique values in the "state" column
finalcpy_df["state"].nunique()


# In[38]:


#Displaying the unique value in the "state" column
finalcpy_df["state"].unique()


# In[39]:


#Displaying the value count of the unique values in the "state" column 
finalcpy_df["state"].value_counts().head(10)


# # Descriptive Statistics

# In[40]:


finalcpy_df[["area_m2","price_usd"]].describe()


# ## Visualisation of the data

# ### Histogram to compare the frequency distribution between "area_m2" and "price_usd"

# In[41]:


#AREA_M2
plt.hist(finalcpy_df["area_m2"] , bins=10)
plt.xlabel("Area [sq meters]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Sizes");


# ### Conclusion
# The histogram above is skewed to the right which is demonstated with most of the home size distribution data lying between 50 sq. metres to 200 sq. metres.

# In[42]:


#PRICE_USD
plt.hist(finalcpy_df["price_usd"], bins=10)
plt.xlabel("Price USD")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices");


# ### Conclusion
# The price_usd column is skewed to the right and most of the prices paid range between 50,000 to 150,000 USD

# ### Boxplot to compare the frequency distribution between "area_m2" and "price_usd"

# In[43]:


#AREA_M2
plt.boxplot(finalcpy_df["area_m2"], vert=False)
plt.xlabel("Area [sq meters]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Sizes");


# From the box plot of the area_m2 the box plot is skewed to the right as most of the properties lie on the lower bounds of the box plot and thus most properties are smaller in size.

# In[44]:


#PRICE_USD
plt.boxplot(finalcpy_df["price_usd"], vert=False)
plt.xlabel("Price USD")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices");


# ### Conclusion
# From the box plot of the price_usd the distribution is skewed to the right with the presence of outliers that are present outside the whiskers.

# ## Research Questions for further analysis

# 1. Which state has the most expensive real estate market?

# In[45]:


finalcpy_df.head()


# In[46]:


#Calculating price per m2 using "price_usd" and "area_m2"
finalcpy_df["price_per_m2"] = finalcpy_df["price_usd"] / finalcpy_df["area_m2"]
finalcpy_df.head()


# In[47]:


#Using the groupby method with visualisation
(
    finalcpy_df
    .groupby("state")
    ["price_per_m2"].mean()
    .sort_values(ascending=False)
    .plot(
           kind="bar",
        xlabel="State",
        ylabel="Mean Price per M^2[USD]",
        title="Mean House Price per M^2 by State"        
    )
);

From the bar chart above, it is shown that the most expensive state to live in would be Distrito Federal.
# 2. Is there a relationship between home size and price?

# In[48]:


#Creating a scatter plot to compare "price_usd" vs "Area_m2"
plt.scatter(x=finalcpy_df["price_usd"], y=finalcpy_df["area_m2"])
plt.xlabel("price_usd")
plt.ylabel("area_m2")
plt.title("Area [sq meters]")
plt.show()  # This line is added to display the plot


# From the scatterplot above, comparing a relationship between the price and area there is a positive correlation thus meaning, an increase in house size results in an increase in price.

# In[49]:


#Calculation of the correlation between the 2 data points
p_correlation = finalcpy_df["area_m2"].corr(finalcpy_df["price_usd"])

# Print correlation coefficient
print("Correlation of 'area_m2' and 'price_usd' (all Mexico):", p_correlation)


# ### Conclusion
# From the correlation done comparing the 2 data points, the correlation coefficient is over 0.5, so there's a moderate relationship house size and price in Mexico.

# ### Subsetting the Dataframe 

# In[50]:


#Subseting to analyse the state of "Pahang"
df_guerrero =  finalcpy_df[finalcpy_df["state"] == "Guerrero"]
df_guerrero.head()


# In[51]:


#A scatter plot of the state of Pahang comparing Price vs Area
plt.scatter(x=df_guerrero["area_m2"], y=df_guerrero["price_usd"])
plt.xlabel("area_m2")
plt.ylabel("price_usd")
plt.title("Guerrero: Price vs. Area")


# In[52]:


#Calculating the correlation coeeficient of the state of Pahang
p_correlation = df_guerrero["area_m2"].corr(df_guerrero["price_usd"])
print("Correlation of 'area_m2' and 'price_usd' (Guerrero):", p_correlation)


# ### Conclusion
# From further analysis done specifically in the state of "Guerrero" it is observed there is a relationshipbetween the area_m2 and the price_usd which is backed up with the correlation of 0.6 hence an increase in area_m2 results in an increase in the price.

# In[ ]:




