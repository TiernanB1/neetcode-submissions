class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        l = 0
        uniqe = set()

        for r in range(len(s)):
            while s[r] in uniqe:
                uniqe.remove(s[l])
                l += 1
            uniqe.add(s[r])
            longest = max(longest, r - l + 1)

        return longest 





        