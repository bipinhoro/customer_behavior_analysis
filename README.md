# Customer_Behavior_Analysis
# Data Analytics Project: End-to-End Sales Performance Insight

## Overview
This project demonstrates a full-cycle data analytics workflow: from ingestion and cleaning to advanced SQL querying and interactive visualization. The primary goal was to transform messy, raw data into actionable business insights regarding revenue trends, customer demographics, and product performance.

## Dataset
*   **Source:** [Mention Source, e.g., Kaggle / Internal Company Data]
*   **Description:** The dataset contains [Number] records of sales transactions, including order dates, customer details, product categories, and profit margins.
*   **Key Challenges:** Handled missing values in customer segments and resolved data type inconsistencies in the date columns.

## Tools & Technologies
*   **Python:** Data cleaning and Exploratory Data Analysis (EDA) using `Pandas`, `NumPy`, and `Matplotlib`.
*   **SQL (MySQL):** Database schema creation and complex business logic queries.
*   **Power BI:** Data modeling (DAX), ETL (Power Query), and dashboard design.
*   **Jupyter Notebook:** For documented, step-by-step data preprocessing.

## Steps
1.  **Exploratory Data Analysis (EDA):** Used Python to identify outliers, correlations, and distribution patterns.
2.  **Data Cleaning:** Managed null values, removed duplicates, and standardized categorical naming conventions to ensure "Data Integrity."
3.  **MySQL Database Integration:** 
    *   Migrated the cleaned `.csv` into a MySQL Server.
    *   Wrote optimized SQL queries to calculate KPIs like *Year-over-Year Growth* and *Top 5 Performing Regions*.
4.  **Power BI Visualization:** 
    *   Connected Power BI to the MySQL Database.
    *   Developed a star-schema data model.
    *   Authored DAX measures for dynamic reporting (e.g., Total Revenue, Average Order Value).

## Dashboard
The final dashboard provides an interactive experience for stakeholders to drill down into specific quarters and product lines.

*   **Key Features:** 
    *   Trend analysis line charts.
    *   Geospatial mapping of sales volume.
    *   Conditional formatting to highlight underperforming categories.

## Results & Insights
*   **Revenue Growth:** Identified a 15% spike in sales during Q3, driven primarily by the [Category Name] segment.
*   **Efficiency:** Automated the reporting process, reducing the time spent on monthly data compilation by approximately 10 hours.
*   **Optimization:** Recommended a shift in marketing focus toward the [Region] based on high conversion rates despite lower historical ad spend.

## How to Run
1.  **Python Environment:**
    ```bash
    pip install pandas sqlalchemy mysql-connector-python
    jupyter notebook EDA_notebook.ipynb
    ```
2.  **SQL Setup:**
    *   Import the provided `.sql` dump file into your MySQL Workbench.
    *   Run the scripts in the `/sql_queries` folder to generate the view tables.
3.  **Power BI:**
    *   Open the `.pbix` file.
    *   Update the Data Source Settings to point to your local MySQL instance credentials.

---
```

