class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ("".join(filter(str.isalnum, s))).lower()
        print(text)
        diff=len(text)-1
        print(diff)
        for i in range(len(text)//2):
            print(text[i], text[i+diff])
            if text[i] != text[i+diff]:
                return False
            diff-=2
        return True

