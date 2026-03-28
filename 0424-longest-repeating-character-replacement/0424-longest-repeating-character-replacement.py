class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            # Count frequency
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Track max frequency in window
            max_freq = max(max_freq, count[s[right]])

            # If more than k replacements needed, shrink window
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update answer
            max_length = max(max_length, right - left + 1)

        return max_length
        