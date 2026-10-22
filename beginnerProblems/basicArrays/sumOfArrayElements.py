class Solution:
    def sum(self,arr,n):
        sum = 0
        for i in range(n):
            sum += arr[i]
        return sum


arr = [1,2,3,4]
n = len(arr)
sol = Solution()
result = sol.sum(arr,n)
print(result)
