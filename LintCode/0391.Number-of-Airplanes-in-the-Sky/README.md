https://www.lintcode.com/problem/number-of-airplanes-in-the-sky

Description


Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?

If landing and taking off of different planes happen at the same time, we consider landing should happen at first.

Have you met this question in a real interview?  

Example

Example 1:

Input: [(1, 10), (2, 3), (5, 8), (4, 7)]

Output: 3

Explanation:

The first airplane takes off at 1 and lands at 10.

The second ariplane takes off at 2 and lands at 3.

The third ariplane takes off at 5 and lands at 8.

The forth ariplane takes off at 4 and lands at 7.

During 5 to 6, there are three airplanes in the sky.

Example 2:

Input: [(1, 2), (2, 3), (3, 4)]

Output: 1

Explanation: Landing happen before taking off.