import sys
import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    base_coords = (0, 0, 0)
    coords_1 = (10, 20, 5)
    print(f"Position Created: {coords_1}")
    factor_1 = (coords_1[0] - base_coords[0]) ** 2
    factor_2 = (coords_1[1] - base_coords[1]) ** 2
    factor_3 = (coords_1[2] - base_coords[2]) ** 2
    distance_1 = float(math.sqrt(factor_1 + factor_2 + factor_3))
    print(f"Distance between {base_coords} and {coords_1} : {distance_1:.2f}")
    print()
    final_coords = []
    try:
        args_cte = 0
        """Iterate over each element in argv"""
        for arg in sys.argv:
            if args_cte == 0:
                args_cte += 1
                continue
            splitted = arg.split(',')
            split_cte = 0
            """Iterate over each element in the argument itself"""
            for i in splitted:
                split_cte += 1
            """Checks the argument length"""
            if split_cte != 3:
                raise ValueError("Coordinates should be (x,y,z)!")
            split_cte = 0
            while split_cte < 3:
                splitted[split_cte] = int(splitted[split_cte])
                split_cte += 1
            splitted = tuple(splitted)
            final_coords += [splitted]
            element_1 = (splitted[0] - base_coords[0]) ** 2
            element_2 = (splitted[1] - base_coords[1]) ** 2
            element_3 = (splitted[2] - base_coords[2]) ** 2
            distance = float(math.sqrt(element_1 + element_2 + element_3))
            args_cte += 1
            print()
            print(f'Parsing coordinates: "{arg}"')
            print(f"Parsed position: {splitted}")
            s = splitted
            print(f"Distance between {base_coords} and {s}:{distance:.1f}")
            print()
        if args_cte == 1:
            print("No Coordinates Provided !")
            print("Hint => python3 <file.py> <coords1> ...")
            print()
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print("Error details:")
        print(f"-> Type: ValueError, Args: {e} (3 numbers)")
        print()
    print("Unpacking demonstration:")
    if args_cte == 1:
        print("No Coordinates Provided for unpacking!")
    for coordinates in final_coords:
        x = coordinates[0]
        y = coordinates[1]
        z = coordinates[2]
        print(f"Player at x={x}, y={y}, z={z}")
        (xx, yy, zz) = coordinates
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
        print()
