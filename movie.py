# from pricing import PriceStrategy, NewRelease, RegularPrice, ChildrensPrice
from typing import Collection
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def get_title(self) -> str:
        return self.title

    def is_genre(self, input_genre: str) -> bool:
        return input_genre.lower() in self.genre

    def __str__(self) -> str:
        return f'{self.title} ({self.year})'
