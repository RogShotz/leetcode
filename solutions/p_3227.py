'''
Alice and Bob are playing a game on a string.

You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:

On Alice's turn, she has to remove any non-empty substring from s that contains an odd number of vowels.
On Bob's turn, he has to remove any non-empty substring from s that contains an even number of vowels.
The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.

Return true if Alice wins the game, and false otherwise.

The English vowels are: a, e, i, o, and u.

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
'''

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_amount = 0
        for char in s:
            if char in vowels:
                vowel_amount += 1
        
        # Alice always wins unless there is no vowels to start since she can't remove any more vowels.
        # If it's odd she'll take all of them in her first move.
        # If it's even she'll just take one, which makes it uneven and bob can't make it odd again
        # so then the above case happens where when it comes back to alice it is now odd and she wins.
        if vowel_amount == 0:
            return False
        else:
            return True