class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        import random
        def findMedian(nums, start, end):
            if end <= start:
                return
            pivotIndex = random.randrange(start, end)
            nums[start], nums[pivotIndex] = nums[pivotIndex], nums[start]
            i = start + 1
            j = end
            while i <= j:
                if nums[i] > nums[start]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    i += 1
            nums[start], nums[j] = nums[j], nums[start]
            findMedian(nums, j + 1, end)
            findMedian(nums, start, j - 1)
        
        findMedian(nums, 0, len(nums) - 1)
        num1 = 1
        for i in range(len(nums)):
            if num1 == nums[i]:
                num1 += 1
        return num1
