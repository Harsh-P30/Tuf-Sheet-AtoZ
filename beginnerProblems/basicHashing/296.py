# Given an array nums of n integers, find the most frequent 
# element in it i.e., the element that occurs the maximum number 
# of times. If there are multiple elements that appear a maximum number
#  of times, find the smallest of them.

class Solution:
    def mostFrequentElement(self,arr):
        freq ={}

        for nums in arr:
            if nums in freq:
                freq[nums] +=1
            else:
                freq[nums] = 1


        max_freq = 0
        max_element = arr[0]

        for num,count in freq.items():
            if count > max_freq:
                max_freq = count
                max_element = num
       
                

        return max_element


sol = Solution()
print(sol.mostFrequentElement([1,2,3,1,2,3,2,5,4,1,2,1,1,1]))