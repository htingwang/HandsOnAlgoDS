https://www.lintcode.com/problem/minimum-window-substring/

Description


Given a string source and a string target, find the minimum window in source which will contain all the characters in target.

If there is no such window in source that covers all characters in target, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in source.

The target string may contain duplicate characters, the minimum window should cover all characters including the duplicate characters in target.

Have you met this question in a real interview?  

Clarification

Should the characters in minimum window has the same order in target?

Not necessary.

Example

Example 1:

Input:

""

""

Output:

""

Example 2:

Input:

"ADOBECODEBANC"

"ABC"

Output:

"BANC"

Challenge

Can you do it in time complexity O(n) ?

