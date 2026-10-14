import sys


if __name__ == "__main__":
    numbers: list[int] = []
    usage = (
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )

    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print(usage)
    else:
        for arg in sys.argv[1:]:
            try:
                numbers.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")

        if len(numbers) == 0:
            print(usage)
        else:
            total = sum(numbers)
            print(f"Scores processed: {numbers}")
            print(f"Total players: {len(numbers)}")
            print(f"Total score: {total}")
            print(f"Average score: {total / len(numbers)}")
            print(f"High score: {max(numbers)}")
            print(f"Low score: {min(numbers)}")
            print(f"Score range: {max(numbers) - min(numbers)}")
