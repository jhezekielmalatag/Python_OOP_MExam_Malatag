class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")
        self._price = value

    def total(self, quantity):
        return self.price * quantity

if __name__ == "__main__":
    product = Product("Notebook", 25)
    product.price = 30
    print(product.total(3))

    try:
        product.price = 0
    except ValueError:
        print("Rejected")