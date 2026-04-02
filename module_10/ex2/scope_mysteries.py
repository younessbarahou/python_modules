def mage_counter() -> callable:
    """ simple counter demonstrates closure"""
    initial = 0

    def counter() -> int:
        nonlocal initial
        initial = initial + 1
        return initial
    return counter


def spell_accumulator(initial_power: int) -> callable:
    """ using arg as a closure """
    def power_acc(given_amount: int) -> int:
        nonlocal initial_power
        initial_power += given_amount
        return initial_power
    return power_acc


def enchantment_factory(enchantment_type: str) -> callable:
    def ench_fact(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return ench_fact


def memory_vault() -> dict[str, callable]:
    """ here it plays the role of a db """
    memory_v = {}

    def store(key: str, value: int) -> None:
        memory_v.update({key: value})

    def recall(key: str):
        try:
            return memory_v[key]
        except KeyError:
            return "Memory not found"

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    try:
        print("\nTesting mage counter...")
        index = 1
        m_counter = mage_counter()
        while index <= 3:
            print(f"Call {index}: {m_counter()}")
            index += 1
        print("\nTesting spell accumulator...")
        s_accum = spell_accumulator(0)
        index = 1
        while index <= 3:
            print(f"+1 added: {s_accum(1)}")
            index += 1
        print("\nTesting echantment factory....")
        types_sample = ["Flaming", "Frozen"]
        items_sample = ["Shield", "Sword"]
        factory_1 = enchantment_factory(types_sample[0])
        factory_2 = enchantment_factory(types_sample[1])
        print(factory_1(items_sample[0]))
        print(factory_2(items_sample[1]))
        print("Testing memory vault...")
        vault = memory_vault()
        vault['store']('element_count', '99')
        print(vault['recall']('element_count'))
        print(vault['recall']('fire'))
    except Exception as e:
        print(e)
