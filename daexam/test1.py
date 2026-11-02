import numpy as np 
import pandas as pd 
import logging 

logging.basicConfig(
    level=logging.INFO,
    format=" %(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

class DataUndestanding():
    def __init__(self) -> None:
        print("Start")
        
    # def load_data(self , df: pd.DataFrame) -> pd.DataFrame:
        
    #     file_path = "stage1_to_stage4_telemetry_practice.csv"
        
    #     raw_data = pd.read_csv(file_path)
        
    #     df = pd.DataFrame(raw_data)
        
    #     return df
    
    def inspect_data(self , df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        logger.info("Shape: \n %s" , df.shape)
        logger.info("Columns: \n %s" , list(df.columns))
        logger.info("Head: \n %s" , df.head(5))
        logger.info("Tail: \n %s" , df.tail(5))
        logger.info("Sample: \n %s" , df.sample(5))
        logger.info("Datatypes: \n %s" , df.dtypes)
        logger.info("Memory usage : \n %s" , df.memory_usage())
        
        return df
    
    def statitical_analysis(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        logger.info("Describe: \n %s ",df.describe())
        logger.info("Describe all : \n %s ",df.describe(include="all"))
        
        return df
    
    def identify_data_types(self , df: pd.DataFrame) -> pd.DataFrame:
        df=df.copy()
        
        numeric_cols = df.select_dtypes(include=["float" , "integer"]).columns.to_list()
        categorical_cols = df.select_dtypes(include=["string" , "object" ,"category"]).columns.to_list()
        datetime_cols = df.select_dtypes(include=["datetime"]).columns.to_list()
        
        logger.info("numerical cols : \n %s" ,numeric_cols)
        logger.info("categorical cols : \n %s" ,categorical_cols)
        logger.info("datetime cols : \n %s" ,datetime_cols)
        return df
    
    def data_profile(self , df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        numeric_cols = df.select_dtypes(include=["float" , "integer"])
        
        for col in numeric_cols:
            
            missing_count_num = df[col].isnull().sum()
            
            unique_num=df[col].nunique()
            
            logger.info("Missing Count : \n %s " , missing_count_num)
            logger.info("Unique : \n %s " , unique_num)
        
        categorical_cols = df.select_dtypes(include=["string" , "object" ,"category"])
                
        for col in categorical_cols:
            
            missing_count_cat = df[col].isnull().sum()
            
            unique_cat=df[col].nunique()
            
            logger.info("Missing Count : \n %s " , missing_count_cat)
            logger.info("Unique : \n %s " , unique_cat)
        
        datetime_cols = df.select_dtypes(include=["datetime"])
        for col in datetime_cols:
                    
            missing_count_dt = df[col].isnull().sum()
            
            unique_dt=df[col].nunique()
            
            logger.info("Missing Count : \n %s " , missing_count_dt)
            logger.info("Unique : \n %s " , unique_dt)
        return df
    def check_missing_values(self,df:pd.DataFrame) -> pd.DataFrame:
        df=df.copy()
        
        missing = df.isnull().sum()
        missing_percentage = missing/len(df) *100
        
        logger.info("Missing Values: \n %s " , missing)
        logger.info("Missing Percentage: \n %s " , missing_percentage)
        return df
    
    def validate_numerical_columns(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        # df["age"]=100>df["age"]>0
        return df
    def validate_categorical_columns(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        categorical_cols = df.select_dtypes(["string","object","category"])
        
        for col in categorical_cols:
            df[col]=df[col].str.strip().str.lower()
        return df
    def validate_datetime_columns(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        date_cols = df.select_dtypes(["datetime"])
        
        for col in date_cols:
            df[col]=pd.to_datetime(
                df[col]
            )
            # mean_date = df[col].mean()
            df[col] = df[col].fillna("Null")
        
        # df["Last Interaction Date"] > df["Signup Date"]
        return df
    def check_duplicates(self , df:pd.DataFrame) -> pd.DataFrame:
        df=df.copy()
        
        dupli_val = df.duplicated().sum()
        # id = df["Customer ID"].duplicated().sum()
        
        # logger.info("Duplicates ID: \n %s" , id)

        # df=df.drop_duplicates(keep="first")
        
        logger.info("Duplicates values \n  %s", dupli_val)
        
        
        return df
    def outlier_detection(self , df:pd.DataFrame) -> pd.DataFrame:
        df=df.copy()
        
        numeric_cols = df.select_dtypes(include=["float" , "integer"])
        
        for col in numeric_cols:
            
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            
            IQR = Q3-Q1

            lowwer_bound = Q1-1.5*IQR
            upper_bound = Q3+1.5*IQR
            
            logger.info("Lower Bound : \n %s ", lowwer_bound)
            logger.info("Upper Bound : \n %s ", upper_bound)
            
        return df
    def standardize_columns(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        
        df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
        return df
    def imputation(self , df:pd.DataFrame) -> pd.DataFrame:
        df=df.copy()
        
        numeric_cols = df.select_dtypes(include=["float" , "integer"])
                
        for col in numeric_cols:
            
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            
        categorical_cols = df.select_dtypes(["string","object","category"])
                
        for col in categorical_cols:
            mode_val = df[col].mode()[0]
            df[col]=df[col].fillna(mode_val)
        return df
    def pipeline(self , df:pd.DataFrame)->pd.DataFrame:
        df_profiled = (
            # df.pipe(self.load_data)
            df.pipe(self.inspect_data)
            .pipe(self.statitical_analysis)
            .pipe(self.identify_data_types)
            .pipe(self.data_profile)
            .pipe(self.check_missing_values)
            .pipe(self.validate_numerical_columns)
            .pipe(self.validate_categorical_columns)
            .pipe(self.validate_datetime_columns)
            .pipe(self.check_duplicates)
            .pipe(self.outlier_detection)
            .pipe(self.standardize_columns)
            .pipe(self.imputation)
        )
        
        return df_profiled
    

class FeatureEngineering():
    def __init__(self):
        pass
if __name__ == "__main__":
    
    file_path = "stage1_to_stage4_telemetry_practice.csv"
            
    raw_data = pd.read_csv(file_path)
    
    df = pd.DataFrame(raw_data)
    
    start = DataUndestanding()
    df_profiled = start.pipeline(df)
    
    pd.set_option("display.max_columns", None)
    print(df_profiled)
    