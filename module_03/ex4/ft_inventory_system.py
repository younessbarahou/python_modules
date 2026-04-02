import sys


def plural_singular(num: int) -> str:
    if num <= 1:
        return ("unit")
    return ("units")


def system_analysis(items: dict) -> list[int]:
    unique_items = 0
    total_items = 0
    for value in items.values():
        total_items += value
    for key in items.keys():
        unique_items += 1
    return ([total_items, unique_items])


def restock_needed(items: dict) -> list[str]:
    items_list = []
    for item in items.keys():
        if items[f"{item}"] <= 1:
            items_list += [item]
    return (items_list)


def inventory_unit(item: dict, total: int) -> int:
    for key in item.keys():
        main_key = key
    percentage = item.get(f"{main_key}") / total * 100
    return (percentage)


def statistics(items: dict) -> list:
    default = False
    minimum = 0
    maximum = 0
    for key in items.keys():
        if default is False or items[f"{key}"] < minimum:
            default = True
            minimum = items[f"{key}"]
            min_key = key
    default = False
    for key in items.keys():
        if default is False or items[f"{key}"] > maximum:
            default = True
            maximum = items[f"{key}"]
            max_key = key
    return ([min_key, minimum, max_key, maximum])


def lookup(items: dict, key: str) -> bool:
    for kkey in items.keys():
        if kkey == key:
            return (True)
    return (False)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print("No Items In Inventory!")
        print("Hint => python3 ft_inventory_system.py <item1>...")
    else:
        try:
            items = {}
            args_cte = 0
            for arg in sys.argv:
                if args_cte == 0:
                    args_cte += 1
                    continue
                splitted = arg.split(':')
                if len(splitted) != 2:
                    raise ValueError("Please enter valid data!")
                items.update({splitted[0]: int(splitted[1])})
            total_items = system_analysis(items)[0]
            unique_items = system_analysis(items)[1]
            print(f"total items in inventory: {total_items}")
            print(f"Unique items types: {unique_items}")
            print()
            for key in items.keys():
                item = items.get(f'{key}')
                noun = plural_singular(item)
                percentage = inventory_unit({key: item}, total_items)
                print(f"{key}: {item} {noun} ({percentage:.1f}%)")
            print("=== Inventory Statistics ===")
            stats = statistics(items)
            noun_max = plural_singular(stats[1])
            noun_min = plural_singular(stats[3])
            print(f"Most abundant: {stats[0]} ({stats[1]} {noun_max})")
            print(f"Least abundant: {stats[2]} ({stats[3]} {noun_min})")
            print()
            print("=== Item Categories ===")
            moderate = {}
            scarce = {}
            for element in items.keys():
                if element == "potion":
                    moderate.update({element: items[element]})
                else:
                    scarce.update({element: items[element]})
            print(f"Moderate: {moderate}")
            print(f"Scarce: {scarce}")
            print()
            print("=== Management Suggestions ===")
            print(f"Restock needed: {restock_needed(items)}")
            print()
            print("=== Dictionry Properties Demo ===")
            keys = []
            values = []
            for key in items.keys():
                keys += [key]
            for value in items.values():
                values += [value]
            in_stock = lookup(items, 'shield')
            print(f"Dictionary keys : {keys}")
            print(f"Dictionar values : {values}")
            print(f"Sample lookup - 'shield' in inventory: {in_stock}")
        except ValueError as e:
            print(f"Error: {e}")
