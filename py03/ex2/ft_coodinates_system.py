import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        try:
            x, y, z = coordinates.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(x)
            y = float(y)
            z = float(z)
        except ValueError as error:
            print(error)
            continue

        return(x, y, z)

def ft_coordinates_system(
    first_pos: tuple[float, float, float],
    second_pos: tuple[float, float, float]
) -> None:
    distance_center = math.sqrt(
        first_pos[0] ** 2
        + first_pos[1] ** 2
        + first_pos[2] ** 2
    )

    print(f"Distance to center: {round(distance_center, 4)}")

    distance_between = math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )

    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance_between, 4)}"
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    first_pos = get_player_pos()

    print(f"Got a first tuple: {first_pos}")
    print(
        f"It includes: X={first_pos[0]}, "
        f"Y={first_pos[1]}, "
        f"Z={first_pos[2]}"
    )

    print("\nGet a second set of coordinates")
    second_pos = get_player_pos()

    ft_coordinates_system(first_pos, second_pos)


if __name__ == "__main__":
    main()