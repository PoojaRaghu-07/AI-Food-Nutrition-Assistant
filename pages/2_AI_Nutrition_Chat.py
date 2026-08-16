import streamlit as st
from utils.gemini_client import ask_gemini

st.set_page_config(
    page_title="AI Nutrition Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Nutrition Chat")
st.caption("Ask questions about your nutrition plan.")

# ----------------------------
# Check if a nutrition plan exists
# ----------------------------

if "result" not in st.session_state:

    st.warning("⚠️ Please generate a nutrition plan from the Home page first.")
    st.stop()

result = st.session_state["result"]

goal = st.session_state["goal"]
diet = st.session_state["diet"]
cuisine = st.session_state["cuisine"]
allergy = st.session_state["allergy"]

# ----------------------------
# Display current profile
# ----------------------------

with st.expander("📋 Current Nutrition Profile", expanded=True):

    st.write(f"**Goal:** {goal}")
    st.write(f"**Diet:** {diet}")
    st.write(f"**Cuisine:** {cuisine}")
    st.write(f"**Allergy:** {allergy}")

# ----------------------------
# User Question
# ----------------------------

question = st.text_area(
    "Ask a nutrition question",
    height=150,
    placeholder="Example: Can you improve my breakfast?"
)

if st.button("🤖 Ask AI", use_container_width=True):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        prompt = f"""
You are an expert nutritionist.

The user already has a personalized nutrition plan.

User Profile

Goal:
{goal}

Diet:
{diet}

Cuisine:
{cuisine}

Food Allergy:
{allergy}

Current Meal Plan

{result["meal_plan"]}

Current Recipes

{result["recipes"]}

Current Grocery List

{result["grocery_list"]}

User Question

{question}

Answer specifically according to the user's plan.

If suggesting improvements,
keep the same calorie target and dietary preference.

Use Markdown formatting.
"""

        with st.spinner("🤖 Analysing your nutrition plan..."):

            answer = ask_gemini(prompt)

        st.success("Answer Generated")

        st.markdown(answer)