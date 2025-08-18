import joblib
import os

class FileClassifier:
    def _init_(self, model_path="../Snapshot/classifier.pkl"):
        # check if model exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Model not found at {model_path}")
        # load model
        self.model = joblib.load(model_path)

    def predict(self, features):
        # features is expected as a dictionary of extracted values
        return self.model.predict([list(features.values())])[0]
