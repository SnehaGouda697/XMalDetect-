# XMalDetect: Hybrid Malware Detection using ML + CNN + Explainable AI  

Malware has become one of the **most critical cyber threats** due to polymorphic and zero-day attacks. Traditional signature-based antivirus solutions often fail against rapidly evolving threats.  
**XMalDetect** provides a hybrid, machine-learning-based approach to detect **malicious PE files** and **malicious URLs**, with added **deep learning (CNN)** and **explainability** features.

---

## 🚀 Features
- **PE File Malware Detection** using Random Forest + CNN (image-based classification).  
- **Malicious URL Detection** using Logistic Regression + TF-IDF.  
- **Explainability with SHAP** → See which features influenced detection.  
- **Streamlit GUI** → Easy-to-use interface for demonstrations.  
- **Model Persistence** using Joblib (saved `.pkl` models).  

---

## 🗂 Datasets
- **PE Header Dataset:** [Kaggle PE Malware Dataset](https://www.kaggle.com/datasets/dscclass/malware)  
- **URL Dataset:** Public datasets of benign/malicious URLs (custom preprocessing applied).  

---

## ⚙️ Architecture
1. **Feature Extraction**  
   - For PE files → Extract PE header features (`pefile` library).  
   - For URLs → Clean + vectorize with TF-IDF.  
2. **Model Training**  
   - Random Forest for PE.  
   - Logistic Regression for URLs.  
   - CNN for image-based PE detection.  
3. **Explainability Layer**  
   - SHAP values for feature importance.  
4. **User Interface**  
   - Streamlit app for file/URL upload & real-time detection.  

---

## 🖥️ How to Run
### 1. Clone this repo  
```bash
git clone https://github.com/sneha-gouda/XMalDetect.git
cd XMalDetect

