#!/usr/bin/env python3


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0

        def add_grow(self) -> None:
            self._grow += 1

        def add_age(self) -> None:
            self._age += 1

        def add_show(self) -> None:
            self._show += 1

        def add_shade(self) -> None:
            self._shade += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow} grow, "
                f"{self._age} age, {self._show} show"
            )

        def display_shade(self) -> None:
            print(f" {self._shade} shade")

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0
    ) -> None:
        self._name = name
        self._height = 0.0
        self._days_old = 0
        self.set_height(height)
        self.set_age(days_old)
        self._stats = Plant._Stats()

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._days_old = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old

    def get_name(self) -> str:
        return self._name

    def show(self) -> None:
        self._stats.add_show()
        print(
            f"{self._name}: {self._height:.1f}cm, "
            f"{self._days_old} days old"
        )

    def grow(self, centimeters: float = 1.0) -> None:
        self.set_height(self._height + centimeters)
        self._stats.add_grow()

    def age(self, days: int = 1) -> None:
        self.set_age(self._days_old + days)
        self._stats.add_age()

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0,
        color: str = "unknown"
    ) -> None:
        super().__init__(name, height, days_old)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

        if self.bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0,
        trunk_diameter: float = 0.0
    ) -> None:
        super().__init__(name, height, days_old)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display_stats(self) -> None:
        super().display_stats()
        self._stats.display_shade()

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces "
            f"a shade of {self._height:.1f}cm long "
            f"and {self.trunk_diameter:.1f}cm wide."
        )
        self._stats.add_shade()


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0,
        harvest_season: str = "Unknown",
    ) -> None:
        super().__init__(name, height, days_old)
        self.harvest_season = harvest_season
        self.nutritional_value: float = 0

    def grow(self, amount: float = 1.0) -> None:
        super().grow(amount)
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self.nutritional_value)}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0,
        color: str = "unknown",
    ) -> None:
        super().__init__(name, height, days_old, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print()
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()