def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> str:
    try:
        if plant_name == "":
            raise ValueError("Plant Name cannot be empty")
        if water_level < 1:
            raise ValueError(f"{water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"{water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"{sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"{sunlight_hours} is too high (max 12)")
        return (f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        return (f"Error: {e}")


def test_plant_checks() -> None:
    print("Testing good values...")
    print(check_plant_health("tomato", 5, 5))
    print()
    print("Testing empty plant name...")
    print(check_plant_health("", 5, 5))
    print()
    print("Testing bad water level...")
    print(check_plant_health("rose", 15, 5))
    print()
    print("Testing bad sunlight hours...")
    print(check_plant_health("rose", 5, -9))
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Check ===")
    print()
    test_plant_checks()
