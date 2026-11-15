from contextlib import contextmanager
from typing import Generator


@contextmanager
def open_file(path: str, mode: str = "r") -> Generator:
    file = open(path, mode)
    try:
        yield file
    finally:
        file.close()
        print("File closed")

@contextmanager
def timer(label: str) -> None:
    import time
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: took {elapsed:0.2f}s")


if __name__ == "__main__":
    with open_file("test.txt", "w") as f:
        f.write("Hello World\n")
        f.write("Hello World 2\n")

    with open_file("test.txt", "r") as f:
        print(f.read())

    with timer("Timer wait cycle"):
        for _ in range(1_000_000):
            pass
        