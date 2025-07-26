# https://leetcode.com/problems/group-anagrams/

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashMap = {}
    result = []

    for string in strs:
        sortedStr = "".join(sorted(string))
        if sortedStr in hashMap:
            hashMap[sortedStr].append(string)
        else:
            hashMap[sortedStr] = [string]
    
    for value in hashMap.values():
        result.append(value)

    return result


# Test Cases

strs = ["eat","tea","tan","ate","nat","bat"]

Output = [["bat"],["nat","tan"],["ate","eat","tea"]]

print(groupAnagrams(strs))

# Time Complexity: O(k*nLogn)
# Space Complexity: O(kn)