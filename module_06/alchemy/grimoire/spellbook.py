def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    ingredient = validate_ingredients(ingredients)
    if ingredient == f"{ingredients} - INVALID":
        return f"Spell rejected: {spell_name} ({ingredient})"
    return f"Spell recorded: {spell_name} ({ingredient})"
