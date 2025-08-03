class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1

        return low

        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        