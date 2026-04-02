def validate_ingredients(ingredients: str) -> str:
    if type(ingredients) is not str or len(ingredients) == 0:
        raise ValueError("Invalid Ingredients format !")
    valid_ingredients = ingredients.split(' ')
    if (
        'fire' not in valid_ingredients
        and 'water' not in valid_ingredients
        and 'earth' not in valid_ingredients
        and 'air' not in valid_ingredients
    ):
        return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
