"""
Title: Real Estate Price Analytics Lifecycle
Description: Fill in the TODO sections across the 5 lifecycle phases.
Dataset: house_prices.csv  (75 rows)
Columns: House_ID, Locality, Area_SqFt, Bedrooms, Age_Years, Price_Lakhs
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, scikit-learn LinearRegression, and metrics


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup (5 Marks)
    - Goal: Load 'house_prices.csv' and inspect structure.
    - Check for null values and handle them (fill numeric NaNs with the median).
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Print first 5 rows, shape, and df.info()
    # TODO: Count missing values per column and impute numeric NaNs with the median
    pass


def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures (10 Marks)
    - Goal: Compute central tendency and dispersion for 'Price_Lakhs'.
    - Detect outliers using the IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, and IQR for Price_Lakhs
    # TODO: Compute lower/upper bounds (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
    # TODO: Print the houses (House_ID) whose Price_Lakhs falls outside the bounds
    # TODO: Print average Price_Lakhs per Locality (groupby)
    pass


def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation (10 Marks)
    - Goal: Examine relationships among Area_SqFt, Bedrooms, Age_Years and Price_Lakhs.
    """
    print("\n[PHASE 3] Bivariate Association")
    print("-" * 65)
    # TODO: Compute Pearson correlation matrix of the numeric columns
    # TODO: Highlight corr(Area_SqFt, Price_Lakhs) and interpret its strength
    # TODO: Name the feature most strongly correlated with Price_Lakhs
    pass


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling (10 Marks)
    - Goal: Predict 'Price_Lakhs' from 'Area_SqFt'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling")
    print("-" * 65)
    # TODO: Set X = df[['Area_SqFt']] and y = df['Price_Lakhs']
    # TODO: Fit LinearRegression; print slope and intercept
    # TODO: Predict Price_Lakhs when Area_SqFt = 1500 sq ft and print the result
    # TODO: return model, X, y
    pass


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendation (5 Marks)
    - Goal: Evaluate the model using R-squared and MAE.
    - Provide operational recommendations for a property-investment advisory firm.
    """
    print("\n[PHASE 5] Evaluation & Recommendations")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    # TODO: Print a prescriptive action item: estimate the price increase per extra 100 sq ft and advise buyers which size range gives the best value
    pass


def run_analytics_lifecycle():
    """Facade Orchestrator function."""
    print("=" * 65)
    print("STARTING REAL ESTATE ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)

    df = phase_1_discovery_and_setup()
    # phase_2_descriptive_statistics(df)
    # phase_3_bivariate_association(df)
    # model, X, y = phase_4_predictive_modeling(df)
    # phase_5_evaluation_and_reporting(model, X, y, df)


if __name__ == "__main__":
    run_analytics_lifecycle()
