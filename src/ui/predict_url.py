import joblib
import os

# Paths to models
MODEL_PATH = "models/url_lr.pkl"
VEC_PATH   = "models/url_vectorizer.pkl"

# Check if files exist before loading
if not os.path.exists(MODEL_PATH) or not os.path.exists(VEC_PATH):
    raise FileNotFoundError("URL model or vectorizer file is missing! Please retrain and save them.")

# Load URL model + vectorizer
VEC = joblib.load(VEC_PATH)
LR  = joblib.load(MODEL_PATH)

def predict_url(url: str):
    """
    Predict if a given URL is malicious or safe.
    Returns: dict with label (0=safe, 1=malicious) and probability.
    """
    X = VEC.transform([url])
    proba = float(LR.predict_proba(X)[0, 1])
    label = int(proba >= 0.5)
    return {"label": label, "prob": proba}
