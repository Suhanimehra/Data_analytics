"""
Title: Food Delivery Time Analytics Lifecycle
Description: Fill in the TODO sections across the 5 lifecycle phases.
Dataset: delivery_times.csv  (90 rows)
Columns: Order_ID, City, Distance_KM, Traffic_Index (1-10), Items_Count, Delivery_Time_Min
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, scikit-learn LinearRegression, and metrics


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup (5 Marks)
    - Goal: Load 'delivery_times.csv' and inspect structure.
    - Check for null values and handle them (drop rows with missing values).
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Print first 5 rows, shape, and df.info()
    # TODO: Count missing values per column and drop rows that contain missing values and print the new shape
    pass


def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures (10 Marks)
    - Goal: Compute central tendency and dispersion for 'Delivery_Time_Min'.
    - Detect outliers using the IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, and IQR for Delivery_Time_Min
    # TODO: Compute lower/upper bounds (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
    # TODO: Print the orders (Order_ID) whose Delivery_Time_Min falls outside the bounds
    # TODO: Print average Delivery_Time_Min per City (groupby)
    pass


def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation (10 Marks)
    - Goal: Examine relationships among Distance_KM, Traffic_Index, Items_Count and Delivery_Time_Min.
    """
    print("\n[PHASE 3] Bivariate Association")
    print("-" * 65)
    # TODO: Compute Pearson correlation matrix of the numeric columns
    # TODO: Highlight corr(Distance_KM, Delivery_Time_Min) and interpret its strength
    # TODO: Name the feature most strongly correlated with Delivery_Time_Min
    pass


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling (10 Marks)
    - Goal: Predict 'Delivery_Time_Min' from 'Distance_KM'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling")
    print("-" * 65)
    # TODO: Set X = df[['Distance_KM']] and y = df['Delivery_Time_Min']
    # TODO: Fit LinearRegression; print slope and intercept
    # TODO: Predict Delivery_Time_Min when Distance_KM = 12 km and print the result
    # TODO: return model, X, y
    pass


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendation (5 Marks)
    - Goal: Evaluate the model using R-squared and MAE.
    - Provide operational recommendations for the logistics team.
    """
    print("\n[PHASE 5] Evaluation & Recommendations")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    # TODO: Print a prescriptive action item: estimate added minutes per extra km and recommend a maximum delivery radius to keep promised delivery times
    pass


def run_analytics_lifecycle():
    """Facade Orchestrator function."""
    print("=" * 65)
    print("STARTING DELIVERY ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)

    df = phase_1_discovery_and_setup()
    # phase_2_descriptive_statistics(df)
    # phase_3_bivariate_association(df)
    # model, X, y = phase_4_predictive_modeling(df)
    # phase_5_evaluation_and_reporting(model, X, y, df)


if __name__ == "__main__":
    run_analytics_lifecycle()
