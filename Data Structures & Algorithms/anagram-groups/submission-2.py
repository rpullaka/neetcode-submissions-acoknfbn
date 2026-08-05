'''
08/05/26
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            D[sorted_word].append(word)
        return list(D.values())