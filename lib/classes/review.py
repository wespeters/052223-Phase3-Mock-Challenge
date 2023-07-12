from .customer import Customer
from .restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        if not isinstance(customer, Customer) or not isinstance(restaurant, Restaurant):
            raise Exception
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise Exception
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        self._customer.add_review(self)
        self._restaurant.add_review(self)
        Review.all_reviews.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def restaurant(self):
        return self._restaurant

    @property
    def rating(self):
        return self._rating
