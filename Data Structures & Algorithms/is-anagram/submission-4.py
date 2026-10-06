from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = dict(sorted(Counter(sorted(s)).items()))
        hash_t = dict(sorted(Counter(sorted(t)).items()))

        if hash_s.keys() == hash_t.keys() and hash_s.items() == hash_t.items():
            return True
        else:
            return False
            
        