class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for st in s:
            countS[st] = countS.get(st,0) + 1
        for ts in t:
            countT[ts] = countT.get(ts,0) + 1

        return countS == countT
        