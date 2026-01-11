class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """Raised when there is a watering or irrigation issue."""
    pass


class Plant:
    """A class representing a plant with protected data."""

    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        if (age == 0 and height > 0) or (age > 0 and height == 0):
            raise PlantError("Cannot have age 0 with height > 0 or vice versa")
        if age < 0:
            raise PlantError("The age of plant cannot be negative!")
        if height < 0:
            raise PlantError("The height of plant cannot be negative!")
        self.age = age
        self.height = height

    def check_plant_health(self, is_wilting: bool):
        if is_wilting:
            raise PlantError(f"The {self.name} plant is wilting!")


class GardenManagement:
    """A class representing the garden management."""

    def __init__(self, owner: str, water_stock: int,
                 plants: list[Plant] = None):
        self.owner = owner.capitalize()
        self.plants = plants if plants else []
        self.number_plants = len(self.plants)
        if water_stock < 0:
            raise WaterError("The value of the water tank cannot be negative!")
        self.water_stock = water_stock

    def watering_garden(self):
        if self.water_stock < self.number_plants:
            raise WaterError("The water tank is not sufficient "
                             "for irrigating the garden!")
        self.water_stock -= self.number_plants

    def check_water_level(self):
        if self.water_stock < self.number_plants:
            raise WaterError("Not enough water in the tank!")


def main():
    plants = [Plant("Tomato", 120, 60), Plant("Rose", 25, 30)]
    garden = GardenManagement("Hamid", 1, plants)

    print("=== Custom Garden Errors Demo ===", end="\n\n")

    print("Testing PlantError...")
    try:
        plants[0].check_plant_health(True)

    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    print("Testing WaterError...")
    try:
        garden.check_water_level()

    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")
    try:
        plants[0].check_plant_health(True)

    except GardenError as error:
        print(f"Caught a garden error: {error}")

    try:
        garden.check_water_level()

    except GardenError as error:
        print(f"Caught a garden error: {error}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
