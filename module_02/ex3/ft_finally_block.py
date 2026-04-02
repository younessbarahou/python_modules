def water_plants(plant_list: list[str]) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if type(plant) is not str or plant == "":
                raise ValueError(f"Cant Water [{plant}] invalid plant!")
            print(f"watering {plant}")
    except ValueError as e:
        print(f"Error : {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("Testing normal watering...")
    water_plants(["rose", "tree", "flower"])
    print()
    print("Testing with error...")
    water_plants(["rose", None, 2])


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
