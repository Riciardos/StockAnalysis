"""Utility classes and functions."""


class Node(object):
    """Node used for linked lists."""
    def __init__(self, data):
        self.data = data  # contains data
        self.next = None  # contains reference to next node


class RSILL(object):
    """Custom linked list class for RSI so calculating the average can be done in constant time."""
    def __init__(self, max_length):
        self.first = None
        self.last = None
        self.length = 0
        self.max_length = max_length
        self.full = False
        self.sum = 0

    def __len__(self):
        return self.length

    def add_node(self,data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = new_node
            self.last.next = None

        self.sum += new_node.data
        self.length += 1
        if self.length > self.max_length:
            self.pop_first()

    def pop_first(self):
        # Sets second node to first, deletes first and returns value of first
        first_data = self.first.data
        self.sum -= first_data
        second = self.first.next
        self.first.next = None
        self.first = second
        self.length -= 1
        return first_data

    def average(self):
        return self.sum/self.length

    def is_full(self):
        if self.length >= self.max_length:
            return True
        else:
            return False

    def print_all(self):
        node = self.first
        print("Start")
        while node:
            print(node.data)
            node = node.next
        print("End")


def folding(array):
    """Folds a 1D array on itself, meaning array[0] += array[-1], array[1] += array [-2] ect.
    Second half is all flattened to zero."""

    for i in range(0,len(array)//2):
        array[i] += array[-(i + 1)]

    for i in range(len(array)//2, len(array)):
        array[i] = 0

    return array