class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        # minimum, maximum, mean, median, and mode
        totalnum = sum(count)
        minimum = 256
        maxinum = -1
        max_cnt = mode = median = totalsum = index = num1 = num2 = float(0)
        pos1 = pos2 = totalnum // 2
        if totalnum % 2 == 0:
            pos1 = pos2 - 1
            
        for i in range(len(count)):
            if count[i] != 0:
                if minimum == 256:
                    minimum = i
                maximum = float(i)
                if count[i] > max_cnt:
                    max_cnt = count[i]
                    mode = i
                totalsum += i * count[i]
                #print(totalsum)

                if index <= pos1 < index + count[i]:
                    num1 = i
                if index <= pos2 < index + count[i]:
                    num2 = i
                    
                median = (num1 + num2) / float(2)
                index += count[i]
        mean = totalsum / totalnum

        return [minimum, maximum, mean, median, mode]
