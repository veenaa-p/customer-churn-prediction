import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🔄",
    layout="wide"
)

# ── Load model ───────────────────────────────────────────────
model = joblib.load('app/churn_model.pkl')

# ── Header ───────────────────────────────────────────────────
st.markdown("""
    <div style='background-color:#2E75B6; padding:20px; border-radius:10px; margin-bottom:20px'>
        <h1 style='color:white; text-align:center'>🔄 Customer Churn Prediction App</h1>
        <p style='color:#D6EAF8; text-align:center'>Enter customer details to predict churn probability</p>
    </div>
""", unsafe_allow_html=True)

# ── Input form ───────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Demographics")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

with col2:
    st.subheader("📦 Services")
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet = st.selectbox("Internet Service", ["Fiber optic", "DSL", "No"])
    security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

with col3:
    st.subheader("💳 Account Info")
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    monthly = st.slider("Monthly Charges ($)", 18.0, 120.0, 65.0)
    total = st.number_input("Total Charges ($)", min_value=0.0, value=float(tenure * monthly))

# ── Predict button ───────────────────────────────────────────
st.markdown("---")
predict_btn = st.button("🔮 Predict Churn", use_container_width=True)

if predict_btn:
    # Encode inputs same way as training
    input_dict = {
        'gender': 1 if gender == "Male" else 0,
        'SeniorCitizen': 1 if senior == "Yes" else 0,
        'Partner': 1 if partner == "Yes" else 0,
        'Dependents': 1 if dependents == "Yes" else 0,
        'tenure': tenure,
        'PhoneService': 1 if phone == "Yes" else 0,
        'MultipleLines': ["No", "No phone service", "Yes"].index(multiple),
        'InternetService': ["DSL", "Fiber optic", "No"].index(internet),
        'OnlineSecurity': ["No", "No internet service", "Yes"].index(security),
        'OnlineBackup': ["No", "No internet service", "Yes"].index(backup),
        'DeviceProtection': ["No", "No internet service", "Yes"].index(protection),
        'TechSupport': ["No", "No internet service", "Yes"].index(support),
        'StreamingTV': ["No", "No internet service", "Yes"].index(tv),
        'StreamingMovies': ["No", "No internet service", "Yes"].index(movies),
        'Contract': ["Month-to-month", "One year", "Two year"].index(contract),
        'PaperlessBilling': 1 if billing == "Yes" else 0,
        'PaymentMethod': [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ].index(payment),
        'MonthlyCharges': monthly,
        'TotalCharges': total
    }

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    # ── Result ───────────────────────────────────────────────
    st.markdown("### 🎯 Prediction Result")
    col_a, col_b = st.columns(2)

    with col_a:
        if prediction == 1:
            st.error(f"⚠️ This customer is likely to **CHURN**")
        else:
            st.success(f"✅ This customer is likely to **STAY**")

    with col_b:
        churn_prob = round(probability[1] * 100, 2)
        stay_prob = round(probability[0] * 100, 2)
        st.metric("Churn Probability", f"{churn_prob}%")
        st.metric("Stay Probability", f"{stay_prob}%")

    # ── Risk level ───────────────────────────────────────────
    st.markdown("### 📊 Risk Level")
    if churn_prob >= 70:
        st.error("🔴 HIGH RISK — Immediate action needed!")
    elif churn_prob >= 40:
        st.warning("🟡 MEDIUM RISK — Monitor this customer")
    else:
        st.success("🟢 LOW RISK — Customer is stable")