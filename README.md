# Singapore Resale Flat Prices Prediction

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-orange)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)  


---

## 🏆 Project Overview

This project predicts the resale prices of HDB flats in Singapore using **machine learning models** trained on historical flat transaction data. It is deployed as a **user-friendly web application** built with Streamlit.

- **Skills Learned:** Data Wrangling, EDA, Feature Engineering, Model Building, Model Deployment  
- **Domain:** Real Estate  

---

## 🎯 Problem Statement

The objective of this project is to develop a machine learning model and deploy it as a web application that predicts the resale prices of flats in Singapore. This predictive model is based on historical resale flat transactions and aims to assist:

- **Homebuyers** in estimating fair resale values.  
- **Sellers** in pricing flats accurately.  
- **Policy makers** in analyzing housing trends.  

---

## 💡 Motivation

The resale flat market in Singapore is highly competitive, and estimating the resale price can be challenging. Many factors influence resale prices, such as location, flat type, floor area, storey range, and lease duration. A predictive model can overcome these challenges and provide a reliable estimate for users.

---

## 🔬 Scope of the Project

The project involves:

1. **Data Collection and Preprocessing:**  
   - Collecting data from HDB resale flat transactions (1990 – Present)  
   - Cleaning and preprocessing the dataset  

2. **Feature Engineering:**  
   - Extracting relevant features: `town`, `flat_type`, `storey_range`, `floor_area_sqm`, `flat_model`, `lease_commence_date`  
   - Adding derived features: `year` from month column  

3. **Exploratory Data Analysis (EDA):**  
   - Understanding data distributions, correlations, and outliers  
   - Visualizations: Scatter plots, bar plots, boxplots, KDE plots, and heatmaps  

4. **Model Training:**  
   - Linear Regression  
   - Decision Tree Regressor (best performing model with R² ≈ 0.86 on test data)  

5. **Model Evaluation:**  
   - Metrics: R² Score, Mean Absolute Error (MAE)  

6. **Streamlit Web Application:**  
   - Allows users to input flat details and predict resale price  
   - Pages: Home, Price Prediction, About Project  

7. **Deployment:**  
   - Deployment using **Render** or any cloud platform  

---

## 📈 Data Details

- **Columns used:**
  - `month`, `town`, `flat_type`, `storey_range`, `floor_area_sqm`, `flat_model`, `lease_commence_date`, `resale_price`, `year`  
- **Rows:** 952,537  
- **Preprocessing steps:**
  - Removed unnecessary columns (`block`, `street_name`)  
  - Converted categorical features using `OrdinalEncoder`  
  - Handled missing data  

---

## 🛠️ Technology Stack

- **Python Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, Streamlit  
- **Machine Learning Models:** Linear Regression, Decision Tree Regressor  
- **Web App Framework:** Streamlit  
- **Deployment:** Render  

---

## 🖥 Screenshots

### Home Page


### Price Prediction Page


### About Project Page
https://github.com/virenemmanuel/Singapore-Resale-Flat-Prices-Predicting/blob/182e18d608eaad64a6c650089fd112a2718d9e3c/About.png

---

## 🚀 How to Run the Application

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Singapore-Resale-Flat-Prices-Predicting

