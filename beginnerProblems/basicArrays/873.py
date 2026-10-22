class Solution:
    def countOdd(self,arr,n):
        count =0
        for i in range(n):
            if arr[i] %2 !=0:
                count=count +1

        return count



arr =[1,2,3,4,5]
n = len(arr)
sol = Solution()
result = sol.countOdd(arr,n)
print(result)