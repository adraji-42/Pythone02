def obj_in_class(obj: object, class_name: str) -> bool:
    """
    Check if an object is an instance of a specific class by its name.

    Args:
        obj (object): The object to be checked.
        class_name (str): The name of the class to compare against.

    Returns:
        bool: True if the object's class name matches class_name,
              False otherwise.
    """
    if obj is None:
        return False
    return obj.__class__.__name__ == class_name


def water_plants(plant_list: list[str]) -> None:
    """
    Simulate the watering process for a list of plants with type validation.

    Args:
        plant_list (list[str]): A list containing the names of plants as
            strings.

    Raises:
        ValueError: If an item in the list is not a string or is None,
            preventing irrigation of invalid data types.
    """
    print("Opening watering system")

    for plant in plant_list:
        if not obj_in_class(plant, "str") or plant is None:
            raise ValueError(
                f"Data Integrity Error: Expected string input for plant "
                f"name, but received '{plant.__class__.__name__}' with value "
                f"'{plant}'. Irrigation sequence aborted."
            )
        if plant == "":
            raise ValueError("The plant name cannot be empty")
        print(f"Watering {plant.lower()}")


def test_watering_system() -> None:
    """
    Run test scenarios for the watering system to verify error handling.
    """
    normal_test = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    error_test = [
        "tomato",
        [2]
    ]

    print("=== Garden Watering System ===", end="\n\n")

    print("Testing normal watering...")
    success = False
    try:
        water_plants(normal_test)
    except ValueError as error:
        print(f"Operational Alert: {error}\n")
    except Exception as error:
        print(f"Unexpected Error: {error}")
    else:
        success = True
    finally:
        print("Closing watering system (cleanup)")

    if success:
        print("Watering completed successfully!", end="\n\n")

    print("Testing with error...")
    success = False
    try:
        water_plants(error_test)
    except ValueError as error:
        print(f"Operational Alert: {error}")
    except Exception as error:
        print(f"Unexpected Error: {error}")
    else:
        success = True
    finally:
        print("Closing watering system (cleanup)", end="\n\n")

    if success:
        print("Watering completed successfully!", end="\n\n")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
