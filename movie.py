import csv
from pricing import NewRelease, RegularPrice, ChildrensPrice
from typing import Collection
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genres: Collection[str]

    def get_title(self) -> str:
        return self.title

    def is_genre(self, input_genre: str) -> bool:
        return input_genre.lower() in (genre.lower() for genre in self.genres)

    def __str__(self) -> str:
        return f'{self.title} ({self.year})'


class MovieCatalog:
    """
    A collection of movies.
    """
    _instance = None
    _movies = []

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance._load_movies('movies.csv')
        return cls._instance

    def _load_movies(self, filename: str):
        """Load movies from the CSV file."""
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            next(reader)
            for _, movie_data in enumerate(reader):
                try:
                    movie = Movie(
                        movie_data['title'],
                        int(movie_data['year']),
                        movie_data['genres'].split('|')
                    )
                    self._movies.append(movie)
                except (TypeError, ValueError):
                    continue

            return self._movies

    def get_movie(self, title, year=None):
        try:
            for movie in self._movies:
                if movie.title.lower() == title.lower() and (
                        year is None or movie.year == year):
                    return movie
        except AttributeError:
            return None
