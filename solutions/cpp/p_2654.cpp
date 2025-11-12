/*
You are given a 0-indexed array nums consisiting of positive integers. You can do the following
operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd
value. Return the minimum number of operations to make all elements of nums equal to 1. If it is
impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

Constraints:

2 <= nums.length <= 50
1 <= nums[i] <= 106

TY: Gopal-Samy for the smart solution, I was stuck for a while figuring out the right incrementers
in the for loops.
*/

#include <iostream>
#include <numeric>
#include <vector>

using namespace std;
class Solution {
   public:
    int minOperations(vector<int>& nums) {
        const int n = nums.size();
        int result = INT_MAX;  // A really large number
        int cnt1 = 0;

        // Track how many 1's are already present
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                cnt1 += 1;
            }
        }

        // Return the amount of remaining operations to make everything 1
        if (cnt1) {
            return n - cnt1;
        }

        for (int i = 0; i < n; i++) {
            int g = nums[i];

            // Increment before so you can get the next element
            for (int j = i + 1; j < n; ++j) {
                g = gcd(g, nums[j]);

                if (g == 1) {
                    result = min(result, j - 1 + n - 1);
                }
            }
        }

        return result == INT_MAX ? -1 : result;
    }
};
