import sys

def ft_command_quest():
    i = 1

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) == 1:
        print("No arguments provided!")
        print("Total arguments: 1")
        return

    print(f"Arguments received: {len(sys.argv) - 1}")

    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1

    print(f"Total arguments: {i}")


if __name__ == "__main__":
    ft_command_quest()