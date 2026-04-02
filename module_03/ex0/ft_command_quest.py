import sys

if __name__ == "__main__":
    print("== Command Quest ==")
    if len(sys.argv) == 1:
        print("No arguments provided !")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        index = 1
        total_size = len(sys.argv)
        while index <= total_size - 1:
            print(f"Argument {index} : {sys.argv[index]}")
            index += 1
        print(f"Total arguments: {total_size}")
