"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
import collections
class Solution(object):
    def __init__(self):
        self.local_buf = collections.deque()
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        need = n
        
        while need > 0 and self.local_buf:
            buf[n - need] = self.local_buf.popleft()
            need -= 1
            
        while need > 0:
            tmp = [""] * 4
            ret = read4(tmp)
            for i in range(4):
                if need:
                    buf[n - need] = tmp[i]
                    need -= 1
                else:
                    self.local_buf.append(tmp[i])
        return n - need
