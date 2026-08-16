import utils.calculator as calculator


def health_agent(state):
    """
    Health Agent:
    Calculates BMI, BMR and Daily Calories,
    then stores them in the shared state.
    """

    bmi = calculator.calculate_bmi(
        state["weight"],
        state["height"]
    )

    bmr = calculator.calculate_bmr(
        state["weight"],
        state["height"],
        state["age"],
        state["gender"]
    )

    calories = calculator.calculate_daily_calories(
        bmr,
        state["activity"]
    )

    state["bmi"] = bmi
    state["bmr"] = bmr
    state["calories"] = calories

    return state