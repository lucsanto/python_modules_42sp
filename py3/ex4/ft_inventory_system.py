
import sys


def store_items() -> dict[str, int]:
    items_dict: dict[str, int] = {}

    for item in sys.argv[1:]:
        result = item.split(":")

        if len(result) != 2 or result[0] == "" or result[1] == "":
            print(f"Error - invalid parameter '{item}'")
            continue

        if result[0] in items_dict:
            print(f"Redundant item '{result[0]}' - discarding")
            continue

        try:
            items_dict.update({result[0]: int(result[1])})
        except ValueError as error:
            print(f"Quantity error for '{result[0]}': {error}")

    return items_dict


def main() -> None:
    print("=== Inventory System Analysis ===")

    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py <item:quantity> ...")

    items = store_items()
    print(f"Got inventory: {items}")

    items_list = list(items.keys())
    print(f"Item list: {items_list}")

    items_total_qty = sum(items.values())
    print(
        f"Total quantity of the {len(items_list)} "
        f"items: {items_total_qty}"
    )

    if items_total_qty != 0:
        for item_name in items:
            quantity = items[item_name]
            x: float = quantity / items_total_qty
            print(f"Item {item_name} represents {round(x * 100, 1)}%")
    elif len(items) > 0:
        print("Cannot calculate percentages: total quantity is zero")

    if len(items_list) > 0:
        most_name = items_list[0]
        least_name = items_list[0]

        for item_name in items:
            if items[item_name] > items[most_name]:
                most_name = item_name
            if items[item_name] < items[least_name]:
                least_name = item_name

        print(
            f"Item most abundant: {most_name} "
            f"with quantity {items[most_name]}"
        )
        print(
            f"Item least abundant: {least_name} "
            f"with quantity {items[least_name]}"
        )

    new_item = "magic_item"
    while new_item in items:
        new_item += "_new"

    items.update({new_item: 1})
    print(f"Updated inventory: {items}")


if __name__ == "__main__":
    main()
