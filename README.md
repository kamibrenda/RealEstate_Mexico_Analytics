# Mexico Real Estate Analysis

## Overview

Welcome to the Mexico Real Estate Analysis project repository. This project is designed to analyze and gain insights into the real estate market in Mexico. The analysis is based on three distinct datasets, each requiring specific cleaning methods before final consolidation for use in the project.

## Datasets

### 1. Housing-in-Mexico.csv

   - Description: ![image](https://github.com/kamibrenda/RealEstate_Mexico_Analytics/assets/42267047/89aca5d6-9a7e-48a1-812b-2419395eafea)

   - Cleaning Aim: To remove '$' and ',' from the price column and change the datatype to floating-point(float) for manipulation of data with pandas.

### 2. Housing-in-Mexico - 2.csv

   - Description: ![image](https://github.com/kamibrenda/RealEstate_Mexico_Analytics/assets/42267047/7f751ca3-edd4-4e0d-9e9e-832b1f834b6e)

   - Cleaning Method: Dropping a column that is not needed

### 3. Housing-in-Mexico - 3.csv

   - Description: ![image](https://github.com/kamibrenda/RealEstate_Mexico_Analytics/assets/42267047/cc9e9edd-bea2-4588-b84a-8a33f61473f4)

   - Cleaning Method: Creating "lat" and "lon" columns for df3 after splitting and dropping the column "place_with_parent_names".

## Tools and Technologies

The project is implemented using the following tools and technologies:

- **Python**: The primary programming language used for data analysis and manipulation.
- **Jupyter Lab/Notebook**: The interactive computing environment for running code, visualizing data, and documenting the analysis process.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone [repository_url]
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Open the Jupyter Notebook or Jupyter Lab:

    ```bash
    jupyter notebook
    ```

    or

    ```bash
    jupyter lab
    ```

4. Navigate to the main analysis notebook and run the cells to execute the analysis.

## Contributing

If you would like to contribute to this project, please follow the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

Happy Analyzing!
