def water_plants(plants: list[str]):

    print("Opening watering system")

    for plant in plants:
        if not isinstance(plant, str):
            raise ValueError("Cannot water None - invalid plant!")
        print(f"Watering {plant.lower()}")


def main():

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
    main()
