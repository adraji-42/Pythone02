def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):

    if len(plant_name) == 0:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(f"Water level {sunlight_hours} is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    print(f"Plant '{plant_name.lower()}' is healthy!")


def main():
    print("=== Garden Plant Health Checker ===", end="\n\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 8)
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print()

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print()

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    main()
