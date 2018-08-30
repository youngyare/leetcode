class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """if nums is null or only has 1 element"""
        if len(nums) <= 1:
            #print("error list")
            return []

        else:
            for i in range(len(nums) - 1):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        #print("found them!")
                        return [i, j]
            #print("failed to match")
            return []


