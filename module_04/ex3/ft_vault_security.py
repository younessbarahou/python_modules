if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    try:
        with open("classified_data.txt", "r") as file_1:
            print("SECURE EXTRACTION:")
            print(file_1.read())
    except FileNotFoundError:
        print("Error: File Not found")
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(e)
    print()
    try:
        with open("security_protocols.txt", "w") as file_2:
            print("SECURE PRESERVATION:")
            data = "[CLASSIFIED] New security protocols archived"
            file_2.write(data)
            print(data)
            print("Vault automatically sealed upon completion")
    except PermissionError:
        print("Error: Permission Denied")
    except Exception as e:
        print(e)
    print()
    print("All vault operations completed with maximum security.")
