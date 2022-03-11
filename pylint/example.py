"""
Car class.
"""
#pylint: disable=too-few-public-methods
class Car:
    """
    Car class which will print color.
    """
    def __init__(self,color):
        self.color = color

MY_CAR = Car('red')
