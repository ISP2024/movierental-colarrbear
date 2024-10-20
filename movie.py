from pricing import PriceStrategy, NewRelease, RegularPrice, ChildrensPrice
from typing import Collection


class Movie:
    """
    A movie available for rent.
    """

    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title: str, year: int, genre: Collection[str]):
        """Initialize a new movie."""
        self.title = title
        self.year = year
        self.genre = genre

    def get_title(self) -> str:
        return self.title

    def is_genre(self, input_genre: str) -> bool:
        return input_genre.lower() in self.genre

    def __str__(self) -> str:
        return f'{self.title} ({self.year})'
