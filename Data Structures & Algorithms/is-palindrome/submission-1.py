class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_s = ''
        
        for i in s:
            if i.isalnum():
                clean_s += i.lower()

        return clean_s == clean_s[::-1]

