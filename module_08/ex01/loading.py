def check_dependencies() -> None:
    check_flag = True
    try:
        # package import
        import pandas
        # package version [if found]
        print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
    except ModuleNotFoundError:
        check_flag = False
        print("[FAIL] pandas not found")
    try:
        # package import
        import numpy
        # package version [if found]
        print(f"[OK] numpy {numpy.__version__} - Network access ready")
    except ModuleNotFoundError:
        check_flag = False
        print("[FAIL] numpy not found")
    try:
        # package import
        import matplotlib
        from matplotlib import pyplot
        # package version [if found]
        print(
            f"[OK] matplotlib {matplotlib.__version__} - Visualisation ready"
            )
    except ModuleNotFoundError:
        check_flag = False
        print("[FAIL] matplotlib not found")
    if check_flag is False:
        print("\n Installation: \n1: Pip => pip install -r ./requirements.txt")
        print("2: Poetry => poetry install")
    else:
        print("Analyzing Matrix data...")
        # creating a data frame using pandas with a matrix sample
        data_frame = pandas.DataFrame([[1, 2, 3, 4], [5, 6, 8, 11]])
        print("Processing some points...")
        print(numpy.square(data_frame))
        print("Generating visualisation...")
        row_1 = data_frame.iloc[0]
        row_2 = data_frame.iloc[1]
        # making a barchart using matplotlib pyplot
        pyplot.bar(row_1, row_2, color='green')
        pyplot.title("Bar Plot")
        # saving the chart as a png file
        pyplot.savefig("matrix_analysis.png")
        print("Analysis complete!")
        print("Results saved to: matrix/analysis.png")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    check_dependencies()
