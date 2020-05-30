#!/usr/bin/python

import bisect
arr = [-2, 0, 2, 3]
print(bisect.bisect_right(arr, 2))
print(bisect.bisect_left(arr, 0))
