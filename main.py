import os
import time
import pyfiglet
from Classifier.file_classifer import FileClassifier
from Classifier.url_classifer import URLClassifier
from Extract.PE_main import extract_pe_features
from Extract.url_main import extract_url_features,sanitization
from src.url.app_tk import main


def run_PE():
    file_path = input("Enter the path and name of the PE file: ")
    try:
        features = extract_pe_features(file_path)       # extract PE features
        clf = FileClassifier()                          # load classifier.pkl
        result = clf.predict(features)                  # make prediction
        print("✅ Malware Detected" if result == 1 else "✅ File is Safe")
    except Exception as e:
        print(f"❌ Error scanning file: {e}")

def run_URL():
    url = input("Enter the URL to scan: ")
    try:
        # Step 1: extract features (optional, for debugging)
        features = extract_url_features(url)
        print("Extracted URL features:", features)

        # Step 2: run through classifier
        clf = URLClassifier()
        result = clf.predict(url)  # URLClassifier already uses vectorizer
        print("⚠️ Malicious URL" if result == 1 else "✅ Safe URL")
    except Exception as e:
        print(f"❌ Error scanning URL: {e}")
def start():
    print(pyfiglet.figlet_format("Malware Detector"))
    print(" Welcome to Anti-Malware Detector \n")
    print(" 1. PE Scanner")
    print(" 2. URL Scanner")
    print(" 3. Exit\n")

    select = input("Enter your choice : ")

    if select == "1":
        run_PE()
    elif select == "2":
        run_URL()
    elif select == "3":
        print("Exiting...")
        time.sleep(2)
        exit()
    else:
        print("❌ Bad input. Exiting...")
        time.sleep(2)
        exit()

    choice = input("\nDo you want to search again? (y/n): ").lower()
    if choice == 'y':
        start()
    else:
        print("Goodbye!")
        time.sleep(2)
        exit()

if __name__ == "__main__":
    start()
