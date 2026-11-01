import numpy as np 
import pandas as pd
import logging 


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"

)

logger = logging.getLogger(__name__)
class Pipeline:
    
    def __init__ (self):
        logger.info("Start")

    def inspect_data(self , df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        logger.info("Inspection Start")
        
        logger.info("Shape: %s" , df.shape)
        logger.info("Columns: %s" , list(df.columns))
        logger.info("First Five Rows: %s" , df.head())
        
        return df

    def check_missing_values(self , df: pd.DataFrame) -> pd.DataFrame:
        df=df.copy()
        
        logger.info("Missing Values")
        
        missing_vals = df.isnull().sum()
        
        missing_cols = pd.DataFrame({
            "Missings Values " : missing_vals
        })
        
        logger.info("Missing Columns: %s" , missing_cols)
        return df
    
    def standardize_columns(self , df: pd.DataFrame)-> pd.DataFrame:
        
        df = df.copy()
        
        df.columns= (df.columns. 
                     str.strip().
                     str.lower().
                     str.replace(" " , "_")
                     )
        
        logger.info("Standardize:  %s " , df )
         
        
        return df
    def normalize_text(self , df:pd.DataFrame)->pd.DataFrame:
        
        df=df.copy()
        
        df["gender"] = df["gender"].str.lower().str.strip()
        
        logger.info("Normalized : %s" , df )
        
        return df 
    def duplicates(self , df:pd.DataFrame)->pd.DataFrame:
        df = df.copy()
        
        
        duplicate_count = df.duplicated().sum()
        
        logger.info("Duplicates record: %s" , duplicate_count)
        df = df.drop_duplicates(keep="first")
        
        
        
        return df 
    def missing_value_imputation(self,df:pd.DataFrame)-> pd.DataFrame:
        df = df.copy()
        
        df["age"] = df["age"].fillna(df["age"].mean())
        
        
        return df
    def identify_data_types(self , df: pd.DataFrame)->pd.DataFrame:
        
        df = df.copy()
        
        numerical = df.select_dtypes(
            include=np.number
        ).columns.to_list()
        
        categorical = df.select_dtypes(
            include = ["object" , "string" , "category"]
        ).columns.to_list()
        
        
        
        logger.info("Numerical: %s" , numerical)
        logger.info("Categorical: %s" , categorical)
        
        return df
    
    def summary(self , df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        summary = df.describe(include ="all")
        
        logger.info("Summary : %s" , summary)
        
        return df
    
    def fit_transform(self , df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        df_profiled = (
            df.pipe(self.inspect_data)
            .pipe(self.check_missing_values)
            .pipe(self.standardize_columns)
            .pipe(self.normalize_text)
            .pipe(self.duplicates)
            .pipe(self.missing_value_imputation)
            .pipe(self.identify_data_types)
            .pipe(self.summary)
        )
        
        return df_profiled


if __name__ == "__main__":
    raw_data = {
    "Employee_ID": [1, 2, 3, 4, 5, 6],
    "Age": [22, 25, np.nan, 30, 22, 35],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [25000, 30000, 28000, 25000, 35000, 40000],
    "Experience": [1, 2, 1, 5, 3, 8],
    "gender":["f","f","m","m","f","m"]
}

df_raw = pd.DataFrame(raw_data)

print("RAW DATASET")
print(df_raw)


full = Pipeline()

df_profiled = full.fit_transform(df_raw)

print(df_profiled)