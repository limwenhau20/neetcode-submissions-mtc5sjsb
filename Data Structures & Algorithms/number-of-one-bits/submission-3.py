class Solution:
    def hammingWeight(self, n: int) -> int:
        # Method 1
        # count = 0
        # while n > 0:
        #     if n & 1:
        #         count += 1
        #     n = n >> 1
        # return count
        
        # Method 2
        # count = 0
        # while n > 0:
        #     count += n & 1
        #     n = n >> 1
        # return count

        # Method 3
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count
        



