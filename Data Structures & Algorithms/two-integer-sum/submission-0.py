class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            counter = target-val
            if counter in hashmap:
                return [hashmap[counter], i]
            hashmap[val] = i
        return