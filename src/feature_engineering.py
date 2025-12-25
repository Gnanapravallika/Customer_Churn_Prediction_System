import pandas as pd
from config import PROCESSED_DATA_PATH

def get_features_and_target():
    df= pd.read_csv(PROCESSED_DATA_PATH)

    X=df.drop(columns=["Churn"])
    y=df["Churn"]

    if "CustomerFeedback" in X.columns:
        X= X.drop(columns=["CustomerFeedback"])

    
    cat_cols= X.select_dtypes(include=["object"]).columns

    #one-hot encode
    X_encoded = pd.get_dummies(X,columns=cat_cols,drop_first=True)

    return X_encoded,y
