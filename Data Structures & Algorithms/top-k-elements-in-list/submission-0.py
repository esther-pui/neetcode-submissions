class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # store each unique
        num_count = {}

        for num in nums:
            if num not in num_count:
                # What should you store for a number seen for the first time?
                num_count[num] = 1
                pass
            else:
                # How do you increase its count?
                num_count[num] += 1
                pass

        sorted_nums = sorted(num_count, key=num_count.get, reverse=True)
        
        return sorted_nums[:k]