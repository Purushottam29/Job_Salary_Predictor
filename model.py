import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv("data/jobs.csv")

# Generate fake salaries for demo (replace with real salary data later)
import numpy as np
df["Salary"] = np.random.randint(40000, 120000, size=len(df))

X = df[["Title", "Tags"]]
y = df["Salary"]

preprocessor = ColumnTransformer(
    transformers=[
        ("title", OneHotEncoder(handle_unknown='ignore'), ["Title"]),
        ("tags", OneHotEncoder(handle_unknown='ignore'), ["Tags"])
    ])

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model.fit(X_train, y_train)

import joblib
joblib.dump(model, "model.joblib")
