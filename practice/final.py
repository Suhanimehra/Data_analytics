# import numpy as np
# import pandas as pd 
# from sklearn.linear_model import LinearRegression , LogisticRegression
# from sklearn.metrics import r2_score,mean_absolute_error
# from sklearn.preprocessing import OneHotEncoder , OrdinalEncoder,StandardScaler
# from sklearn.model_selection import train_test_split

# class DataCleaning:
    
#     def __init__(self , df:pd.DataFrame) -> None:
#         self.df=df.copy()
    
#     def phase1_discovery_and_setup(self):
        
#         print(self.df.head())
#         print(self.df.shape)
#         print(self.df.columns)
#         self.df.info()
#         print(self.df.describe())
        
#         missing_vals = self.df.isnull().sum()
#         missing_percentage = (missing_vals/len(self.df))*100
        
#         dupli = self.df.duplicated().sum()
        
#         print("missing vals : " , missing_vals)
#         print("missing percentage : " , missing_percentage)
        
#         print("Duplicated vals : ",dupli)
#         # print("Citys" , self.df['City'].nunique)
        
        
#         return self 
#     def snake_case(self):
        
#         self.df.columns = (self.df.columns.str.strip().str.lower().str.replace(" ","_"))
        
#         return self 
    
#     def sanitize_text(self):
        
#         categorical_cols = self.df.select_dtypes(include = ['string' , 'object' , 'category']).columns
        
#         for col in categorical_cols :
#            self.df[col]=self.df[col].str.strip().str.lower().str.replace(" ","_").astype("string")
#         return self
    
#     def convert_data_types(self):
        
#         self.df["application_date"]=pd.to_datetime(
#             self.df["application_date"],
#             errors = "coerce"
#         )
        
#         numeric_cols = self.df.select_dtypes(include = np.number).columns
        
#         for col in numeric_cols:
#             self.df[col] = pd.to_numeric(
#                 self.df[col],
#                 errors = "coerce"
#             )

        
#         return self
    
#     def find_missing(self):
        
#         missing_vals = self.df.isnull().sum()
#         missing_percentage = (missing_vals/len(self.df))*100
        
        
#         print("missing vals : " , missing_vals)
#         print("missing percentage : " , missing_percentage)
        
#         return self
    
#     def duplicates(self):
        
#         dupli = self.df['applicant_id'].duplicated().sum()
        
#         self.df = self.df.drop_duplicates(subset = ['applicant_id'], keep = 'first')
#         print("Duplicates: " , dupli)
        
#         return self   
    
#     def fill_missing(self):
#         numeric_cols = self.df.select_dtypes(include = np.number).columns

#         categorical_cols = self.df.select_dtypes(['string','category','object']).columns
        
#         date_cols = self.df.select_dtypes(['datetime64[ns]']).columns

#         for col in numeric_cols:
#             self.df[col]=self.df[col].fillna(self.df[col].median())
#         for col in categorical_cols:
#             self.df[col]=self.df[col].fillna(self.df[col].mode()[0])
#         for col in date_cols:
#             self.df[col]=self.df[col].fillna(self.df[col].median())
        
#         return self   
    
#     def remove_outliers(self):
#         numeric_cols = self.df.select_dtypes(include = np.number).columns
        
#         for col in numeric_cols:
#             q1 = self.df[col].quantile(0.25)
#             q3 = self.df[col].quantile(0.75)
#             iqr = q3-q1

#             lower = float(q1-1.5*iqr)
#             upper = float(q3+1.5*iqr)

#             # print("loweer: ",lower)
#             # print("upper: " , upper)
            
#             outliers = self.df[(
#                 self.df[col] <lower
#             ) | (self.df[col]>upper)]
#             self.df[col] = self.df[col].clip(
#                 lower=lower,
#                 upper=upper
#                 )
#             # print("outliers : " , outliers)
            
#             # self.df[col] = outliers.clip(lower,upper)
            
#         return self
#     def standardize_city(self):
#         regional_mapping = {
#             "blr" : "bengaluru",
#             "bengaluru":"bengaluru",
#             "bangalore" : "bengaluru",
#             "mum":"mumbai",
#             "mumbai":"mumbai",
#             "bombay":"mumbai",
#             "del":"delhi",
#             "delhi":"delhi",
#             "hyderabad":"hyderabad",
#             "hyd":"hyderabad"
#         }
        
#         self.df['city'] = self.df['city'].replace(regional_mapping)
#         return self
    
#     def EDA(self):
#         # mean_annual = self.df['annual_income'].mean()
#         # median_annual = self.df['annual_income'].median()
#         # std_annual = self.df['annual_income'].std()
#         # mean_loan = self.df['loan_amount'].mean()
#         # median_loan = self.df['loan_amount'].median()
#         # std_loan = self.df['loan_amount'].std()
#         # mean_credit = self.df['credit_score'].mean()
#         # median_credit = self.df['credit_score'].median()
#         # std_credit = self.df['credit_score'].std()
        
#         q1=self.df['loan_amount_k'].quantile(0.25)
#         q3=self.df['loan_amount_k'].quantile(0.75)
        
#         iqr = q3-q1
#         print("IQR LOAN AMOUNT " , iqr)
#         numeric_cols = self.df.select_dtypes(include = np.number)
        
#         corr_matrix = numeric_cols.corr(method='pearson')
#         print(corr_matrix)
        
        
#         return self
#     def FeatureEngineering(self):
        
#         self.df['loan_to_income_ratio'] = self.df['loan_amount_k']/self.df['annual_income_k'].replace(0,np.nan)
#         self.df['loan_to_income_ratio'] = (
#             self.df['loan_to_income_ratio'].fillna(0)
#         )
#         bins = [18,25,35,50,100]
#         label =["young","adult","middle_aged","senior"]
#         self.df['age_groups']= pd.cut(
#             self.df['age'],
#             bins = bins,
#             labels=label
#         )
        
#         category = ["low","medium","high","very_high"]
#         self.df["income_segments"] = pd.qcut(
#             self.df['annual_income_k'],
#             labels = category,
#             q=4
#         )
#         self.df['has_existing_loan'] = np.where(
#             self.df['loan_amount_k'] >0,1,0)
#         self.df['is_home_owner'] = np.where(
#             self.df['housing_status'] == 'own',1,0)
        
#         encoder_cols =[
#             'employment_type',
#             'housing_status',
#             'city',
#             'loan_purpose '
#             ]
#         self.encoder = OneHotEncoder(
#             sparse_output=False,
#             handle_unknown='ignore',
#             dtype=int
#         ) 
#         encoded_array = self.encoder.fit_transform(self.df[encoder_cols])
        
#         encoded_df = pd.DataFrame(
#             encoded_array,
#             columns = self.encoder.get_feature_names_out(encoder_cols),
#             index=self.df.index
#         )
        
#         self.df = pd.concat(
#             [
#                 self.df.drop(columns = encoder_cols),
#                 encoded_df
#             ],
#             axis=1
#         )
#         order = [['school', 'graduate', 'postgraduate']]
#         self.encoder_o = OrdinalEncoder(
#             categories= order,
#             dtype=int
            
#         )
        
#         encoded = self.encoder_o.fit_transform(
#             self.df[['education_level']]
#         )
#         encoded_array = pd.DataFrame(
#             encoded ,
#             columns = ['education_level'],
#             index = self.df.index
#         )
#         self.df['education_level']=encoded_array['education_level']
#         return self
#     def training(self):
        
#         y = self.df['default_flag']

#         X = self.df.drop(
#             columns=['default_flag', 'applicant_id', 'applicant_name'],
#             errors='ignore'
#         )
#         X = X.astype(float)
#         X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)
#         # Scaling
#         self.scaler = StandardScaler()

#         X_train = self.scaler.fit_transform(X_train)

#         X_test = self.scaler.transform(X_test)
#         self.model = LogisticRegression()
#         self.model.fit(X_train,y_train)
#         self.y_test = y_test
#         self.prediction = self.model.predict(X_test)
#         print("prediction: ", self.prediction)
#         return self
#     def model_evaluate(self):
#         return self
#     def pipeline(self) -> pd.DataFrame:
        
#         df_profiled = (
#             self.phase1_discovery_and_setup()
#             .snake_case()
#             .sanitize_text()
#             .convert_data_types()
#             .find_missing()
#             .duplicates()
#             .fill_missing()
#             .remove_outliers()
#             .standardize_city()
#             .EDA()
#             .FeatureEngineering()
#         )
#         return df_profiled.df

# if __name__ =="__main__":
    
#     df = pd.read_csv("combined_da_ml_loan_risk_practical.csv")
    
#     object = DataCleaning(df)
#     df_profiled = object.pipeline()


import numpy as np
import pandas as pd
import joblib

from sklearn.preprocessing import (
    OneHotEncoder,
    OrdinalEncoder,
    StandardScaler
)

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)


# ==========================================================
# CLASS 1: DATA CLEANING AND ANALYTICS
# ==========================================================

class DataCleaning:

    def __init__(self, df: pd.DataFrame) -> None:

        self.df = df.copy()


    # ------------------------------------------------------
    # PHASE 1: DATA DISCOVERY
    # ------------------------------------------------------

    def phase1_discovery_and_setup(self):

        print("\n========== DATA DISCOVERY ==========")

        print(self.df.head())

        print("\nShape:")
        print(self.df.shape)

        print("\nColumns:")
        print(self.df.columns)

        print("\nInformation:")
        self.df.info()

        print("\nStatistical Summary:")
        print(self.df.describe(include='all'))

        missing_vals = self.df.isnull().sum()

        missing_percentage = (
            missing_vals / len(self.df)
        ) * 100

        print("\nMissing Values:")
        print(missing_vals)

        print("\nMissing Percentage:")
        print(missing_percentage)

        print("\nDuplicate Rows:")
        print(self.df.duplicated().sum())

        print("\nTarget Distribution:")
        print(self.df['Default Flag'].value_counts(dropna=False))

        return self


    # ------------------------------------------------------
    # PHASE 2: STANDARDIZE COLUMN NAMES
    # ------------------------------------------------------

    def snake_case(self):

        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_", regex=False)
        )

        return self


    # ------------------------------------------------------
    # PHASE 3: SANITIZE TEXT
    # ------------------------------------------------------

    def sanitize_text(self):

        categorical_cols = self.df.select_dtypes(
            include=['object', 'string', 'category']
        ).columns

        for col in categorical_cols:

            self.df[col] = (
                self.df[col]
                .astype('string')
                .str.strip()
                .str.lower()
                .str.replace(" ", "_", regex=False)
            )

        return self


    # ------------------------------------------------------
    # PHASE 4: CONVERT DATA TYPES
    # ------------------------------------------------------

    def convert_data_types(self):

        self.df['application_date'] = pd.to_datetime(
            self.df['application_date'],
            errors='coerce',
            dayfirst=True
        )

        numeric_cols = [
            'age',
            'annual_income_k',
            'loan_amount_k',
            'credit_score',
            'existing_loans',
            'employment_years',
            'loan_term_months',
            'default_flag'
        ]

        for col in numeric_cols:

            self.df[col] = pd.to_numeric(
                self.df[col]
                .astype('string')
                .str.replace(',', '', regex=False),
                errors='coerce'
            )

        return self


    # ------------------------------------------------------
    # PHASE 5: FIND MISSING VALUES
    # ------------------------------------------------------

    def find_missing(self):

        missing_vals = self.df.isnull().sum()

        missing_percentage = (
            missing_vals / len(self.df)
        ) * 100

        print("\n========== MISSING VALUE REPORT ==========")

        print(missing_vals)

        print("\nMissing Percentage:")
        print(missing_percentage)

        return self


    # ------------------------------------------------------
    # PHASE 6: REMOVE DUPLICATES
    # ------------------------------------------------------

    def duplicates(self):

        duplicate_count = (
            self.df['applicant_id'].duplicated().sum()
        )

        self.df = self.df.drop_duplicates(
            subset=['applicant_id'],
            keep='first'
        )

        print("\nDuplicates Removed:", duplicate_count)

        return self


    # ------------------------------------------------------
    # PHASE 7: HANDLE MISSING VALUES
    # ------------------------------------------------------

    def fill_missing(self):

        numeric_cols = self.df.select_dtypes(
            include=np.number
        ).columns

        categorical_cols = self.df.select_dtypes(
            include=['object', 'string', 'category']
        ).columns

        date_cols = self.df.select_dtypes(
            include=['datetime64[ns]']
        ).columns

        # Numeric: median
        for col in numeric_cols:

            self.df[col] = self.df[col].fillna(
                self.df[col].median()
            )

        # Categorical: mode
        for col in categorical_cols:

            mode_values = self.df[col].mode()

            if not mode_values.empty:

                self.df[col] = self.df[col].fillna(
                    mode_values[0]
                )

        # Date: median date
        for col in date_cols:

            median_date = self.df[col].dropna().median()

            self.df[col] = self.df[col].fillna(
                median_date
            )

        return self


    # ------------------------------------------------------
    # PHASE 8: REMOVE OUTLIERS USING IQR
    # ------------------------------------------------------

    def remove_outliers(self):

        numeric_cols = [
            'age',
            'annual_income_k',
            'loan_amount_k',
            'credit_score',
            'employment_years',
            'loan_term_months'
        ]

        print("\n========== OUTLIER TREATMENT ==========")

        for col in numeric_cols:

            q1 = self.df[col].quantile(0.25)

            q3 = self.df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr

            upper = q3 + 1.5 * iqr

            outlier_count = (
                (self.df[col] < lower) |
                (self.df[col] > upper)
            ).sum()

            print(col, "Outliers:", outlier_count)

            self.df[col] = self.df[col].clip(
                lower=lower,
                upper=upper
            )

        return self


    # ------------------------------------------------------
    # PHASE 9: STANDARDIZE CITY
    # ------------------------------------------------------

    def standardize_city(self):

        regional_mapping = {

            'blr': 'bengaluru',
            'bangalore': 'bengaluru',
            'bengaluru': 'bengaluru',

            'mum': 'mumbai',
            'bombay': 'mumbai',
            'mumbai': 'mumbai',

            'del': 'delhi',
            'delhi': 'delhi',

            'hyd': 'hyderabad',
            'hyderabad': 'hyderabad'
        }

        self.df['city'] = (
            self.df['city'].replace(regional_mapping)
        )

        return self


    # ------------------------------------------------------
    # PHASE 10: EXPLORATORY DATA ANALYSIS
    # ------------------------------------------------------

    def EDA(self):

        print("\n========== EXPLORATORY DATA ANALYSIS ==========")

        cols = [
            'annual_income_k',
            'loan_amount_k',
            'credit_score'
        ]

        print("\nMean:")
        print(self.df[cols].mean())

        print("\nMedian:")
        print(self.df[cols].median())

        print("\nStandard Deviation:")
        print(self.df[cols].std())

        q1 = self.df['loan_amount_k'].quantile(0.25)

        q3 = self.df['loan_amount_k'].quantile(0.75)

        iqr = q3 - q1

        print("\nLoan Amount IQR:", iqr)

        numeric_cols = self.df.select_dtypes(
            include=np.number
        )

        corr_matrix = numeric_cols.corr(
            method='pearson'
        )

        print("\nCorrelation Matrix:")
        print(corr_matrix)

        print("\nDefault Flag Distribution:")
        print(self.df['default_flag'].value_counts())

        return self


    # ------------------------------------------------------
    # PHASE 11: FEATURE ENGINEERING
    # ------------------------------------------------------

    def FeatureEngineering(self):

        print("\n========== FEATURE ENGINEERING ==========")

        # Feature 1: Loan to income ratio

        self.df['loan_to_income_ratio'] = (
            self.df['loan_amount_k'] /
            self.df['annual_income_k'].replace(0, np.nan)
        )

        self.df['loan_to_income_ratio'] = (
            self.df['loan_to_income_ratio'].fillna(0)
        )


        # Feature 2: Age groups

        bins = [17, 25, 35, 50, 100]

        labels = [
            'young',
            'adult',
            'middle_aged',
            'senior'
        ]

        self.df['age_groups'] = pd.cut(
            self.df['age'],
            bins=bins,
            labels=labels
        )


        # Feature 3: Income segments

        category = [
            'low',
            'medium',
            'high',
            'very_high'
        ]

        self.df['income_segments'] = pd.qcut(
            self.df['annual_income_k'],
            q=4,
            labels=category,
            duplicates='drop'
        )


        # Feature 4: Existing loan indicator

        self.df['has_existing_loan'] = np.where(
            self.df['existing_loans'] > 0,
            1,
            0
        )


        # Feature 5: Home ownership indicator

        self.df['is_home_owner'] = np.where(
            self.df['housing_status'] == 'own',
            1,
            0
        )


        # Feature 6: One Hot Encoding

        encoder_cols = [
            'employment_type',
            'housing_status',
            'city',
            'loan_purpose',
            'age_groups',
            'income_segments'
        ]

        self.encoder = OneHotEncoder(
            sparse_output=False,
            handle_unknown='ignore',
            dtype=int
        )

        encoded_array = self.encoder.fit_transform(
            self.df[encoder_cols]
        )

        encoded_df = pd.DataFrame(
            encoded_array,
            columns=self.encoder.get_feature_names_out(
                encoder_cols
            ),
            index=self.df.index
        )

        self.df = pd.concat(
            [
                self.df.drop(columns=encoder_cols),
                encoded_df
            ],
            axis=1
        )


        # Feature 7: Ordinal Encoding

        order = [
            ['school', 'graduate', 'postgraduate']
        ]

        self.ordinal_encoder = OrdinalEncoder(
            categories=order,
            dtype=int
        )

        encoded = self.ordinal_encoder.fit_transform(
            self.df[['education_level']]
        )

        self.df['education_level'] = encoded.astype(int)

        print("\nFeature Engineering Completed")

        print("\nFinal Columns:")
        print(self.df.columns.tolist())

        return self


    # ------------------------------------------------------
    # PHASE 12: TRAIN TEST SPLIT + MODEL TRAINING
    # ------------------------------------------------------

    def training(self):

        print("\n========== MODEL TRAINING ==========")

        y = self.df['default_flag']

        X = self.df.drop(
            columns=[
                'default_flag',
                'applicant_id',
                'applicant_name',
                'application_date'
            ],
            errors='ignore'
        )

        # Ensure all predictors are numeric
        X = X.astype(float)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        # Scaling
        self.scaler = StandardScaler()

        X_train = self.scaler.fit_transform(X_train)

        X_test = self.scaler.transform(X_test)

        # Logistic Regression
        self.model = LogisticRegression(
            max_iter=1000,
            random_state=42
        )

        self.model.fit(X_train, y_train)

        self.y_test = y_test

        self.prediction = self.model.predict(X_test)

        print("\nModel Training Completed")

        return self


    # ------------------------------------------------------
    # PHASE 13: MODEL EVALUATION
    # ------------------------------------------------------

    def model_evaluate(self):

        print("\n========== MODEL EVALUATION ==========")

        print(
            "Accuracy:",
            accuracy_score(
                self.y_test,
                self.prediction
            )
        )

        print(
            "Precision:",
            precision_score(
                self.y_test,
                self.prediction,
                zero_division=0
            )
        )

        print(
            "Recall:",
            recall_score(
                self.y_test,
                self.prediction,
                zero_division=0
            )
        )

        print(
            "F1 Score:",
            f1_score(
                self.y_test,
                self.prediction,
                zero_division=0
            )
        )

        print("\nConfusion Matrix:")

        print(
            confusion_matrix(
                self.y_test,
                self.prediction
            )
        )

        print("\nClassification Report:")

        print(
            classification_report(
                self.y_test,
                self.prediction,
                zero_division=0
            )
        )

        return self


    # ------------------------------------------------------
    # PHASE 14: SAVE MODEL
    # ------------------------------------------------------

    def save_model(self):

        joblib.dump(
            self.model,
            'loan_default_model.pkl'
        )

        joblib.dump(
            self.scaler,
            'loan_scaler.pkl'
        )

        joblib.dump(
            self.encoder,
            'loan_encoder.pkl'
        )

        joblib.dump(
            self.ordinal_encoder,
            'education_encoder.pkl'
        )

        print("\nModel and preprocessing objects saved")

        return self


    # ------------------------------------------------------
    # PHASE 15: COMPLETE PIPELINE
    # ------------------------------------------------------

    def pipeline(self):

        self.phase1_discovery_and_setup()

        self.snake_case()

        self.sanitize_text()

        self.convert_data_types()

        self.find_missing()

        self.duplicates()

        self.fill_missing()

        self.remove_outliers()

        self.standardize_city()

        self.EDA()

        self.FeatureEngineering()

        self.training()

        self.model_evaluate()

        self.save_model()

        return self.df


# ==========================================================
# MAIN FUNCTION
# ==========================================================

if __name__ == "__main__":

    df = pd.read_csv(
        "combined_da_ml_loan_risk_practical.csv"
    )

    cleaner = DataCleaning(df)

    df_profiled = cleaner.pipeline()

    print("\n========== FINAL DATASET ==========")

    print(df_profiled.head())

    print("\nFinal Shape:", df_profiled.shape)


    # Load saved model

    loaded_model = joblib.load(
        'loan_default_model.pkl'
    )

    loaded_scaler = joblib.load(
        'loan_scaler.pkl'
    )

    print("\nSaved model loaded successfully")
 