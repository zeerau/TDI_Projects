# Wine Ratings Data Cleaning Project

## Introduction
This project focuses on cleaning and analyzing a global wine quality dataset. The dataset includes information such as wine names, regions, varieties, ratings, and tasting notes. The goal is to clean the data, standardize formats, and extract meaningful insights, such as wine quality categories, regional diversity, and top descriptive words for each quality category.

## Process
The following steps were performed to clean and analyze the dataset:

1. **Data Loading**: The dataset was loaded using Pandas for manipulation.
2. **Initial Exploration**: Inspected the dataset structure, data types, and missing values.
3. **Data Cleaning**:
   - Removed duplicate rows and rows with missing values.
   - Standardized the `region` column by grouping similar regions (e.g., combining California, Washington, and Oregon into "United States").
   - Converted all text columns (`name` and `notes`) to lowercase for uniformity.
   - Removed numbers and punctuation from text columns to simplify analysis.
   - Tokenized the `notes` column into individual words and removed stopwords.
4. **Feature Engineering**:
   - Created a `wine_quality` column to classify wines into categories:
     - **Good**: Ratings between 85-89.
     - **Outstanding**: Ratings between 90-94.
     - **Exceptional**: Ratings between 95-100.
   - Calculated the percentage distribution of wine varieties.
5. **Analysis**:
   - Identified the top 5 most frequent descriptive words for each wine quality category.
   - Determined the top 5 regions producing "Exceptional" quality wines.
   - Analyzed regional diversity by counting the number of unique wine varieties per region.

## Tech Tools
- **Python**: Core programming language used for data manipulation.
- **Pandas**: For data cleaning and transformation.
- **NLTK**: For natural language processing tasks like tokenization and stopword removal.
- **Jupyter Notebook**: For interactive coding and documentation.

## Conclusion
The wine quality dataset was successfully cleaned and analyzed. Key outcomes include:
- Standardized and cleaned text data for uniformity.
- Categorized wines into quality levels based on ratings.
- Extracted insights into regional diversity and descriptive words for each quality category.
- Identified top regions producing "Exceptional" quality wines.

### Tags
- Wine Data Cleaning
- Data Transformation
- Natural Language Processing
- Python Data Analysis
- Feature Engineering
- Jupyter Notebook