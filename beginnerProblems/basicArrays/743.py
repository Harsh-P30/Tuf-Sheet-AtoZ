class Solution:
    # def arraySortedOrNot(self,arr,n):
    #     if arr[0]>arr[1]:
    #         for i in range(n-1):
    #             if (arr[i])< (arr[i+1]):
    #                 return False
    #     else:
    #         for i in range(n-1):
    #             if (arr[i]) > (arr[i+1]):
    #                 return False

    #     return True

    def arraySortedOrNot(self,arr,n):
        ascending = True
        descending = True

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                ascending = False
            if arr[i] < arr[i+1]:
                descending = False

        return ascending or descending

sol = Solution()

print(sol.arraySortedOrNot([1,2,3,4,5],5))
print(sol.arraySortedOrNot([1,20,3,48,5],5))
print(sol.arraySortedOrNot([6,5,4,3,2,1],6))