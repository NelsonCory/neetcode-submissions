class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for i in strs:
            anagramKey = str(sorted(i))
            if anagramDict.get(anagramKey,0):
                anagramDict[anagramKey].append(i)
            else:
                anagramDict[anagramKey] = [i]
        
        return list(anagramDict.values())