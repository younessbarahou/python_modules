#!/usr/bin/python3
""" Class that handles multipe gardens """


class GardenManager:
    gardens = []
    number_of_gardens = 0

    """Display General Infos About Gardens Managed"""
    @classmethod
    def create_garden_network(cls):
        i = 0
        validation = 0
        while i < cls.number_of_gardens:
            j = 0
            while (j < cls.gardens[i].plant):
                if cls.gardens[i].plants[j].height <= 0:
                    validation += 1
                j += 1
            i += 1
        if (validation != 0):
            validation = False
            print(f"Height validation test: {validation}")
        else:
            validation = True
            print(f"Height validation test: {validation}")
        i = 0
        print("== Garden Scores ==")
        while i < cls.number_of_gardens:
            print(f"{cls.gardens[i].name}:{cls.gardens[i].score}")
            i += 1
        print(f"Total gardens managed:{cls.number_of_gardens}")
    """Blueprint For Creating Gardens"""
    class Garden:
        """Blueprint For Creating Plants"""
        class Plant:
            def __init__(self, data):
                self.name = data["name"]
                self.height = data["height"]
                self.type = data["type"]
        """Blueprint For Creating FloweringPlants"""
        class FloweringPlant(Plant):
            def __init__(self, data):
                super().__init__(data)
                self.color = data["color"]
        """Blueprint For Creating PrizeFlowers"""
        class PrizeFlower(FloweringPlant):
            def __init__(self, data):
                super().__init__(data)
                self.prize_points = data["prize_points"]
        """ Initialization of garden """
        def __init__(self, garden_name):
            self.name = garden_name
            self.plants = []
            self.growth = 0
            self.plant = 0
            self.flowering = 0
            self.prize = 0
            self.score = 0
        """ Adding Plants To Gardens """
        def add_plant(self, plant):
            if plant["type"] == "Plant":
                plant = self.Plant(plant)
                self.plant += 1
                self.score += 100
                self.plants += [plant]
            elif plant["type"] == "FloweringPlant":
                plant = self.FloweringPlant(plant)
                self.flowering += 1
                self.plants += [plant]
            else:
                plant = self.PrizeFlower(plant)
                self.prize += 1
                self.plants += [plant]
            print(f"Added {plant.name} to {self.name}'s garden")
            return (plant)
        """ Growing a single plant """
        def grow_plant(self, plant):
            plant.height += 1
            self.growth += 1
            print(f"{plant.name} grew 1cm")
        """ Growing all plants """
        def grow_all_plants(self):
            print(f"{self.name} is helping all plants grow...")
            i = 0
            while i < self.plant + self.flowering + self.prize:
                self.grow_plant(self.plants[i])
                i += 1
    """Adding garden to the class itself"""
    @classmethod
    def add_garden(cls, garden_name, garden_height):
        garden = cls.Garden(garden_name)
        cls.gardens += [garden]
        cls.number_of_gardens += 1
        return (garden)
    """Specific Garden Statistics"""
    class GardenStats:
        """Display Plants in a specific garden"""
        @staticmethod
        def plants_in_garden(garden):
            print("== Plants in garden ==")
            total = garden.plant + garden.flowering + garden.prize
            i = 0
            while total > i:
                x = garden.plants[i]
                if x.type == "Plant":
                    print(x.name, ":", x.height, "cm")
                elif x.type == "FloweringPlant":
                    print(x.name, ":", x.height, x.color)
                elif x.type == "PrizeFlower":
                    print(f"{x.name}:", x.height, x.color, x.prize_points)
                i += 1
        """Plants added in a garden given"""
        @staticmethod
        def plants_added(garden):
            return (garden.plant + garden.flowering + garden.prize)
        """growth in a garden given"""
        @staticmethod
        def growth_tracker(garden):
            return (garden.growth)
        """counts how many plants added to garden"""
        @staticmethod
        def is_plant_type(garden):
            return (garden.plant)
        """counts how many floweringplants added to garden"""
        @staticmethod
        def is_flowering_type(garden):
            return (garden.flowering)
        """counts how many plants added to garden"""
        @staticmethod
        def is_prize_type(garden):
            return (garden.prize)


if __name__ == "__main__":
    gm = GardenManager()
    abc = gm.add_garden("Alice", 1)
