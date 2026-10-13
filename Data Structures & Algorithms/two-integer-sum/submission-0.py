class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create an empty dictionary to store numbers and their indices
        seen = {}

        # Step 1: Loop through nums and get each number's index and value
        for i, num in enumerate(nums):

            # Step 2: Calculate the number needed to reach the target
            needed = target - num

            # Step 3: Check if the needed number is already in the dictionary
            if needed in seen:

                # Step 4: Return the indices of both numbers
                return [seen[needed], i]

            # Step 5: If no match is found, store the current number and its index
            seen[num] = i