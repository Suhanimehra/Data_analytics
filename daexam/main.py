import numpy as np 
import pandas as pd 
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s "
)
logger = logging.getLogger(__name__)

class DA:
    
    def __init__(self) -> None:
        logger.info("======Start========")
        
        
    def inspect_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        logger.info("===Inspect Data =======")
        
        logger.info("Shape: %s" , df.shape)
        logger.info("Header: %s" , df.head())
        logger.info("Columns List: %s " , list(df.columns))
        
        return df
    
    def check_missing_values(self , df: pd.DataFrame)-> pd.DataFrame:
        df=df.copy()
        
        missing_vals = df.isnull().sum()
        
        missing_percentage = (missing_vals/len(df))*100
        logger.info("Missing vals: %s \n" , missing_vals)
        logger.info("Missing Pecentage: %s" , missing_percentage)
        
        return df
    
    def identify_data_types(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        numerical_cols = df.select_dtypes(include=["float","integer"]).columns
        
        categorical_cols = df.select_dtypes(include=["string","object","category"]).columns
        
        datetime = df.select_dtypes(include=["datetime"]).columns
        
        logger.info("Numerical cols are : %s" , numerical_cols)
        logger.info("Categorical cols are : %s" , categorical_cols)
        logger.info("Datetime cols are : %s" , datetime)
        
        return df
    def summary(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        logger.info("Summary: ")
        logger.info(df.describe())
        return df    
    
    def standardize_columns(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        df.columns =(df.columns.
            str.strip().
            str.lower().
            str.replace(" ","_",regex = False) )
        
        return df
    
    def normalize_text(self , df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        numeric_cols = df.select_dtypes(include=["float"])
        
        for col in numeric_cols:
            df[col] = pd.to_numeric(
                df[col].astype("float"),
                errors = "coerce"
            )
        
        
        string_cols = df.select_dtypes(include = [ "object"]).columns
        df[string_cols] = df[string_cols].apply(
            lambda x : x.str.strip().str.lower()
        )
            
        
            
        print(df.info())
        return df 

    def regional_mapping(self , df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        regional_mapping={
            
            "Bengaluru" : "Bengaluru",
            "bengaluru" : "Bengaluru",
            "Chennai" : "Chennai",
            "chennai" : "Chennai",
            "CHENNAI" : "Chennai",
            "Mumbai" : "Mumbai",
            "mumbai" : "Mumbai",
            "MUMBAI" : "Mumbai",
            "Pune" : "Pune",
            "PUNE" : "Pune",
            "pune" : "Pune",
            "Delhi" : "Delhi",
            "delhi" : "Delhi",
            "Hyderabad" : "Hyderabad",
            "hyderabad" : "Hyderabad",
            "HYDERABAD" : "Hyderabad"
        }
        
        df["city"]=df["city"].replace(regional_mapping)
        return df
    def duplicates(self, df: pd.DataFrame)->pd.DataFrame:
        df = df.copy()
        
        duplicated = df.duplicated().sum()
        
        logger.info("Duplicated Values : \n %s" , duplicated )
        
        df = df.drop_duplicates()
        
        # logger.info("Dataframe after dropping Dupliacted \n %s " , df)
        logger.info("Shape after dropping : %s" , df.shape)
        
        df["employee_id"] = df["employee_id"].drop_duplicates()
        
        return df
    
    def numerical_imputer(self,df:pd.DataFrame)-> pd.DataFrame:
        df = df.copy()
        
        numeric_cols = df.select_dtypes(include=["float" , "integer"])
        
        for col in numeric_cols:
            
            median_val = df[col].median()
            
            df[col] = df[col].fillna(median_val)
            logger.info("Median Values Are :\n %s" , median_val)
        return df
    def categorical_imputer(self,df:pd.DataFrame)-> pd.DataFrame:
        df = df.copy()
        
        categorical_cols = df.select_dtypes(include=["string","object","category"])
        
        for col in categorical_cols:
            
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)
            
            logger.info("Mode Value : \n %s" , mode_val)
        return df
    def datetime_imputer(self,df:pd.DataFrame)-> pd.DataFrame:
        df=df.copy()
        
        datetime = df.select_dtypes(include="datetime").columns

        for col in datetime:
            
            date = df[col].median()
            
            df[col] = df[col].fillna(date)
            
            logger.info("Filling Date: \n %s " , date)
        return df
    def convert_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        # dates = df.select_dtypes(include="datetime").columns
        df["joining_date"]= pd.to_datetime(
            df["joining_date"],
            errors = "coerce"
        )
        return df 
    
    def outlier_detection(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        outliers_cols = df.select_dtypes(["float"]).columns
        
        for col in outliers_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            
            IQR = Q3-Q1

            upper_bound = Q3 +(1.5*IQR)
            lower_bound = Q1 - (1.5*IQR)
            
            # logger.info("Upper Bound =  \n %s" , upper_bound)
            # logger.info("Lower Bound =  \n %s" , lower_bound)
            
            outliers = df[(df[col]>=lower_bound ) & (df[col]<= upper_bound)]
            logger.info("Outliers in %s: %s", col, len(outliers))
            
        return df
    
    def fit_transform(self,df:pd.DataFrame)->pd.DataFrame:
        
        df_profiled = (
            df.pipe(self.inspect_data)
            .pipe(self.check_missing_values)
            .pipe(self.identify_data_types)
            .pipe(self.summary)
            .pipe(self.standardize_columns)
            .pipe(self.normalize_text)
            .pipe(self.regional_mapping)
            .pipe(self.duplicates)
            .pipe(self.numerical_imputer)
            .pipe(self.categorical_imputer)
            .pipe(self.datetime_imputer)
            .pipe(self.convert_datetime)
            .pipe(self.outlier_detection)
        )
        
        # print(df_profiled["city"].unique())
        print(df_profiled.shape)
        return df_profiled
if __name__ == "__main__":
    
    file_path = "employee_data_cleaning_practice.csv"
    
    raw_data = pd.read_csv(file_path)
    # print(raw_data)
    
    df = pd.DataFrame(raw_data)
    pd.set_option("display.max_rows",None)
    # pd.set_option("display.length",None)
    # print(df)
    
    
    
    final = DA()
    
    df_profiled = final.fit_transform(df)
    print(df_profiled)
    


