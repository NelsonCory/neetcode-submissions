class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False

        for i in s:
            if sDict.get(i):
                sDict[i] += 1
            else:
                sDict[i] = 1
        for i in t:
            if tDict.get(i):
                tDict[i] += 1
            else:
                tDict[i] = 1
        
        for i in sDict:
            if sDict.get(i) != tDict.get(i):
                return False
        return True