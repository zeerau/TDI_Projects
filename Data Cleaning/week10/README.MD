# Data Cleaning and Analysis Project

## Introduction
This project focuses on cleaning and analyzing job-related data to extract meaningful insights. The dataset contains information about companies, job descriptions, salaries, and other relevant details. The primary goal of this project is to preprocess the data, extract key information, and generate visualizations to better understand trends in the job market, particularly for AI-related roles.

## Process
The project followed these steps:

1. **Data Loading**: 
   - The dataset was loaded from a CSV file using `pandas`, with error handling for bad lines.

2. **Data Cleaning**:
   - Removed duplicate rows and handled missing values by dropping rows with `NaN`.
   - Standardized text by converting to lowercase and removing special characters.
   - Extracted specific information such as:
     - Minimum number of employees from the `Company_Overview` column.
     - Industry type and founding year using regex patterns.
     - Salary ranges and average salaries from the `Salary_fork` column.

3. **Feature Engineering**:
   - Created new columns for extracted data, such as `Industry_Type`, `founded_year`, `Min_Salary`, `Max_Salary`, and `Average_Salary`.
   - Tokenized job descriptions and removed stopwords and short words to clean the text further.

4. **Analysis**:
   - Filtered AI-related jobs and calculated the average salary for these roles.
   - Generated a word cloud to visualize frequently used terms in job descriptions.
   - Created a histogram to analyze the distribution of job description lengths.

5. **Visualization**:
   - Used `matplotlib` to create visualizations, including histograms and word clouds, to better understand the data.

6. **Final Cleanup**:
   - Dropped unnecessary columns to streamline the dataset for further analysis.

## Tech Tools
The following tools and libraries were used in this project:
- **Python**: The primary programming language for data processing and analysis.
- **Pandas**: For data manipulation and cleaning.
- **NumPy**: For numerical operations.
- **Matplotlib**: For data visualization.
- **NLTK**: For natural language processing tasks, such as tokenization and stopword removal.
- **WordCloud**: For generating word clouds.
- **Regex**: For extracting patterns from text.

## Conclusion
The project successfully cleaned and analyzed the dataset, providing insights into job trends and salary distributions. Key outcomes include:
- Extracted and visualized industry types, founding years, and salary ranges.
- Identified the average salary for AI-related jobs.
- Generated a word cloud to highlight common terms in job descriptions.
- Created a histogram to analyze job description lengths.

This project demonstrates the importance of data cleaning and preprocessing in extracting actionable insights from raw datasets.

## Tags
- Data Cleaning
- Data Analysis
- Python
- Pandas
- AI Jobs
- Salary Analysis
- Word Cloud
- Job Market Trends