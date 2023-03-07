class Car:
    # What is SELF in Python? SELF represents the instance of class.
    # This handy keyword allows you to access variables, attributes
    # ,and methods of a defined class in Python

    # The __init__ method lets the class initialize the
    # object's attributes and serves no other purpose. It is only used within classes

    wheels = 4 #class variable



    def __init__(self,make,model,year,color):

        self.make = make # instance variable
        self.model = model # instance variable
        self.year = year # instance variable
        self.color = color # instance variable

    def drive(self):
        print("This "+self.model+ " is driving")

    def stop(self):
        print("This "+ self.model+ " is stopped")