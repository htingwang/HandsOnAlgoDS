https://www.lintcode.com/problem/copy-books-ii

Given n books and each book has the same number of pages. There are k persons to copy these books and the i-th person needs times[i] minutes to copy a book.

Each person can copy any number of books and they start copying at the same time. What's the best strategy to assign books so that the job can be finished at the earliest time?

Return the shortest time.


Example 1:

```
Input: n = 4, times = [3, 2, 4]
Output: 4
Explanation: 
    First person spends 3 minutes to copy 1 book.
    Second person spends 4 minutes to copy 2 books.
    Third person spends 4 minutes to copy 1 book.
```

Example 2:

```
Input: n = 4, times = [3, 2, 4, 5]
Output: 4
Explanation: Use the same strategy as example 1 and the forth person does nothing.
```