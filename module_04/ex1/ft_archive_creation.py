if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    try:
        file_name = "new_discovery.txt"
        print(f"Initializing new storage unit: {file_name}")
        file = open("./new_discovery.txt", "w")
        print("Storage unit created successfully")
        print()
        print("Inscribing preservation data...")
        file.write("[ENTRY 001] New quantum algorithm discovered")
        print("[ENTRY 001] New quantum algorithm discovered")
        file.write("\n[ENTRY 002] Efficiency increased by 347%")
        print("[ENTRY 002] Efficiency increased by 347%")
        file.write("\n[ENTRY 003] Archived by Data Archivist trainee")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        file.close()
        print("\nData inscription [SUCCESSFULL], Storage unit sealed.")
        print(f"Archive {file_name} ready for long-term preservation !")
    except PermissionError:
        print("Error: Permission Denied !")
    except Exception as e:
        print(e)
