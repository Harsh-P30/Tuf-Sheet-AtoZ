# Python does not have a traditional switch-case statement; 
# instead, 
# it uses the match-case statemen
## In a match-case statement, the case keyword expects a pattern (like a literal value, a variable to bind, or a structure), not a boolean condition.
# Use a wildcard pattern _ (or capture the variable) followed by if to check the condition.


a = int(input("enter a number"))

def arrangement(num):
    match num:
        case _ if num > 5:
            print(" Enter number is more than 5.")
        
        case _ if num < 5:
            print("enter number is less than 5.")
        
        case _:
            print("number is 5")

arrangement(a)