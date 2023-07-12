class Customer:
    all_customers = []

    def __init__(self, first_name, last_name):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise Exception
        if not (1 <= len(first_name) <= 25) or not (1 <= len(last_name) <= 25):
            raise Exception
        self._first_name = first_name
        self._last_name = last_name
        self._reviews = []
        Customer.all_customers.append(self)

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def add_review(self, review):
        self._reviews.append(review)

    def restaurants(self):
        return [review.restaurant for review in self._reviews]

    def reviews(self):
        return self._reviews

    def num_reviews(self):
        return len(self._reviews)
