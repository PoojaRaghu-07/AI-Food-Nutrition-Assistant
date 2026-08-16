from utils.gemini_client import ask_gemini


def grocery_agent(state):
    """
    Generates a categorized grocery list from the recipes.
    """

    prompt = f"""
You are an expert nutrition assistant.

Below are the recipes for one day's meals.

{state["recipes"]}

Create a well-organized grocery shopping list.

Requirements:

1. Group ingredients into categories:
   - Vegetables
   - Fruits
   - Dairy
   - Grains
   - Pulses & Legumes
   - Spices
   - Oils
   - Others

2. Mention approximate quantity for each ingredient.

3. Remove duplicate ingredients.

4. Format nicely using Markdown.

Do NOT include cooking instructions.
"""

    grocery_list = ask_gemini(prompt)

    state["grocery_list"] = grocery_list

    return state