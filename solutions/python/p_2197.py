'''
You are given an array of integers nums. Perform the following steps:

Find any two adjacent numbers in nums that are non-coprime.
If no such numbers are found, stop the process.
Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
Repeat this process as long as you keep finding two adjacent non-coprime numbers.
Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less than or equal to 108.

Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

1 <= nums.length <= 105
1 <= nums[i] <= 105
The test cases are generated such that the values in the final array are less than or equal to 108.
'''

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        non_coprimes = []

        for num in nums:
            while non_coprimes:
                gcd_calc = gcd(non_coprimes[-1], num)
                # list already made sure neighbors are sorted, upon first hit break to do next num
                if gcd_calc == 1:
                    break

                # modify num to be the representing number of the popped coprimes from the stack
                num = (non_coprimes.pop() * num) // gcd_calc

            # append the new num
            non_coprimes.append(num)
        
        return non_coprimes