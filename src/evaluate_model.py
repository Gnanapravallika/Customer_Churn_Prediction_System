import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from config import MODEL_PATH, RANDOM_STATE, TEST_SIZE
from feature_engineering import get_features_and_target

def evaluate():

    X,y = get_features_and_target()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y

    )

    model = joblib.load(MODEL_PATH)
    y_pred= model.predict(X_test)
    y_prob=model.predict_proba(X_test)[:,1]

    print(classification_report(y_test,y_train))
    print("ROC-AUC: ",roc_auc_score(y_test,y_prob))

if __name__=="__main__":
    evaluate()