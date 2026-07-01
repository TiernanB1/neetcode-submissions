class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        visited = set()
        def isanagram(a, b):

            if len(a) != len(b):
                return False

            countW, countC = {}, {}

            for i in range(len(a)):
                countW[a[i]] = 1 + countW.get(a[i], 0)
                countC[b[i]] = 1 + countC.get(b[i], 0)
            return countW == countC 

        for i in range(len(strs)):
            if i in visited:
                continue 
            group = [strs[i]]
            for j in range(i + 1, len(strs)):
                if j not in visited and isanagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited.add(j)
            output.append(group)
        return output
                

        




        
        