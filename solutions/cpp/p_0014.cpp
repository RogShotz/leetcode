/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    string longestCommonPrefix(vector<string>& strs) {
        for (int i = 0; i < strs[0].size(); i++) {
            for (string word : strs) {
                if (i > word.size() || word[i] != strs[0][i]) {
                    return strs[0].substr(0, i);
                }
            }
        }

        return strs[0];  // All the same
    }
};
