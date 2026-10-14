
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


def gen_player_achievements() -> set[str]:
    amount = random.randint(5, 10)
    return set(random.sample(ACHIEVEMENTS, amount))


def unique_achievements(
    player1: set[str], player2: set[str],
    player3: set[str], player4: set[str]
) -> set[str]:
    unique_ach = player1.union(player2, player3, player4)
    print(f"All distinct achievements: {unique_ach}")
    print(f"Total unique achievements: {len(unique_ach)}\n")
    return unique_ach


def rare_achievements(
    player1: set[str], player2: set[str],
    player3: set[str], player4: set[str]
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
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    print("=== Achievement Analytics ===")

    unique_achievements(alice, bob, charlie, dylan)
    print(
        "Common achievements: "
        f"{alice.intersection(bob, charlie, dylan)}\n"
    )

    rare_achievements(alice, bob, charlie, dylan)

    all_ach = set(ACHIEVEMENTS)
    print(f"Alice is missing: {all_ach.difference(alice)}")
    print(f"Bob is missing: {all_ach.difference(bob)}")
    print(f"Charlie is missing: {all_ach.difference(charlie)}")
    print(f"Dylan is missing: {all_ach.difference(dylan)}")


if __name__ == "__main__":
    ft_achievement_tracker()
