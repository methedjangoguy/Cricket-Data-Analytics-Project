# 🏏 End To End Cricket Data Analytics Project Using Web Scraping, Python, Pandas, and Power BI

## Table of Contents
1. Problem Statement
2. Requirement Scoping
3. Installation Instructions
4. Data Collection
5. Data Cleaning and Transformation in Python Pandas
6. Data Transformation in Power Query
7. Data Modeling and Building Parameters using DAX
8. Build Dashboard in Power BI

## Problem Statement
The objective of this project is to analyze cricket data to derive meaningful insights and present them through an interactive dashboard. This involves collecting data from ESPN Cricinfo, cleaning and transforming it using Python and Pandas, further transforming it in Power Query, modeling the data using DAX, and finally visualizing it in Power BI.

## Requirement Scoping
- **Tools Required**: Python, Pandas, Power BI, Web Scraping libraries (BeautifulSoup, requests)
- **Data Source**: ESPN Cricinfo website
- **Skills Needed**: Web scraping, data cleaning, data transformation, data modeling, and data visualization

## Installation Instructions
### Prerequisites
- **Python**: Ensure Python is installed on your system. You can download it from python.org.
- **Power BI**: Download and install Power BI Desktop from powerbi.microsoft.com.

### Python Libraries
Install the required Python libraries using pip:
```bash
pip install pandas beautifulsoup4 requests
```

### Power BI
- **Power Query**: Power Query is integrated into Power BI Desktop, so no additional installation is required.

## Data Collection
### Steps:
1. **Identify the Data Source**: ESPN Cricinfo website.
2. **Web Scraping**: Use Python libraries like BeautifulSoup and requests to scrape the required cricket data.
3. **Save Data**: Store the scraped data in a CSV file for further processing.

## Data Cleaning and Transformation in Python Pandas
### Steps:
1. **Load Data**: Read the CSV file into a Pandas DataFrame.
2. **Data Cleaning**: Handle missing values, remove duplicates, and correct data types.
3. **Data Transformation**: Perform necessary transformations such as aggregations, calculations, and feature engineering.

## Data Transformation in Power Query
### Steps:
1. **Import Data**: Load the cleaned data into Power BI using Power Query.
2. **Transform Data**: Use Power Query Editor to perform additional transformations like merging tables, creating calculated columns, and filtering data.

## Data Modeling and Building Parameters using DAX
### Steps:
1. **Data Modeling**: Define relationships between tables and create a data model.
2. **DAX Calculations**: Use Data Analysis Expressions (DAX) to create measures, calculated columns, and parameters for analysis.

## Build Dashboard in Power BI
### Steps:
1. **Design Dashboard**: Create an interactive dashboard in Power BI using various visualizations like charts, tables, and slicers.
2. **Add Interactivity**: Implement features like drill-through, tooltips, and filters to enhance user experience.
3. **Publish Dashboard**: Publish the dashboard to the Power BI service for sharing and collaboration.

## Conclusion
This project demonstrates the end-to-end process of data analytics, from data collection to visualization, providing valuable insights into cricket data.

## Acknowledgments
- ESPN Cricinfo for providing the data.
- Python and Power BI communities for their support and resources.
