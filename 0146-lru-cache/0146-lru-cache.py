class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self._remove_node(node)
            self._add_node(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.val = value
            self._remove_node(node)
            self._add_node(node)
            return
        
        if len(self.cache) == self.capacity:
            del self.cache[self.tail.prev.key]
            self._remove_node(self.tail.prev)

        node = Node(key, value)
        self._add_node(node)
        self.cache[key] = node


    def _add_node(self, node: Node):
        curr = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = curr
        curr.prev = node

    def _remove_node(self, node: Node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)