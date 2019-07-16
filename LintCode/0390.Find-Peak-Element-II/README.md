https://www.lintcode.com/problem/find-peak-element-ii/

# 390. Find Peak Element II


Given an integer matrix A which has the following features :

- The numbers in adjacent positions are different.
- The matrix has n rows and m columns.
- For all i < n, A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1].
- For all j < m, A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]
We define a position [i, j] is a peek if:

-   A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] && 
-   A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]
Find a peak element in this matrix. Return the index of the peak.

Guarantee that there is at least one peak, and if there are multiple peaks, return any one of them.

Example 1:

```
Input: 
    [
      [1, 2, 3, 6,  5],
      [16,41,23,22, 6],
      [15,17,24,21, 7],
      [14,18,19,20,10],
      [13,14,11,10, 9]
    ]
Output: [1,1]
Explanation: [2,2] is also acceptable. The element at [1,1] is 41, greater than every element adjacent to it.
```

Example 2:

```
Input: 
    [
      [1, 5, 3],
      [4,10, 9],
      [2, 8, 7]
    ]
Output: [1,1]
Explanation: There is only one peek.
```

Challenge
Solve it in O(n+m) time.

If you come up with an algorithm that you thought it is O(nlogm) or O(mlogn), can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?