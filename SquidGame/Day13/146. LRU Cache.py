class Node:
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.prev, self.next = None, None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right =  Node(-1, -1), Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        if node.key not in self.cache:
            return
        del self.cache[node.key]
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node 
        self.cache[node.key] = node
        if len(self.cache) > self.capacity:
            next = self.left.next
            next.next.prev = self.left
            self.left.next = next.next
            if next.key in self.cache:
                del self.cache[next.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def printNodes(self):
        vals = []
        curr = self.left
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals 


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)