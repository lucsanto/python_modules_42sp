
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
    ]
    print(f"Initial list of players: {players}")

    capitalized_list = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized_list}")

    capitalized_only = [p for p in players if p == p.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}\n")

    score_dict = {p: random.randrange(0, 1000) for p in capitalized_list}
    print(f"Score dict: {score_dict}")

    if len(score_dict) == 0:
        print("No players to analyze")
        return

    score_average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(score_average, 2)}")

    high_scores = {p: s for p, s in score_dict.items() if s > score_average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
