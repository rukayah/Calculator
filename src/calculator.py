class Calculator:
    """A calculator class that performs basic operations"""
    
    def __init__(self, memory:float = 0):

        """Calculator only accept int or float type, if otherwise raise Typeerror"""
        if not isinstance(memory,(int,float)):
            raise TypeError
        self.__memory = memory
    
    @property
    def memory(self):
        return self.__memory
    
    def add(self, num:float):
        """ Takes in a number num, returns the sum of num and memory """
        self.__memory += num
        return self.__memory

    def subtract(self, num:float):
        """Takes in a number num, return the difference of memory and num"""
        self.__memory  -= num
        return self.__memory

    def multiply(self, num:float):
        """Takes in a number num, return the multiplication of memory and num"""
        self.__memory *= num
        return self.__memory

    def divide(self, num:float):
        """Takes in a number num, return the division of memory and num"""
        if num == 0:
            raise ZeroDivisionError
        self.__memory /= num
        return self.__memory
    
    def root(self, num: int):
        """Takes in a number num, return the nth root"""
        self.__memory **= (1/num)
        return self.__memory

    def reset(self):
        """Reset the memory to zero"""
        self.__memory = 0
        return self.__memory


