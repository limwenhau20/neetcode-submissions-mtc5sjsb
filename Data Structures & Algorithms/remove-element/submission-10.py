class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        ##### Easy to understand (inplace)
        ##### 2 Pointer from start
        position = 0
        for num in nums:
            if num != val:
                nums[position] = num
                position += 1
        return position


        ##### HARD to understand (inplace)
        ##### pointer from start, and from end
        # i = 0
        # n = len(nums)
        # while i < n:
        #     if nums[i] == val:
        #         n -= 1
        #         nums[i] = nums[n]
        #     else:
        #         i += 1
        # return n