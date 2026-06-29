from typing import Any


class Node:
    value: Any
    next: "Node | None"

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node ({self.value})"


class Queue:
    start: Node | None
    length: int

    def __init__(self):
        self.start = None
        self.length = 0

    def __repr__(self) -> str:
        result = "Queue ("
        curr = self.start

        while curr:
            result += str(curr)
            if curr.next is not None:
                result += ", "
            curr = curr.next

        return result

    def enqueue(self, value):
        new_node = Node(value)
        curr = self.start

        if self.start is None:
            self.start = new_node
        else:
            while curr:
                if curr.next is None:
                    curr.next = new_node
                    break
                curr = curr.next
        self.length += 1

    def dequeue(self):
        value = self.start.value if self.start else None

        self.start = self.start.next if self.start else None

        return value
