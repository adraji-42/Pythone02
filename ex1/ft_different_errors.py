def garden_operations(error_type: str = "") -> None:
    """
    Simulate and trigger specific Python exceptions for testing purposes.

    Args:
        error_type (str, optional): The identifier for the exception to raise.
            Supported values:
            - 'value': Raises ValueError (invalid string to int).
            - 'zero': Raises ZeroDivisionError (division by zero).
            - 'file': Raises FileNotFoundError (missing text file).
            - 'key': Raises KeyError (missing dictionary key).
            If None or an unrecognized string is provided, no exception is
            raised and the function completes normally.
    """

    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        print(10 / 0)
    elif error_type == "file":
        file = open("missing.txt", "r")
        file.close()
    elif error_type == "key":
        garden = {"plant": "tomato"}
        print(garden["missing_plant"])


def test_error_types() -> None:
    """
    Test and catch garden_operations exceptions with concise logging.
    """

    print("=== Garden Error Types Demo ===", end="\n\n")

    # 1. ValueError
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print(
            "ERROR: Failed to convert string to integer. "
            "Ensure the input contains only numeric digits.", end="\n\n"
        )
    except Exception as error:
        print(f"Unexpected Error: {error}")
    else:
        print("Execution successful", end="\n\n")

    # 2. ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print(
            "ERROR: Mathematical operation failed. "
            "Division by zero is undefined in this system.", end="\n\n"
        )
    except Exception as error:
        print(f"Unexpected Error: {error}")
    else:
        print("Execution successful", end="\n\n")

    # 3. FileNotFoundError
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as error:
        print(
            "ERROR: Resource missing. "
            f"Could not find file: '{error.filename}'", end="\n\n"
        )
    except Exception as error:
        print(f"Unexpected Error: {error}")
    else:
        print("Execution successful", end="\n\n")

    # 4. KeyError
    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as error:
        print(
            f"ERROR: Database lookup failed. Missing key: {error}", end="\n\n"
        )
    except Exception as error:
        print(f"Unexpected Error: {error}")
    else:
        print("Execution successful", end="\n\n")

    # 5. Multiple errors together
    print("Testing multiple errors together...")
    try:
        garden_operations("file")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print(
            "GENERAL ERROR: An operation failed during execution. "
            "The system handled the exception and will proceed.", end="\n\n"
        )
    except Exception as error:
        print(f"Unexpected Error: {error}")
    else:
        print("Execution successful", end="\n\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
