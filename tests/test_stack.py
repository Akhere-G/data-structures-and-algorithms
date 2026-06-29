import pytest
from src.data_structures.stack import Stack


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def populated_stack():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    return stack


def test_push(empty_stack, populated_stack):
    empty_stack.push(50)

    assert empty_stack.top.value == 50

    populated_stack.push(50)

    assert populated_stack.top.value == 50


def test_pop(empty_stack, populated_stack):
    assert empty_stack.pop() is None

    assert populated_stack.pop() == 30
    assert populated_stack.pop() == 20
    assert populated_stack.pop() == 10


def test_peek(empty_stack, populated_stack):
    assert empty_stack.peek() is None
    assert populated_stack.peek() == 30
    assert populated_stack.peek() == 30


def test_is_empty(empty_stack, populated_stack):
    assert empty_stack.is_empty()
    assert not populated_stack.is_empty()
