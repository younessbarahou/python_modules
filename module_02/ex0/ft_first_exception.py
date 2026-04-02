def check_temperature(temp_str: str) -> int:
    try:
        num = int(temp_str)
        if num < 0:
            raise ValueError(f"{num}C is too cold for plants (min 0C)")
        elif num > 40:
            raise ValueError(f"{num}C is too hot for plants (max 40C)")
        return (num)
    except ValueError as e:
        return (f"Error: {e}")


def test_temperature_input() -> None:
    temp_1 = "25"
    temp_2 = "abc"
    temp_3 = "100"
    temp_4 = "-50"
    print(f"Testing Temperature: {temp_1}")
    print(f"Temperature {check_temperature(temp_1)} is perfect for plants!")
    print()
    print(f"Testing Temperature: {temp_2}")
    print(check_temperature(temp_2))
    print()
    print(f"Testing Temperature: {temp_3}")
    print(check_temperature(temp_3))
    print()
    print(f"Testing Temperature: {temp_4}")
    print(check_temperature(temp_4))
    print()
    print("All tests Completed - program didn't crash")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature_input()
