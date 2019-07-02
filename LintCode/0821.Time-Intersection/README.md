https://www.lintcode.com/problem/time-intersection/

Description


Give two users' ordered online time series, and each section records the user's login time point x and offline time point y. Find out the time periods when both users are online at the same time, and output in ascending order.you need return a list of intervals.

We guarantee that the length of online time series meet 1 <= len <= 1e6.

For a user's online time series, any two of its sections do not intersect.

Have you met this question in a real interview?  

Example

Example 1:

Input: seqA = [(1,2),(5,100)], seqB = [(1,6)]

Output: [(1,2),(5,6)]

Explanation: In these two time periods (1,2), (5,6), both users are online at the same time.

Example 2:

Input: seqA = [(1,2),(10,15)], seqB = [(3,5),(7,9)]

Output: []

Explanation: There is no time period, both users are online at the same time.
