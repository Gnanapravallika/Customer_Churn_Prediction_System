import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from config import MODEL_PATH, RANDOM_STATE, TEST_SIZE
from feature_engineering import get_features_and_target

def train():
    X,y = get_features_and_target()

    X_train,X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=RANDOM_STATE,
        class_weight="balanced"

    )

    model.fit(X_train,y_train)

    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved to:", MODEL_PATH)


if __name__ == "__main__":
    train()