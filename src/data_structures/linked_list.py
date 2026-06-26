from typing import Optional, Any


class Node:
    next: Optional["Node"]
    value: Any

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class LinkedList:
    head: Optional[Node]
    tail: Optional[Node]
    length: int

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        if self.head is None:
            return "LL (empty)"

        curr = self.head
        result = "LL ("
        while curr:
            result += str(curr)
            if curr.next:
                result += ", "
            curr = curr.next
        return result + ")"

    def __len__(self):
        return self.length

    def __contains__(self, value):
        return self.contains(value)

    def __iter__(self):
        curr = self.head

        while curr:
            yield curr.value
            curr = curr.next

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        return self.get(index)

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        self.set(index, value)

    def prepend(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        self.length += 1
        if self.tail is None:
            self.tail = self.head

    def append(self, value):
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head
            self.length = 1
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1

    def pop_front(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        self.length -= 1

        if self.head is None:
            self.tail = None

        return value

    def pop_back(self):
        if self.head is None or self.tail is None:
            return None
        if self.length == 1:
            curr = self.head
            self.head = self.tail = None
            self.length = 0
            return curr.value

        prev = self.head
        curr = prev.next if prev else None
        while curr and curr is not self.tail:
            prev = curr
            curr = curr.next

        prev.next = None
        self.tail = prev
        self.length -= 1
        return curr.value if curr else None

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == self.length - 1:
            return self.tail.value if self.tail else None

        curr = self.head

        for _ in range(index):
            if curr:
                curr = curr.next

        return curr.value if curr else None

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return

        if index == self.length - 1 and self.tail:
            self.tail.value = value

        curr = self.head

        for _ in range(index):
            if curr:
                curr = curr.next

        if curr:
            curr.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return

        if index == 0:
            self.prepend(value)
            return

        if index == self.length:
            self.append(value)
            return

        prev = self.head
        for _ in range(index - 1):
            if prev:
                prev = prev.next

        if prev:
            new_node = Node(value)
            new_node.next = prev.next
            prev.next = new_node
            self.length += 1

    def contains(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.head = self.tail = None
        self.length = 0

    def to_list(self):
        result = []

        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next

        return result
