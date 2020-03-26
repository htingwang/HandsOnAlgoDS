from collections import deque
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.w = width
        self.h = height
        self.food = food
        self.score = 0
        self.length = 1
        self.queue = deque()
        self.queue.append((0, 0))

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        i, j = self.queue[-1]
        if direction == "U":
            i -= 1
        if direction == "L":
            j -= 1
        if direction == "R":
            j += 1
        if direction == "D":
            i += 1
        
        if 0 <= i < self.h and 0 <= j < self.w:
            self.queue.append((i, j))
            if self.length < self.score + 1:
                self.length += 1
            else:
                self.queue.popleft()
            #print(i, j, self.length, self.queue)
            if self.length != len(set(self.queue)):
                return -1

            if self.score < len(self.food) and [i, j] == self.food[self.score]:
                self.score += 1
            return self.score
        return -1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
