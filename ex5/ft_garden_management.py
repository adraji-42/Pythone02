class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """Raised when there is a watering or irrigation issue."""
    pass


class SunLightError(GardenError):
    """Raised when there is a sunlight exposure issue."""
    pass


class Plant:
    """A class representing a plant with protected data."""

    def __init__(
            self, name: str, height: int, age: int,
            water_level: int, sunlight_hours: int
            ) -> None:
        if name == "":
            raise PlantError("Plant name cannot be empty!")
        if (age == 0 and height > 0) or (age > 0 and height == 0):
            raise PlantError("Cannot have age 0 with height > 0 or vice versa")
        if age < 0:
            raise PlantError("The age of plant cannot be negative!")
        if height < 0:
            raise PlantError("The height of plant cannot be negative!")
        if water_level < 0:
            raise WaterError("The water level of plant cannot be negative!")
        if sunlight_hours < 0:
            raise SunLightError(
                "The sunlight hours of plant cannot be negative!"
                )
        self.name = name.capitalize()
        self.age = age
        self.height = height
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """A class representing the garden management."""

    def __init__(self, name: str, owner: str, water_stock: int) -> None:
        if name == "":
            raise GardenError("Garden name cannot be empty!")
        if owner == "":
            raise GardenError("Garden owner name cannot be empty!")
        if water_stock < 0:
            raise WaterError("The value of the water tank cannot be negative!")
        self.name = name.capitalize()
        self.owner = owner.capitalize()
        self.plants = []
        self.number_plants = 0
        self.water_stock = water_stock

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden list."""
        self.plants.append(plant)
        self.number_plants += 1
        print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        """Water all plants and handle water stock errors."""
        print("Opening watering system")
        if self.water_stock < len(self.plants):
            raise WaterError("Not enough water in tank")
        for plant in self.plants:
            print(f"Watering {plant.name} - success")
            self.water_stock -= 1

    def check_water_tank(self) -> None:
        if self.water_stock < self.number_plants:
            raise WaterError("Not enough water in tank!")

    def check_plant_health(self) -> None:
        """Check the health status of all plants."""

        def plants_is_health(water_level, sunlight_hours):

            if water_level > 10:
                raise WaterError(f"Water level {water_level} "
                                 f"is too high (max 10)")
            if water_level < 1:
                raise WaterError(f"Water level {water_level} "
                                 "is too low (min 1)")
            if sunlight_hours > 12:
                raise SunLightError(f"Sunlight hours {sunlight_hours} "
                                    "is too high (max 12)")
            if sunlight_hours < 2:
                raise SunLightError(f"Sunlight hours {sunlight_hours} "
                                    "is too low (min 2)")

        for plant in self.plants:
            try:
                plants_is_health(plant.water_level, plant.sunlight_hours)
            except GardenError as error:
                print(f"Error checking {plant.name}: {error}")
            else:
                print(f"{plant.name.lower()}: healthy "
                      f"(water: {plant.water_level}, "
                      f"sun: {plant.sunlight_hours})")


def test_garden_management() -> None:
    print("=== Garden Management System ===", end="\n\n")

    garden = GardenManager("Konoha", "Naruto", 3)

    print("Adding plants to garden...")
    try:
        garden.add_plant(Plant("Sakora", 600, 2143, 8, 10))
        garden.add_plant(Plant("Blue Spider Lily", 25, 45, 9, 15))
        garden.add_plant(Plant("", 15, 25, 5, 7))
    except GardenError as error:
        print(f"Error adding plant: {error}")
    finally:
        print()

    print("Watering plants...")
    try:
        garden.water_plants()
    except GardenError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)", end="\n\n")

    print("Checking plant health...")
    try:
        garden.check_plant_health()
    except GardenError as error:
        print(f"Error: {error}")
    finally:
        print()

    print("Testing error recovery...")
    try:
        garden.check_water_tank()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...", end="\n\n")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
