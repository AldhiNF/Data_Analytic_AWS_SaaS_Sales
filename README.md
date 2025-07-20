<h1> Sales Insight Analysis Project </h1>

## 1. Project Overview
This project analyzes SaaS Sales data to extract meaningful insights, improve decision-making, and identify key trends across industries and countries. The primary focus is to:

- Understand which industries and countries generate the most revenue.
- Identify top-selling products per industry.
- Provide visual summaries of sales distribution.

Key Objectives:
- Objective 1: Analyze sales performance across countries.
- Objective 2: Identify top 3 products per industry.
- Objective 3: Visualize sales and profit distribution to aid strategic planning.

## 2. Data Sources
- [`saas_sales.csv`](link) - Sales data containing fields like Industry, Country, Product, Sales, Profit, Discount, and Quantity.

## 3. Technologies Used
- Programming Language: Python (Pandas, NumPy)
- Visualization: Matplotlib, Seaborn
- Interactive Dashboard: Tableau (to be created from processed insights)
- Version Control: Git
- Development Environment: Jupyter Notebook

## 4. Project Structure

├── README.md          <- The top-level README for developers using this project.
|
├── data
│   ├── SaaS-Sales            <- Data from third party sources.
│   └── SaaS-Sales_cleaned        <- The data that has been cleaned.
│
├── notebooks          <- `data_sales.ipynb` <- Jupyter notebook containing full analysis pipeline.
│
├── reports            <- Generated analysis as PowerPoint.
|   ├── slide          <- Final PowerPoint presentation for stakeholders.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- List of dependencies used (to be generated).
│                         generated with `pip freeze > requirements.txt`
│
└── src                <- [Source code for use in this project](https://www.kaggle.com/code/hieremiaskevin/amazon-web-service-saas-sales-data-analysis).


## 5. Summary of Findings
### 5.1 Business Insight
- The Finance industry has the highest demand, especially for ContactMatcher, Support, and FinanceHub.
- Countries with the highest total sales include the United States and Canada.
- Significant variation in profit margins across products indicates room for pricing optimization.
- Discount and Quantity show no linear correlation to Profit in this dataset.

### 5.2 Actionable Recommendation
- Focus marketing and upselling on top-performing industries like Finance.
- Investigate pricing strategies for products with low profit despite high sales.
- Tailor regional sales campaigns based on top-performing countries.

## 6. Contact
- Name: Aldhi Nur Faith
- Email: Mellaldhi@gmail.com

