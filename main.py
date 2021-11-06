# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, PriceCode
from rental import Rental
from customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman", 2000, ['demo'], 'demo'),
        Movie("CitizenFour", 2000, ['demo'], 'demo'),
        Movie("Frozen", 2000, ['demo'], 'demo'),
        Movie("El Camino", 2000, ['demo'], 'demo'),
        Movie("Particle Fever", 2000, ['demo'], 'demo')
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, PriceCode.normal))
        days += 1
    print(customer.statement())
