import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 2024, ["Adventure"])
        self.regular_movie = Movie("CitizenFour", 2014, ["Documentary"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Children"])


    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_amount(self):
        self.c.add_rental(Rental(self.new_movie, 1))
        self.assertEqual(3.00, self.c.get_total_amount())
        self.c.add_rental(Rental(self.regular_movie, 10))
        self.assertEqual(17.00, self.c.get_total_amount())
        self.c.add_rental(Rental(self.childrens_movie, 4))
        self.assertEqual(20.00, self.c.get_total_amount())

    def test_get_rental_points(self):
        self.c.add_rental(Rental(self.new_movie, 1))
        self.assertEqual(1, self.c.get_total_rental_points())
        self.c.add_rental(Rental(self.regular_movie, 10))
        self.assertEqual(2, self.c.get_total_rental_points())
        self.c.add_rental(Rental(self.childrens_movie, 4))
        self.assertEqual(3, self.c.get_total_rental_points())
