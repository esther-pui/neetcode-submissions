class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Step 1: Check if both strings have the same length
        # If their lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Create two empty dictionaries
        # One dictionary to count letters in s
        s_count = {}
        # Another dictionary to count letters in t
        t_count = {}
        

        # Step 3: Loop through each letter in s
        # Count how many times each letter appears
        # Hint: Use .get() to get the current count, defaulting to 0
        for s_letter in s:
            s_count[s_letter] = s_count.get(s_letter, 0) + 1

        # Step 4: Loop through each letter in t
        # Count how many times each letter appears
        # Use the same counting logic as Step 3
        for t_letter in t:
            t_count[t_letter] = t_count.get(t_letter, 0) + 1


        # Step 5: Compare the two dictionaries
        # If the letter counts are identical, return True
        # Otherwise, return False
        if s_count == t_count:
            return True
        else:
            return False
       
