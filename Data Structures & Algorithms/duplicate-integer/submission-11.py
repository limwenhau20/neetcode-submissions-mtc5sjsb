class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        read = set()
        for i in nums:
            if i not in read:
                read.add(i)
            else:
                return True
        return False