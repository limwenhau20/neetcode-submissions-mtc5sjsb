class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        
        if len(s) != len(t):
            return False

        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1

        for i in t:
            if i in dict_t:
                dict_t[i] += 1
            else:
                dict_t[i] = 1

        # for i in range(0,len(s)):
        #     dict_s[s[i]] = dict_s.get(s[i], 0) + 1
        #     dict_t[t[i]] = dict_t.get(t[i], 0) + 1
        
        return dict_s == dict_t