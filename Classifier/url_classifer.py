import pickle
import os

class URLClassifier:
    def __init__(self):
        # Load the saved logistic regression model
        model_path = os.path.join("Snapshot", "pickle_model.pkl")
        vectorizer_path = os.path.join("Snapshot", "pickle_vector.pkl")

        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        with open(vectorizer_path, "rb") as f:
            self.vectorizer = pickle.load(f)

    def predict(self, url: str) -> int:
        """
        Predict if the given URL is malicious (1) or safe (0).
        """
        x = self.vectorizer.transform([url])
        return self.model.predict(x)[0]