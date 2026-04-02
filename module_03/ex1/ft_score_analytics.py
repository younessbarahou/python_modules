import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argv_size = len(sys.argv)
    if argv_size == 1:
        print("No Scores Provided!")
        print("Hint => python3 ft_score_analytics.py <score1> ...")
    else:
        try:
            players_scores = []
            index = 1
            while index < argv_size:
                players_scores += [int(sys.argv[index])]
                index += 1
            avg = sum(players_scores) / len(players_scores)
            print(f"Scores processed: {players_scores}")
            print(f"Total Players: {len(players_scores)}")
            print(f"Total score: {sum(players_scores)}")
            print(f"Average score: {avg}")
            print(f"High score: {max(players_scores)}")
            print(f"Low score: {min(players_scores)}")
            print(f"Score range: {max(players_scores) - min(players_scores)}")
            print()
        except ValueError:
            print("Invalid Score ! Hint => Add Valid Numeric Scores Only")
