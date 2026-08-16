from agents.health_agent import health_agent
from agents.meal_agent import meal_agent
from agents.recipe_agent import recipe_agent
from agents.grocery_agent import grocery_agent
from agents.reflection_agent import reflection_agent


def run_workflow(state):
    """
    Runs all AI agents in sequence.
    """

    # Step 1
    state = health_agent(state)

    # Step 2
    state = meal_agent(state)

    # Step 3
    state = recipe_agent(state)

    # Step 4
    state = grocery_agent(state)

    # Step 5
    state = reflection_agent(state)

    return state