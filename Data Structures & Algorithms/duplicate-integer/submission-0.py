class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in len(nums)-1:
        #     if nums[i] == nums
        return len(nums) != len(set(nums))    
        