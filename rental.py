from pricing import PriceStrategy, NewRelease, RegularPrice, ChildrensPrice
from datetime import datetime
from movie import Movie


def price_code_for_movie(movie: Movie) -> PriceStrategy:
    """Return the price code for a movie based on its year and genres."""
    current_year = datetime.now().year
    if movie.year == current_year:
        return NewRelease()
    elif any(genre.lower() in ["children", "childrens"] for genre in
             movie.genres):
        return ChildrensPrice()
    else:
        return RegularPrice()


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie, days_rented: int):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code_for_movie(movie)

    def get_price_code(self):
        """Return the price code for this rental."""
        return self.price_code

    def get_movie(self):
        """Return the movie for this rental."""
        return self.movie

    def get_days_rented(self):
        """Return the number of days this movie was rented."""
        return self.days_rented

    def get_price(self):
        """compute the price of the rental based on movie price code"""
        return self.price_code.get_price(self.days_rented)

    def get_rental_points(self):
        """compute the frequent renter points based on movie price code"""
        return self.price_code.get_rental_points(self.days_rented)
