"""runs a simple machine learning expirement"""
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def main():
    """runs a basic logistic regression model
    and logs it with mlflow"""
    df = pd.read_csv("data/airline-safety.csv", delimiter=",")

    features = df[
        [
            "incidents_85_99",
            "fatal_accidents_85_99",
            "fatalities_85_99",
            "incidents_00_14",
            "fatal_accidents_00_14",
            "fatalities_00_14",
        ]
    ]
    target = df["avail_seat_km_per_week"]

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    clf = LogisticRegression(max_iter=1000)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    with mlflow.start_run():
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("data_path", "data/airline-safety.csv")

        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(clf, "mlruns/0")


if __name__ == "__main__":
    main()
