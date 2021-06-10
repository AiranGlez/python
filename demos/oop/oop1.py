class Car():

    chassislenght = 250        #This are the properties of the class
    chassiswidth = 250
    wheels = 4
    moving = False

    def startup(self):        #This is a method of the class. 'Self' it is a reference to the instanced object of the class
        self.moving = True

    def status(self):
        if self.moving:
            return "My car is moving"
        else:
            return "My car is stopped"


myCar = Car()                 #Here we create an instance of the class

print("Length of my car is", myCar.chassislenght)

print("My car has", myCar.wheels, "wheels")

myCar.startup()

print(myCar.status())

