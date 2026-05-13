class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countS = {}
        countT = {}
        for c in s:
            countS[c] = countS.get(c,0) + 1
        for d in t:
            countT[d] = countT.get(d,0) + 1
        
        return countS==countT