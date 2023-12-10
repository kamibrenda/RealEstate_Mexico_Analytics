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


#importing the dataset in csv format
dfa = pd.read_csv ("Housing-in-Mexico.csv")
dfb = pd.read_csv ("Housing-in-Mexico - 2.csv")
dfc = pd.read_csv ("Housing-in-Mexico - 3.csv")


# In[4]:


#Making a copy of the dataframe
dfacopy = dfa.copy()


# In[5]:


dfbcopy = dfb.copy()


# In[6]:


dfccopy = dfc.copy()


# # Data Wrangling

# In[7]:


#Checking for the shape of the dataset i.e the number of observations and features
dfacopy.shape


# In[8]:


dfbcopy.shape


# In[9]:


dfccopy.shape


# In[10]:


#Checking for the datatypes of the dataset
dfacopy.info()


# In[11]:


dfbcopy.info()


# In[12]:


dfccopy.info()


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


# In[19]:


#dfbcopy.head(20)
dfbcopy.info()
dfbcopy.dropna(inplace=True)


# In[20]:


#Convert pesos to usd
#dfbcopy["price_usd"] = dfbcopy["price_mxn"] / 19
 
"""To drop a column that is not needed or in use then use the method"""
#dfbcopy.drop(columns= ["price_mxn"], inplace=True)


# In[21]:


dfccopy.head()


# In[22]:


# Ensure 'price' column is of string data type
dfccopy['price_usd'] = dfccopy['price_usd'].astype(str)
dfccopy.head()


# In[23]:


#Drop null values from dataframe 3
dfccopy.dropna(inplace=True)

dfccopy[["lat", "lon"]] = dfccopy["lat-lon"].str.split(",", expand=True)

dfccopy.head()


# In[24]:


#Create "state" column for dfccopy
dfccopy["state"] = dfccopy["place_with_parent_names"].str.split("|", expand =True)

#Drop the column "place_with_parent_names" and "lat-lon" from df3---highlighted out as the column is dropped 
dfccopy.drop(columns=["place_with_parent_names" , "lat-lon"], inplace=True)  

dfccopy.head(5)


# In[25]:


#Concatenation of the 3 cleaned datasets
final_df = pd.concat([dfacopy, dfbcopy, dfccopy])
final_df.info()


# In[26]:


finalcpy_df = final_df.copy()
finalcpy_df.head()
finalcpy_df.info()


# In[27]:


#Saving the final dataframe to a CSV file
final_df.to_csv("C:\\Users\\admin\\Desktop\\Personal_stuff\\Datascience_Pandas_with_python\\Proj1_Housing.csv", index = False)
finalcpy_df.to_csv("C:\\Users\\admin\\Desktop\\Personal_stuff\\Datascience_Pandas_with_python\\Proj1_Housing.csv", index = False)


# # Exploratory Data Analysis

# In[28]:


#Loading the clean and conctenated dataset
finalcpy_df = pd.read_csv("Proj1_Housing.csv")


# In[29]:


finalcpy_df.shape


# In[30]:


finalcpy_df.info()


# In[31]:


final_df.head(20)


# In[32]:


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

# In[33]:


#Displaying the number of unique values in the "state" column
finalcpy_df["state"].nunique()


# In[34]:


#Displaying the unique value in the "state" column
finalcpy_df["state"].unique()


# In[35]:


#Displaying the value count of the unique values in the "state" column 
finalcpy_df["state"].value_counts().head(10)


# # Descriptive Statistics

# In[36]:


finalcpy_df[["area_m2","price_usd"]].describe()


# ## Visualisation of the data

# ### Histogram to compare the frequency distribution between "area_m2" and "price_usd"

# In[37]:


#AREA_M2
plt.hist(finalcpy_df["area_m2"] , rwidth=0.8, bins=10)
plt.xlabel("Area [sq meters]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Sizes");


# ### Conclusion
# The histogram which shows the frequency distribution of the column "area_m2" which is normally distributed.

# In[38]:


#PRICE_USD
plt.hist(finalcpy_df["price_usd"], rwidth=0.8, bins=10)
plt.xlabel("Price USD")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices");


# ### Conclusion
# The price_usd column is skewed to the left and most of the prices paid range between 0 to 300,000 USD

# ### Boxplot to compare the frequency distribution between "area_m2" and "price_usd"

# In[39]:


#AREA_M2
plt.boxplot(finalcpy_df["area_m2"], vert=False)
plt.xlabel("Area [sq meters]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Sizes");


# From the box plot of the area_m2 the distribution is fairly centralised  but most of the properties lie on the lower bounds of the box plot and thus most properties are smaller in size.

# In[40]:


#PRICE_USD
plt.boxplot(finalcpy_df["price_usd"], vert=False)
plt.xlabel("Price USD")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices");


# ### Conclusion
# From the box plot of the price_usd the distribution is fairly centralised  but most of the properties lie on the lower bounds of the box plot and thus most people are paying less than 200,000 USD

# ## Research Questions for further analysis

# 1. Which state has the most expensive real estate market?

# In[41]:


finalcpy_df.head()


# In[42]:


#Calculating price per m2 using "price_usd" and "area_m2"
finalcpy_df["price_per_m2"] = finalcpy_df["price_usd"] / finalcpy_df["area_m2"]
finalcpy_df.head()


# In[43]:


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


# 2. Is there a relationship between home size and price?

# In[44]:


#Creating a scatter plot to compare "price_usd" vs "Area_m2"
plt.scatter(x=finalcpy_df["price_usd"], y=finalcpy_df["area_m2"])
plt.xlabel("price_usd")
plt.ylabel("area_m2")
plt.title("Area [sq meters]")
plt.show()  # This line is added to display the plot


# In[45]:


#Calculation of the correlation between the 2 data points
p_correlation = finalcpy_df["area_m2"].corr(finalcpy_df["price_usd"])

# Print correlation coefficient
print("Correlation of 'area_m2' and 'price_usd' (all Mexico):", p_correlation)


# ### Conclusion
# From the visualisation above comparing the price to the area there is little to no correlation according to the result. Hence neither directly influence each other. From the correlation done comparing the 2 data points a 0.06 is an indicator and mathematical representation of the lack of relationship.

# ### Subsetting the Dataframe 

# In[46]:


#Subseting to analyse the state of "Pahang"
df_pahang =  finalcpy_df[finalcpy_df["state"] == "Pahang"]
df_pahang.head()


# In[47]:


#A scatter plot of the state of Pahang comparing Price vs Area
plt.scatter(x=df_pahang["area_m2"], y=df_pahang["price_usd"])
plt.xlabel("area_m2")
plt.ylabel("price_usd")
plt.title("Pahang: Price vs. Area")


# In[48]:


#Calculating the correlation coeeficient of the state of Pahang
p_correlation = df_pahang["area_m2"].corr(df_pahang["price_usd"])
print("Correlation of 'area_m2' and 'price_usd' (Pahang):", p_correlation)


# ### Conclusion
# From further analysis done specifically in the state of "Pahang" it is observed there is no relationship whatseoever between the area_m2 and the price_usd which is also backed up with the correlation of a 0 yet again to demonstrate the lack of a relationship between the 2.
