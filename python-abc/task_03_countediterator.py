#!/usr/bin/env python3
"""
CountedIterator: Tracks the number of iterated items.
"""


class CountedIterator:
    def __init__(self, iterable):
        """Initialize iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Get next item and increment counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return iteration count."""
        return self.count
