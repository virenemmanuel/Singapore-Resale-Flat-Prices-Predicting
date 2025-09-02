import numpy as np
import streamlit as st
import pickle
from sklearn.preprocessing import OrdinalEncoder

# ---------------- STREAMLIT CONFIG ----------------
st.set_page_config(
    page_title="Singapore Resale Flat Prices Prediction",
    layout="wide"
)

# ---------------- SIDEBAR MENU ----------------
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "💰 Price Prediction", "📘 About Project"])

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":
    st.title("🏡 Singapore Resale Flat Prices Prediction")
    st.divider()

    st.header("✨ Project Overview")
    st.write(
        """
        **Project Name**: Singapore Resale Flat Prices Prediction  
        **Technologies Used**: Python, Data Preprocessing, EDA, Streamlit  
        **Domain**: Real Estate  

        📌 The goal of this project is to build a **machine learning model** and deploy it as a
        **Streamlit app** that predicts the resale prices of flats in Singapore.
        """
    )

# ---------------- PRICE PREDICTION PAGE ----------------
elif page == "💰 Price Prediction":
    st.title("💰 Flat Price Prediction")
    st.subheader("Enter Flat Details Below")
    st.divider()

    storey_range_options = [
        '10 TO 12', '04 TO 06', '07 TO 09', '01 TO 03', '13 TO 15',
        '19 TO 21', '16 TO 18', '25 TO 27', '22 TO 24', '28 TO 30',
        '31 TO 33', '40 TO 42', '37 TO 39', '34 TO 36', '46 TO 48',
        '43 TO 45', '49 TO 51', '06 TO 10', '01 TO 05', '11 TO 15',
        '16 TO 20', '21 TO 25', '26 TO 30', '36 TO 40', '31 TO 35'
    ]

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            month = st.selectbox("📅 Month", options=list(range(1, 13)))
            floor_area_sqm = st.number_input("📏 Floor Area (sqm)", min_value=28, max_value=306, step=1)
            lease_commence_date = st.number_input("📜 Lease Commence Date", min_value=1966, max_value=2023, step=1)
            year = st.number_input("📆 Year of Sale", min_value=1990, max_value=2023, step=1)

        with col2:
            storey_range = st.selectbox("🏢 Storey Range", options=storey_range_options)
            predict = st.form_submit_button("🔮 Predict Selling Price")

        if predict:
            try:
                with st.spinner("🔄 Running Prediction..."):
                    # Load trained model
                    with open(
                        "C:\\Users\\viren\\OneDrive\\Desktop\\IIT-MADARAS(GUVI)\\data\\Singapore_flat_model_DTR\\DTR_model.pkl",
                        "rb"
                    ) as f:
                        model = pickle.load(f)

                    # Encode storey_range
                    ordinal_encoder = OrdinalEncoder(categories=[storey_range_options])
                    categorical_features = np.array([[storey_range]])
                    ordinal_encoded = ordinal_encoder.fit_transform(categorical_features)

                    # Prepare input
                    input_data = np.array([[month, *ordinal_encoded[0], floor_area_sqm,
                                            lease_commence_date, year]])

                    # Prediction
                    prediction = model.predict(input_data)[0]

                    st.success("✅ Prediction Successful!")
                    st.metric("Predicted Selling Price", f"${prediction:,.0f}")

            except Exception as e:
                st.error(f"⚠️ An error occurred: {e}")

# ---------------- ABOUT PROJECT PAGE ----------------
elif page == "📘 About Project":
    st.title("📘 About the Project")
    st.divider()

    st.header("🎯 Objective")
    st.write("This project predicts the resale prices of HDB flats in Singapore using a machine learning model.")

    st.header("🔑 Key Features")
    st.write(
        """
        - Data preprocessing & cleaning  
        - Exploratory Data Analysis (EDA)  
        - Feature engineering (storey range, year, floor area, lease date)  
        - Model training with **Decision Tree Regressor**  
        - Deployment using **Streamlit**
        """
    )

    st.header("🌍 Impact")
    st.write(
        """
        - 🏡 Helps **homebuyers** estimate fair resale values  
        - 🏢 Assists **policy makers** in analyzing housing trends  
        - 🏘️ Supports **real estate agents** with market predictions
        """
    )
    
