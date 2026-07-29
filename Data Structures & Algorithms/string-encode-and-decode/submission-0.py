class Solution:


    def encode(self, strs: List[str]) -> str:


        output = []
        for word in strs:
            output.append(len(word))
            output.append("$")  
            output.append(word)
        ans = "".join(str(item) for item in output)
        return ans 


    def decode(self, s: str) -> List[str]:
        
        output = []
        i = 0

        while i < len(s): 
            j = i
            while s[j] != "$":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            output.append(s[i: j])
            i = j
        
        return output





