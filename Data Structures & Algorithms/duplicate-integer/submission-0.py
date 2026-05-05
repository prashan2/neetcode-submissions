class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums1 = nums[:]
        self.set_num1 = set(self.nums1)
        if len(self.nums1) == len(self.set_num1):
            return False
        else:
            return True
        

nums = [1,2,3,4]
handle = Solution()
print(handle.hasDuplicate(nums))