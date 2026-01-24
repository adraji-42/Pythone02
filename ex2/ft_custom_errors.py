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


class Plant:
    """
    A class representing a plant with growth and health monitoring.

    Attributes:
        name (str): The common name of the plant.
        height (int): The current height of the plant in centimeters.
        age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes and validate biological constraints."""
        if name == "":
            raise PlantError("Validation Failed: Plant identity is missing. "
                             "Name cannot be an empty string.")
        if age == 0 and height > 0:
            raise PlantError("Biological Inconsistency: A newborn plant "
                             "(age 0) cannot have a positive height.")
        if age < 0:
            raise PlantError(f"Invalid Age: {age} days. Age cannot be "
                             "negative.")
        if height < 0:
            raise PlantError(f"Invalid Height: {height} cm. Height cannot be "
                             "negative.")
        self.name = name.capitalize()
        self.age = age
        self.height = height

    def check_plant_health(self, is_wilting: bool) -> None:
        """Check if the plant shows signs of distress."""
        if is_wilting:
            raise PlantError(f"Health Alert: The {self.name.lower()} "
                             "is wilting! Immediate care required.")


class GardenManagement:
    """
    Manage garden operations including plant inventory and water resources.

    Attributes:
        owner (str): The name of the person managing the garden.
        water_stock (int): Current units of water available in the tank.
    """

    def __init__(self, owner: str, water_stock: int) -> None:
        """Initialize garden management with an owner and water supply."""
        if not owner:
            raise GardenError("Initialization Error: A garden must have an "
                              "assigned owner name.")
        if water_stock < 0:
            raise WaterError(f"Tank Error: {water_stock} units is invalid. "
                             "Water levels cannot be negative.")
        self.owner = owner.capitalize()
        self.plants: list[Plant] = []
        self.number_plants = 0
        self.water_stock = water_stock

    def add_plant(self, plant: Plant) -> None:
        """Add a new Plant instance to the garden collection."""
        if plant is None or not ft_isinstance(plant, Plant.__name__):
            raise TypeError("System Error: Addition failed. Only valid Plant "
                            "objects are permitted.")
        else:
            self.plants.append(plant)
            self.number_plants += 1

    def watering_garden(self) -> None:
        """Use water stock to irrigate all plants in the garden."""
        if self.water_stock < self.number_plants:
            raise WaterError(f"Irrigation Failure: Available water "
                             f"({self.water_stock}) is insufficient for "
                             f"{self.number_plants} plants.")
        self.water_stock -= self.number_plants

    def check_water_tank(self) -> None:
        """Verify if current water stock meets minimum requirements."""
        if self.water_stock < self.number_plants:
            raise WaterError(f"Critical Low Water: Tank ({self.water_stock}) "
                             "cannot sustain the current garden population.")


def ft_isinstance(obj: object, class_name: str) -> bool:
    """
    Manually check if an object is an instance of a specific class.

    Args:
        obj (object): The object to inspect.
        class_name (str): The string name of the target class.

    Returns:
        bool: True if class_name is found in the object's MRO.
    """

    if obj is None:
        return False
    family_tree = [cls.__name__ for cls in obj.__class__.__mro__]
    return class_name in family_tree


def report_error(error: Exception) -> None:
    """Print a standardized diagnostic report for any caught exception."""

    tb = error.__traceback__

    print(f"DIAGNOSTIC - {error.__class__.__name__}: {error}")

    if not tb:
        return
    while tb.tb_next:
        tb = tb.tb_next

    line_number = tb.tb_lineno
    full_path = tb.tb_frame.f_code.co_filename
    file_name = full_path.split('/')[-1]
    if file_name == full_path:
        file_name = full_path.split('\\')[-1]

    print(
        f"LOCATION - Line: {line_number} | File: {file_name}", end="\n\n"
    )


def main() -> None:
    """Entry point for the garden management simulation."""

    plants = [Plant("Tomato", 120, 60), Plant("Rose", 25, 30)]
    garden = GardenManagement("Hamid", 1)

    for plant in plants:
        garden.add_plant(plant)

    print("=== Custom Garden Errors Demo ===", end="\n\n")

    print("Testing PlantError...")
    try:
        plants[0].check_plant_health(True)
    except PlantError as error:
        print(f"Caught Expected PlantError: {error}", end="\n\n")
    except Exception as error:
        report_error(error)
    else:
        print("Execution successful", end="\n\n")

    print("Testing WaterError...")
    try:
        garden.check_water_tank()
    except WaterError as error:
        print(f"Caught Expected WaterError: {error}", end="\n\n")
    except Exception as error:
        report_error(error)
    else:
        print("Execution successful", end="\n\n")

    print("Testing Hierarchy Catch (GardenError)...")
    try:
        plants[0].check_plant_health(True)
    except GardenError as error:
        print(f"Caught via Base Class (GardenError): {error}")
    except Exception as error:
        report_error(error)
    else:
        print("Execution successful")

    try:
        garden.check_water_tank()
    except GardenError as error:
        print(f"Caught via Base Class (GardenError): {error}", end="\n\n")
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
