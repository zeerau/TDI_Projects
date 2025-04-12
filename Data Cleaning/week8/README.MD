# Netflix Data Cleaning Project

## Introduction
This project focuses on cleaning and transforming a Netflix dataset to prepare it for analysis. The dataset contains information about Netflix titles, including details such as cast, release year, genres, and more. The goal is to clean the data, standardize formats, and extract meaningful features for further analysis.

## Process
The following steps were performed to clean and transform the dataset:

1. **Data Loading**: The dataset was loaded using Pandas for manipulation.
2. **Initial Exploration**: Inspected the dataset structure, data types, and missing values.
3. **Column Removal**: Removed unnecessary columns like `show_id`, `description`, and `director`.
4. **Handling Missing Values**: Eliminated rows with missing values to ensure data consistency.
5. **Date Transformation**:
   - Converted `date_added` and `release_year` columns to datetime format.
   - Extracted year, month, and day from `date_added`.
6. **Feature Engineering**:
   - Calculated the total number of cast members for each title.
   - Extracted the lead actor's name from the `cast` column.
   - Standardized the `duration` column by converting it into an integer format.
   - Cleaned and capitalized country names in the `country` column.
   - Calculated the number of genres listed for each title.
7. **Final Inspection**: Verified the cleaned dataset by displaying the first few rows.

## Tech Tools
- **Python**: Core programming language used for data manipulation.
- **Pandas**: For data cleaning and transformation.
- **Jupyter Notebook**: For interactive coding and documentation.

## Conclusion
The Netflix dataset was successfully cleaned and transformed. Key outcomes include:
- Removal of unnecessary columns and rows with missing values.
- Standardization of date formats and numeric columns.
- Extraction of new features such as lead actor, cast count, and genre count.
- Cleaned and formatted country names for consistency.

### Tags
- Netflix Data Cleaning
- Data Transformation
- Python Data Analysis
- Feature Engineering
- Jupyter Notebook