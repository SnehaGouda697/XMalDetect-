import os
from src.pe.predict_pe import predict_pe_file

def is_pe(path: str) -> bool:
    return path.lower().endswith((".exe",".dll",".sys"))

def scan_folder(folder: str):
    results = []
    for root, _, files in os.walk(folder):
        for f in files:
            if is_pe(f):
                fp = os.path.join(root, f)
                try:
                    res = predict_pe_file(fp)
                    results.append((fp, res["label"], res["prob"]))
                except Exception:
                    pass
    return results
