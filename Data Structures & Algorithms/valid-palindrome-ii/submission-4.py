class Solution:
    def validPalindrome(self, s: str) -> bool:

        # l, r = 0, len(s)-1

        # while l < r:
        #     if s[l] == s[r]:
        #         l += 1
        #         r -= 1
        #     elif s[l] != s[r]:
        #         # Check either (deleting from start) or (deleting from end) is palindrome
        #         skip_l = s[l+1: r+1]
        #         skip_r = s[l:r]
                
        #         return (skip_l == skip_l[::-1] or skip_r == skip_r[::-1])

        # return True

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (is_palindrome(l + 1, r) or 
                        is_palindrome(l, r - 1))
            l += 1
            r -= 1

        return True