class Solution:
    def secondMostFrequentElement(self, nums):
        freq ={}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1


        max_freq =0
        sec_max_freq =0
        max_value = nums[-1]
        secMaxVal = nums[-1]


        for i, j in freq.items():
            if max_freq < j:
                sec_max_freq = max_freq
                max_freq = j
                secMaxVal = max_value  
                max_value = i
            elif j > sec_max_freq:
                sec_max_freq = j
                secMaxVal = i
        return secMaxVal

sol = Solution()
print(sol.secondMostFrequentElement([1,2,3,1,2,3,1,2,1]))