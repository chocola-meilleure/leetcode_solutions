class Solution:
    def groupAnagrams(self, strs: List[strs])->List[List[str]]:
        anagrams=collections.defaultdict(list)

        for word in strs:
            #sorting and add to dict
            anagrams[''.join(sorted(word))].append(word) #key is sorted word

        return list(anagrams.values())
