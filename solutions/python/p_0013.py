'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        #roman_vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        s = s[::-1] # Reverse S, it makes it easier to process
        
        sum = 0
        # Has the next digit order been triggered yet? This determines if something is + or -
        V_or_X = False
        L_or_C = False
        D_or_M = False
        for char in s:
            # I check
            if char == 'I':
                if not V_or_X:
                    sum += 1
                else:
                    sum -= 1

            elif char == 'V':
                V_or_X = True
                sum += 5
            elif char == 'X':
                V_or_X = True
                if not L_or_C:
                    sum += 10
                else:
                    sum -= 10
            
            elif char == 'L':
                L_or_C = True
                sum += 50
            elif char == 'C':
                L_or_C = True
                if not D_or_M:
                    sum += 100
                else:
                    sum -= 100

            elif char == 'D':
                D_or_M = True
                sum += 500
            elif char == 'M':
                D_or_M = True
                sum += 1000
        
        return sum