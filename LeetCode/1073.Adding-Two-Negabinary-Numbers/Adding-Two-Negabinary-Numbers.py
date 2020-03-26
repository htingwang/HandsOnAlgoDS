class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        if len(arr2) > len(arr1):
            arr1, arr2 = arr2, arr1;
        arr = [0] * (len(arr1) + 2);
        
        i, j, k = len(arr1) - 1, len(arr2) - 1, len(arr) - 1;
        carry = 0;
        lead_one = k;
        while i >= -2:
            add1 = add2 = 0;
            if i >= 0: add1 = arr1[i];
            if j >= 0: add2 = arr2[j];
            if (len(arr1) - 1 - i) % 2 == 0: # positive
                tmp = carry + add1 + add2;
                if tmp < 0: carry = -1;
                else: carry = (abs(tmp) // 2);
            else: # negative
                tmp = carry - add1 - add2;
                if tmp > 0: carry = 1;
                else: carry = -(abs(tmp) // 2);
            arr[k] = abs(tmp % 2);
            if arr[k]: lead_one =k;
            i -= 1;
            j -= 1;
            k -= 1;
        
        #print arr
        return arr[lead_one:]   
