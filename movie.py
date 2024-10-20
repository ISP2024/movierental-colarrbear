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

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
