from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days

    def get_price(self, days):
        """return rental price for a new release"""
        return 3.0 * days


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_rental_points(self, days):
        """Regular rentals earn 1 point regardless of days rented."""
        return 1

    def get_price(self, days):
        """Regular rentals cost $2 for the first 2 days, then $1.5 per day."""
        if days <= 2:
            return 2.0
        return 2.0 + (days - 2) * 1.5


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children's movies."""

    def get_rental_points(self, days):
        """Children's rentals earn 1 point regardless of days rented."""
        return 1

    def get_price(self, days):
        """Children's rentals cost $1.5 for the first 3 days, then $1.5 per day."""
        if days <= 3:
            return 1.5
        return 1.5 + (days - 3) * 1.5
