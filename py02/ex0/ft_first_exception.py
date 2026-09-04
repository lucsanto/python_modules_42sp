def check_temperature(temp: str) -> None:
    print(f"Input data is '{repr(temp)}'")
    try:
        result = int(temp)
        print(f"Temperature is now {result}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

def test_temperature_input() -> None:
    print("=== Garden Temperature ===")
    check_temperature("abc")
    check_temperature(25)
    check_temperature("ola 42")
    check_temperature(42)

    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()
