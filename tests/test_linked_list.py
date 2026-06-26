import pytest
from src.data_structures.linked_list import LinkedList


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def populated_list():
    ls = LinkedList()
    ls.append(10)
    ls.append(20)
    ls.append(30)
    return ls


def test_initialisation(empty_list):
    assert empty_list.is_empty() is True
    assert len(empty_list) == 0
    assert empty_list.head is None
    assert empty_list.tail is None


def test_append(empty_list):
    empty_list.append(5)
    assert len(empty_list) == 1
    assert empty_list.head.value == 5
    assert empty_list.tail.value == 5

    empty_list.append(15)
    assert len(empty_list) == 2
    assert empty_list.head.value == 5
    assert empty_list.tail.value == 15


def test_prepend(empty_list):
    empty_list.prepend(5)
    assert len(empty_list) == 1
    assert empty_list.head.value == 5
    assert empty_list.tail.value == 5

    empty_list.prepend(15)
    assert len(empty_list) == 2
    assert empty_list.head.value == 15
    assert empty_list.tail.value == 5


def test_pop_front(populated_list, empty_list):
    assert populated_list.pop_front() == 10
    assert len(populated_list) == 2
    assert populated_list.head.value == 20

    assert empty_list.pop_front() is None


def test_pop_back(populated_list, empty_list):
    assert populated_list.pop_back() == 30
    assert len(populated_list) == 2
    assert populated_list.tail.value == 20

    assert empty_list.pop_back() is None


def test_pop_back_single_item():
    ls = LinkedList()
    ls.append(100)
    assert ls.pop_back() == 100
    assert ls.is_empty() is True
    assert ls.head is None
    assert ls.tail is None


def test_get(populated_list):
    assert populated_list.get(0) == 10
    assert populated_list.get(1) == 20
    assert populated_list.get(2) == 30
    assert populated_list.get(5) is None
    assert populated_list.get(-1) is None


def test_getitem(populated_list):
    assert populated_list[0] == 10
    assert populated_list[2] == 30


def test_set(populated_list):
    populated_list.set(0, 1)
    populated_list.set(1, 2)
    populated_list.set(2, 3)

    assert populated_list.head.value == 1
    assert populated_list.get(1) == 2
    assert populated_list.tail.value == 3


def test_setitem(populated_list):
    populated_list[0] = 1
    populated_list[1] = 2
    populated_list[2] = 3

    assert populated_list.head.value == 1
    assert populated_list.get(1) == 2
    assert populated_list.tail.value == 3


def test_insert(populated_list, empty_list):
    empty_list.insert(0, 0)

    assert empty_list.head.value == 0
    assert empty_list.length == 1

    populated_list.insert(0, 5)
    populated_list.insert(4, 40)

    assert populated_list.head.value == 5
    assert populated_list.tail.value == 40
    assert populated_list.length == 5


def test_getitem_out_of_bounds(populated_list):
    # pytest.raises checks that the correct error is thrown
    with pytest.raises(IndexError, match="Index out of range"):
        _ = populated_list[5]

    with pytest.raises(IndexError):
        _ = populated_list[-1]


def test_contains(populated_list):
    assert populated_list.contains(20) is True
    assert populated_list.contains(99) is False
    # Testing the __contains__ dunder method
    assert 10 in populated_list
    assert 50 not in populated_list


def test_iteration(populated_list):
    items = [item for item in populated_list]
    assert items == [10, 20, 30]


def test_clear(populated_list):
    populated_list.clear()
    assert populated_list.is_empty() is True
    assert len(populated_list) == 0
    assert populated_list.head is None
    assert populated_list.tail is None


def test_to_list(populated_list, empty_list):
    assert populated_list.to_list() == [10, 20, 30]
    assert empty_list.to_list() == []
