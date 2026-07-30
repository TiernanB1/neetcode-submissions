import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1 
        post = 1
        output = [1]
        for i in range(len(nums) - 1):
            pre *= nums[i]
            output.append(pre)

        for j in range(len(nums) - 1, 0, -1):

            post *= nums[j]
            output[j - 1] *= post 
  
        return output


      
    

            
        