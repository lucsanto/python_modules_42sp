import sys

if __name__ == "__main__":
    numbers = []

    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        for arg in sys.argv[1:]:
            try:
                numbers.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")

        if len(numbers) == 0:
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            print(f"Scores processed: {numbers}")
            print(f"Total players: {len(numbers)}")
            print(f"Total score: {sum(numbers)}")
            print(f"Average score: {sum(numbers) / len(numbers)}")
            print(f"High score: {max(numbers)}")
            print(f"Low score: {min(numbers)}")
            print(f"Score range: {max(numbers) - min(numbers)}")