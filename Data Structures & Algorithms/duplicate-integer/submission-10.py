class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
                return True
        return False

