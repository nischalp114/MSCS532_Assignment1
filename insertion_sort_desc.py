#!/usr/bin/env python3
"""
Insertion Sort (descending / monotonically decreasing).

This implementation sorts the list in-place for O(1) extra space.
Time complexity: O(n^2) worst/average, O(n) best (already sorted descending).
"""

from typing import List, Any

def insertion_sort_desc(a: List[Any]) -> None:
    """
    Sorts the list 'a' in-place into monotonically decreasing order.

    Example:
        a = [5, 2, 9, 1]
        insertion_sort_desc(a)
        # a -> [9, 5, 2, 1]
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # For decreasing order: shift while a[j] < key
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def main() -> None:
    import sys
    if len(sys.argv) > 1:
        # Example: python insertion_sort_desc.py 7 3 9 1
        arr = [int(x) for x in sys.argv[1:]]
    else:
        raw = input("Enter numbers separated by spaces: ").strip()
        arr = [int(x) for x in raw.split()] if raw else []

    insertion_sort_desc(arr)
    print(arr)


if __name__ == "__main__":
    main()
