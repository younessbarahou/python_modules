import sys
import os

if __name__ == "__main__":
    # Comparaison between the base prefix and the prefix
    if sys.base_prefix == sys.prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        # print interpretor location
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None Detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        # to initialize a virtual environement (UNIX)
        print("python -m venv matrix_env")
        # to activate the virtual environement (UNIX)
        print("source matrix_env/bin/activate # On Unix")
        # to initialize a virtual environement (WINDOWS)
        print("matrix_env")
        print("Scripts")
        # to activate the virtual environement (WINDOWS)
        print("activate # On Windows")
        print("Then run this program again.")
    else:
        print("\nMATRIX STATS: Welcome to the construct\n")
        # print interpreter location
        print(f"Current Python: {sys.executable}")
        # print venv name
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        # print the venv full path
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affectin the global system.")
        print()
        print("Package installation path:")
        # print the package installation path for the virtual environement
        print(sys.path[len(sys.path) - 1])
