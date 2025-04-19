import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Loan Eligibility Checker", layout="wide")

# --- Sidebar navigation ---
menu = st.sidebar.radio("Navigation", ["🏠 Home", "📜 Loan Rules & Guidelines", "🎓 Education Loan", "🏠 House Loan", "🚗 Car Loan"])

# --- Home Page ---
if menu == "🏠 Home":
    st.title("💰 Loan Eligibility Checker")
    st.markdown("""
    Check your eligibility instantly for Education, House, and Car loans using our smart system!
    """)
    
    st.markdown("""
    ### 📌 Available Loan Types:
    - 🎓 **Education Loan**: For students pursuing higher studies.
    - 🏠 **House Loan**: To help you own your dream house.
    - 🚗 **Car Loan**: For purchasing your desired vehicle.
    """)

# --- Loan Rules & Guidelines Page ---
elif menu == "📜 Loan Rules & Guidelines":
    st.title("📜 Loan Types & Their Eligibility Rules")
    st.markdown("<h3 style='color: #FF6F61;'>Learn about eligibility criteria for different loan types</h3>", unsafe_allow_html=True)

    st.subheader("🎓 Education Loan")
    st.markdown("""
    - Must be enrolled in a recognized institution.
    - Co-applicant required with min ₹15,000/month income.
    - Upload admission letter.
    - Loan range: ₹1,00,000 to ₹10,00,000.
    """)
    
    st.subheader("🏠 House Loan")
    st.markdown("""
    - Age: 21 to 60 years.
    - Monthly income ≥ ₹25,000.
    - Credit score > 650.
    - Upload property documents.
    - Loan tenure: Up to 30 years.
    """)
    
    st.subheader("🚗 Car Loan")
    st.markdown("""
    - Age: 21 to 60 years.
    - Monthly income ≥ ₹20,000.
    - Upload car invoice and driving license.
    - Loan tenure: 1 to 7 years.
    """)

# --- Education Loan Page ---
elif menu == "🎓 Education Loan":
    st.title("🎓 Education Loan Application", anchor="education-loan")
    st.markdown("Check your eligibility for an Education Loan.")
    
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=18, max_value=60)
    email = st.text_input("Email")
    institution = st.text_input("Institution Name")
    admission_letter = st.file_uploader("Upload Admission Letter (PDF)", type="pdf")
    co_applicant = st.text_input("Co-Applicant Name")
    co_income = st.number_input("Co-Applicant Income (₹)", min_value=0)
    monthly_expenses = st.number_input("Monthly Expenses (₹)", min_value=0)
    requested_loan = st.number_input("Requested Loan Amount (₹)", min_value=10000)

    if st.button("Check Eligibility"):
        if not institution or not co_applicant or co_income < 15000 or not admission_letter:
            st.error("❌ Not Eligible: Valid institution, co-applicant income above ₹15,000, and admission letter required.")
        elif requested_loan < 100000 or requested_loan > 1000000:
            st.error("❌ Not Eligible: Loan amount must be between ₹1,00,000 to ₹10,00,000.")
        else:
            st.success("✅ You are eligible for an Education Loan!")

# --- House Loan Page ---
elif menu == "🏠 House Loan":
    st.title("🏠 House Loan Application", anchor="house-loan")
    st.markdown("Check your eligibility for a House Loan.")
    
    name = st.text_input("Applicant Name")
    age = st.number_input("Age", min_value=21, max_value=60)
    monthly_income = st.number_input("Monthly Income (₹)", min_value=0)
    property_location = st.text_input("Property Location")
    property_value = st.number_input("Property Estimated Value (₹)", min_value=0)
    land_docs = st.file_uploader("Upload Land/Property Documents (PDF)", type="pdf")
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900)
    tenure = st.slider("Desired Tenure (Years)", 1, 30)

    if st.button("Check Eligibility"):
        if monthly_income < 25000:
            st.error("❌ Not Eligible: Minimum income must be ₹25,000.")
        elif credit_score < 650:
            st.error("❌ Not Eligible: Credit score must be above 650.")
        elif not land_docs:
            st.error("❌ Not Eligible: Property documents required.")
        else:
            st.success("✅ You are eligible for a House Loan!")

# --- Car Loan Page ---
elif menu == "🚗 Car Loan":
    st.title("🚗 Car Loan Application", anchor="car-loan")
    st.markdown("Check your eligibility for a Car Loan.")
    
    name = st.text_input("Applicant Name")
    age = st.number_input("Age", min_value=21, max_value=60)
    monthly_income = st.number_input("Monthly Income (₹)", min_value=0)
    car_model = st.text_input("Car Brand & Model")
    car_invoice = st.file_uploader("Upload Car Invoice/Quotation (PDF)", type="pdf")
    license = st.file_uploader("Upload Driving License (PDF)", type="pdf")
    tenure = st.slider("Loan Term (Years)", 1, 7)

    if st.button("Check Eligibility"):
        if monthly_income < 20000:
            st.error("❌ Not Eligible: Monthly income must be at least ₹20,000.")
        elif not license or not car_invoice:
            st.error("❌ Not Eligible: Both driving license and car invoice are required.")
        else:
            st.success("✅ You are eligible for a Car Loan!")

 if __name__ == "__main__":
    # Optional: run with specific host and port using os.system
    import os
    os.system("streamlit run your_script.py --server.port 8501 --server.address 0.0.0.0")

