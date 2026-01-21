def obj_in_class(obj: object, class_name: str) -> bool:
    """Check if an object is an instance of a specific class by its name."""
    if obj is None:
        return False
    return obj.__class__.__name__ == class_name


def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:

    if not obj_in_class(plant_name, "str"):
        raise TypeError("The name must be string")
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(f"Water level {sunlight_hours} is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    print(f"Plant '{plant_name.lower()}' is healthy!", end="\n\n")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===", end="\n\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 8)
    except Exception as error:
        print(f"Error: {error}", end="\n\n")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except Exception as error:
        print(f"Error: {error}", end="\n\n")

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except Exception as error:
        print(f"Error: {error}", end="\n\n")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except Exception as error:
        print(f"Error: {error}", end="\n\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
