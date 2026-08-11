class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seq = 0 
        row = set(nums)

        for n in row:
            if (n - 1) not in row:
                length = 1
                while (n + length) in row:
                    length += 1

                seq = max(length, seq)
        return seq

                        
        

        
                

  

        


        


        