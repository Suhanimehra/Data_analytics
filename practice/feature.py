import pandas as pd
import logging
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

logging.basicConfig(
    level=logging.INFO,
    datefmt=r'%Y-%m-%d %H:%M:%S',
    format= '%(asctime)s [%(levelname)s] %(message)s'
)

logger = logging.getLogger(__name__)

# filepath = './customer_subscription_sales_messy.csv'
filepath =  './customer_subscription_analytics_320.csv'

class DataCleaning:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def snake_case(self) -> "DataCleaning":
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(r'[\s\-]+', '_', regex=True)
            .str.replace(r'[^a-z0-9_]', '', regex=True)
        )
        logger.log(logging.INFO, "Converted columns to snake_case")
        return self

    def sanitize_text(self) -> "DataCleaning":
        string_col = self.df.select_dtypes(include=['object', 'string']).columns
        self.df[string_col] = self.df[string_col].apply(lambda x: x.str.strip().str.lower())
        logger.log(logging.INFO, "Sanitized text columns")

        if 'customer_name' in self.df.columns:
            self.df['customer_name'] = self.df['customer_name'].str.title()
            logger.log(logging.INFO, "Capitalized customer_name column")

        return self

    def convert_data_type(self) -> "DataCleaning":

        # Convert payment method to string
        self.df['payment_method'] = (
            self.df['payment_method'].astype('string')
        )

        # Remove commas and convert revenue to numeric
        self.df['monthly_revenue'] = pd.to_numeric(
            self.df['monthly_revenue']
            .astype('string')
            .str.replace(',', '', regex=False),
            errors='coerce'
        )

        self.df['signup_date'] = pd.to_datetime(
            self.df['signup_date'],
            format='mixed',
            dayfirst=True,
            errors='coerce'
        )

        logger.info("Converted column data types")

        return self


    def find_missing(self) -> "DataCleaning":
        missing_count = self.df.isnull().sum()
        missing_percentage = (
                self.df.isnull().mean() * 100
        ).round(2)
        missing_report = pd.DataFrame({
            "Missing Count": missing_count,
            "Missing Percentage": missing_percentage
        })
        logger.info(f"\nMissing Value Report:\n{missing_report}")
        return self

    def drop_duplicates(self) -> "DataCleaning":

        initial_rows = len(self.df)

        self.df = (
            self.df
            .drop_duplicates(subset=['customer_id'], keep='first')
            .reset_index(drop=True)
        )

        removed = initial_rows - len(self.df)

        logger.info(
            "Duplicate removal completed | Before: %d | After: %d | Removed: %d",
            initial_rows,
            len(self.df),
            removed
        )

        return self

    def fill_missing(self)-> "DataCleaning":
        # if 'satisfaction_score' in self.df.columns:
        #     self.df['satisfaction_score'] = self.df['satisfaction_score'].fillna(self.df['satisfaction_score'].mean())

        numeric_cols = self.df.select_dtypes(
            include='number'
        ).columns.drop('customer_id', errors='ignore')

        for col in numeric_cols:
            self.df[col]= self.df[col].fillna(self.df[col].median())

        string_col = self.df.select_dtypes(include=['object','string','category']).columns
        for col in string_col:
            if col == 'email':
                self.df['email'] = self.df['email'].fillna("Unknown")
                continue

            mode_value = self.df[col].mode()
            self.df[col] = self.df[col].fillna(mode_value.iloc[0])

        date_cols = self.df.select_dtypes(include=['datetime64[ns]']).columns
        for col in date_cols:
            self.df[col] = self.df[col].fillna(self.df[col].median())


        return self

    def remove_outliers(self) -> "DataCleaning":
        numeric_cols = self.df.select_dtypes(include=['float','integer']).columns
        for col in numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            # print lower bound and upper bound for debugging
            logger.info('Column: %s, Lower Bound: %f, Upper Bound: %f', col, lower_bound, upper_bound)
            logger.info('Removing outliers from column: %s', col)

            self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
        logger.info("Removed outliers from numeric columns")
        return self


    def standardize_city(self) -> "DataCleaning":
        city_mapping = {
            "blr": "bengaluru",
            "bangalore": "bengaluru",
            "bengaluru": "bengaluru",

            "mum": "mumbai",
            "bombay": "mumbai",
            "mumbai": "mumbai",

            "del": "delhi",
            "new delhi": "delhi",
            "delhi": "delhi",

            "hyd": "hyderabad",
            "hyderabad": "hyderabad",

            "chn": "chennai",
            "madras": "chennai",
            "chennai": "chennai",

            "pnq": "pune",
            "pune": "pune",

            "ccu": "kolkata",
            "calcutta": "kolkata",
            "kolkata": "kolkata",

            "jai": "jaipur",
            "jaipur": "jaipur",

            "amd": "ahmedabad",
            "ahmedabad": "ahmedabad",

            "cok": "kochi",
            "cochin": "kochi",
            "kochi": "kochi"
        }

        self.df["city"] = (
            self.df["city"]
            .replace(city_mapping)
        )

        logger.info("City standardized successfully")
        return self

    def get_data(self) -> pd.DataFrame:
        return self.df

class FeatureEngineering:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
    
    def one_hot_encoder(self)->FeatureEngineering:
        
        categorical_cols = self.df.select_dtypes(include=['object','category','string'])
        
        encoder = OneHotEncoder(
            sparse_output = False,
            dtype = int,
            handle_unknown = 'ignore'
        )
        
        encoded_array = encoder.fit_transform(categorical_cols)
        
        encoded_df=pd.DataFrame(
            encoded_array,
            columns = encoder.get_feature_names_out(categorical_cols.columns),
            index=self.df.index
            
        )
        
        self.df=pd.concat(
            [self.df.drop(columns = categorical_cols.columns),
            encoded_df],
            axis=1
        )
        
        return self