#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def total_length(l):
    """
    Returns the sum of the lengths of the elements in a given list of strings.
    """
    total = 0
    for x in l:
        total += len(x)
    return total


class TestTotalLength(unittest.TestCase):
    def test_total_length(self):
        self.assertEqual(total_length([]), 0)
        self.assertEqual(total_length(["One"]), 3)
        self.assertEqual(total_length(["One", "Two", "Three"]), 11)


if __name__ == "__main__":
    unittest.main()
