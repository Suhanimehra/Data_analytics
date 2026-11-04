"""
Title: Retail Store Sales & Marketing Analytics Lifecycle
Description: Fill in the TODO sections across the 5 lifecycle phases.
Dataset: store_sales.csv  (60 stores)
Columns: Store_ID, Region, Ad_Spend_K (Rs '000), Footfall (visitors/month),
         Staff_Count, Monthly_Sales_K (Rs '000)
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, scikit-learn LinearRegression, and metrics
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score , mean_absolute_error

def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup (5 Marks)
    - Goal: Load 'store_sales.csv' and inspect structure.
    - Check for null values and handle them (fill numeric NaNs with the median).
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Print first 5 rows, shape, and df.info()
    # TODO: Count missing values per column and impute with median
    df = pd.read_csv("store_sales.csv")
    print(df.shape)
    print(df.head())
    df.info()
    # print(df)
    
    missing = df.isnull().sum()
    print(missing)
    
    missing_percentage = (missing / len(df)) *100
    print(missing_percentage)
    numeric= df.select_dtypes(include= np.number)
    
    for col in numeric:
        
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
    
    
    
    return df

def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures (10 Marks)
    - Goal: Compute central tendency and dispersion for 'Monthly_Sales_K'.
    - Detect outliers using the IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, and IQR for Monthly_Sales_K
    # TODO: Compute lower/upper bounds (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
    # TODO: Print the stores (Store_ID) whose sales fall outside the bounds
    # TODO: Print average Monthly_Sales_K per Region (groupby)
    
    df.columns = df.columns.str.strip().str.lower()
    mean = df['monthly_sales_k'].mean()
    median = df['monthly_sales_k'].median()
    std = df['monthly_sales_k'].std()
    
    print(f"MEAN < MEDIAN < STD: , {mean:.2f}, {median:.2f} , {std:.2f}" )
    
    q1 = df['monthly_sales_k'].quantile(0.25)
    q3 = df['monthly_sales_k'].quantile(0.75)
    iqr = q3-q1

    print(f"iqr: {iqr:.2f}" )
    
    lower_bound = q1-1.5*iqr
    upper_bound = q3+ 1.5*iqr
    
    print("Lower: " , lower_bound)
    print("Upper: ", upper_bound)
    
    outliers= df[(df['monthly_sales_k'] < lower_bound) | (df['monthly_sales_k']>upper_bound)]
    
    print(outliers['store_id'])
    
     

    return df
def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation (10 Marks)
    - Goal: Examine relationships among Ad_Spend_K, Footfall,
      Staff_Count and Monthly_Sales_K.
    """
    print("\n[PHASE 3] Bivariate Association")
    print("-" * 65)
    # TODO: Compute Pearson correlation matrix of the numeric columns
    # TODO: Highlight corr(Ad_Spend_K, Monthly_Sales_K) and interpret its strength
    # TODO: Name the feature most strongly correlated with Monthly_Sales_K
    
    numeric_cols = df.select_dtypes(include = np.number)
    
    correlation = numeric_cols.corr(method='pearson')
    print("Coreelation" , correlation)
    
    highlight = correlation.loc['ad_spend_k' , 'monthly_sales_k']
    
    print(f"Highlight correlation : {highlight:.2f} ")
    # highest = correlation.df['monthly_sales_k'].max()
    # print(highest)
    return df

def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling (10 Marks)
    - Goal: Predict 'Monthly_Sales_K' from 'Ad_Spend_K'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling")
    print("-" * 65)
    # TODO: Set X = df[['Ad_Spend_K']] and y = df['Monthly_Sales_K']
    # TODO: Fit LinearRegression; print slope and intercept
    # TODO: Predict sales for an ad spend of Rs 30K and print the result
    # TODO: return model, X, y
    X = df[['ad_spend_k']] 
    y = df['monthly_sales_k']

    model = LinearRegression()
    
    model.fit(X,y)
    
    print("Slope: " , model.coef_[0])
    print("Intercept: " , model.intercept_)
    
    # result = model.predict(X[30000])
    # print(result)
    
    return model , X , y,df
    
    

def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendation (5 Marks)
    - Goal: Evaluate the model using R-squared and MAE.
    - Provide operational recommendations for the marketing budget.
    """
    print("\n[PHASE 5] Evaluation & Marketing Recommendations")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    # TODO: Print a prescriptive action item, e.g. how much extra sales
    #       each additional Rs 1K of ad spend is expected to bring, and
    #       whether increasing the ad budget is justified
    
    y_pred = model.predict(X)
    r2 = r2_score(y,y_pred)
    mae = mean_absolute_error(y,y_pred)
    
    print("r2: ", r2)
    print("mae: " , mae)

def run_analytics_lifecycle():
    """Facade Orchestrator function."""
    print("=" * 65)
    print("STARTING STORE ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)

    df = phase_1_discovery_and_setup()
    phase_2_descriptive_statistics(df)
    phase_3_bivariate_association(df)
    model, X, y ,df = phase_4_predictive_modeling(df)
    phase_5_evaluation_and_reporting(model, X, y, df)

    # print(df)

if __name__ == "__main__":
    run_analytics_lifecycle()
