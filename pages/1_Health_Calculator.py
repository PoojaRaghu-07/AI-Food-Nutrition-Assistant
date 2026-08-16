import streamlit as st
import utils.calculator as calculator

st.set_page_config(page_title="Health Calculator", page_icon="📊")

st.title("📊 Health Calculator")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    format="%.1f"
)

height = st.number_input(
    "Height (cm)",
    min_value=1.0,
    format="%.1f"
)

activity = st.selectbox(
    "Activity Level",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active",
        "Extra Active"
    ]
)

if st.button("Calculate"):

    bmi = calculator.calculate_bmi(weight, height)

    bmr = calculator.calculate_bmr(
        weight,
        height,
        age,
        gender
    )

    calories = calculator.calculate_daily_calories(
        bmr,
        activity
    )

    st.success(f"✅ BMI : {bmi}")
    st.info(f"🔥 BMR : {bmr} kcal/day")
    st.warning(f"🍽 Daily Calories : {calories} kcal/day")