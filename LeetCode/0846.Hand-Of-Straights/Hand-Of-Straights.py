class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        return self.isNStraightHand2(hand, W)
    
    def isNStraightHand2(self, hand, W):
        count = collections.Counter(hand)
        last, opened = -1, 0
        start = collections.deque()
        for num in sorted(count):
            if count[num] < opened or (opened > 0 and num > last + 1): return False
            start.append(count[num] - opened)
            last, opened = num, count[num]
            if len(start) == W: opened -= start.popleft()
        return opened == 0
            
        
    def isNStraightHand1(self, hand, W):
        count = collections.Counter(hand)
        
        for num in sorted(count):
            if count[num] > 0:
                for i in range(W)[::-1]:
                    count[num + i] -= count[num]
                    if count[num + i] < 0: return False
        return True
