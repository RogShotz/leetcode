'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        max_freq = max(freqs.values())

        matches_max = 0
        for v in freqs.values():
            if v == max_freq:
                matches_max += 1
        
        return max_freq * matches_max