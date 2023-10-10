# Leetcode_sol_for_1512_Number_of_Good_Pairs
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a dictionary to count the occurrences of each number
        num_count = {}

        # Initialize the count of good pairs
        good_pairs = 0

        # Iterate through the array and count occurrences
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        # Calculate good pairs for each number that occurs more than once
        for count in num_count.values():
            if count > 1:
                good_pairs += (count - 1) * count // 2

        return good_pairs
