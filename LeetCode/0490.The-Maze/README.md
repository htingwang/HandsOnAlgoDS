https://leetcode.com/problems/the-maze/

# 490. The Maze


There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

```
Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

<<<<<<< HEAD
=======
Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
>>>>>>> 7e91b4668796b9604c0259ae514666f555e50b2b
```
<img src = "img/maze_1_example_1.png"></br>

Example 2:

```
Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

```
<<<<<<< HEAD
<img src = "img/maze_1_example_2.png"></br> 
=======
 <img src = "img/maze_1_example_2.png"></br>
>>>>>>> 7e91b4668796b9604c0259ae514666f555e50b2b

Note:

- There is only one ball and one destination in the maze.
- Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
- The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
- The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
