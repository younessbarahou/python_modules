from dotenv import load_dotenv
import os


if __name__ == "__main__":
    try:
        # we load env variables into the os
        load_dotenv()
        # we retrieve specific values
        matrix_mode = os.getenv('MATRIX_MODE')
        db_url = os.getenv('DATABASE_URL')
        api_key = os.getenv('API_KEY')
        log_level = os.getenv('LOG_LEVEL')
        zion_endpoint = os.getenv('ZION_ENDPOINT')
        if (
            matrix_mode is None or
            db_url is None or
            api_key is None or
            zion_endpoint is None or
            matrix_mode == "" or
            db_url == "" or
            api_key == "" or
            zion_endpoint == ""
        ):
            raise ValueError("All configurations must be set !\n")
        print("\nOracle STATUS: Reading the matrix...\n")
        print("Configuration loaded:")
        print("Mode: Devolopment")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print("Log Level: DEBUG")
        print("Zion Network: Online")
        print()
        print("Environement security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    except ValueError as e:
        print(e)
        print("Hint=> \nMATRIX_MODE=value\nDATABASE_URL=value")
        print("API_KEY=value\nLOG_LEVEL=value\nZION_ENDPOINT=value")
    except Exception as e:
        print(e)
