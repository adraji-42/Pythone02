def check_temperature(temp_str: str) -> int:
    """
    Convert a string input to an integer and validate the temperature range.

    Args:
        temp_str (str): The temperature value as a string.

    Returns:
        int: The validated temperature if it falls within the safe range.

    Raises:
        ValueError: If input is not a numeric string or outside (0-40) range.
    """

    try:
        temp: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Invalid input: '{temp_str}' is not a number.")

    if temp < 0:
        raise ValueError(
            f"Low temperature alert: {temp}°C is below 0°C (min 0°C)"
            )
    elif temp > 40:
        raise ValueError(
            f"High temperature alert: {temp}°C exceeds 40°C (max 40°C)"
            )
    else:
        return temp


def test_temperature_input() -> None:
    """Test temperature validation with various inputs."""

    tests: list[str] = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===", end="\n\n")

    try:
        for test in tests:
            try:
                print(f"Testing temperature: {test}")
                temp = check_temperature(test)
                print(
                    f"Temperature {temp}°C is perfect for plants!", end="\n\n"
                )
            except ValueError as error:
                print(f"Validation Error: {error}", end="\n\n")

        print("All tests completed - program didn't crash!")
    except Exception as error:
        print(f"Unexpected Error: {error}")


if __name__ == "__main__":
    test_temperature_input()
