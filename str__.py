class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString

    def __str__ (self):
        return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'


myObject = MyClass(12345, "Hello")


'''The __str__ method in Python represents the class objects as a string


The __str__ method is called when the following functions are invoked on the object and return a string:
print()
str()

If we have not defined the __str__, then it will call the __repr__ method


The __repr__ method returns a string that describes the pointer of the object by default (if the programmer does not define it).

'''


print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())