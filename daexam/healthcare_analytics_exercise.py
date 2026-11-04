"""
Title: Healthcare Patient Analytics Lifecycle 
Description: Fill in the TODO sections across the 5 lifecycle phases using 
             'patient_health_data.csv'.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, LinearRegression from sklearn.linear_model, and evaluation metrics
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , r2_score

def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup 
    - Goal: Load 'patient_health_data.csv' and inspect structure.
    - Check for null values and print summary info.
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Print first 5 rows and verify dataset shape
    # TODO: Check for any missing values
    
    file_path = 'patient_health_data.csv'
    
    df = pd.read_csv(file_path)
    
    print(df.head())
    print(df.shape)
    print("Missing Values : " , df.isnull().sum())
    df.info()

    return df 
def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures 
    - Goal: Compute measures of central tendency and dispersion 
      for 'Systolic_BP'.
    - Check for potential outliers using the IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics ")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, Variance, and IQR for Systolic_BP
    # TODO: Identify any values falling outside 1.5 * IQR bounds
    df.columns = df.columns.str.strip().str.lower()
    
    mean = df['systolic_bp'].mean()
    median =df['systolic_bp'].median()
    std_dev = df['systolic_bp'].std()
    variance = df['systolic_bp'].var()
    q1 = df['systolic_bp'].quantile(0.25)
    q3 = df['systolic_bp'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df['systolic_bp'] < lower_bound) | (df['systolic_bp'] > upper_bound)]    
    
    print(f"Mean: {mean}, Median: {median}, Std Dev: {std_dev}, Variance: {variance}, IQR: {iqr}")
    print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
    print(f"Outliers: {outliers}")
    return df


def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation 
    - Goal: Examine relationships between BMI, Daily Steps, and Systolic BP.
    - Compute Pearson correlation matrix.
    """
    print("\n[PHASE 3] Bivariate Association ")
    print("-" * 65)
    # TODO: Select numeric columns and compute Pearson correlation matrix
    # TODO: Highlight correlations involving Systolic_BP
    numeric_cols = df.select_dtypes(include =np.number)
    
    correlation_matrix = numeric_cols.corr(method='pearson')
    print(correlation_matrix)
    
    correlations_with_systolic_bp = correlation_matrix['systolic_bp'].sort_values(ascending=False)
    print("Correlations with Systolic_BP:")
    print(correlations_with_systolic_bp)
    
    
    return df
            


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling 
    - Goal: Predict 'Systolic_BP' based on 'BMI'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling ")
    print("-" * 65)
    # TODO: Set X = df[['BMI']] and y = df['Systolic_BP']
    # TODO: Fit Linear Regression model and output slope & intercept
    x =df[['bmi']]
    y=df['systolic_bp']
    
    model = LinearRegression()
    
    evaluate = model.fit(x,y)
    print(evaluate)
    
    slope = model.coef_[0]
    intercept = model.intercept_
    
    print("Slope" , slope)
    print("intercept" , intercept)

    return model,x,y
def phase_5_evaluation_and_reporting(model, x, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendations (5 Marks)
    - Goal: Evaluate model performance using R-squared and MAE.
    - Provide prescriptive clinical recommendations based on findings.
    """
    print("\n[PHASE 5] Evaluation & Clinical Action (5 Marks)")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    # TODO: Print prescriptive clinical action items
    
    pred_y = model.predict(x)
    print("Predicted Values : " , pred_y)
    
    r2_score_value = r2_score(y,pred_y)
    mae_val = mean_absolute_error(y,pred_y)
    
    print("R2 Score : " , r2_score_value)
    print("Mean Absolute Error : " , mae_val)
    
    


def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING HEALTHCARE ANALYTICS LIFECYCLE ")
    print("=" * 65)
    
    # Executing phases chronologically
    df = phase_1_discovery_and_setup()
    df = phase_2_descriptive_statistics(df)
    df = phase_3_bivariate_association(df)
    model, x, y = phase_4_predictive_modeling(df)
    phase_5_evaluation_and_reporting(model, x, y, df)


if __name__ == "__main__":
    run_analytics_lifecycle()