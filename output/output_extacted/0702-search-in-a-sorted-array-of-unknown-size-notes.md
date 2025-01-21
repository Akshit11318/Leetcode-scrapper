## Search in a Sorted Array of Unknown Size

**Problem Link:** https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description

**Problem Statement:**
- Input format and constraints: We are given an API `ArrayReader` which has a method `int query(int index)` that returns the value at a given index in the sorted array. We need to find the index of a target value in the sorted array.
- Expected output format: The index of the target value in the sorted array if it exists, otherwise -1.
- Key requirements and edge cases to consider:
  - The size of the array is unknown.
  - The array is sorted in ascending order.
  - The target value may or may not exist in the array.
- Example test cases with explanations:
  - If the target value is in the array, return its index.
  - If the target value is not in the array, return -1.
  - If the array is empty, return -1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try to find the target value by checking every element in the array.
- Step-by-step breakdown of the solution:
  1. Start from index 0 and keep querying the `ArrayReader` until we find the target value or reach the end of the array.
  2. If we find the target value, return its index.
  3. If we reach the end of the array without finding the target value, return -1.
- Why this approach comes to mind first: It is the most straightforward way to find an element in an array.

```cpp
class Solution {
public:
    int search(ArrayReader* reader, int target) {
        int index = 0;
        while (true) {
            int val = reader->query(index);
            if (val == target) {
                return index;
            } else if (val > target) {
                return -1; // since the array is sorted
            }
            index++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the size of the array, because in the worst case we need to query every element in the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the index and the value.
> - **Why these complexities occur:** The time complexity is linear because we are potentially checking every element in the array, and the space complexity is constant because we are not using any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a modified binary search algorithm to find the target value in the sorted array.
- Detailed breakdown of the approach:
  1. First, we need to find the upper bound of the array by repeatedly querying the `ArrayReader` with increasing indices until we find a value that is greater than the target value or we reach the end of the array.
  2. Once we have the upper bound, we can use binary search to find the target value within the range of indices we have determined.
- Proof of optimality: This approach is optimal because we are reducing the search space by half at each step, which is the best we can do for a sorted array.
- Why further optimization is impossible: We are already using the most efficient algorithm for searching a sorted array, which is binary search.

```cpp
class Solution {
public:
    int search(ArrayReader* reader, int target) {
        int right = 1;
        while (reader->query(right) < target) {
            right *= 2;
        }
        int left = 0;
        while (left < right) {
            int mid = left + (right - left) / 2;
            int val = reader->query(mid);
            if (val == target) {
                return mid;
            } else if (val < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ where $n$ is the size of the array, because we are using binary search to find the target value.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the indices and the value.
> - **Optimality proof:** The time complexity is logarithmic because we are reducing the search space by half at each step, which is the best we can do for a sorted array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, modified binary search for unknown size array.
- Problem-solving patterns identified: Using binary search to find an element in a sorted array.
- Optimization techniques learned: Reducing the search space by half at each step.
- Similar problems to practice: Searching in a rotated sorted array, searching in a sorted matrix.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the end of the array, not handling the case where the target value is not in the array.
- Edge cases to watch for: The array is empty, the target value is at the beginning or end of the array.
- Performance pitfalls: Using a linear search algorithm instead of binary search.
- Testing considerations: Test the algorithm with different sizes of arrays, different target values, and edge cases.