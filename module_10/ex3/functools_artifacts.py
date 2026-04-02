from functools import reduce, partial, lru_cache, singledispatch
from operator import ge, le
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda x, y: x + y, spells)
    elif operation == "multiply":
        return reduce(lambda x, y: x * y, spells)
    elif operation == "max":
        return reduce(lambda x, y: x if ge(x, y) else y, spells)
    elif operation == "min":
        return reduce(lambda x, y: x if le(x, y) else y, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire_enchant = partial(base_enchantment, 50, 'fire')
    ice_enchant = partial(base_enchantment, 50, 'ice')
    lightning_enchant = partial(base_enchantment, 50, 'lightning')
    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': lightning_enchant
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """ least recently used cache """
    if n < 0:
        return ("n Cannot be negative !")
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """ simulates overloading with only one argument"""
    @singledispatch
    def spell(arg: Any) -> None:
        return "argument is not a valid type"

    @spell.register(int)
    def spell_int(arg: int) -> str:
        return f"damage spell : {arg}"

    @spell.register(str)
    def spell_str(arg: str) -> str:
        return f"Enchantement spell: {arg}"

    @spell.register(list)
    def spell_list(arg: list) -> str:
        return f"spells available ({len(arg)}): {arg}"
    return spell


if __name__ == "__main__":
    try:
        print("\nTesting spell reducer...")
        spells_sample = [100, 1, 928, 10, 384, 58]
        sp_rd_sum = spell_reducer(spells_sample, "add")
        sp_rd_product = spell_reducer(spells_sample, "multiply")
        sp_rd_min = spell_reducer(spells_sample, "min")
        sp_rd_max = spell_reducer(spells_sample, "max")
        print(f"Sum: {sp_rd_sum}")
        print(f"Product: {sp_rd_product}")
        print(f"Min: {sp_rd_min}")
        print(f"Max: {sp_rd_max}")
        print()
        print("Testing partial enchanter...")

        def base_enchantment(power: int, element: str, target: str) -> str:
            return f"{element} with power: {power} and target: {target}"
        partials = partial_enchanter(base_enchantment)
        print(partials['fire_enchant']('enemy1'))
        print(partials['ice_enchant']('enemy2'))
        print(partials['lightning_enchant']('enemy3'))
        print()
        print("Testing memoized fibonacci...")
        fib_5 = memoized_fibonacci(5)
        fib_6 = memoized_fibonacci(6)
        fib_10 = memoized_fibonacci(10)
        print(f"Fib(5): {fib_5}")
        print(f"Fib(6): {fib_6}")
        print(f"Fib(10): {fib_10}")
        print()
        print("Testing spell dispatcher...")
        dispatcher = spell_dispatcher()
        print("Testing with int: ")
        print(dispatcher(5))
        print("Testing with str: ")
        print(dispatcher("Fireball"))
        print("Testing with a list...")
        sample_data = ["ice-attack", "fire-healing", "ultimate-fist"]
        print(dispatcher(sample_data))
    except Exception as e:
        print(e)
