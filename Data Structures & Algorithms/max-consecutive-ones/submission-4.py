class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        current_len = 0
        for num in nums:
            if num == 0:
                max_len = max(max_len, current_len)
                current_len = 0

            elif num == 1:
                current_len += 1

        return max(max_len, current_len)
            
