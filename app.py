import streamlit as st
from graph.workflow import run_workflow
from reports.pdf_generator import generate_pdf

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Food & Nutrition Assistant",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 AI Food & Nutrition Assistant")
st.caption("Your Personal AI Nutrition & Health Assistant")

st.divider()

# ----------------------------------------------------
# User Inputs
# ----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=22
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        value=70.0
    )

    height = st.number_input(
        "Height (cm)",
        min_value=1.0,
        value=175.0
    )

with col2:

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

    goal = st.selectbox(
        "Goal",
        [
            "Weight Loss",
            "Maintain Weight",
            "Weight Gain"
        ]
    )

    diet = st.selectbox(
        "Diet Preference",
        [
            "Vegetarian",
            "Non-Vegetarian",
            "Vegan"
        ]
    )

    cuisine = st.selectbox(
        "Preferred Cuisine",
        [
            "South Indian",
            "North Indian",
            "Indian",
            "Chinese",
            "Italian"
        ]
    )

    allergy = st.selectbox(
        "Food Allergy",
        [
            "None",
            "Milk",
            "Egg",
            "Nuts",
            "Seafood"
        ]
    )

st.divider()

# ----------------------------------------------------
# Generate Nutrition Plan
# ----------------------------------------------------

if st.button("🚀 Generate Complete Nutrition Plan", use_container_width=True):

    state = {
        "age": age,
        "gender": gender,
        "weight": weight,
        "height": height,
        "activity": activity,
        "goal": goal,
        "diet": diet,
        "cuisine": cuisine,
        "allergy": allergy,

        "bmi": 0,
        "bmr": 0,
        "calories": 0,

        "meal_plan": "",
        "recipes": "",
        "grocery_list": "",
        "final_report": ""
    }

    progress = st.progress(0)

    progress.progress(10, text="📊 Health Agent...")

    result = run_workflow(state)

    progress.progress(100, text="✅ AI Workflow Completed!")

    st.session_state["result"] = result
    st.session_state["goal"] = goal
    st.session_state["diet"] = diet
    st.session_state["cuisine"] = cuisine
    st.session_state["allergy"] = allergy

# ----------------------------------------------------
# Display Results
# ----------------------------------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    st.success("🎉 Nutrition Plan Generated Successfully!")

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("BMI", result["bmi"])

    with c2:
        st.metric("BMR", f"{result['bmr']} kcal/day")

    with c3:
        st.metric("Daily Calories", f"{result['calories']} kcal/day")

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🥗 Meal Plan",
            "🍳 Recipes",
            "🛒 Grocery List",
            "🧠 Reflection"
        ]
    )

    with tab1:
        st.markdown(result["meal_plan"])

    with tab2:
        st.markdown(result["recipes"])

    with tab3:
        st.markdown(result["grocery_list"])

    with tab4:
        st.markdown(result["final_report"])

    st.divider()

    st.info(
        f"""
### 📋 Current Preferences

🎯 Goal: **{st.session_state['goal']}**

🥗 Diet: **{st.session_state['diet']}**

🍛 Cuisine: **{st.session_state['cuisine']}**

⚠️ Allergy: **{st.session_state['allergy']}**
"""
    )

    # ----------------------------------------------------
    # Download PDF
    # ----------------------------------------------------

    st.divider()

    st.subheader("📄 Export Nutrition Report")

    try:

        pdf_file = generate_pdf(result)

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download Nutrition Report",
                data=file.read(),
                file_name="Nutrition_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    except Exception as e:

        st.error(f"PDF Generation Error: {e}")