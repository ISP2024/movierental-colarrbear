# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer

from pricing import PriceStrategy, NEW_RELEASE


def make_movies():
    """Some sample movies."""
    movie_catalog = MovieCatalog()
    movies = [
        # Movie("Air", Movie.NEW_RELEASE),
        # Movie("Oppenheimer", Movie.REGULAR),
        # Movie("Frozen", Movie.CHILDRENS),
        # Movie("Bitconned", Movie.NEW_RELEASE),
        # Movie("Particle Fever", Movie.REGULAR)
        movie_catalog.get_movie("Air"),
        movie_catalog.get_movie("Oppenheimer"),
        movie_catalog.get_movie("Frozen"),
        movie_catalog.get_movie("Bitconned"),
        movie_catalog.get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        if movie:
            customer.add_rental(Rental(movie, days))
            days = (days + 2) % 5 + 1
        else:
            print(f"Movie not found in catalog.")
    print(customer.statement())

    # to check it get the movie or not
    # Get the Singleton Movie Catalog
    # catalog = MovieCatalog()
    # # Get the first movie named 'Mulan'
    # # movie = catalog.get_movie("Mulan")
    # # # Get 'Mulan' released in 1998
    # # old_movie = catalog.get_movie("Mulan", 1998)
    # # print(movie)
    # # print(old_movie)
    # movie = catalog.get_movie("Top Gun: Maverick")
    # # print(movie)
    # days = 4
    # price_code = NEW_RELEASE  # or PriceStrategy.NEW_RELEASE
    # rental = Rental(movie, days)
    # print(rental.get_movie())
    # print(rental.get_price())
