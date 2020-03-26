class Node(object):
    def __init__(self, key, val, freq):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
        self.freq = freq

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}
        # self.head = None
        self.freq_to_node = {}
        self.min_freq = float('inf')

    def get(self, key):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.update(node)
            return node.val
        return -1

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.update(node)
            return
        if len(self.key_to_node) == self.capacity:
            self.delete(self.freq_to_node[self.min_freq].prev)
        self.insert(Node(key, value, 1))

    def insert(self, node):
        if node.freq in self.freq_to_node:
            node.next = self.freq_to_node[node.freq]
            node.prev = self.freq_to_node[node.freq].prev
            self.freq_to_node[node.freq].prev = node
            node.prev.next = node
        else:
            node.prev = node
            node.next = node
        self.freq_to_node[node.freq] = node
        self.key_to_node[node.key] = node
        if self.min_freq not in self.freq_to_node or node.freq < self.min_freq:
            self.min_freq = node.freq
        
    def delete(self, node):
        if node.prev == node:
            del self.freq_to_node[node.freq]
        elif self.freq_to_node[node.freq] == node:
            self.freq_to_node[node.freq] = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.key_to_node[node.key]

    def update(self, node):
        self.delete(node)
        node.freq += 1
        self.insert(node)
