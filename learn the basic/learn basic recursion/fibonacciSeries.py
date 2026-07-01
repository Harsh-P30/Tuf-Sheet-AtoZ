# Fibonacci series
# value = (n-1) + (n-2)
n = int(input("Enter a number: "))
a = 0
b =1 
print(a,b)

while n > 0:
    print(a+b)

    a,b = b , a+b
    # c = b
    # b = a+b
    # a = c
    n =n-1
