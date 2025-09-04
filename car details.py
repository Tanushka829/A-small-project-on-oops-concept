class car():
    def __init__(self):
        name = str(input("enter owner name:"))
        age = int(input("enter age:"))
        print("Name of owner:",name,"\nAge of owner:", age)

    def car_details(self):
        brand = str(input("enter brand name:"))
        price = float(input("enter price of car in lakh:"))
        print("car details are:")
        print("brand:",brand," and price(in lakh):",price)
# we cant use name and age after 2nd def they both have different area

car1=car()
car1.car_details()
# perfect

