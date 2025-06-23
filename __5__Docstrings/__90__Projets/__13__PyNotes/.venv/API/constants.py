from pathlib import Path
import os

NOTES_DIR = os.path.join(Path.home(), ".notes")

if __name__ == "__main__":
    print(NOTES_DIR)
    print(type(NOTES_DIR))