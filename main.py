# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer


def make_movies():
    """Some sample movies."""
    movie_catalog = MovieCatalog()
    movies = [
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
    movies = make_movies()  # Store all movies in a list

    for index, movie in enumerate(movies):
        if movie:
            customer.add_rental(Rental(movie, days))
            days = (days + 2) % 5 + 1
        else:
            print(
                f"Movie '{['Air', 'Oppenheimer', 'Frozen', 'Bitconned', 'Particle Fever'][index]}' not found in catalog.")
    print(customer.statement())
