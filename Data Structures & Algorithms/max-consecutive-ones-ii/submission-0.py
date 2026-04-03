class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        answer = 0
        k = 1

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1

            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

            answer = max(answer, r - l + 1)

        return answer