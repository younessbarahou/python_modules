class GardenError(Exception):
    pass


class PlantError(GardenError):
    message = "Caught PlantError"


class WaterError(GardenError):
    message = "Caught WaterError"


def test_Water_Error() -> None:
    try:
        raise PlantError("The Plant is wilting")
    except PlantError as e:
        print(f"{e.message} : {e}")


def test_Plant_Error() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"{e.message} : {e}")


def test_Garden_Error() -> None:
    try:
        raise PlantError("The Plant is wilting!")
    except GardenError as e:
        print(f"Caught Garden Error : {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught Garden Error : {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    test_Plant_Error()
    print()
    print("Testing WaterError...")
    test_Water_Error()
    print()
    print("Testing catching all garden errors...")
    test_Garden_Error()
    print()
    print("All custom error types work correctly!")
