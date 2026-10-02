A machine learning-powered Walmart Sales Intelligence Platform designed to analyze historical sales data, understand customer behavior, visualize business performance, and predict future sales.

The project is developed using Python, Pandas, Plotly, Scikit-learn, and Streamlit, with VS Code as the development environment.

https://ai-data-science06.streamlit.app/

🚀 Project Overview

The Walmart Sales Intelligence Platform transforms raw sales data into meaningful business insights through interactive dashboards and machine learning.

The platform allows users to:

Explore sales performance
Analyze customer behavior
Study different product categories
Compare payment methods
Filter data by city and other parameters
Visualize trends using interactive Plotly charts
Predict future sales using Machine Learning
View important business insights
Explore the original dataset
✨ Main Features
📊 Dashboard

The main dashboard provides an overview of the business performance through interactive visualizations and key metrics.

It includes:

Total sales
Number of transactions
Average sales
Sales trends
Category performance
City-wise performance
Payment method analysis
Interactive Plotly charts
👥 Customer Analysis

The Customer Analysis section focuses on understanding customer purchasing behavior.

It can be used to analyze:

Customer spending patterns
Customer distribution
Purchase behavior
Customer ratings
Sales by customer-related attributes
High-performing customer segments
📈 Sales Analysis

The Sales Analysis section provides detailed information about sales performance.

Users can explore:

Sales by city
Sales by category
Sales trends
Quantity sold
Revenue performance
Payment method distribution
Category-wise sales performance

Interactive Plotly visualizations make it easier to identify patterns and trends.

📁 Dataset

The Dataset section provides access to the sales data used by the application.

The project works with a dataset containing 10,000 records and allows users to explore and understand the underlying data.

Users can:

View the dataset
Check available columns
Filter records
Understand data distributions
Explore the data used for Machine Learning
🤖 Machine Learning

The Machine Learning section uses historical sales information to predict future sales.

The general workflow is:

Historical Sales Data
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Data Preparation
        ↓
Machine Learning Model
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Future Sales Prediction

The ML section can also display model performance metrics such as:

Accuracy, where applicable
MAE
MSE
RMSE
R² Score

Note: Accuracy is mainly appropriate for classification problems. For a future-sales prediction model, which is usually a regression problem, metrics such as MAE, RMSE, and R² are more appropriate.

💡 Business Insights

The Business Insights section converts analytical results into useful business recommendations.

Examples include:

Identifying high-performing categories
Finding cities with stronger sales
Understanding customer purchasing patterns
Identifying popular payment methods
Detecting sales trends
Supporting inventory planning
Supporting future sales planning
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Pandas	Data manipulation and analysis
Scikit-learn	Machine Learning
Plotly	Interactive data visualization
Streamlit	Web dashboard
VS Code	Development environment
📂 Project Structure

A recommended project structure is:

Walmart-Sales-Intelligence/
│
├── app.py
├── data/
│   └── walmart_sales.csv
│
├── models/
│   └── sales_model.pkl
│
├── notebooks/
│   └── analysis.ipynb
│
├── pages/
│   ├── dashboard.py
│   ├── customer_analysis.py
│   ├── sales_analysis.py
│   ├── dataset.py
│   ├── machine_learning.py
│   └── business_insights.py
│
├── requirements.txt
└── README.md
⚙️ Installation

Clone or download the project and open it in VS Code.

Install the required Python libraries:

pip install pandas plotly scikit-learn streamlit

Or, if you have a requirements.txt file:

pip install -r requirements.txt
▶️ Run the Application

Start the Streamlit application with:

streamlit run app.py

The application will open in your browser.

🔮 Future Sales Prediction

One of the main objectives of this project is to use historical sales data to estimate future sales.

The model learns patterns from historical data and uses those patterns to generate predictions.

Example workflow:

Historical Sales
      ↓
Data Preprocessing
      ↓
Feature Selection
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Future Sales Prediction

For a regression-based sales prediction model, recommended evaluation metrics include:

MAE

Measures the average absolute difference between actual and predicted sales.

RMSE

Measures prediction error while giving greater weight to larger errors.

R² Score

Measures how well the model explains variation in the target sales values.

📌 Project Goals

The major goals of this project are:

Analyze Walmart sales data.
Build an interactive sales dashboard.
Understand customer purchasing behavior.
Analyze sales across cities and categories.
Visualize important business trends.
Develop a Machine Learning model for future sales prediction.
Evaluate the performance of the prediction model.
Generate actionable business insights.
🎯 Conclusion

The Walmart Sales Intelligence Platform combines data analysis, interactive visualization, and Machine Learning into a single application.

It provides a user-friendly way to explore sales data, understand customer and business behavior, and use historical information to support future sales prediction and data-driven decision making.
