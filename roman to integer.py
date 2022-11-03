class Solution:
    def romanToInt(self, s: str) -> int:
        data={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res=0
        i=len(s)-1
        while(i>=0):
            if i<len(s)-1 and data[s[i]]<data[s[i+1]]:
                res-=data[s[i]]
            else:
                res+=data[s[i]]
            i-=1
        return res
