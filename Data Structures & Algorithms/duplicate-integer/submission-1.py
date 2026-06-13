class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}

        for num in nums:
            if num not in countMap:
                countMap[num] = 1
                continue
            else:
                return True
        return False