class Node(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}
        self.head = None

    def get(self, key):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.update(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.update(node)
            return
        if len(self.key_to_node) == self.capacity:
            self.delete(self.head.prev)
        self.insert(Node(key, value))

    def insert(self, node):
        if self.head:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
            node.prev.next = node
        else:
            node.prev = node
            node.next = node
        self.head = node
        self.key_to_node[node.key] = node
        
    def delete(self, node):
        if node.prev == node:
            self.head = None
        elif self.head == node:
            self.head = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.key_to_node[node.key]

    def update(self, node):
        self.delete(node)
        self.insert(node)

