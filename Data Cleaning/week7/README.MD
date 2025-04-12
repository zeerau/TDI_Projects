# Data Cleaning Project - Airbnb NYC Dataset

## Introduction
This project focuses on cleaning and preprocessing the Airbnb NYC dataset (`AB_NYC_2019.csv`) to prepare it for further analysis. The dataset contains information about Airbnb listings in New York City, including details such as host names, room types, prices, and reviews. The goal of this project is to handle missing values, remove duplicates, and standardize the data to ensure its quality and usability for analysis.

## Process
The data cleaning process followed these steps:

1. **Data Loading**:
   - Imported the dataset using `pandas` and displayed the first few rows to understand its structure.

2. **Exploratory Data Analysis**:
   - Checked the dataset size, number of records, and columns.
   - Analyzed data types and identified columns with missing values.

3. **Handling Missing Values**:
   - Dropped the `reviews_per_month` column due to excessive missing values.
   - Replaced missing values in the `host_name` column with "Airbnb".
   - Forward-filled missing values in the `last_review` column.
   - Filled missing values in the `price` column with the mean price.

4. **Removing Duplicates**:
   - Identified and removed duplicate rows based on `name`, `host_id`, and `price`.

5. **Data Transformation**:
   - Standardized text by replacing occurrences of "Kitchen" with "Restaurant" in the `neighbourhood` column.
   - Filtered rows where `name` contains specific keywords like "park".
   - Checked for numeric values in the `host_name` column.

6. **Data Validation**:
   - Verified the data types of columns such as `room_type`.
   - Counted and displayed the most frequent room types and their occurrences.

## Tech Tools
The following tools and libraries were used in this project:
- **Python**: The primary programming language for data cleaning.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Regex**: For pattern matching and text processing.

## Conclusion
The cleaned dataset is now ready for further analysis, such as identifying trends in Airbnb listings, analyzing pricing strategies, and understanding customer preferences. The project successfully handled missing values, removed duplicates, and standardized the data, ensuring its quality and reliability.

## Tags
- Data Cleaning
- Airbnb NYC Dataset
- Python Data Analysis
- Pandas
- Data Preprocessing
- Data Quality