class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr2.sort()
        res = 0
        
        for i in range(len(arr1)):
            if (i+1 < len(arr1) and arr1[i + 1] <= arr1[i]) or (i > 0 and arr1[i] <= arr1[i - 1]):
                #if arr2[0] >= arr1[i + 1]: return -1
                left, right = 0, len(arr2) - 1
                target = arr1[i - 1] if i > 0 else float('-inf')
                while left <= right:
                    mid = (left + right) // 2
                    if arr2[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                if right + 1 < len(arr2) and arr2[right + 1] > target:
                    arr1[i] = arr2[right + 1]
                else:
                    return -1
                res += 1
        print(arr1)
        return res
