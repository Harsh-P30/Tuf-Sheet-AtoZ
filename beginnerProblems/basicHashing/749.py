# 749. Sum of Highest and Lowest Frequency
import sys
class Solution:
    def sumHighestAndLowestFrequency(self, nums):

        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        max_freq = -sys.maxsize - 1
        max_val =nums[0]
        min_freq = sys.maxsize
        min_val = nums[0]
        for i,j in freq.items():
            if max_freq <= j :
                max_freq = j
                max_val = i
            if min_freq >= j :
                min_freq = j
                min_val = i

        return max_val+min_val

sol = Solution()

print(sol.sumHighestAndLowestFrequency([1,2,1,2,1,23,4,5,2,23,4,5,656,3,3,4,32,3,4,5,56,1]))