if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    try:
        file_name = "ancient_fragment.txt"
        file = open(file_name, "r")
        print(f"Accessing Vault: {file_name}")
        print("Connection established...")
        print()
        content = file.read()
        print("RECOVERED DATA:")
        print(content)
        print()
        print("Data Recovery Complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("Error: Storage vault not found")
    except PermissionError:
        print("Error: Permission Denied")
    except Exception as e:
        print(e)
