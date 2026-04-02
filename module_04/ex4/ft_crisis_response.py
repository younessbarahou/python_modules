def crisis_handler(file_name: str) -> None:
    try:
        with open(file_name) as file_1:
            print(f"Archive Recovered - ''{file_1.read()}''")
            print("Status: Normal operations resumed")
    except FileNotFoundError:
        print("Response: Archive not found in storage")
        print("Status: Crisis handled, system stable")
    except PermissionError:
        print("Response: Security protocols deny access")
        print("Status: Crisis handled, security maintained")
    except Exception as e:
        print(f"Response: {e}")
        print("Status: Crisis handled, system maintained")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis_handler("lost_archives.txt")
    print()
    print("CRISIS ALERT: Attempting acces to 'classified_vault'...")
    crisis_handler("classified_vault.txt")
    print()
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    crisis_handler("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")
