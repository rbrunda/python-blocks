class Card:
    def __init__(self, imageUrl, deviceType, price, rating):
        self.imageUrl = imageUrl
        self.deviceType = deviceType
        self.price = price
        self.rating = rating


Product1 = Card("Dummy-url 1", "Mobile", 56000, 4.5)
Product2 = Card("Dummy-url 2", "Laptop", 94000, 4.8)
Product3 = Card("Dummy-url 3", "Smart-watch", 18000, 3.5)


print("Product - 1 :")
print("imageUrl:", Product1.imageUrl)
print("deviceType:", Product1.deviceType)
print("price:", Product1.price)
print("rating:", Product1.rating)
print()

print("Product - 2 :")
print("imageUrl:", Product2.imageUrl)
print("deviceType:", Product2.deviceType)
print("price:", Product2.price)
print("rating:", Product2.rating)
print()

print("Product - 3 :")
print("imageUrl:", Product3.imageUrl)
print("deviceType:", Product3.deviceType)
print("price:", Product3.price)
print("rating:", Product3.rating)
