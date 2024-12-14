#functions inside a class are methods 'self'
class   Calculator:
    val = 44  #class variable
    #selgf defines object
    # def __init__(self):
    #     print("I am a constructor, called automatically when object is created")
    
    #parameterised
    def __init__(self,a,b):
        self.first_num = a    #first num and sec num are instance variables
        self.sec_num = b
        
    def sum(self,a,b):
        return f"sum of {a} and {b}  is {a+b}"
    '''The self parameter allows the method to access the instance's attributes and 
    other methods.Without self,Python doesn't know the method belongs
    to the instance, leading to an error.'''
    
    def summation(self):
        return self.first_num + self.sec_num + Calculator.val
    
#creating an object to the class
# obj = Calculator()

obj = Calculator(5,7) 
print(obj.sum(3,4))
print(obj.val)   
print(obj.summation())


    
    