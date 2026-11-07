import json
from pathlib import Path


POSTS_FILE = Path("./posts.json")


def read_posts(path: Path) -> list:
    try:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)

    except FileNotFoundError:
        print(f"File {path} doesn't exist")
        data = []

    else:
        data = data
        print(f"File {path} exists, data: {len  (data)}")

    finally:
        print(f"File {path} closed")
    return data
if __name__ == "__main__":

    read_posts(POSTS_FILE)