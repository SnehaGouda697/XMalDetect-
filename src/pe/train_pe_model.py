import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load dataset (correct path)
data = pd.read_csv("Dataset/data.csv",delimiter="|")

print("Columns in dataset:", data.columns)

# Handle label column
if "label" in data.columns:
    y = data["label"]
    X = data.drop("label", axis=1)
elif "legitimate" in data.columns:
    y = data["legitimate"]
    X = data.drop("legitimate", axis=1)
else:
    # Fallback: assume last column is label
    y = data.iloc[:, -1]
    X = data.iloc[:, :-1]

# Drop non-numeric columns if present
for col in ["Name", "md5"]:
    if col in X.columns:
        X = X.drop(col, axis=1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make sure models folder exists
os.makedirs("models", exist_ok=True)

# Save model and features
joblib.dump(clf, "models/pe_rf.pkl")
joblib.dump(list(X.columns), "models/pe_features.pkl")

print("✅ Model trained and saved successfully!")



