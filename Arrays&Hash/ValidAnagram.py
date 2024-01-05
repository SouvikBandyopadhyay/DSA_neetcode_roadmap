class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1=dict()
        h2=dict()
        for i in s:
            h1[i]=h1.get(i,0)+1
        for i in t:
            h2[i]=h2.get(i,0)+1
        for i in h1:
            h2[i]=h2.get(i,-1)-h1[i]
        for i in h2:
            if h2[i]!=0:
                return False
        return True
        # return sorted(s)==sorted(t)
    

                
