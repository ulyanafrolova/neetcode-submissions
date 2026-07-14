class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        literals = {}
        for i in s:
            if i in literals:
                literals[i]+=1
            else:
                literals[i]=1
        for j in t:
            if j in literals:
                if literals[j]>0:
                    literals[j]-=1
                else:
                    return False;
            else:
                return False
        return True;
            

            