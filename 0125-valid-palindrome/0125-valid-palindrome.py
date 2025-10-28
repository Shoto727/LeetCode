class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            
            # skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # compare lowercase versions of characters
            if s[left].lower() != s[right].lower():
                return False

            # move both pointers inward
            left += 1
            right -= 1

        # if all characters matched
        return True
