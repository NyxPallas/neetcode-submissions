from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = dict(Counter(s))
        hash_t = dict(Counter(t))

        if hash_s.keys() == hash_t.keys() and hash_s.items() == hash_t.items():
            return True
        else:
            return False
            
        