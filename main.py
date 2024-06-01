import streamlit as st
from streamlit_lottie import st_lottie
import requests


# Function to load Lottie animations
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Streamlit page configuration
st.set_page_config(page_title="Income Tax Calculation", page_icon="💰", layout="centered",
                   initial_sidebar_state="collapsed")

# CSS for custom styling
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .main {
            background-color: #2a2c39;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
        }
        .stButton button {
            background-color: #d49797;
            color: #2a2c39;
            font-size: 16px;
            border-radius: 10px;
            border: none;
            padding: 0.5rem 1rem;
            transition: background-color 0.3s ease;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
        }
        .stButton button:hover {
            background-color: #b07a7a;
        }
        .stSelectbox, .stNumberInput, .stCheckbox label {
            font-size: 16px;
            color: #d2caca;
            border-radius: 8px;
            padding: 0.5rem;
            background-color: #3c3f52;
            border: 2px solid #3c3f52;
        }
        .stSelectbox, .stNumberInput {
            margin-bottom: 1rem;
        }
        .stSelectbox:hover, .stNumberInput:hover, .stCheckbox label:hover {
            border-color: #d49797;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #d49797;
        }
    </style>
""", unsafe_allow_html=True)

# Title with icon
st.markdown("<h1>💰 Income Tax Calculation Application</h1>", unsafe_allow_html=True)

# Load Lottie animation
lottie_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
if lottie_animation:
    st_lottie(lottie_animation, height=200, key="tax_calculator")

# User inputs
income_type = st.selectbox("Select Income Type:", ["Monthly", "Yearly"])
income = st.number_input("Your Income (TL):", min_value=0, step=1000)
company_type = st.selectbox("Company Type:",
                            ["Individual", "Limited Company", "Anonymous Company", "Limited Partnership"])
young_entrepreneur = st.checkbox("Are you benefiting from Young Entrepreneur Support?")

# Convert monthly income to yearly if necessary
if income_type == "Monthly":
    income *= 12

# Tax brackets and rates based on company type
if company_type == "Individual":
    tax_brackets = [(110000, 0.15), (230000, 0.20), (580000, 0.27), (3000000, 0.35), (float('inf'), 0.40)]
    if young_entrepreneur:
        income = max(0, income - 230000)
elif company_type == "Limited Company":
    tax_brackets = [(float('inf'), 0.25)]
elif company_type == "Anonymous Company":
    tax_brackets = [(float('inf'), 0.25)]
elif company_type == "Limited Partnership":
    tax_brackets = [(float('inf'), 0.20)]


# Function to calculate tax
def calculate_tax(income, tax_brackets):
    tax = 0
    for limit, rate in tax_brackets:
        if income > limit:
            tax += limit * rate
            income -= limit
        else:
            tax += income * rate
            break
    return tax


# Calculate tax
if st.button("Calculate Tax"):
    tax = calculate_tax(income, tax_brackets)
    st.success(f"Total tax payable: {tax:.2f} TL")
