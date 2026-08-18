class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        

        count1 = {}
        count2 = {}

        l = 0

        for k in s1:
            count1[k] = 1 + count1.get(k, 0)

        for o in s2[:len(s1)]:
            count2[o] = 1 + count2.get(o, 0)

        while l <= len(s2) - len(s1):

            if count1 == count2:
                return True

            count2[s2[l]] -= 1

            if count2[s2[l]] == 0:
                del count2[s2[l]]

            r = l + len(s1)

            if r < len(s2):
                count2[s2[r]] = 1 + count2.get(s2[r], 0)

            l += 1

        return False


                

                

            




        