class GardenError(Exception):
    """Base class for all garden-related errors."""
    def __init__(
        self,
        messege: str = "An error of the following type occurred: GardenError"
    ) -> None:
        super().__init__(messege)


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    def __init__(
        self,
        messege: str = "An error of the following type occurred: PlantError"
    ) -> None:
        super().__init__(messege)


class WaterError(GardenError):
    """Raised when there is a watering or irrigation issue."""
    def __init__(
        self,
        messege: str = "An error of the following type occurred: WaterError"
    ) -> None:
        super().__init__(messege)


class SunLightError(GardenError):
    """Raised when there is a sunlight exposure issue."""
    def __init__(
        self,
        messege: str = "An error of the following type occurred: SunLightError"
    ) -> None:
        super().__init__(messege)


class Plant:
    """
    A class representing a plant with physiological and environmental data.

    Attributes:
        name (str): The common name of the plant.
        height (int): The current height of the plant in centimeters.
        age (int): The age of the plant in days.
        water_level (int): The current hydration level of the plant.
        sunlight_hours (int): Daily sunlight exposure in hours.
    """

    def __init__(
            self, name: str, height: int, age: int,
            water_level: int, sunlight_hours: int
    ) -> None:
        """Initialize plant and validate biological and environmental data."""
        if not obj_in_class(name, "str"):
            raise TypeError(f"Type Error: 'name' must be a string, not "
                            f"'{name.__class__.__name__}'.")
        if name == "":
            raise PlantError("Identification Error: Plant name cannot be "
                             "empty.")
        if (age == 0 and height > 0) or (age > 0 and height == 0):
            raise PlantError(f"Biological Mismatch: Inconsistent age ({age}) "
                             f"and height ({height}) relationship.")
        if age < 0:
            raise PlantError(f"Value Error: Age cannot be negative ({age}).")
        if height < 0:
            raise PlantError(f"Value Error: Height cannot be negative "
                             f"({height}).")
        if water_level < 0:
            raise WaterError(f"Hydration Error: Water level cannot be "
                             f"negative ({water_level}).")
        if sunlight_hours < 0:
            raise SunLightError(f"Photosynthesis Error: Sunlight hours "
                                f"cannot be negative ({sunlight_hours}).")
        self.name = name.capitalize()
        self.age = age
        self.height = height
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """
    A class to manage garden plants and resource allocation.

    Attributes:
        name (str): The name of the garden.
        owner (str): The owner of the garden.
        water_stock (int): Available units of water in the tank.
    """

    def __init__(self, name: str, owner: str, water_stock: int) -> None:
        """Initialize garden management with resource validation."""
        if not obj_in_class(name, "str"):
            raise TypeError("Type Error: Garden 'name' must be a string.")
        if not obj_in_class(owner, "str"):
            raise TypeError("Type Error: Garden 'owner' must be a string.")
        if name == "":
            raise GardenError("Registry Error: Garden name cannot be empty.")
        if owner == "":
            raise GardenError("Registry Error: Owner name cannot be empty.")
        if water_stock < 0:
            raise WaterError(f"Inventory Error: Water stock cannot be "
                             f"negative ({water_stock}).")
        self.name = name.capitalize()
        self.owner = owner.capitalize()
        self.plants: list[Plant] = []
        self.number_plants = 0
        self.water_stock = water_stock

    def add_plant(self, plant: Plant) -> None:
        """Add a validated Plant object to the garden collection."""
        if not obj_in_class(plant, "Plant"):
            raise TypeError(f"Type Error: Expected 'Plant' object, got "
                            f"'{plant.__class__.__name__}'.")
        self.plants.append(plant)
        self.number_plants += 1
        print(f"Success: {plant.name} added to {self.name}.")

    def water_plants(self) -> None:
        """Execute irrigation for all plants if resources permit."""
        print("Opening watering system...")
        if self.water_stock < len(self.plants):
            raise WaterError(f"Resource Scarcity: Tank level "
                             f"({self.water_stock}) is below required "
                             f"amount ({len(self.plants)}).")
        for plant in self.plants:
            print(f"Irrigating {plant.name} - OK")
            self.water_stock -= 1

    def check_water_tank(self) -> None:
        """Validate if current water reserves meet the minimum threshold."""
        if self.water_stock < self.number_plants:
            raise WaterError(f"Critical Level: Low water reserves "
                             f"({self.water_stock} units remaining).")

    def check_plant_health(self) -> None:
        """Perform a health diagnostic for every plant in the garden."""

        def plants_is_health(water_level: int, sunlight_hours: int) -> None:
            """Validate health parameters against environmental thresholds."""
            if water_level > 10:
                raise WaterError(f"Oversaturation: Water level {water_level} "
                                 "exceeds safety limit (max 10).")
            if water_level < 1:
                raise WaterError(f"Dehydration: Water level {water_level} "
                                 "is below survival limit (min 1).")
            if sunlight_hours > 12:
                raise SunLightError(f"Overexposure: {sunlight_hours}h "
                                    "sunlight exceeds limit (max 12h).")
            if sunlight_hours < 2:
                raise SunLightError(f"Light Deficiency: {sunlight_hours}h "
                                    "is below metabolic limit (min 2h).")

        for plant in self.plants:
            try:
                plants_is_health(plant.water_level, plant.sunlight_hours)
            except GardenError as error:
                raise PlantError(f"Diagnostic Failure for {plant.name}: "
                                 f"{error}")
            else:
                print(f"Status - {plant.name.lower()}: healthy "
                      f"(H2O: {plant.water_level}, "
                      f"UV: {plant.sunlight_hours})")


def obj_in_class(obj: object, class_name: str) -> bool:
    """
    Check if an object is an instance of a specific class by its name.

    Args:
        obj (object): The object to verify.
        class_name (str): The name of the class to check for.

    Returns:
        bool: True if class names match, False otherwise.
    """
    if obj is None:
        return False
    return obj.__class__.__name__ == class_name


def test_garden_management() -> None:
    """Execute integrated test suite for Garden Management System."""
    print("=== Garden Management System ===", end="\n\n")

    garden = GardenManager("Konoha", "Naruto", 3)

    print("Adding plants to garden...")
    try:
        garden.add_plant(Plant("Sakora", 600, 2143, 8, 10))
        garden.add_plant(Plant("Blue Spider Lily", 25, 45, 9, 15))
        garden.add_plant(Plant("", 15, 25, 5, 7))
    except GardenError as error:
        print(f"Catch (Garden Management): {error}", end="\n\n")
    except Exception as error:
        print(f"Catch (Unexpected): {error}", end="\n\n")

    print("Watering plants...")
    try:
        garden.water_plants()
    except Exception as error:
        print(f"Irrigation Error: {error}")
    finally:
        print("Closing watering system (cleanup)", end="\n\n")

    print("Checking plant health...")
    try:
        garden.check_plant_health()
    except PlantError as error:
        print(f"Health Monitoring Alert: {error}", end="\n\n")
    except Exception as error:
        print(f"Catch (Unexpected): {error}", end="\n\n")

    print("Testing error recovery...")
    try:
        garden.check_water_tank()
    except GardenError as error:
        print(f"System Recovery Catch: {error}")
    except Exception as error:
        print(f"Catch (Unexpected): {error}")
    finally:
        print("System integrity verified. Continuing operation...", end="\n\n")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
