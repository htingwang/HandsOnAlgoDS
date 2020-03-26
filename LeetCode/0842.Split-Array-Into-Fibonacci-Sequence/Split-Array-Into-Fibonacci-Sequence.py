class Solution:
    result = []
    max_int = 2 ** 31 - 1

    def splitIntoFibonacci(self, S:str) -> List[int]:
        self.findFibRecursion(S, [])
        return self.result

    def isFib(self, cur_num, fib_list):
        # only for if the num starts with 0, return false.
        if len(cur_num) > 1 and cur_num[0] == "0":
            return False
        if len(fib_list) >= 2:
            if (fib_list[-1] + fib_list[-2]) == int(cur_num):
                return True
            else:
                return False
        else:
            return True

    def findFibRecursion(self, nums, fib_list):
        # nums reduces to "" in the end of loop.
        # also the fibonacci-like sequence was found in flb_list.
        if nums is "" and len(fib_list) > 2:
            self.result = fib_list
            return
        else:
            for i in range(len(nums)):
                if int(nums[:i + 1]) > self.max_int:
                    break
                cur_num = nums[:i + 1]
                if self.isFib(cur_num, fib_list):
                    self.findFibRecursion(nums[i + 1:], fib_list + [int(cur_num)])
