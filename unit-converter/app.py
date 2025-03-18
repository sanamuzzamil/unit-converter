import streamlit as st

# Title of the app
st.title("📏 Unit Converter App 📏")

# Define conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    return value  # Same unit, no conversion needed

# Sidebar for selecting conversion type
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    st.header("📏 Length Converter")
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", ["meters", "kilometers", "miles", "feet", "inches"])
    to_unit = st.selectbox("To", ["meters", "kilometers", "miles", "feet", "inches"])
    result = convert_length(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Weight":
    st.header("⚖️ Weight Converter")
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", ["grams", "kilograms", "pounds", "ounces"])
    to_unit = st.selectbox("To", ["grams", "kilograms", "pounds", "ounces"])
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    st.header("🌡️ Temperature Converter")
    value = st.number_input("Enter value", format="%.2f")
    from_unit = st.selectbox("From", ["celsius", "fahrenheit"])
    to_unit = st.selectbox("To", ["celsius", "fahrenheit"])
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")