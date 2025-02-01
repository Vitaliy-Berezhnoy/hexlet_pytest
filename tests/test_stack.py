import pytest


def test_stack():
    stack = []
    assert not stack
    stack.append('1')
    stack.append('2')
    assert stack.pop() == '2'
    assert stack.pop() == '1'


def test_emptiness():
    stack = []
    assert not stack
    stack.append('1')
    assert bool(stack)   # not not stack
    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
