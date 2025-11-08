# Given an integer x, return true if x is a palindrome, and false otherwise.

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev_int = 0
        consume_int = x

        while consume_int > 0:
            rev_int = rev_int * 10 + consume_int % 10
            consume_int = consume_int // 10

        return x == rev_int