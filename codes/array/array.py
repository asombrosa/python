#https://neetcode.io/problems/valid-anagram/question?list=neetcode150
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = Counter(t)
        key_t=dict(freq)

        for ch in s:
            if ch in key_t:
                if key_t[ch]==0:
                    return False
                key_t[ch]=key_t[ch]-1
            if ch not in key_t:
                return False

        return True       