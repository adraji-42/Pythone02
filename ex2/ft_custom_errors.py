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

    def __init__(self, name: str, height: int, age: int) -> None:
        if name == "":
            raise PlantError("The plant name cannot be empty")
        if age == 0 and height > 0:
            raise PlantError("Cannot have age 0 with height > 0")
        if age < 0:
            raise PlantError("The age of plant cannot be negative!")
        if height < 0:
            raise PlantError("The height of plant cannot be negative!")
        self.name = name.capitalize()
        self.age = age
        self.height = height

    def check_plant_health(self, is_wilting: bool) -> None:
        if is_wilting:
            raise PlantError(f"The {self.name.lower()} plant is wilting!")


class GardenManagement:
    """A class representing the garden management."""

    def __init__(self, owner: str, water_stock: int) -> None:
        if not owner:
            raise GardenError("The plant owner cannot be empty or None")
        if water_stock < 0:
            raise WaterError("The value of the water tank cannot be negative!")
        self.owner = owner.capitalize()
        self.plants = []
        self.number_plants = 0
        self.water_stock = water_stock

    def add_plant(self, plant: Plant) -> None:
        if plant is None or not ft_isinstance(plant, "Plant"):
            raise TypeError("Only Plant objects can be added to the garden")
        else:
            self.plants.append(plant)
            self.number_plants += 1

    def watering_garden(self) -> None:
        if self.water_stock < self.number_plants:
            raise WaterError("The water tank is not sufficient "
                             "for irrigating the garden!")
        self.water_stock -= self.number_plants

    def check_water_tank(self) -> None:
        if self.water_stock < self.number_plants:
            raise WaterError("Not enough water in the tank!")


def ft_isinstance(obj: object, class_name: str) -> bool:
    """Manual simulation of isinstance."""
    if obj is None:
        return False
    family_tree = [cls.__name__ for cls in obj.__class__.__mro__]
    return class_name in family_tree


def report_error(error: Exception):
    """Prints a standardized error report with the deepest line number."""
    tb = error.__traceback__
    while tb.tb_next:
        tb = tb.tb_next
    line_number = tb.tb_lineno

    print(f"Caught {error.__class__.__name__}: {error}")
    print(f"Error in line: {line_number}", end="\n\n")


def main() -> None:
    plants = [Plant("Tomato", 120, 60), Plant("Rose", 25, 30)]
    garden = GardenManagement("Hamid", 1)

    for plant in plants:
        garden.add_plant(plant)

    print("=== Custom Garden Errors Demo ===", end="\n\n")

    print("Testing PlantError...")
    try:
        plants[0].check_plant_health(True)
    except PlantError as error:
        print(f"Caught PlantError: {error}", end="\n\n")
    except Exception as error:
        report_error(error)
    else:
        print("Execution successful", end="\n\n")

    print("Testing WaterError...")
    try:
        garden.check_water_tank()
    except WaterError as error:
        print(f"Caught WaterError: {error}", end="\n\n")
    except Exception as error:
        report_error(error)
    else:
        print("Execution successful", end="\n\n")

    print("Testing catching all garden errors...")
    try:
        plants[0].check_plant_health(True)
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    except Exception as error:
        report_error(error)
    else:
        print("Execution successful")

    try:
        garden.check_water_tank()
    except GardenError as error:
        print(f"Caught a garden error: {error}", end="\n\n")
    except Exception as error:
        report_error(error)
    else:
        print("Execution successful")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        report_error(error)
