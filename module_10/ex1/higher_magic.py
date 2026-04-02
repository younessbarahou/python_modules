from typing import Union


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def spell_1_2() -> tuple:
        result = (spell1(), spell2())
        return result
    return spell_1_2


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def multipe() -> Union[int, float]:
        return base_spell() * multiplier
    return multipe


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(target: str) -> str:
        if condition(target) is True:
            spell(target)
            return "Spell Casted"
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def caster(target: str) -> list:
        result = []
        for spell in spells:
            result += [spell(target)]
        return result
    return caster


if __name__ == "__main__":
    try:
        print("Testing spell combiner...")
        print("Combined spell result: ")

        def spell1() -> str:
            return "FireBall"

        def spell2() -> str:
            return "SnowBall"

        print(spell_combiner(spell1, spell2)())
        print()
        print("Testing power amplifier...")

        def base_spell() -> Union[int, float]:
            return 5
        amplified = power_amplifier(base_spell, 5)()
        print(
            f"Original: {base_spell()}, Amplified: {amplified}"
            )
        print()
        print("Testing conditional caster...")

        def condition(target: str) -> bool:
            if target:
                return True
            return False

        def spell(target: str) -> str:
            return f"Spell has been used on {target}"
        result = conditional_caster(condition, spell)('Enemy')
        print(f"Conditional-result: {result}")
        print()
        print("Testing spell sequence...")

        def spell_1(target: str) -> str:
            return f"spell_1 to {target}"

        def spell_2(target: str) -> str:
            return f"spell_2 to {target}"

        print(spell_sequence([spell_1, spell_2])('Enemy'))
    except Exception as e:
        print(e)
