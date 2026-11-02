# 357. Reverse a String II

class Solution: 
    def reverseString(self, s):
        val=""
        # for i in  reversed(s):
        #     val+=i

        # for i in range(len(s)-1,-1,-1):  # using range-> size,start,step
        #     val+=s[i]

        val+=s[::-1] # slicing

        return val



sol = Solution()
print(sol.reverseString("hello"))