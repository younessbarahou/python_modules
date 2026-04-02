def garden_operations(type_error: str) -> None:
    if type_error == "ValueError":
        int("abc")
    elif type_error == "ZeroDivisionError":
        1 / 0
    elif type_error == "FileNotFoundError":
        file = open("file.txt", 'r')
        file.close()
    elif type_error == "KeyError":
        dic_1 = {"one": 1, "two": 2}
        dic_1["three"]
    elif type_error == "All Errors":
        int("abc")
        1 / 0
        file = open("file.txt", 'r')
        file.close()
        dic_1 = {"one": 1, "two": 2}
        dic_1["three"]


def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()
    print("Testing FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()
    print("Testing KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()
    print("Testing multipe errors together...")
    try:
        garden_operations("All Errors")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()
