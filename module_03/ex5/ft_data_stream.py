def events_processor(data: list[dict]) -> None:
    for player in data:
        name = player["player"]
        event_type = player["event_type"]
        level = player["data"]["level"]
        yield ([name, event_type, level])


def is_prime(numb: int) -> bool:
    i = 2
    while i ** 2 <= numb:
        if i != numb and numb % i == 0:
            return (False)
        i += 1
    return (True)


def prime(n: int) -> None:
    j = 2
    for _ in range(n):
        while j >= 0:
            if is_prime(j) is False:
                j += 1
                continue
            else:
                yield (j)
                j += 1
                break


def fibo(n: int) -> None:
    a = 0
    b = 1
    current = None
    yield (a)
    yield (b)
    for _ in range(0, n - 2):
        current = a + b
        a = b
        b = current
        yield (current)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    process = events_processor([{
        'id': 1,
        'player': 'frank',
        'event_type': 'login',
        'timestamp': '2024-01-01T23:17',
        'data': {
            'level': 16,
            'score_delta': 128,
            'zone': 'pixel_zone_2'
            }
        }])
    index = 1
    total_events = 0
    high_level = 0
    treasure = 0
    level_up = 0
    for data in process:
        total_events += 1
        if data[2] > 10:
            high_level += 1
        if data[1] == "treasure":
            treasure += 1
        if data[1] == "level_up":
            level_up += 1
        print(f"Event {index}: {data[0]}-{data[1]}")
        index += 1
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: Fast")
    print()
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):")
    fibo_seq = fibo(10)
    for num in fibo_seq:
        print(num)
    print("Prime numbers (first 5):")
    primes = prime(5)
    for num in primes:
        print(num)
