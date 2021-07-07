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
    
    def add(self, num1:float, num2:float = None):
        """ Takes in a number num1, returns the sum of num1 and memory if num2 = None,
        else return the sum of num1 and num2"""
        if num2 == None:
            result = self.__memory + num1
            self.__memory = result
            return result
        else:
            result = num1 + num2
            self.__memory = result
            return num1 + num2

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

calculator = Calculator()
res = calculator.add(9,9)
print(res)