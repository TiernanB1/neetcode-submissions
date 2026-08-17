class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 
        l = 0 
        letters = {}

        for r in range(len(s)): 

            letters[s[r]] = 1 + letters.get(s[r], 0)
            while (r - l + 1) - max(letters.values()) > k:
                letters[s[l]] = -1 + letters.get(s[l], 0)
                l += 1 
            
            longest = max(longest, r - l + 1)
        
        return longest

            




            


            
        