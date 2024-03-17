# import contextlib

# with contextlib.suppress(ValueError):
#     # Code block where ValueError may occur
#     value = int(input("Enter a number: "))  # This may raise ValueError
#     print("hi")
#     print("You entered:", value)
    
from abc import ABC, abstractmethod

# Top level abstract class specifying abstract methods
class AbstractClass(ABC):
    @abstractmethod
    def method1(self):
        pass
    
    @abstractmethod
    def method2(self):
        pass

# Middle level specifying the constructor
class MiddleClass(AbstractClass):
    # @abstractmethod
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

# Bottom level implementing the abstract methods
class BottomClass(MiddleClass):
    def method1(self):
        print("Implementation of method1 in BottomClass")
    
    def method2(self):
        print("Implementation of method2 in BottomClass")

# Example usage
obj = BottomClass("arg1_value", "arg2_value")
obj.method1()
obj.method2()

obj = MiddleClass("arg1_value", "arg2_value")
# obj.