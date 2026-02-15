def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    else:
        if unit == "grams":
            print(f"{seed_type} seeds: {quantity} grams total")
        else:
            if unit == "area":
                print(f"{seed_type} seeds: covers {quantity} sqaure meters")
            else:
                print("Unknown unit type")
