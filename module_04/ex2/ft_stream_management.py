import sys


def std_in() -> str:
    archivist_id = ""
    for element in sys.stdin:
        flag = False
        for letter in element:
            if letter == '\n':
                flag = True
                break
            archivist_id += letter
        if flag is True:
            break
    return (archivist_id)


if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
        print()
        print("Input Stream active. Enter archivist ID: ", end="", flush=True)
        archivist_id = std_in()
        status_report = input("Input Stream active. Enter status report: ")
        print()
        print(f"[STANDARD] Archive from {archivist_id}: {status_report}")
        sys.stderr.write("[ALERT] Diagnostic: channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        print()
        print("Three-channel communication test successful")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(e)
