class Solution(object):
    def __init__(self, rects):
        self.rects = rects
        self.acc_area = [0] * len(rects)
        self.acc_area[0] = (rects[0][2] - rects[0][0] + 1) * (rects[0][3] - rects[0][1] + 1)
        for i in range(1, len(rects)):
            self.acc_area[i] = self.acc_area[i - 1] + (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1)

    def pick(self):
        area = random.randint(0, self.acc_area[-1] - 1)
        left, right = 0, len(self.acc_area) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.acc_area[mid] <= area:
                left = mid + 1
            else:
                right = mid 
        return [random.randint(self.rects[left][0], self.rects[left][2]), random.randint(self.rects[left][1], self.rects[left][3])]

