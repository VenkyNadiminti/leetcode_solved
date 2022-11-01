class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=1
        sl=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>sl:
                sl=nums[i]
                nums[c]=sl
                c+=1
        return c
