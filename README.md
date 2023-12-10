# Mexico Real Estate Analysis

## Overview

Welcome to the Mexico Real Estate Analysis project repository. This project is designed to analyze and gain insights into the real estate market in Mexico. This repository contains a Jupyter notebook that analyzes housing data from different sources, cleans the data, and performs exploratory data analysis (EDA). The goal is to gain insights into the real estate market, explore relationships between variables, and answer specific research questions.

## Data Sources
The housing data is collected from three separate CSV files:

1. `Housing-in-Mexico.csv`
    - Description: ![image](https://github.com/kamibrenda/RealEstate_Mexico_Analytics/assets/42267047/89aca5d6-9a7e-48a1-812b-2419395eafea)

2. `Housing-in-Mexico - 2.csv`
    - Description: ![image](https://github.com/kamibrenda/RealEstate_Mexico_Analytics/assets/42267047/7f751ca3-edd4-4e0d-9e9e-832b1f834b6e)
   
3. `Housing-in-Mexico - 3.csv`
    - Description: ![image](https://github.com/kamibrenda/RealEstate_Mexico_Analytics/assets/42267047/cc9e9edd-bea2-4588-b84a-8a33f61473f4)

## Project Structure
The notebook is organized into the following sections:

1. **Introduction and Setup**
   - Overview of the project.
   - Loading necessary libraries and modules.

2. **Data Loading and Initial Exploration**
   - Importing the dataset from CSV files.
   - Making copies of the dataframes for data wrangling.

3. **Data Wrangling**
   - Checking the shape and data types of the datasets.
   - Handling missing values.
   - Cleaning and formatting the "price_usd" column.
   - Concatenating the three cleaned datasets.

4. **Exploratory Data Analysis (EDA)**
   - Loading the clean and concatenated dataset.
   - Visualizing the geographic distribution of houses using a scatter map.
   - Analyzing categorical data (e.g., unique states and their counts).
   - Descriptive statistics of key numerical columns.

5. **Data Visualization**
   - Histograms to compare frequency distribution of "area_m2" and "price_usd".
   - Boxplots to visualize the distribution of "area_m2" and "price_usd".

6. **Research Questions and Analysis**
   - Investigating the most expensive state in the real estate market.
   - Calculating and visualizing the mean house price per square meter by state.
   - Analyzing the relationship between home size and price.
   - Subsetting the dataframe to analyze the state of "Pahang" and its correlation between area and price.

7. **Conclusion**
   - Summarizing key findings and insights.

8. **Future Work**
   - Proposing research questions for further analysis.

## Conclusion
The analysis provides valuable insights into the housing market, geographic distribution, and relationships between key variables. Further research questions and potential areas for exploration are suggested for future work.

## Usage
To run the notebook, ensure you have the required libraries installed. You can install them using the following command:
```bash
pip install pandas numpy matplotlib plotly
```
Then, execute the notebook cell by cell.

Happy Analyzing!
