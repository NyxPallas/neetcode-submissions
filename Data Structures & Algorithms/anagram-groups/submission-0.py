class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_dict = {}
        anagram_list = []
        key_list = []

        for letter in strs:
            key_list.append(''.join(sorted(letter)))
        for key in key_list:
            letter_dict[key] = []
        for j in strs:
            if ''.join(sorted(j)) in letter_dict.keys():
                letter_dict[''.join(sorted(j))].append(j)
        for y in letter_dict:
            anagram_list.append(letter_dict[y])
        anagram_list.sort(key=len)
        return anagram_list