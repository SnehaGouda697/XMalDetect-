import joblib, pefile
import numpy as np

# Load models from models/ folder
CLF = joblib.load("models/pe_rf.pkl")
FEATS = joblib.load("models/pe_features.pkl")

def extract_pe_header_features(path: str) -> dict:
    pe = pefile.PE(path, fast_load=True)
    pe.parse_data_directories()
    feats = {
      "SizeOfCode": pe.OPTIONAL_HEADER.SizeOfCode,
      "SizeOfInitializedData": pe.OPTIONAL_HEADER.SizeOfInitializedData,
      "NumberOfSections": len(pe.sections),
      "DllCharacteristics": pe.OPTIONAL_HEADER.DllCharacteristics,
    }
    return feats

def vectorize_for_model(feat_dict: dict):
    return np.array([feat_dict.get(f, 0) for f in FEATS], dtype=float).reshape(1, -1)

def predict_pe_file(path: str):
    fd = extract_pe_header_features(path)
    X = vectorize_for_model(fd)
    proba = float(CLF.predict_proba(X)[0,1])
    label = int(proba >= 0.5)
    return {"label": label, "prob": proba, "features": fd}
