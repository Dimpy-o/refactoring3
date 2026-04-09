class Product:
    def __init__(self, product_id, name, price):
        self._id = product_id
        self._name = name
        self._price = price

    def get_price(self):
        return self._price


class Order:
    def __init__(self, order_id):
        self._id = order_id
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)

    def calculate_total(self):
        return sum(p.get_price() for p in self._products)
    
    @property
    def products(self):
        return self._products


class User:
    def __init__(self, user_id, username, password):
        self._id = user_id
        self._username = username
        self._password = password
        self._orders = []

    def register(self):
        return f"User {self._username} registered"

    def login(self, password):
        return self._password == password

    def add_order(self, order):
        self._orders.append(order)

    def view_orders(self):
        return self._orders
    
    @property
    def orders(self):
        return self._orders
