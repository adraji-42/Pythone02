class InvalidPlant(ValueError):
    pass


class Plant:
    """A class representing a plant with protected data."""

    def __init__(self, name: str):
        self.name = name.capitalize()


def water_plants(plant_list: list[Plant]):

    print("Opening watering system")

    for plant in plant_list:
        if not isinstance(plant, Plant):
            raise InvalidPlant("Cannot water None - invalid plant!")
        print(f"Watering {plant.name}")


def main():

    normal_test = [
                Plant("tomato"),
                Plant("lettuce"),
                Plant("carrots")
            ]
    error_test = [
                Plant("tomato"),
                "this is not plant",
                Plant("carrots")
            ]

    print("=== Garden Watering System ===", end="\n\n")
    print("Testing normal watering...")
    try:
        water_plants(normal_test)

    except InvalidPlant as error:
        print(f"Error: {error}\n")

    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!", end="\n\n")

    print("Testing with error...")
    try:
        water_plants(error_test)

    except InvalidPlant as error:
        print(f"Error: {error}")

    finally:
        print("Closing watering system (cleanup)", end="\n\n")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
