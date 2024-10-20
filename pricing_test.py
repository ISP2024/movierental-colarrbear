import unittest
from rental import Rental
from movie import Movie
from datetime import datetime
from pricing import NewRelease, RegularPrice, ChildrensPrice


class RentalTest(unittest.TestCase):
    """Test that it returns the correct price strategy for each type of movie."""

    def test_new_release_movie(self):
        """Test that a new release movie returns the correct price strategy."""
        this_year = datetime.now().year
        movie = Movie("Air", this_year, ["Action"])
        rental = Rental(movie, 1)
        self.assertIsInstance(rental.get_price_code(), NewRelease)

    def test_regular_movie(self):
        """Test that a regular movie returns the correct price strategy."""
        movie = Movie("Oppenheimer", 2023, ["Documentary"])
        rental = Rental(movie, 1)
        self.assertIsInstance(rental.get_price_code(), RegularPrice)

    def test_childrens_movie(self):
        """Test that a children's movie returns the correct price strategy."""
        movie = Movie("Frozen", 2023, ["Children", "Animation"])
        rental = Rental(movie, 1)
        self.assertIsInstance(rental.get_price_code(), ChildrensPrice)

        movie2 = Movie("Cinderella", 2023, ["Children", "Musical"])
        rental2 = Rental(movie2, 166)
        self.assertIsInstance(rental2.get_price_code(), ChildrensPrice)

        movie3 = Movie("Raya and the Last Dragon", 2023, ["Children", "Adventure"])
        rental3 = Rental(movie3, 28)
        self.assertIsInstance(rental3.get_price_code(), ChildrensPrice)




