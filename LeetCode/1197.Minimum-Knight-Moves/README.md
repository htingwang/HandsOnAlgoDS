https://leetcode.com/problems/minimum-knight-moves/

# 1197. Minimum Knight Moves

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

<p><img src="img/demo2.png"></br>

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
```

Example 2:

```
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
``` 

Constraints:

- |x| + |y| <= 300
