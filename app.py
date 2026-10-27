
import json
import os


def load_config():
    """Load a simple configuration from an environment variable."""
    config = os.getenv("APP_CONFIG", "{}")
    return json.loads(config)


def main():
    config = load_config()
    print("RelixQ branch detection test")
    print(f"Loaded config keys: {list(config.keys())}")


if __name__ == "__main__":
    main()
