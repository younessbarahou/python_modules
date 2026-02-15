def recursive(days, i):
    if (i >= days):
        return
    else:
        print(f"day {i + 1}")
        recursive(days, i + 1)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive(days, 0)
    print("Harvest time!")
