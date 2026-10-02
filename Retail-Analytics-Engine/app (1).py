#--- IMPORT LIBRARIES --- #

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import ( mean_absolute_error,mean_squared_error, r2_score, accuracy_score)
import joblib



#--- PAGE TITLE ---#

st.set_page_config(
    page_title="Walmart Sales Intelligence",
    layout="wide"
)

st.title("Walmart Sales Intelligence Dashboard")
df=pd.read_csv("Walmart.csv")



# ---- DATA CLEANING ----#

df['unit_price']=(df['unit_price'].astype(str)
.str.replace("$","",regex=False).str.replace(",","",regex=False).astype(float))

df['time']=pd.to_datetime(
    df['time'],format="%H:%M:%S",errors="coerce"
)
df=df.drop_duplicates()
print(df.isnull().sum())

numeric_columns=df.select_dtypes(include=np.number).columns
for col in numeric_columns:
    df[col]=df[col].fillna(df[col].median())

categorical_columns=df.select_dtypes(include="object").columns
for col in categorical_columns:
    df[col]=df[col].fillna(df[col].mode()[0])




#--- FEATURE ENGINEERING ---#

df['total_sales']=df["unit_price"]*df['quantity']

df['profit']=df['total_sales'] * df['profit_margin']

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month
df['month_name']=df['date'].dt.month_name()
df['day']=df['date'].dt.day
df['day_name']=df['date'].dt.day_name()
df['hour']=df['time'].dt.hour

def get_time_period(hour):
    if hour< 12:
        return "Morning"
    elif hour<17:
        return "Afternoon"
    else:
        return "Evening"
df['time_period']=df['hour'].apply(get_time_period)




#------- KPI DEVELOPMENT -------#

st.subheader("Executive Overview")
total_sales=df['total_sales'].sum()
total_profit=df['profit'].sum()
total_orders=df['invoice_id'].nunique()
avg_rating=df['rating'].mean()
avg_profit_margin=df['profit_margin'].mean()

col1,col2,col3,col4,col5=st.columns(5)
col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Total Orders",
    f"{total_orders:,.2f}"
)

col4.metric(
    "Avg Rating",
    f"{avg_rating:,.2f}"
)

col5.metric(
    "Profit Margin",
    f"{avg_profit_margin:,.2f}"
)
st.write('-------')




#----- SIDEBAR FORMATION ------#
st.sidebar.title("Walmart")
st.sidebar.markdown("Sales Intelligence Platform")
page=st.sidebar.radio(
    "Navigation",[
        "Dashboard",
        "Customer Analysis",
        "Sales Analysis",
        "Dataset",
        "Machine Learning",
        "Business Insights",
        
    ]
)
#----- MAKE A FILTER SECTION -----#

st.sidebar.subheader("FILTER ")
selected_city=st.sidebar.multiselect(
    "Select City",
    options=df['City'].unique(),
    default=df['City'].unique()
)

selected_category=st.sidebar.multiselect(
    "Select Category",
    options=df['category'].unique(),
    default=df['category'].unique()
)

selected_payment=st.sidebar.multiselect(
    "Payment Method",
    options=df['payment_method'].unique(),
    default=df['payment_method'].unique()
)

filtered_df=df[
    (df['City'].isin(selected_city))&
    (df['category'].isin(selected_category))&
    (df['payment_method'].isin(selected_payment))
]


#------- 1. DASHBOARD ----------
if page=="Dashboard":
    st.subheader(" DASHBOARD")
    #------ BAR-GRAPH CATEGORY VS SALES -----#
    category_sales=(
        filtered_df.groupby("category")['total_sales'].sum().reset_index()
    )
    fig=px.bar(
        category_sales,
        x="category",
        y="total_sales",
        title="Sales by Product Category",
        text_auto=".2s"
    )
    st.plotly_chart(fig,use_container_width=True)

    #------ BAR-GRAPH CITY VS SALES -----#

    city_sales=(filtered_df.groupby("City")['total_sales'].sum().sort_values(ascending=False).reset_index())
    fig=px.bar(
        city_sales,
        x='City',
        y="total_sales",
        title="Sales by City"
    )
    top_cities=city_sales.head(10)
    fig=px.bar(top_cities,x="City",y="total_sales",title="Top 10 Cities by Sales")
    st.plotly_chart(fig,use_container_width=True)


    #----- BAR-GRAPH BRANCH VS SALES ------#

    branch_sales=(filtered_df.groupby("Branch")['total_sales'].sum().sort_values(ascending=False).reset_index())
    fig=px.bar(
        branch_sales.head(10),
        x="Branch",
        y="total_sales",
        title="Top Branches by Sales"
    )
    st.plotly_chart(fig,use_container_width=True)

    #------- LINE-CHART MONTH_NAME VS TOTAL_SALES ------#

    monthly_sales=(filtered_df.groupby('month_name')['total_sales'].sum().reset_index())
    month_order=[
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    monthly_sales['month_name']=pd.Categorical(monthly_sales['month_name'],categories=month_order,ordered=True)
    monthly_sales=monthly_sales.sort_values("month_name")
    fig=px.line(
        monthly_sales,
        x='month_name',
        y='total_sales',
        title="Monthly Sales Trend"
    )
    st.plotly_chart(fig,use_container_width=True)

    #------ PIE CHART PAYMENT METHOD VS SALES -------#

    payment_sales=(filtered_df.groupby('payment_method')['total_sales'].sum().reset_index())
    fig=px.pie(
        payment_sales,
        names="payment_method",
        values="total_sales",
        hole=0.45,
        title="Sales by Payment Method"
    )
    st.plotly_chart(fig,use_container_width=True)

    #------- BAR-CHART CATEGORY VS QUANTITY ------#

    category_quantity=(filtered_df.groupby('category')['quantity'].sum().reset_index())
    fig=px.bar(
        category_quantity,
        x="category",
        y='quantity',
        title=" Quantity Sold by Category",
        text_auto=".2s"
    )
    st.plotly_chart(fig,use_container_width=True)

    #----- BAR-GRAPH TIME PERIOD VS SALES ------#

    time_sales=(filtered_df.groupby('time_period')['total_sales'].sum().reset_index())
    fig=px.bar(
        time_sales,
        x="time_period",
        y='total_sales',
        title='Sales by Time Period'
    )
    st.plotly_chart(fig,use_container_width=True)



#-------- 2. CUSTOMER ANALYSIS ---------

if page=="Customer Analysis":
     #------ SCATTER-PLOT RATING VS SALES -----#
    st.subheader("CUSTOMER ANALYSIS")
    rating_sales=(filtered_df.groupby('rating')['total_sales'].sum().reset_index())
    fig=px.scatter(
        rating_sales,
        x='rating',
        y='total_sales',
        title="Customer Rating vs Sales"
    )
    st.plotly_chart(fig,use_container_width=True)

    #----- CORRELATION BETWEEN UNIT_PRICE , QUANTITY , RATING , PROFIT_MARGIN, SALES , PROFIT  ------#
    st.subheader("Correlation Analysis")
    numeric_df=filtered_df[['unit_price','quantity','rating','profit_margin','total_sales','profit']]
    corr=numeric_df.corr()
    fig,ax=plt.subplots()
    sns.heatmap(
        corr,annot=True,cmap="coolwarm",ax=ax
    )
    st.pyplot(fig)


#------ WRITE A CAPTION ---------
st.sidebar.markdown("---")
st.sidebar.caption(f"Records: {len(df):,}")
st.sidebar.caption("Python • Pandas • Plotly • Scikit-learn • Streamlit")


#----- TRAIN MACHINE LEARNING MODEL -------#
features=[
    'Branch','City','category','unit_price',
    'quantity','rating','profit_margin','payment_method',
    'month','day','hour'
]
x=df[features]
y=df['total_sales']
x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)
categorical_features=[
    'Branch',"City",'category','payment_method'
]
numerical_features=[
    'unit_price','quantity','rating','profit_margin','month','day','hour'
]
preprocessor=ColumnTransformer(transformers=[("cat",
OneHotEncoder(handle_unknown='ignore'), 
categorical_features)],
remainder="passthrough")
model=Pipeline(steps=[
    ("preprocessor",preprocessor),
    ("model",RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
)
])
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
mae=mean_absolute_error(y_test,y_pred)
rmse=np.sqrt(mean_squared_error(y_test,y_pred))
r2=r2_score(y_test,y_pred)




# ------3. SALES ANALYSIS--------
if page=="Sales Analysis":
    st.subheader("SALES ANALYSIS")
    st.write("Mean_Absolute_Error(MSE) --->",mae)
    st.write("Root_Mean_Square_Erorr(RMSE) --->",rmse)
    st.write("R2_Score --->",r2)
  
    prediction_df = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": y_pred
    })
    plot_df = prediction_df.melt(
        var_name="Type",
        value_name="Sales"
    )
    fig = px.scatter(
        plot_df,
        x=plot_df.index,
        y="Sales",
        color="Type",
        color_discrete_map={
            "Actual": "blue",
            "Predicted": "red"
        },
        title="Actual vs Predicted Sales"
    )
    fig.update_layout(
        xaxis_title="Test Data",
        yaxis_title="Total Sales",
        legend_title="Sales Type"
    )
    st.plotly_chart(fig, use_container_width=True)

    
    


#----- 4. MACHINE LEARNING ------
if page=="Machine Learning":
    st.header("Sales Prediction")
    branch=st.selectbox("Branch",df["Branch"].unique())
    city=st.selectbox("City",df['City'].unique())
    category=st.selectbox("category",df['category'].unique())
    unit_price=st.number_input("unit price",min_value=1)
    quantity=st.number_input("Quantity",min_value=1)
    rating=st.slider('Rating',1.0,10.0,5.0)
    profit_margin=st.number_input("Profit Margin",min_value=0.0,max_value=1.0)
    payment_method=st.selectbox("Payment Method",df['payment_method'].unique())
    if st.button("Predict Sales"):
        input_data=pd.DataFrame({
            "Branch":[branch],
            'City':[city],
            'category':[category],
            'unit_price':[unit_price],
            'quantity':[quantity],
            'rating':[rating],
            'profit_margin':[profit_margin],
            'payment_method':[payment_method],
            'month':[8],
            'day':[21],
            'hour':[14]

        })
        prediction=model.predict(input_data)[0]
        st.success(f'Predicted Sales: ${prediction:,.2f}')
        joblib.dump(model,"sales_model.pkl")
        model=joblib.load("sales_model.pkl")



# ------ 5. DATASET --------
if page=='Dataset':

    st.header("Dataset Info")
    st.write("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")
    st.write("Rows: " ,df.shape[0])
    st.write("Columns: ",df.shape[1])
    st.write("Duplicate Values")
    st.write(df.duplicated().sum())

#------ 6. BUSINESS INSIGHTS --------
if page=="Business Insights":
    #------ BUSINESS INSIGHTS --------
    best_category=(filtered_df.groupby('category')['total_sales'].sum().idxmax())
    best_city=(filtered_df.groupby("City")['total_sales'].sum().idxmax())
    best_payment=(filtered_df.groupby("payment_method")['total_sales'].sum().idxmax())

    st.subheader("Business Insights")
    st.info(f'Best performing category:{best_category}')
    st.info(f'Highest sales city:{best_city}')
    st.info(f'Most used Payment method:{best_payment}')

    lowest_category=(filtered_df.groupby('category')['total_sales'].sum().idxmin())
    st.warning(f"{lowest_category} is the lowest-performing category."
    "Consider promotional campaigns or pricing strategies.")
