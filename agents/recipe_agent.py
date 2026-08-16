from utils.gemini_client import ask_gemini


def recipe_agent(state):
    """
    Generates recipes for the AI meal plan.
    """

    prompt = f"""
You are an expert chef and nutritionist.

Below is a one-day meal plan.

{state["meal_plan"]}

Generate recipes for every meal.

For each recipe include:

1. Ingredients
2. Preparation steps
3. Cooking time
4. Calories (Approx.)

Format the response nicely using Markdown.
"""

    recipes = ask_gemini(prompt)

    state["recipes"] = recipes

    return state