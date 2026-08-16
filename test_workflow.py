from graph.workflow import run_workflow

state = {
    "age": 22,
    "gender": "Male",
    "weight": 70,
    "height": 175,
    "activity": "Moderately Active",
    "goal": "Weight Loss",
    "diet": "Vegetarian",
    "cuisine": "South Indian",
    "allergy": "None",

    "bmi": 0,
    "bmr": 0,
    "calories": 0,

    "meal_plan": "",
    "recipes": "",
    "grocery_list": "",
    "final_report": ""
}

result = run_workflow(state)

print("=" * 70)
print("🤖 AI FOOD & NUTRITION ASSISTANT")
print("=" * 70)

print(f"\nBMI            : {result['bmi']}")
print(f"BMR            : {result['bmr']} kcal/day")
print(f"Daily Calories : {result['calories']} kcal/day")

print("\n" + "=" * 70)
print("🥗 AI MEAL PLAN")
print("=" * 70)

print(result["meal_plan"])

print("\n" + "=" * 70)
print("🍳 AI RECIPES")
print("=" * 70)

print(result["recipes"])

print("\n" + "=" * 70)
print("🛒 AI GROCERY LIST")
print("=" * 70)

print(result["grocery_list"])

print("\n" + "=" * 70)
print("✅ WORKFLOW COMPLETED SUCCESSFULLY")
print("=" * 70)