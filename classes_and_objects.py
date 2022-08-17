# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "Car"
    color = ""
    value = 100.00

    def description_percent_operator(self):
        desc_str = "%s is a %s %s worth $%s"%(self.name, self.color, self.kind, self.value)
        return desc_str


# I've added a second vehicle class, which uses the initializer and f-strings. - Andrew.
class VehicleTwo:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description_f_string(self):
        desc_str = f"{self.name} is a {self.color} {self.kind} worth ${self.value}"
        return desc_str


# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.000

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

car3 = VehicleTwo("Sarge", "Jeep Wrangler", "Green", 52000.00)

# test code
print(car1.description_percent_operator())
print(car2.description_percent_operator())
print(car3.description_f_string())
