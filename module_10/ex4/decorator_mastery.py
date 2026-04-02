from functools import wraps
from random import random


def spell_timer(func: callable) -> callable:
    """ simple decorator """
    @wraps(func)
    def wraper(spell_name: str) -> str:
        func_name = func.__name__
        print(f"Casting {func_name}")
        result = func(spell_name)
        print(f"Spell completed in {random():.2f} seconds")
        return result
    return wraper


def power_validator(min_power: int) -> callable:
    """ decorator factory is like a decorator with args"""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wraper(*args) -> str:
            if args[-1] >= min_power:
                return func(*args)
            else:
                return "Insufficient power for this spell"
        return wraper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wraper(spell_name: str, spell_power: int) -> str:
            base = 1
            while base <= max_attempts:
                try:
                    result = func(spell_name, spell_power)
                    return result
                except ValueError:
                    print("Spell failed, retrying...")
                    base += 1
            return f"Spell casting failed after {max_attempts} times"
        return wraper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if type(name) is not str or len(name) < 3:
            return False
        for element in name:
            if not element.isalpha() and not element.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    try:
        print("Testing spell timer...")

        @spell_timer
        def spell(spell_name: str) -> str:
            return f"{spell_name} Cast"
        print(spell("FireBall"))
        print()

        print("Testing power validator...")
        min_power = 5

        @power_validator(min_power)
        def spell_1(*args) -> str:
            return f"{args[0]} has been executed! with power {args[1]}"
        print(spell_1('Ice Attack', 5))
        print()

        print("Testing retry spell...")

        @retry_spell(5)
        def spell_2(spell_name: str, power: int) -> str:
            if power < 2:
                raise ValueError("Spell power is very low to use.")
            return f"{spell_name} with power: {power} casted successfully"
        print(spell_2("Ice ball", 1))
        print()

        print("Testing MageGuild...")
        mage_1 = MageGuild()
        print(mage_1.validate_mage_name('abc1'))
        print(mage_1.validate_mage_name('abc'))
        print(mage_1.cast_spell("Attacking", 15))
        print(mage_1.cast_spell("Healing", 5))
    except Exception as e:
        print(e)
