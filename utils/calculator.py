def calculate_bmi(weight, height):
    """
    Calculate BMI.

    Parameters:
        weight (float): Weight in kilograms.
        height (float): Height in centimeters.

    Returns:
        float: BMI rounded to 2 decimal places.
    """

    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)

    return round(bmi, 2)

def calculate_bmr(weight, height, age, gender):
    """
    Calculate BMR using the Mifflin-St Jeor Equation.
    """

    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    return round(bmr, 2)

def calculate_daily_calories(bmr, activity_level):
    """
    Calculate daily calorie requirement based on activity level.
    """

    activity_factors = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extra Active": 1.9
    }

    calories = bmr * activity_factors[activity_level]
    return round(calories, 2)