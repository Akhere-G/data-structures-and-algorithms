from typing import Any


class Node:
    value: Any
    next: "Node | None"

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node ({self.value})"


class Stack:
    top: Node | None
    length: int

    def __init__(self):
        self.top = None
        self.length = 0

    def __repr__(self):
        result = "Stack ("

        curr = self.top

        while curr:
            result += str(curr)
            if curr.next:
                result += ", "
            curr = curr.next

        return result + ")"

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return None
        result = self.top.value
        self.top = self.top.next
        self.length -= 1
        return result

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None
