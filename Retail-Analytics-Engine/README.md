
# 🛒 Retail Analytics Engine

<p align="center">
  <img src="https://img.shields.io/badge/Retail-Analytics-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

<p align="center">
  <b>📊 Analyze • 🔍 Discover • 🤖 Predict • 🚀 Optimize</b>
</p>

---

## 🌟 Project Overview

**Retail Analytics Engine** is a data science and machine learning project built around **Walmart retail sales data**.

The system transforms raw retail transaction data into meaningful business insights using:

* 📊 Exploratory Data Analysis
* 🧹 Data preprocessing
* ⚙️ Feature engineering
* 📈 Sales and KPI analytics
* 🤖 Machine learning
* 📊 Interactive visualizations
* 🚀 Streamlit dashboard

The goal is to understand **sales performance, product behavior, profitability, customer patterns, and business trends** while also using machine learning to support sales prediction.

---

# 🎯 Problem Statement

Retail businesses generate large amounts of transactional data every day.

Raw transaction data contains information such as:

* Product category
* Branch
* City
* Quantity
* Unit price
* Rating
* Payment method
* Profit margin
* Sales amount
* Date and time

Simply storing this data does not provide actionable insights.

The **Retail Analytics Engine** processes this data to answer important analytical questions:

```text
📊 What are the total sales?

🏪 Which branches perform better?

🛍️ Which product categories generate more sales?

💰 Which categories are more profitable?

📅 When are sales highest?

💳 Which payment methods are commonly used?

📈 What factors influence total sales?

🤖 Can sales be predicted using Machine Learning?
```

---

# 🚀 Key Features

## 📊 1. Retail KPI Dashboard

The system provides important business KPIs such as:

* 💰 Total Sales
* 🛒 Total Quantity Sold
* 📦 Number of Transactions
* ⭐ Average Customer Rating
* 📈 Average Sales
* 💵 Profit Margin
* 🏪 Branch Performance

Example:

```text
┌──────────────────┐
│   TOTAL SALES    │
│     ₹XXXXXX      │
└──────────────────┘

┌──────────────────┐
│ TOTAL QUANTITY   │
│      XXXXX       │
└──────────────────┘

┌──────────────────┐
│ AVG. RATING      │
│       X.X        │
└──────────────────┘

┌──────────────────┐
│ TRANSACTIONS     │
│      XXXXX       │
└──────────────────┘
```

---

# 🔍 2. Exploratory Data Analysis

The project performs detailed analysis of retail transactions.

### Analysis includes:

* Product category analysis
* Branch analysis
* City analysis
* Sales distribution
* Quantity analysis
* Rating analysis
* Payment-method analysis
* Profitability analysis
* Time-based analysis

---

# 🏪 3. Branch & City Analysis

Compare sales performance across different Walmart branches and locations.

The analysis can identify:

* High-performing branches
* Low-performing branches
* Sales contribution by city
* Average sales per branch
* Product-category performance by location

---

# 🛍️ 4. Product Category Analysis

Analyze product categories based on:

* Sales
* Quantity sold
* Profitability
* Customer ratings
* Transaction volume

This helps identify products and categories that contribute significantly to retail performance.

---

# 💰 5. Profitability Analysis

Analyze the relationship between:

```text
Sales
  ↓
Cost
  ↓
Profit Margin
  ↓
Profitability
```

The system can identify:

* High-profit categories
* Low-profit categories
* Branch profitability
* Profit-margin patterns
* Sales vs. profitability relationships

---

# ⏰ 6. Time-Based Sales Analysis

Time-related features are extracted from transaction timestamps.

### Engineered features include:

```text
Year
Month
Day
Hour
```

These features can be used to analyze:

* Monthly sales trends
* Daily sales patterns
* Peak sales hours
* Seasonal behavior
* Sales fluctuations

---

# 💳 7. Payment Method Analysis

Analyze customer payment behavior.

Possible payment methods include:

```text
💳 Credit Card
💵 Cash
📱 E-wallet
```

The system can compare transaction volume and sales across payment methods.

---

# ⭐ 8. Customer Rating Analysis

Customer ratings can be analyzed to understand relationships between:

* Product categories
* Sales
* Branches
* Customer satisfaction
* Transaction behavior

---

# 🤖 9. Machine Learning Sales Prediction

The project uses **Random Forest Regression** to predict sales based on available retail features.

### ML Workflow

```text
Retail Dataset
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Categorical Encoding
      ↓
Train/Test Split
      ↓
Random Forest Regression
      ↓
Sales Prediction
      ↓
Model Evaluation
```

---

# 🌲 Random Forest Model

The project uses:

```python
RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
```

### Why Random Forest?

Random Forest combines multiple decision trees to produce a stronger prediction model.

It can capture:

* Non-linear relationships
* Feature interactions
* Complex patterns
* Categorical and numerical feature relationships after preprocessing

---

# ⚙️ Feature Engineering

The project creates additional features from the raw retail dataset.

### Original Features

```text
Branch
City
Category
Unit Price
Quantity
Rating
Payment Method
Profit Margin
```

### Engineered Features

```text
Month
Day
Hour
Total Sales
```

The target variable used for prediction is:

```text
Total Sales
```

---

# 🔄 Data Processing Pipeline

```text
                 RAW DATA
                    │
                    ▼
             Data Cleaning
                    │
                    ▼
           Missing Value Check
                    │
                    ▼
          Feature Engineering
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    Numerical Data       Categorical Data
          │                   │
          │              One-Hot Encoding
          │                   │
          └─────────┬─────────┘
                    ▼
              Train/Test Split
                    │
                    ▼
          Random Forest Model
                    │
                    ▼
               Prediction
                    │
                    ▼
             Model Evaluation
```

---

# 📈 Model Evaluation

The regression model can be evaluated using:

### MAE

**Mean Absolute Error**

Measures the average absolute difference between actual and predicted values.

```text
MAE = Average(|Actual - Predicted|)
```

---

### RMSE

**Root Mean Squared Error**

Penalizes larger prediction errors more strongly.

```text
RMSE = √MSE
```

---

### R² Score

Measures how well the model explains variation in the target variable.

```text
R² → closer to 1 generally indicates better fit
```

---

# 📊 Interactive Streamlit Dashboard

The project includes a Streamlit interface for exploring retail data and model predictions.

### Dashboard sections

```text
🏠 Dashboard
│
├── 📊 KPI Overview
│
├── 📈 Sales Analysis
│
├── 🏪 Branch Analysis
│
├── 🛍️ Category Analysis
│
├── 💰 Profit Analysis
│
├── 💳 Payment Analysis
│
├── ⏰ Time Analysis
│
└── 🤖 ML Predictions
```

---

# 📊 Visualizations

The project uses interactive visualizations to communicate business insights.

Possible charts include:

* 📊 Sales by Category
* 📊 Sales by Branch
* 📈 Monthly Sales Trend
* 📊 Quantity by Category
* 🥧 Payment Method Distribution
* 📈 Profitability Analysis
* ⭐ Rating Distribution
* 🔥 Correlation Heatmap
* 📉 Actual vs Predicted Sales

---

# 🧠 Example Insights

The analysis can be used to discover patterns such as:

```text
📌 Which product categories generate the most sales?

📌 Which branches contribute the most revenue?

📌 Which categories have stronger profit margins?

📌 During which months are sales higher?

📌 Which payment methods are frequently used?

📌 Which factors contribute to sales variation?

📌 How accurately can sales be predicted?
```

> Actual findings should be generated directly from the dataset used in the repository rather than hard-coded into the README.

---

# 🛠️ Technology Stack

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| 🐍 Python       | Core programming          |
| 🐼 Pandas       | Data manipulation         |
| 🔢 NumPy        | Numerical computation     |
| 🤖 Scikit-learn | Machine Learning          |
| 📊 Plotly       | Interactive visualization |
| 📈 Matplotlib   | Visualization             |
| 🎨 Seaborn      | Statistical visualization |
| 🚀 Streamlit    | Interactive dashboard     |
| 💻 VS Code      | Development               |
| 🔧 Git & GitHub | Version control           |

---

# 📂 Project Structure

```text
Retail-Analytics-Engine/
│
├── 📁 data/
│   └── walmart_sales.csv
│
├── 📁 images/
│   ├── dashboard.png
│   ├── sales_analysis.png
│   └── prediction.png
│
├── 📄 app.py
├── 📄 model.py
├── 📄 analysis.py
├── 📄 requirements.txt
└── 📄 README.md
```

> Update the structure if your actual repository uses different filenames.

---

# 💻 Installation

Clone the repository:

```bash
git clone https://github.com/nodanbhatia/Retail-Analytics-Engine.git
```

Move into the project:

```bash
cd Retail-Analytics-Engine
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install the main libraries manually:

```bash
pip install pandas numpy scikit-learn plotly streamlit matplotlib seaborn
```

---

# ▶️ Run the Application

Start the Streamlit dashboard:

```bash
streamlit run app.py
```

After running the command, open the local Streamlit URL displayed in the terminal.

---

# 🧪 Example Machine Learning Pipeline

```python
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

X = df.drop("total_sales", axis=1)
y = df["total_sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            RandomForestRegressor(
                n_estimators=200,
                random_state=42
            )
        )
    ]
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

---

# 📌 Project Workflow

```text
             🛒 Walmart Retail Data
                       │
                       ▼
               🧹 Data Cleaning
                       │
                       ▼
                🔍 EDA
                       │
                       ▼
             ⚙️ Feature Engineering
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      📊 Business Analytics   🤖 ML Model
             │                   │
             │                   ▼
             │             Sales Prediction
             │                   │
             └─────────┬─────────┘
                       ▼
               📊 Streamlit App
                       │
                       ▼
              💡 Business Insights
```

---

# 🎯 Real-World Applications

The Retail Analytics Engine demonstrates how data science can support retail businesses with:

* 📊 Sales monitoring
* 🏪 Store performance analysis
* 🛍️ Product analysis
* 💰 Profitability analysis
* 📈 Sales forecasting
* 👥 Customer behavior analysis
* 💳 Payment trend analysis
* 📦 Inventory-related analysis
* 🤖 Data-driven decision support

---

# 🔮 Future Improvements

## Version 2.0

* 📦 Inventory forecasting
* 📈 Advanced sales forecasting
* 🏪 Store-level performance comparison
* 📊 Automated KPI reports

## Version 3.0

* 🤖 Advanced ML models
* 📅 Time-series forecasting
* 🔥 Demand prediction
* 🧠 Customer segmentation

## Version 4.0

```text
Retail Data
     ↓
Data Engineering
     ↓
Analytics
     ↓
Machine Learning
     ↓
Forecasting
     ↓
Generative AI
     ↓
AI Retail Assistant
```

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

* Python
* Pandas
* NumPy
* Data preprocessing
* Exploratory Data Analysis
* Feature engineering
* Categorical encoding
* Regression
* Random Forest
* Model evaluation
* Business analytics
* Data visualization
* Streamlit
* Git & GitHub

---

# ⭐ Project Highlights

```text
📊 Retail Analytics
       +
🔍 Exploratory Data Analysis
       +
⚙️ Feature Engineering
       +
🤖 Machine Learning
       +
📈 Interactive Visualization
       +
🚀 Streamlit Dashboard
       =
🛒 Retail Analytics Engine
```

---

# 👨‍💻 Author

## Nodan Bhatia

🎓 **BTech CSE — Data Science**

💡 **Data Science | Machine Learning | AI | NLP | Agentic AI**

<p align="center">

<a href="https://github.com/nodanbhatia">
<img src="https://img.shields.io/badge/GitHub-Nodan%20Bhatia-black?style=for-the-badge&logo=github" />
</a>

<a href="https://www.linkedin.com/in/nodan-bhatia-888951424/">
<img src="https://img.shields.io/badge/LinkedIn-Nodan%20Bhatia-blue?style=for-the-badge&logo=linkedin" />
</a>

</p>

---

# ⭐ Support

If you find this project useful:

⭐ **Star the repository**

🍴 **Fork the repository**

📢 **Share the project**

---

<p align="center">
  <b>🛒 Turning Walmart Retail Data into Actionable Business Insights 📊</b>
</p>
