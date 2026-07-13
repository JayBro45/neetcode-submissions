class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        
        for i in strs:
            l = len(i)
            s += str(l) + "#" + i
        
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i=0

        while(i<len(s)):
            num = ''
            while(s[i]!='#'):
                num += s[i]
                i+=1

            num = int(num)

            word = ''
            i+=1

            for j in range(num):
                word += s[i]
                i+=1
            
            strs.append(word)
        
        return strs
                
