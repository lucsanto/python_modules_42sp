def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    temperatures = ["25", "abc"]

    for temp in temperatures:
        print(f"\nInput data is '{temp}'")

        try:
            result = input_temperature(temp)
            print(f"Temperature is now {result}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()