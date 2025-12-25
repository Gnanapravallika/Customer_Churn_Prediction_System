import pandas as pd
import os
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def preprocess_data():

    df=pd.read_csv(RAW_DATA_PATH)

    if "customerID" in df.columns:
        df=df.drop(columns=["customerID"])

    if "TotalCharges" in df.columns:
        df["TotalCharges"]=pd.to_numeric(df["TotalCharges"],errors="coerce")
    
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    cat_cols = df.select_dtypes(include=["object"]).columns
    if "CustomerFeedback" in cat_cols:
        cat_cols = cat_cols.drop("CustomerFeedback")

    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    # Encode target
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Save processed data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print(" Data preprocessing complete. Saved to:", PROCESSED_DATA_PATH)


if __name__ == "__main__":
    preprocess_data()