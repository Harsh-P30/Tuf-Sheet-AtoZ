num = input("Enter a number: ")
print("You entered:", num)
string = input("Enter a string: ")
print("You entered:", string)
# The input() function always returns a string, so if you want to work with numbers, you need to convert the input to the appropriate type.
num = int(input("Enter a number: "))
print("You entered:", num)
# You can also use float() to convert to a floating-point number.
num = float(input("Enter a number: "))
print("You entered:", num)
# If you want to take multiple inputs in one line, you can use the split() method.
num1, num2 = input("Enter two numbers separated by space: ").split()
num1 = int(num1)
num2 = int(num2)
print("You entered:", num1, "and", num2)