class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        current_len = 0
        for i in nums:
            if i == 0:
                current_len = 0

            elif i == 1:
                current_len += 1
            
            max_len = max(max_len, current_len)

        return max_len
            
