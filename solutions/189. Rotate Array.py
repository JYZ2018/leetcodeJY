class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        rotate_times=k % numsLen
        nums[:]= nums[-1*rotate_times:]+nums[:-1*rotate_times]
        return nums
        
