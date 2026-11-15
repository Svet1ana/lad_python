from typing import Generator
from itertools import chain


def squares(number: int) -> Generator[int]:
    for num in range(number):
        yield num * num

def read_lines(filename: str) -> Generator[str, None, None]:
    with open(filename, encoding="utf-8") as f:
        for line in f:
            yield line


if __name__ == '__main__':
    for numb in squares(5):
        print(numb)
    print(list(squares(10)))


    with open("big.log", "w", encoding="utf-8") as f:
        for num in squares(100):
            f.write(f"SQUARE {num}\n")


    for line in read_lines("big.log"):
        if "18" in line:
            print(line)

    list_1 = list(squares(4))
    list_2 = tuple(squares(5))
    list_3 = list("squares(15)")

    for element in chain(list_1, list_2, list_3):
        print(element)