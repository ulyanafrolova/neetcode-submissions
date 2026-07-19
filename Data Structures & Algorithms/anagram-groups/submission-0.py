from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        result = []

        for s in strs:
            key = frozenset(Counter(s).items())
            if key in my_dict:
                result[my_dict[key]].append(s)
            else:
                new_idx = len(result)
                result.append([])
                result[new_idx].append(s)
                my_dict[key]=new_idx

        return result

            