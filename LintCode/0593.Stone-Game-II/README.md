https://www.lintcode.com/problem/stone-game-ii

# 593. Stone Game II


There is a stone game.At the beginning of the game the player picks n piles of stones in a circle.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.


Example 1:

```
Input:
[1,1,4,4]
Output:18
Explanation:
1. Merge second and third piles => [2, 4, 4], score +2
2. Merge the first two piles => [6, 4]，score +6
3. Merge the last two piles => [10], score +10
```

Example 2:

```
Input:
[1, 1, 1, 1]
Output:8
Explanation:
1. Merge first and second piles => [2, 1, 1], score +2
2. Merge the last two piles => [2, 2]，score +2
3. Merge the last two piles => [4], score +4
```