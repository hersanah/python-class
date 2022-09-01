class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums = nums
        self.target = target
        index = []
        
        for num in nums:
            complement = target - num
            if complement > 0 and complement in nums:
                if nums.index(num) not in index:
                    index.extend([nums.index(num), nums.index(complement)])
        
        return index

        
nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))