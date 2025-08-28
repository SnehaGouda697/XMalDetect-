import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Example dataset (replace with your real dataset)
urls = ["http://good.com", "http://badmalware.com"]
labels = [0, 1]

# Train vectorizer + model
VEC = TfidfVectorizer()
X = VEC.fit_transform(urls)
LR = LogisticRegression()
LR.fit(X, labels)

# Save both to models/ folder
joblib.dump(LR, "models/url_lr.pkl")
joblib.dump(VEC, "models/url_vectorizer.pkl")
print("✅ URL model & vectorizer saved successfully!")

