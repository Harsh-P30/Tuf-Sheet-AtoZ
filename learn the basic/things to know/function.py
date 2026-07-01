# Python Functions
# A function is a block of code which only runs when it is called.

# A function can return data as a result.
# The code inside the function must be indented. Python uses indentation to define code blocks.
# A function helps avoiding code repetition.

def sayHello(name): # function definition (name is argument) 
    print("Hello " + name)

sayHello("harsh") # calling the function , (harsh is parameter)


# *args and **kwargs
# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args

# If you do not know how many arguments will be passed into your function, add a * before the parameter name.

def multipleargument(*args):
    print(args)

multipleargument(1,2,3,4,5)


# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, 
# add two asterisks ** before the parameter name. the function will receive a dictionary of arguments 
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")