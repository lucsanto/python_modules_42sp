def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        var = "abc"
        number = int(var)
    elif operation_number == 1:
        var = 2 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "erro" + 25
    else:
        return
    
def test_error_types() -> None:
    operations = [0, 1, 2, 3, 4]
    print("=== Garden Error Types Demo ===")

    for operation in operations:
        print(f"Testing operation {operation}...")

        try:
            garden_operations(operation)

        except ValueError as error:
            print(f"Caught ValueError: {error}")

        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")

        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")

        except TypeError as error:
            print(f"Caught TypeError: {error}")

        else:
            print("Operation completed successfully")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()