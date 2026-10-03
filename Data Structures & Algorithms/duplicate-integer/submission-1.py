class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # empty set
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        # no duplicate
        return False