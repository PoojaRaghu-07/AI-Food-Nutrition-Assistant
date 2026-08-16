from utils.gemini_client import ask_gemini


def meal_agent(state):
    """
    Meal Agent:
    Reads the user's health information from the shared state,
    generates an AI meal plan,
    and stores it back into the state.
    """

    prompt = f"""
You are an expert nutritionist.

Create a healthy one-day meal plan.

User Details:
Age: {state["age"]}
Gender: {state["gender"]}
Weight: {state["weight"]} kg
Height: {state["height"]} cm
Daily Calories: {state["calories"]}
Goal: {state["goal"]}
Diet Preference: {state["diet"]}
Preferred Cuisine: {state["cuisine"]}
Food Allergy: {state["allergy"]}

Requirements:
1. Respect the calorie target.
2. Follow the user's goal.
3. Follow the diet preference.
4. Avoid allergy foods.
5. Prefer the selected cuisine.
6. Include:
   - Breakfast
   - Lunch
   - Snack
   - Dinner
7. Mention approximate calories for each meal.

Return the response in Markdown format.
"""

    state["meal_plan"] = ask_gemini(prompt)

    return state