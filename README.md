# MSCS532_Assignment1

Insertion Sort in **monotonically decreasing** order (Python 3.8+).

## How to run
```bash
python insertion_sort_desc.py 7 3 9 1
# -> [9, 7, 3, 1]
```

Or interactive:
```bash
python insertion_sort_desc.py
Enter numbers separated by spaces: 5 2 9 1
# -> [9, 5, 2, 1]
```

## Tests
```bash
python -m unittest
```

## Complexity & Notes
- Time: O(n^2) worst/average, O(n) best (already sorted descending).
- Space: O(1) extra (in-place).
- Stable: Yes (relative order of equals is preserved).

## Quick Verify
```bash
python -m unittest
python insertion_sort_desc.py 10 2 10 -1
# -> [10, 10, 2, -1]

## Notes
- In-place, O(1) extra space.
- Time: O(n^2) worst/average, O(n) best when already sorted descending.
