from pricing import PriceStrategy, NewRelease, RegularPrice, ChildrensPrice


class Movie:
    """
    A movie available for rent.
    """

    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title: str, price_strategy: PriceStrategy):
        """Initialize a new movie."""
        self.title = title
        self.price_strategy = price_strategy  # get_price_code
        # self.price_code = price_strategy

    def get_price_code(self):
        return self.price_strategy

    # def get_rental_points(self, days_rented: int):
    #     """Get the rental points for renting this movie for a number of days."""
    #     return self.price_strategy.get_rental_points(days_rented)
    #
    # def get_price(self, days: int):
    #     """Get the price for renting this movie for a number of days."""
    #     return self.price_strategy.get_price(days)

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
