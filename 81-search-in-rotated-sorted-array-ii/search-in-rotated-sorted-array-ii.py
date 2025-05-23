class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return True
        # return False
        if target in nums:
            return True 
        return False