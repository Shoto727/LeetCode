class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()

        for r in range(len(s)):
            # If character already exists, shrink the window from left
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            # Add the new character
            sett.add(s[r])

            # Calculate window length
            w = r - l + 1
            longest = max(longest, w)

        return longest
