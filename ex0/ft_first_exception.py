def check_temperature(temp_str: str) -> None:
    """
    Converts a string to an integer and checks if it exists inside it
    Safe range for plants (0-40 degrees).
    """

    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"{temp_str} is not a valid number")

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        return temp


def test_temperature_input() -> None:
    """
    Script entry point. Runs multiple test cases for demonstration
    Exception handling and data validation.
    """

    tests = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===", end="\n\n")

    for test in tests:
        try:
            print(f"Testing temperature: {test}")
            temp = check_temperature(test)
            print(f"Temperature {temp}°C is perfect for plants!", end="\n\n")
        except ValueError as error:
            print(f"Error: {error}", end="\n\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
