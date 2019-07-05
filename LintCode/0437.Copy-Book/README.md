https://www.lintcode.com/problem/copy-books

Description


Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.


Have you met this question in a real interview?  

Example

Example 1:

Input: pages = [3, 2, 4], k = 2

Output: 5

Explanation: 

First person spends 5 minutes to copy book 1 and book 2.

Second person spends 4 minutes to copy book 3.

Example 2:

Input: pages = [3, 2, 4], k = 3

Output: 4

Explanation: Each person copies one of the books.

Challenge

O(nk) time

