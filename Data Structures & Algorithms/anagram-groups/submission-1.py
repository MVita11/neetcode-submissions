class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagram = {}

        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted not in groupAnagram:
                groupAnagram[word_sorted] = []
            groupAnagram[word_sorted].append(word)
        return list(groupAnagram.values())
