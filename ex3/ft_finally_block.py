def obj_in_class(obj: object, class_name: str) -> bool:
    """Check if an object is an instance of a specific class by its name."""
    if obj is None:
        return False
    return obj.__class__.__name__ == class_name


def water_plants(plant_list: list[str]) -> None:

    print("Opening watering system")

    for plant in plant_list:
        if not obj_in_class(plant, "str") or plant is None:
            raise ValueError("Cannot water None - invalid plant!")
        print(f"Watering {plant.lower()}")


def test_watering_system() -> None:

    normal_test = [
                "tomato",
                "lettuce",
                "carrots"
            ]
    error_test = [
                "tomato",
                1
            ]

    print("=== Garden Watering System ===", end="\n\n")

    print("Testing normal watering...")
    try:
        water_plants(normal_test)
    except ValueError as error:
        print(f"Error: {error}\n")

    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!", end="\n\n")

    print("Testing with error...")
    try:
        water_plants(error_test)

    except ValueError as error:
        print(f"Error: {error}")

    finally:
        print("Closing watering system (cleanup)", end="\n\n")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
