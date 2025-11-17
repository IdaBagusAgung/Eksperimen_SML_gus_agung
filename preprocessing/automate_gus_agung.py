"""
Automatic Preprocessing Script for Hotel Bookings Dataset
Author: gus_agung
Description: This script automates the preprocessing pipeline for hotel bookings data
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os
from datetime import datetime


class HotelBookingPreprocessor:
    """
    A comprehensive preprocessing class for hotel booking data
    """
    
    def __init__(self, random_state=42):
        """
        Initialize the preprocessor with required transformers
        
        Args:
            random_state (int): Random state for reproducibility
        """
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.feature_names = None
        self.target_column = 'is_canceled'
        
    def load_data(self, filepath):
        """
        Load dataset from CSV file
        
        Args:
            filepath (str): Path to the CSV file
            
        Returns:
            pd.DataFrame: Loaded dataframe
        """
        print(f"[INFO] Loading data from {filepath}")
        df = pd.read_csv(filepath)
        print(f"[INFO] Data loaded successfully. Shape: {df.shape}")
        return df
    
    def handle_missing_values(self, df):
        """
        Handle missing values in the dataset
        
        Args:
            df (pd.DataFrame): Input dataframe
            
        Returns:
            pd.DataFrame: Dataframe with handled missing values
        """
        print("[INFO] Handling missing values...")
        
        # Replace 'NULL' string with actual NaN
        df = df.replace('NULL', np.nan)
        
        # Fill children with 0
        if 'children' in df.columns:
            df['children'] = df['children'].fillna(0)
        
        # Fill agent and company with mode or 0
        if 'agent' in df.columns:
            df['agent'] = df['agent'].fillna(0)
        if 'company' in df.columns:
            df['company'] = df['company'].fillna(0)
            
        # Fill country with mode
        if 'country' in df.columns:
            df['country'] = df['country'].fillna(df['country'].mode()[0])
        
        print(f"[INFO] Missing values handled. Remaining NaN: {df.isnull().sum().sum()}")
        return df
    
    def remove_duplicates(self, df):
        """
        Remove duplicate rows
        
        Args:
            df (pd.DataFrame): Input dataframe
            
        Returns:
            pd.DataFrame: Dataframe without duplicates
        """
        print("[INFO] Removing duplicates...")
        initial_shape = df.shape[0]
        df = df.drop_duplicates()
        removed = initial_shape - df.shape[0]
        print(f"[INFO] Removed {removed} duplicate rows")
        return df
    
    def feature_engineering(self, df):
        """
        Create new features from existing ones
        
        Args:
            df (pd.DataFrame): Input dataframe
            
        Returns:
            pd.DataFrame: Dataframe with engineered features
        """
        print("[INFO] Engineering features...")
        
        # Total nights
        df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
        
        # Total guests
        df['total_guests'] = df['adults'] + df['children'] + df['babies']
        
        # Has special requests
        df['has_special_requests'] = (df['total_of_special_requests'] > 0).astype(int)
        
        # Booking lead time category
        df['lead_time_category'] = pd.cut(df['lead_time'], 
                                          bins=[-1, 7, 30, 90, 365, 999],
                                          labels=['very_short', 'short', 'medium', 'long', 'very_long'])
        
        # Month to season mapping
        season_map = {
            'January': 'Winter', 'February': 'Winter', 'December': 'Winter',
            'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
            'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
            'September': 'Fall', 'October': 'Fall', 'November': 'Fall'
        }
        df['season'] = df['arrival_date_month'].map(season_map)
        
        print(f"[INFO] Feature engineering completed. New shape: {df.shape}")
        return df
    
    def handle_outliers(self, df, columns=['adr', 'lead_time']):
        """
        Handle outliers using IQR method
        
        Args:
            df (pd.DataFrame): Input dataframe
            columns (list): Columns to check for outliers
            
        Returns:
            pd.DataFrame: Dataframe with handled outliers
        """
        print("[INFO] Handling outliers...")
        
        for col in columns:
            if col in df.columns:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                # Cap outliers instead of removing
                df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)
        
        print("[INFO] Outliers handled")
        return df
    
    def encode_categorical(self, df, fit=True):
        """
        Encode categorical variables
        
        Args:
            df (pd.DataFrame): Input dataframe
            fit (bool): Whether to fit encoders or use existing ones
            
        Returns:
            pd.DataFrame: Dataframe with encoded categorical variables
        """
        print("[INFO] Encoding categorical variables...")
        
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        # Remove target if present
        if self.target_column in categorical_cols:
            categorical_cols.remove(self.target_column)
        
        for col in categorical_cols:
            if fit:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.label_encoders[col] = le
            else:
                if col in self.label_encoders:
                    # Handle unseen labels
                    le = self.label_encoders[col]
                    df[col] = df[col].apply(lambda x: x if x in le.classes_ else 'unknown')
                    df[col] = le.transform(df[col].astype(str))
        
        print(f"[INFO] Encoded {len(categorical_cols)} categorical columns")
        return df
    
    def scale_features(self, X_train, X_test=None, fit=True):
        """
        Scale numerical features
        
        Args:
            X_train (pd.DataFrame): Training features
            X_test (pd.DataFrame, optional): Test features
            fit (bool): Whether to fit scaler or use existing one
            
        Returns:
            tuple: Scaled training and test features
        """
        print("[INFO] Scaling features...")
        
        if fit:
            X_train_scaled = self.scaler.fit_transform(X_train)
        else:
            X_train_scaled = self.scaler.transform(X_train)
        
        X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)
        
        if X_test is not None:
            X_test_scaled = self.scaler.transform(X_test)
            X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns, index=X_test.index)
            return X_train_scaled, X_test_scaled
        
        return X_train_scaled, None
    
    def preprocess_pipeline(self, df, fit=True):
        """
        Complete preprocessing pipeline
        
        Args:
            df (pd.DataFrame): Input dataframe
            fit (bool): Whether to fit transformers
            
        Returns:
            pd.DataFrame: Preprocessed dataframe
        """
        print("\n" + "="*50)
        print("Starting Preprocessing Pipeline")
        print("="*50)
        
        # Step 1: Handle missing values
        df = self.handle_missing_values(df)
        
        # Step 2: Remove duplicates
        df = self.remove_duplicates(df)
        
        # Step 3: Feature engineering
        df = self.feature_engineering(df)
        
        # Step 4: Handle outliers
        df = self.handle_outliers(df)
        
        # Step 5: Encode categorical variables
        df = self.encode_categorical(df, fit=fit)
        
        print("="*50)
        print("Preprocessing Pipeline Completed")
        print("="*50 + "\n")
        
        return df
    
    def prepare_for_training(self, filepath, test_size=0.2, save_path='preprocessing'):
        """
        Complete data preparation for model training
        
        Args:
            filepath (str): Path to raw data
            test_size (float): Proportion of test set
            save_path (str): Directory to save processed data
            
        Returns:
            tuple: X_train, X_test, y_train, y_test
        """
        # Load data
        df = self.load_data(filepath)
        
        # Preprocess
        df = self.preprocess_pipeline(df, fit=True)
        
        # Separate features and target
        if self.target_column not in df.columns:
            raise ValueError(f"Target column '{self.target_column}' not found in dataframe")
        
        X = df.drop(columns=[self.target_column])
        y = df[self.target_column]
        
        # Store feature names
        self.feature_names = X.columns.tolist()
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state, stratify=y
        )
        
        # Scale features
        X_train, X_test = self.scale_features(X_train, X_test, fit=True)
        
        # Save processed data
        os.makedirs(save_path, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        X_train.to_csv(os.path.join(save_path, f'X_train_{timestamp}.csv'), index=False)
        X_test.to_csv(os.path.join(save_path, f'X_test_{timestamp}.csv'), index=False)
        y_train.to_csv(os.path.join(save_path, f'y_train_{timestamp}.csv'), index=False)
        y_test.to_csv(os.path.join(save_path, f'y_test_{timestamp}.csv'), index=False)
        
        # Also save without timestamp for easy access
        X_train.to_csv(os.path.join(save_path, 'X_train.csv'), index=False)
        X_test.to_csv(os.path.join(save_path, 'X_test.csv'), index=False)
        y_train.to_csv(os.path.join(save_path, 'y_train.csv'), index=False)
        y_test.to_csv(os.path.join(save_path, 'y_test.csv'), index=False)
        
        # Save the entire preprocessed dataset
        df.to_csv(os.path.join(save_path, 'hotel_bookings_preprocessed.csv'), index=False)
        
        # Save preprocessor objects
        joblib.dump(self.scaler, os.path.join(save_path, 'scaler.pkl'))
        joblib.dump(self.label_encoders, os.path.join(save_path, 'label_encoders.pkl'))
        joblib.dump(self.feature_names, os.path.join(save_path, 'feature_names.pkl'))
        
        print(f"\n[SUCCESS] Processed data saved to {save_path}/")
        print(f"[INFO] Training set: {X_train.shape}")
        print(f"[INFO] Test set: {X_test.shape}")
        
        return X_train, X_test, y_train, y_test
    
    def load_preprocessor(self, save_path='preprocessing'):
        """
        Load saved preprocessor objects
        
        Args:
            save_path (str): Directory containing saved objects
        """
        print(f"[INFO] Loading preprocessor from {save_path}/")
        self.scaler = joblib.load(os.path.join(save_path, 'scaler.pkl'))
        self.label_encoders = joblib.load(os.path.join(save_path, 'label_encoders.pkl'))
        self.feature_names = joblib.load(os.path.join(save_path, 'feature_names.pkl'))
        print("[SUCCESS] Preprocessor loaded successfully")


def main():
    """
    Main function to run the preprocessing pipeline
    """
    # Initialize preprocessor
    preprocessor = HotelBookingPreprocessor(random_state=42)
    
    # Path to raw data (adjust based on your structure)
    raw_data_path = '../hotel_bookings.csv'
    
    # Check if file exists
    if not os.path.exists(raw_data_path):
        print(f"[ERROR] File not found: {raw_data_path}")
        print("[INFO] Please ensure hotel_bookings.csv is in the correct location")
        return
    
    # Run preprocessing
    try:
        X_train, X_test, y_train, y_test = preprocessor.prepare_for_training(
            filepath=raw_data_path,
            test_size=0.2,
            save_path='hotel_bookings_preprocessed'
        )
        
        print("\n" + "="*50)
        print("Preprocessing Summary")
        print("="*50)
        print(f"Total features: {len(preprocessor.feature_names)}")
        print(f"Training samples: {len(X_train)}")
        print(f"Test samples: {len(X_test)}")
        print(f"Target distribution (train): {y_train.value_counts().to_dict()}")
        print("="*50)
        
    except Exception as e:
        print(f"[ERROR] Preprocessing failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
