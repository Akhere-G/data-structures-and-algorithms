import pytest
from src.data_structures.queue import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def populated_queue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    return queue


def test_enqueue(empty_queue, populated_queue):
    empty_queue.enqueue(10)
    assert empty_queue.start.value == 10
    assert empty_queue.length == 1

    populated_queue.enqueue(40)
    assert populated_queue.start.value == 10
    assert populated_queue.start.next.value == 20
    assert populated_queue.start.next.next.value == 30
    assert populated_queue.start.next.next.next.value == 40
    assert populated_queue.start.next.next.next.next is None
    assert populated_queue.length == 4


def test_dequeue(empty_queue, populated_queue):
    assert empty_queue.dequeue() is None
    assert empty_queue.start is None
    assert empty_queue.length == 0

    assert populated_queue.dequeue() == 10
    assert populated_queue.dequeue() == 20
    assert populated_queue.dequeue() == 30
