# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.
class Solution:
    def reverse(self,arr:list,n:int)->None:
        i=0
        j = n-1

        while i <=j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1

        return arr


sol = Solution()
print(sol.reverse([1,2,3,4],4))