/*
Given a string s, find the length of the longest substring without duplicate characters.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

TY: GeeksForGeeks for the window method: https://www.geeksforgeeks.org/dsa/length-of-the-longest-substring-without-repeating-characters/
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        size_t n = s.size();

        if (n == 0 || n == 1) {
            return n;
        }
        int max_len = 0;

        vector<bool> chars_list(122 - ' ', false);

        // - ' ' to give a 0 based index based on space... not the best but has to be included isntead of a
        // due to it containing spaces and numbers
        int left = 0, right = 0;
        while (right < n) {
            while (chars_list[s[right] - ' '] == true) {
                chars_list[s[left] - ' '] = false;
                left++;
            }

            chars_list[s[right] - ' '] = true;

            max_len = max(max_len, (right - left + 1));
            right++;
        }

        return max_len;
    }
};
