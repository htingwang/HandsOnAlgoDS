https://www.lintcode.com/problem/longest-continuous-increasing-subsequence-ii

# 398. Longest Continuous Increasing Subsequence II


Given an integer matrix. Find the longest increasing continuous subsequence in this matrix and return the length of it.

The longest increasing continuous subsequence here can start at any position and go up/down/left/right.


Example 1:

```
Input: 
    [
      [1, 2, 3, 4, 5],
      [16,17,24,23,6],
      [15,18,25,22,7],
      [14,19,20,21,8],
      [13,12,11,10,9]
    ]
Output: 25
Explanation: 1 -> 2 -> 3 -> 4 -> 5 -> ... -> 25 (Spiral from outside to inside.)
```

Example 2:

```
Input: 
    [
      [1, 2],
      [5, 3]
    ]
Output: 4
Explanation: 1 -> 2 -> 3 -> 5
```

Challenge
- Assume that it is a N x M matrix. Solve this problem in O(NM) time and memory.