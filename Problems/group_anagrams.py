from typing import List
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]

expected = [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = []

    for word in strs:
        char_count = defaultdict(int)
        for char in word:
            char_count[char] += 1

        count_tuple = tuple(char_count.items())
        # print(count_tuple)
        res.append((word, count_tuple))

    res_2 = []
    seen = {}

    for word, key in res:
        if key in seen:
            seen[key].append(word)
        else:
            seen[key] = [word]

    for words in seen.values():
        res_2.append(words)

    return(res_2)

print(groupAnagrams(None, strs))


