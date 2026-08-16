from utils.gemini_client import ask_gemini


def reflection_agent(state):
    """
    Reviews the generated nutrition plan and provides feedback.
    """

    prompt = f"""
You are a senior nutritionist reviewing an AI-generated nutrition plan.

User Profile

Age: {state["age"]}
Gender: {state["gender"]}
Goal: {state["goal"]}
Diet: {state["diet"]}
Cuisine: {state["cuisine"]}
Allergy: {state["allergy"]}

BMI:
{state["bmi"]}

BMR:
{state["bmr"]}

Daily Calories:
{state["calories"]}

Meal Plan

{state["meal_plan"]}

Recipes

{state["recipes"]}

Grocery List

{state["grocery_list"]}

Please review the nutrition plan.

Check:

1. Goal alignment
2. Calorie suitability
3. Protein intake
4. Fibre intake
5. Diet compatibility
6. Allergy safety
7. Strengths
8. Possible improvements

Give a final rating out of 10.

Format using Markdown.
"""

    report = ask_gemini(prompt)

    state["final_report"] = report

    return state