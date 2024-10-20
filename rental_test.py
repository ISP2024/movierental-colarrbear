import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        """Create some movies for testing"""
        # self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
        # self.regular_movie = Movie("Air", Movie.REGULAR)
        # self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)
        self.new_movie = Movie("Dune: Part Two", 2024, ["Adventure"])
        self.regular_movie = Movie("Air", 2021, ["Drama"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Childrens"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2021, ["Drama"])
        self.assertEqual("Air", m.get_title())
        self.assertTrue(m.is_genre("Drama"))
        self.assertFalse(m.is_genre("Action"))

    def test_rental_price(self):
        """Test the price calculation for each movie type"""
        # new release
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        # regular movie
        rental = Rental(self.regular_movie, 10)
        self.assertEqual(rental.get_price(), 14.0)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        # childrens movie
        rental = Rental(self.childrens_movie, 10)
        self.assertEqual(rental.get_price(), 12.0)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)

    def test_rental_points(self):
        """Test the frequent renter points calculation for each movie type"""
        # new release: 1 point per day rented
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)

        # regular movie: 1 point per rental
        rental = Rental(self.regular_movie, 10)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_rental_points(), 1)

        # childrens movie: 1 point per rental
        rental = Rental(self.childrens_movie, 10)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)
