class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.result = nums[:]
        for i in nums:
            self.result.append(i)
        return self.result

handle = Solution()
#num = list(map(int,input('enter the list of nums').split(' ')))
num = [1,3,5,2]
print(handle.getConcatenation(num))