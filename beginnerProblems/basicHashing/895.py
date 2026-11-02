
# 895. Palindrome Check

class Solution:    
    def palindromeCheck(self, s):
        rev =""

        for i in range(len(s)-1,-1,-1):
            rev+=s[i]

        return rev ==s


sol = Solution()
print(sol.palindromeCheck(input("enter a string/number to check palindrome :-  ",)))