https://www.lintcode.com/problem/coins-in-a-line


There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.

Have you met this question in a real interview?  

Example

Example 1:

Input: 1

Output: true

Example 2:

Input: 4

Output: true

Explanation:

The first player takes 1 coin at first. Then there are 3 coins left.

Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.

Challenge

O(n) time and O(1) memory
