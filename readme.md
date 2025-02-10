# 🏏 End-to-End Cricket Data Analytics Project Using Web Scraping, Python, Pandas, and Power BI

## Table of Contents

1. Introduction
2. Problem Statement
3. Requirement Scoping
4. Installation Instructions
5. Data Collection
6. Data Cleaning and Transformation in Python Pandas
7. Data Transformation in Power Query
8. Data Modeling and Building Parameters using DAX
9. Building an Interactive Dashboard in Power BI
10. Conclusion
11. Acknowledgments

---

## 1. Introduction

This project is designed to provide meaningful insights into cricket data using web scraping, Python, Pandas, and Power BI. By following an end-to-end data analytics workflow, we will extract, clean, transform, and visualize the data, creating an interactive dashboard for better analysis and decision-making.

## 2. Problem Statement

The objective of this project is to analyze cricket data to uncover valuable insights and trends. The process includes:

- Scraping data from **ESPN Cricinfo**
- Cleaning and transforming the data using **Python and Pandas**
- Performing additional transformations in **Power Query**
- Modeling the data and building parameters using **DAX (Data Analysis Expressions)**
- Creating an **interactive dashboard in Power BI**

## 3. Requirement Scoping

### **Tools & Technologies Required**

- **Python**: Data extraction and preprocessing
- **Pandas**: Data manipulation
- **Power BI**: Data visualization and analysis
- **Web Scraping Libraries**: BeautifulSoup, Requests

### **Skills Needed**

- Web Scraping
- Data Cleaning & Transformation
- Data Modeling
- Data Visualization

## 4. Installation Instructions

### **Prerequisites**

- **Python**: Download and install from [python.org](https://www.python.org/)
- **Power BI**: Download and install from [powerbi.microsoft.com](https://powerbi.microsoft.com/)

### **Install Required Python Libraries**

Run the following command to install dependencies:

```bash
pip install pandas beautifulsoup4 requests
```

## 5. Data Collection

### **Steps:**

1. **Identify Data Source**: ESPN Cricinfo website.
2. **Web Scraping**: Extract cricket data using **BeautifulSoup** and **Requests**.
3. **Store Data**: Save the scraped data into a **CSV file** for further processing.

## 6. Data Cleaning and Transformation in Python Pandas

### **Steps:**

1. **Load Data**: Read the CSV file into a **Pandas DataFrame**.
2. **Data Cleaning**:
   - Handle missing values
   - Remove duplicates
   - Correct data types
3. **Data Transformation**:
   - Perform aggregations
   - Create calculated columns
   - Implement feature engineering

## 7. Data Transformation in Power Query

### **Steps:**

1. **Import Data**: Load the cleaned data into **Power BI** using **Power Query**.
2. **Transform Data**:
   - Merge tables
   - Create calculated columns
   - Filter data for better analysis

## 8. Data Modeling and Building Parameters using DAX

### **Steps:**

1. **Data Modeling**:
   - Define relationships between tables
   - Optimize data schema
2. **DAX Calculations**:
   - Create measures
   - Develop calculated columns
   - Build parameters for enhanced analysis

## 9. Building an Interactive Dashboard in Power BI

### **Steps:**

1. **Dashboard Design**:
   - Utilize charts, tables, slicers, and KPIs for visualization
2. **Enhance Interactivity**:
   - Implement drill-through, tooltips, and filters
3. **Publish & Share**:
   - Deploy the dashboard to **Power BI Service** for collaboration

## 10. Conclusion

This project showcases the **complete lifecycle of a data analytics project**, from **data collection to visualization**. By integrating Python, Pandas, Power BI, and DAX, we successfully extract meaningful insights from cricket data and present them in an interactive format.

## 11. Acknowledgments

- **ESPN Cricinfo** for the data source.
- **Python & Power BI Communities** for valuable tools and resources.

---
## Configuration and File Paths
### Important: Update Paths
Do change your paths in the "\Cricket Data Analytics Project\WebScrapping\config\config.json" file:
```json
{
    "base_url": "https://www.espncricinfo.com",
    "t20_url": "https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450",
    "espn_t20_wc_2022_results_csv_file_path": "yourpath//Cricket Data Analytics Project//archive//csv//t20_wc_match_results.csv",
    "batting_summary_csv_file_path": "yourpath//Cricket Data Analytics Project//archive//csv//t20_wc_batting_summary.csv",
    "bowling_summary_csv_file_path": "yourpath//Cricket Data Analytics Project//archive//csv//t20_wc_bowling_summary.csv",
    "player_details_csv_file_path": "yourpath//Cricket Data Analytics Project//archive//csv//t20_wc_player_info.csv",
    "player_details_with_imageurl_csv_file_path": "yourpath//Cricket Data Analytics Project//archive//csv//t20_wc_player_info_with_imageurl.csv",
    "espn_t20_wc_2022_results_json_filepath": "yourpath//Cricket Data Analytics Project//archive//json//t20_wc_match_results.json",
    "batting_summary_json_file_path": "yourpath//Cricket Data Analytics Project//archive//json//t20_wc_batting_summary.json",
    "bowling_summary_json_file_path": "yourpath//Cricket Data Analytics Project//archive//json//t20_wc_bowling_summary.json",
    "player_details_json_file_path": "yourpath//Cricket Data Analytics Project//archive//json//t20_wc_player_info.json",
    "player_details_with_imageurl_json_file_path": "yourpath//Cricket Data Analytics Project//archive//json//t20_wc_player_info_with_imageurl.json",
    "scorecard_urls_json_file_path": "yourpath//Cricket Data Analytics Project//archive//json//scorecard_urls.json"
}
```
Similarly, change paths in your script files accordingly.

🌟 **Happy Analyzing!**
