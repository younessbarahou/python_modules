if __name__ == "__main__":
    players = {
        'alice':
        {
            "score": 2300,
            "active": True,
            "achievement": "Gold",
            "region": "north"
        },
        'bob':
        {
            "score": 1800,
            "active": False,
            "achievement": "Bronze",
            "region": "east"
        },
        'charlie':
        {
            "score": 2150,
            "active": True,
            "achievement": "Bronze",
            "region": "west"
        },
        'diana':
        {
            "score": 2050,
            "active": False,
            "achievement": "Iron",
            "region": "west"
        },
        'eve':
        {
            "score": 1500,
            "active": True,
            "achievement": "Gold",
            "region": "south"
        },
        'max':
        {
            "score": 2900,
            "active": False,
            "achievement": "Steel",
            "region": "north"
        },
    }
    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")
    high_scorers = [p["score"] for p in players.values() if p["score"] > 2000]
    scores_doubled = [p["score"] * 2 for p in players.values()]
    act = "active"
    active_players = [p for p in players.keys() if players[p][act] is True]
    print(f"High scorers: {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_regions = {players[x]["region"] for x in players.keys()}
    unique_achievements = {x["achievement"] for x in players.values()}
    print(f"unique regions: {unique_regions}")
    print(f"unique achievements: {unique_achievements}")
    print()
    print("=== Dict Comprehension Examples ===")
    scores = {x: players[x]["score"] for x in players.keys()}
    ach = "achievement"
    categories = {
        "Gold": sum(1 for x in players.values() if x[ach] == "Gold"),
        "Iron": sum(1 for x in players.values() if x[ach] == "Iron"),
        "Steel": sum(1 for x in players.values() if x[ach] == "Steel"),
        "Bronze": sum(1 for x in players.values() if x[ach] == "Bronze")
    }
    infos = {x: sum(1 for x in players[x]) for x in players.keys()}
    print(f"Player scores: {scores}")
    print(f"Achievement categories: {categories}")
    print(f"infos count: {infos}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    scores_sum = [x["score"] for x in players.values()]
    print(f"Average score: {sum(scores_sum) / len(scores_sum):.2f}")
    print(f"Top performer: {max(scores)}")
