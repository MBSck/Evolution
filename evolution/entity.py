from typing import Self, Tuple


class Entity:
    def __init__(self: Self, age: int,
                 max_age: int,
                 position: Tuple[int, int],
                 color: str) -> None:
        self.age = age
        self.max_age = age
        self.position = position
        self.color = color


if __name__ == "__main__":
    ...
