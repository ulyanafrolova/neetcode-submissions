class Solution:
    # Algorithm: ["Hello","World"] -> "5#Hello5#World"
    def encode(self, strs: List[str]) -> str:
        if len(strs) ==0:
            return ""
        result=""
        for i in range(len(strs)):
            result+=str(len(strs[i]))
            result+="#"
            result +=strs[i]
            
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        p=0
        while p!= len(s):
            curr_num="0"
            while s[p] != '#':
                curr_num+=s[p]
                p+=1
            p+=1
            num=int(curr_num)
            new_word=""
            for i in range(num):
                new_word+=s[p]
                p+=1
            result.append(new_word)
                
        if len(result)==0:
            result=[]
        return result
