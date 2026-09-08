class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for i in range(len(nums)):
            if nums[i] not in values:
                values.add(nums[i])
            elif nums[i] in values:
                return True
        return False