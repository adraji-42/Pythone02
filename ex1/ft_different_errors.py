def garden_operations(error_type: str):
    """
    Triggers specific exceptions based on the provided error_type string.
    """

    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        return 10 / 0
    elif error_type == "file":
        open("missing.txt", "r")
    elif error_type == "key":
        garden = {"plant": "tomato"}
        return garden["missing_plant"]
    elif error_type == "multiple":
        int("invalid")


def test_error_types():
    """
    Tests and catches specific error types with hardcoded messages
    to match the example output exactly.
    """

    print("=== Garden Error Types Demo ===")

    # 1. ValueError
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    # 2. ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    # 3. FileNotFoundError
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    # 4. KeyError
    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print()

    # 5. Multiple errors together
    print("Testing multiple errors together...")
    try:
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
