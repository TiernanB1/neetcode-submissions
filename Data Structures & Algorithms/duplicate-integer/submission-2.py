class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        safe = set()
        for i in range(len(nums)):
            if nums[i] in safe:
                return True 
            else:
                safe.add(nums[i])

        return False

        


        