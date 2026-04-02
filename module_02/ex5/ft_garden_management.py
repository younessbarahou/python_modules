class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(PlantError):
    pass


class SunlightError(PlantError):
    pass


class GardenManager:
    def __init__(self, garden_manager: str) -> None:
        self.__garden_manager = garden_manager
        self.__plants = []
        self.__tracker = 0
        self.__tank = 3

    def add_plant(self, plant: str, water: int, sunlight: int) -> None:
        try:
            if plant == "" or type(plant) is not str:
                raise PlantError("Plant Name Should be valid!")
            elif type(water) is not int:
                raise WaterError("Water level should be a valid number!")
            elif type(sunlight) is not int:
                raise SunlightError("Sunlight should be a valid number!")
            self.__plants += [{"p": plant, "w": water, "s": sunlight}]
            self.__tracker += 1
            print(f"Added {plant} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening Watering system")
        try:
            if self.__tracker == 0:
                raise ValueError("No Plants To Water !!")
            for plant in self.__plants:
                new_tank = self.__tank - 1
                if new_tank < 0:
                    raise GardenError("Not enough water in tank!")
                plant["w"] += 1
                self.__tank -= 1
                print(f"watering {plant['p']} - success")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        for plant in self.__plants:
            try:
                if plant["w"] < 1:
                    raise WaterError(f"{plant['p']} : Water level is too low")
                if plant["w"] > 10:
                    raise WaterError(f"{plant['p']} : Water level is too high")
                if plant["s"] > 12:
                    raise SunlightError(f"{plant['p']} : Sunlight is too high")
                if plant["s"] < 2:
                    raise SunlightError(f"{plant['p']} : Sunlight is too low")
                a = plant['p']
                b = plant['w']
                c = plant['s']
                print(f"{a}: healthy (water : {b}, sun : {c})")
            except PlantError as e:
                print(f"Error checking {e}")

    def get_tank(self) -> None:
        return (self.__tank)


def test_garden_management() -> None:
    try:
        garden_1 = GardenManager("garden_1")
        print("adding plants to garden...")
        garden_1.add_plant("plant_1", 1, 2)
        garden_1.add_plant("plant_2", 1, -12)
        garden_1.add_plant("plant_3", 1, 2)
        print()
        print("Watering plants...")
        garden_1.water_plants()
        print()
        print("Checking plant health...")
        garden_1.check_plant_health()
        if garden_1.get_tank() == 0:
            raise GardenError("Not enough water in tank!")
    except GardenError as e:
        print(f"\nCaught GardenError: {e}")
    finally:
        print("\nSystem recovered and continuing...")
        print()


if __name__ == "__main__":
    print("=== Garden Management System ===")
    print()
    test_garden_management()
    print("Garden management system test complete!")
