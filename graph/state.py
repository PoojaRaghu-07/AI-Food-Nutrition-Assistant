from typing import TypedDict


class NutritionState(TypedDict):
    """
    Shared state passed between all AI agents.
    """

    age: int
    gender: str
    weight: float
    height: float
    activity: str
    goal: str
    diet: str
    cuisine: str
    allergy: str

    bmi: float
    bmr: float
    calories: float

    meal_plan: str
    recipes: str
    grocery_list: str
    final_report: str