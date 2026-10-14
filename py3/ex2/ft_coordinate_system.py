
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        try:
            x_text, y_text, z_text = coordinates.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(x_text)
            y = float(y_text)
            z = float(z_text)
        except ValueError as error:
            print(f"Error on parameter: {error}")
            continue

        return (x, y, z)


def ft_coordinates_system(
    first_pos: tuple[float, float, float],
    second_pos: tuple[float, float, float]
) -> float:
    distance = math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )
    return distance


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

    center = (0.0, 0.0, 0.0)
    distance_center = ft_coordinates_system(first_pos, center)
    print(f"Distance to center: {round(distance_center, 4)}")

    print("\nGet a second set of coordinates")
    second_pos = get_player_pos()

    distance_between = ft_coordinates_system(first_pos, second_pos)
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance_between, 4)}"
    )


if __name__ == "__main__":
    main()
