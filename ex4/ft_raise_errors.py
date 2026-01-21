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


def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
) -> None:
    """
    Validate environmental conditions for a specific plant.

    Args:
        plant_name (str): The name of the plant.
        water_level (int): Current water level (scale 1-10).
        sunlight_hours (int): Daily sunlight exposure (hours 2-12).

    Raises:
        TypeError: If plant_name is not a string.
        ValueError: If environmental parameters are outside safe ranges.
    """
    if not obj_in_class(plant_name, "str"):
        raise TypeError(
            f"Type mismatch: 'plant_name' expected 'str' but "
            f"received '{plant_name.__class__.__name__}'."
        )

    if plant_name == "":
        raise ValueError("Invalid Input: Plant name cannot be empty.")

    if water_level > 10:
        raise ValueError(
            f"Irrigation Alert: Water level {water_level} exceeds "
            "maximum safety threshold (10)."
        )
    if water_level < 1:
        raise ValueError(
            f"Irrigation Alert: Water level {water_level} is below "
            "minimum hydration requirements (1)."
        )

    if sunlight_hours > 12:
        raise ValueError(
            f"Exposure Alert: Sunlight duration {sunlight_hours}h exceeds "
            "safe metabolic limit (12h)."
        )
    if sunlight_hours < 2:
        raise ValueError(
            f"Exposure Alert: Sunlight duration {sunlight_hours}h is "
            "insufficient for photosynthesis (min 2h)."
        )

    print(f"Plant '{plant_name.lower()}' is healthy!", end="\n\n")


def test_plant_checks() -> None:
    """
    Execute a diagnostic suite to verify plant health validation logic.
    """
    print("=== Garden Plant Health Checker ===", end="\n\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 8)
    except Exception as error:
        print(f"Diagnostic Error: {error}", end="\n\n")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except Exception as error:
        print(f"Diagnostic Error: {error}", end="\n\n")

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except Exception as error:
        print(f"Diagnostic Error: {error}", end="\n\n")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except Exception as error:
        print(f"Diagnostic Error: {error}", end="\n\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
