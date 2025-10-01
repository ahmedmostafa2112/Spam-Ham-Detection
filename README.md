# Spam-Ham-Detection
This project is a machine learning model for classifying SMS messages as either Spam or Ham (Not Spam). It uses the SMS Spam Collection Dataset from Kaggle and applies text preprocessing, feature extraction, and logistic regression with a Flask API for real-time predection.
# 📩 SMS Spam-Ham Detection  

A Machine Learning project to classify SMS messages as **Spam** or **Ham (Not Spam)** using text preprocessing, feature extraction, and Logistic Regression.  
Also includes a **Flask API** for real-time predictions.  

---

## 🔹 Features  
- Data cleaning & preprocessing (lowercasing, regex).  
- Feature extraction using **Bag of Words (BoW)** and **TF-IDF**.  
- Logistic Regression model with class balancing.  
- Model persistence using `joblib` for reuse.  
- **Flask API** to serve predictions on new SMS messages.  

---

## 📂 Project Structure  

MS-Spam-Ham-Detection
│── 📄 README.md

│── 📄 requirements.txt

│── 📄 train_model.py # Script for training the model

│── 📄 app.py # Flask API for real-time predictions

│── 📄 spam_detection.pkl # Saved trained model

│── 📄 BoW_vectorizer.pkl # Saved vectorizer

│── 📄 Spam-Ham_detection.ipynb # Full notebook (EDA + training)



📊 Model Performance

          Accuracy: ~98%
          Precision (Spam): 0.92
          Recall (Spam): 0.91

          

📜 Dataset

SMS Spam Collection Dataset from Kaggle.
Link: https://www.kaggle.com/code/ishansoni/sms-spam-collection-dataset



📄 requirements.txt:
    1.pandas
    
    2.numpy
    
    3.scikit-learn
    
    4.matplotlib
    
    5.joblib
    
    6.flask
