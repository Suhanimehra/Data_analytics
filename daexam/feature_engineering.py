import pandas as pd
import numpy as np

df = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105],
    "age": [22, 28, 35, 42, 30],
    "monthly_salary": [25000, 40000, 60000, 80000, 35000],
    "years_experience": [1, 4, 10, 18, 3],
    "department": ["IT", "HR", "IT", "Finance", "HR"],
    "joining_date": [
        "2022-01-10",
        "2021-05-15",
        "2019-08-20",
        "2015-03-12",
        "2023-06-01"
    ]
})


class FeatureEngineering():
    
    def __init__(self) -> None:
        print("Start")
    
    def create_domain_features(self , df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        df["anual_salary"] = df["monthly_salary"] * 12
        
        df["salary_per_experience"] = (df["monthly_salary"]/(df["years_experience"] + 1))
        
        conditions =[
            df["years_experience"] <2,
            df["years_experience"] >5,
            df["years_experience"].between(2,5)
        ]
        
        choices = ["junior" , "Senior" , "Mid"]
        
        
        df["experience_level"] = np.select(
            conditions,
            choices,
            default="Unknown"
        )
        
        return df 
    
    def create_datetime_features(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        # df["datetime"] = pd.to_datetime(
        #     df["joining_date"]
        # )
        df["joining_date"] = pd.to_datetime(
            df["joining_date"],
            errors="coerce"
        )
        
        df["joining_year"] = df["joining_date"].dt.year
        df["joining_month"] = df["joining_date"].dt.month
        df["joining_day"] = df["joining_date"].dt.day
        df["joining_day_of_week"] = df["joining_date"].dt.day_of_week # return numbers not strings monday is 0.
        
        condition = [
            df["joining_day_of_week"] == 5,
            df["joining_day_of_week"]== 6
        ]
        
        choice = [1,1]
        
        df["is_weekend"] = np.select(
            condition,
            choice,
            default=0
        )
        
        return df

if __name__=="__main__":
    
    feature = FeatureEngineering()
    
    data = feature.create_domain_features(df)
    date=feature.create_datetime_features(data)
    
    # print(data)
    print(date)