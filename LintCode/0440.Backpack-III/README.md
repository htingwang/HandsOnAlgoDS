https://www.lintcode.com/problem/backpack-iii/

Description

Given n kinds of items, and each kind of item has an infinite number available. The i-th item has size A[i] and value V[i].

Also given a backpack with size m. What is the maximum value you can put into the backpack?

You cannot divide item into small pieces.

Total size of items you put into backpack can not exceed m.

Have you met this question in a real interview?  

Example

Example 1:

Input: A = [2, 3, 5, 7], V = [1, 5, 2, 4], m = 10

Output: 15

Explanation: Put three item 1 (A[1] = 3, V[1] = 5) into backpack.

Example 2:

Input: A = [1, 2, 3], V = [1, 2, 3], m = 5

Output: 5

Explanation: Strategy is not unique. For example, put five item 0 (A[0] = 1, V[0] = 1) into backpack.

