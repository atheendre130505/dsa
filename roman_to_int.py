class Solution(object):
    def romanToInt(self, s):
        d1={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        value=0
        i=0
        while i<len(s)-1:
            if d1[s[i]]>=d1[s[i+1]]:
                value+=d1[s[i]]
                i+=1
            else:
                x=(d1[s[i+1]]-d1[s[i]])
                value+=x
                i+=2
        if i==len(s)-1:
            value+=d1[s[-1]]
        return value

        """
        :type s: str
        :rtype: int
        """
        