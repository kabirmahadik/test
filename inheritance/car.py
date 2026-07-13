class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def start(self):
        print(self.brand, self.model, "has started.")

    def stop(self):
        print(self.brand, self.model, "has stopped.")

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Color :", self.color)
        print("Price :", self.price)


car1 = Car("Toyota", "Fortuner", "Black", 4500000)
car2 = Car("BMW", "X5", "White", 9500000)

car1.display()
car1.start()

print("-" * 30)

car2.display()
car2.start()
car2.stop()