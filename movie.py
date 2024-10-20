import csv
from typing import Collection
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """A movie available for rent."""
    title: str
    year: int
    genres: Collection[str]

    def get_title(self) -> str:
        """Return the title of this movie."""
        return self.title

    def is_genre(self, input_genre: str) -> bool:
        """Return True if the input genre is in the list of genres."""
        return input_genre.lower() in (genre.lower() for genre in self.genres)

    def __str__(self) -> str:
        """Return a string representation of this movie."""
        return f'{self.title} ({self.year})'


class MovieCatalog:
    """A collection of movies."""
    __instance = None
    _movies = []

    def __new__(cls):
        """Singleton pattern to ensure only one MovieCatalog instance."""
        if not cls.__instance:
            cls.__instance = super(MovieCatalog, cls).__new__(cls)
            cls.__instance.__load_movies('movies.csv')
        return cls.__instance

    def __load_movies(self, filename: str):
        """Load movies from the CSV file."""
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # reading line by line
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
        """Return the movie with the given title and year, if it exists."""
        try:
            for movie in self._movies:
                if movie.title.lower() == title.lower() and (
                        year is None or movie.year == year):
                    return movie
        except AttributeError:
            return None
