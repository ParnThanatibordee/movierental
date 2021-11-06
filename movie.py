from enum import Enum


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 2.0 + (1.5 * (days - 2)) if (days > 2) else 2.0,
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 + (1.5 * (days - 3)) if (days > 3) else 1.5,
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def frequent(self, days: int) -> float:
        "Return the frequent renter points for a given number of days"""
        frequent = self.value["frp"]
        return frequent(days)


class Movie:
    """A movie available for rent."""

    def __init__(self, title):
        # Initialize a new movie.
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
