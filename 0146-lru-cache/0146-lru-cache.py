class LRUCache:

    class Node:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        current = self.cache.get(key)
        if current:
            self._remove_node(current)
            self._add_node(current)
            return current.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        current = self.cache.get(key)
        if current:
            self._remove_node(current)
            current.val = value
            self._add_node(current)
            return

        if len(self.cache) == self.capacity:
            del self.cache[self.tail.prev.key]
            self._remove_node(self.tail.prev)

        current = self.Node(key, value)
        self._add_node(current)
        self.cache[key] = current

    def _add_node(self, node: Node) -> None:
        current = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = current
        current.prev = node
        
    def _remove_node(self, node: Node) -> None:
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)