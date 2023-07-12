class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1:
            raise Exception
        self._name = name
        self._reviews = []
        Restaurant.all_restaurants.append(self)

    @property
    def name(self):
        return self._name

    def add_review(self, review):
        self._reviews.append(review)

    def customers(self):
        return [review.customer for review in self._reviews]

    def reviews(self):
        return self._reviews

    def average_star_rating(self):
        return sum([review.rating for review in self._reviews]) / len(self._reviews)

    @classmethod
    def get_all_restaurants(cls):
        return cls.all_restaurants
