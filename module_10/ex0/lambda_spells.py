def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda element: element['power'])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    result_max = max(mages, key=lambda x: x['power'])
    result_min = min(mages, key=lambda x: x['power'])
    result_sum = sum(map(lambda x: x['power'], mages))
    result_avg = result_sum / len(mages)
    return {'max_power': result_max['power'],
            'min_power': result_min['power'],
            'avg_power': round(result_avg, 2)}


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    sample_list = [
        {
            'name': 'Dragon',
            'power': 1000,
            'type': "Legendary"
        },
        {
            'name': 'Sorcerer',
            'power': 880,
            'type': "RARE"
        },
        {
            'name': 'Alchemist',
            'power': 900,
            'type': "COMMON"
        },
        ]
    print("Sorting by power...")
    print(f"sorted artifact: {artifact_sorter(sample_list)}")
    print()
    print("Filtering by power...")
    min_power = 900
    print(f"Filter: power >= {min_power}")
    print(f"Filtered: {power_filter(sample_list, min_power)}")
    print()
    print("Transforming spell...")
    only_names = map(lambda x: x['name'], sample_list)
    transformed_names = spell_transformer(only_names)
    for name in transformed_names:
        print(f"{name} ", end="")
    print()
    print()
    print("Mage Stats...")
    print(mage_stats(sample_list))
