class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # clean_s = ''
        
        # for i in s:
        #     if i.isalnum():
        #         clean_s += i.lower()

        # return clean_s == clean_s[::-1]

        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
            
        return True