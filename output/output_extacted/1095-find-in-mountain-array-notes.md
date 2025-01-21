## Find in Mountain Array

**Problem Link:** https://leetcode.com/problems/find-in-mountain-array/description

**Problem Statement:**
- Input format: A `MountainArray` object and a target integer `target`.
- Constraints: The mountain array is sorted in ascending order up to a peak element, then sorted in descending order.
- Expected output format: The index of the target element if it exists in the mountain array, otherwise -1.
- Key requirements and edge cases to consider:
  - The mountain array is guaranteed to have a peak element.
  - The target element may not exist in the mountain array.
  - The mountain array may contain duplicate elements.

**Example Test Cases:**

* Example 1:
  - Input: `mountain_arr = [1, 2, 3, 1]`, `target = 2`
  - Output: `1`
* Example 2:
  - Input: `mountain_arr = [0, 1, 2, 4, 2, 1, 3]`, `target = 3`
  - Output: `6`

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to find an element in an array is to check each element one by one.
- Step-by-step breakdown of the solution:
  1. Iterate through the mountain array from left to right.
  2. For each element, check if it matches the target element.
  3. If a match is found, return the index of the element.
  4. If the iteration completes without finding a match, return -1.

```cpp
class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        for (int i = 0; i < n; i++) {
            if (mountainArr.get(i) == target) {
                return i;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the mountain array. This is because in the worst case, we need to iterate through the entire array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the index and the target element.
> - **Why these complexities occur:** The brute force approach involves checking each element in the array, resulting in linear time complexity. The space complexity is constant because we do not use any data structures that grow with the input size.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The mountain array has a peak element, and the elements before the peak are in ascending order, while the elements after the peak are in descending order. We can use a modified binary search algorithm to find the target element.
- Detailed breakdown of the approach:
  1. Find the peak element in the mountain array using binary search.
  2. Perform a binary search on the left half of the mountain array (before the peak) to find the target element.
  3. If the target element is not found in the left half, perform a binary search on the right half (after the peak) to find the target element.

```cpp
class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        int peakIndex = findPeak(mountainArr, 0, n - 1);
        int result = binarySearch(mountainArr, 0, peakIndex, target, true);
        if (result != -1) {
            return result;
        }
        return binarySearch(mountainArr, peakIndex + 1, n - 1, target, false);
    }
    
    int findPeak(MountainArray &mountainArr, int left, int right) {
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
    
    int binarySearch(MountainArray &mountainArr, int left, int right, int target, bool ascending) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (mountainArr.get(mid) == target) {
                return mid;
            }
            if (ascending) {
                if (mountainArr.get(mid) < target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                if (mountainArr.get(mid) < target) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the mountain array. This is because we use binary search to find the peak element and the target element.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the indices and the target element.
> - **Optimality proof:** The optimal approach involves using binary search, which has a logarithmic time complexity. This is the best possible time complexity for searching in a sorted array.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, modified binary search for mountain arrays.
- Problem-solving patterns identified: Using a peak element to divide the array into two sorted halves.
- Optimization techniques learned: Using binary search to reduce the time complexity from linear to logarithmic.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the binary search algorithm or not handling the peak element correctly.
- Edge cases to watch for: Handling the case where the target element is the peak element or is not present in the array.
- Performance pitfalls: Using a brute force approach instead of binary search, resulting in a higher time complexity.
- Testing considerations: Testing the solution with different mountain arrays and target elements to ensure correctness.