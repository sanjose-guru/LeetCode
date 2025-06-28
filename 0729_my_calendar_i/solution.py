class Node:
    def __init__(self, start, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, startTime, endTime: int) -> bool:
        if not self.root:
            self.root = Node(startTime, endTime)
            return True
        return self._insert(self.root, startTime, endTime)

    def _insert(self, node: Node, startTime, endTime: int):
        if endTime <= node.start:
            if node.left:
                return self._insert(node.left, startTime, endTime)
            else:
                node.left = Node(startTime, endTime)
                return True
        elif startTime >= node.end:
            if node.right:
                return self._insert(node.right, startTime, endTime)
            else:
                node.right = Node(startTime, endTime)
                return True
        else:
            return False
