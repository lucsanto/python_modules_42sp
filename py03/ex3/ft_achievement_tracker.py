import random


ACHIEVEMENTS = [
    "first_kill",
    "level_10",
    "treasure_hunter",
    "speed_demon",
    "boss_slayer",
    "collector",
    "perfectionist",
    "world_savior",
    "master_explorer",
    "untouchable",
    "strategist",
    "survivor",
    "sharp_mind",
    "hidden_path_finder",
]


def gen_player_achievements() -> set:
    amount = random.randint(5, 10)
    return set(random.sample(ACHIEVEMENTS, amount))


def unique_achievements(
    player1: set, player2: set, player3: set, player4: set
) -> set:
    unique_ach = player1.union(player2, player3, player4)
    print(f"All unique achievements: {unique_ach}")
    print(f"Total unique achievements: {len(unique_ach)}\n")
    return unique_ach


def rare_achievements(
    player1: set, player2: set, player3: set, player4: set
) -> None:
    print(
        f"Only Alice has: "
        f"{player1.difference(player2.union(player3, player4))}"
    )
    print(
        f"Only Bob has: "
        f"{player2.difference(player1.union(player3, player4))}"
    )
    print(
        f"Only Charlie has: "
        f"{player3.difference(player1.union(player2, player4))}"
    )
    print(
        f"Only Dylan has: "
        f"{player4.difference(player1.union(player2, player3))}\n"
    )


def ft_achievement_tracker() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice achievements: {alice}")
    print(f"Player Bob achievements: {bob}")
    print(f"Player Charlie achievements: {charlie}")
    print(f"Player Dylan achievements: {dylan}\n")

    print("=== Achievement Analytics ===")

    all_ach = unique_achievements(alice, bob, charlie, dylan)

    print(
        f"Common to all players: "
        f"{alice.intersection(bob, charlie, dylan)}\n"
    )

    rare_achievements(alice, bob, charlie, dylan)

    print(f"Alice is missing: {all_ach.difference(alice)}")
    print(f"Bob is missing: {all_ach.difference(bob)}")
    print(f"Charlie is missing: {all_ach.difference(charlie)}")
    print(f"Dylan is missing: {all_ach.difference(dylan)}")


if __name__ == "__main__":
    ft_achievement_tracker()