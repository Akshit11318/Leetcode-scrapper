## Find First and Last Position of Element in Sorted Array

**Problem Link:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description

**Problem Statement:**
- Given a sorted array of integers `nums` and an integer `target`, return the indices of the first and last appearance of `target` in `nums`. If `target` is not found in `nums`, return `[-1, -1]`.
- Input format: `nums` is a sorted array of integers, and `target` is an integer.
- Expected output format: An array of two integers representing the first and last indices of `target` in `nums`.
- Key requirements and edge cases to consider:
  - The input array `nums` is sorted in ascending order.
  - The `target` may not be present in `nums`.
  - If `target` is present, it may appear multiple times.
- Example test cases with explanations:
  - `nums = [5, 7, 7, 8, 8, 10], target = 8` should return `[3, 4]`.
  - `nums = [5, 7, 7, 8, 8, 10], target = 6` should return `[-1, -1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through the array `nums` and find the first and last occurrences of `target`.
- Step-by-step breakdown of the solution:
  1. Initialize two variables, `first` and `last`, to store the indices of the first and last occurrences of `target`.
  2. Iterate through the array `nums` from left to right to find the first occurrence of `target`.
  3. If `target` is found, update the `first` variable with the current index.
  4. Iterate through the array `nums` from right to left to find the last occurrence of `target`.
  5. If `target` is found, update the `last` variable with the current index.
  6. Return the `first` and `last` indices.

```cpp
vector<int> searchRange(vector<int>& nums, int target) {
    int first = -1, last = -1;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == target) {
            if (first == -1) {
                first = i;
            }
            last = i;
        }
    }
    return {first, last};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array `nums`, because we are iterating through the array twice in the worst case.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the `first` and `last` indices.
> - **Why these complexities occur:** The brute force approach has a linear time complexity because we are iterating through the array twice, and a constant space complexity because we are using a fixed amount of space to store the indices.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a modified binary search algorithm to find the first and last occurrences of `target` in the sorted array `nums`.
- Detailed breakdown of the approach:
  1. Define a helper function `binarySearch` that takes a boolean `findFirst` as an argument.
  2. If `findFirst` is `true`, the function returns the index of the first occurrence of `target`. Otherwise, it returns the index of the last occurrence.
  3. Use the `binarySearch` function to find the first and last occurrences of `target`.
- Proof of optimality: The modified binary search algorithm has a logarithmic time complexity, which is optimal for searching in a sorted array.

```cpp
vector<int> searchRange(vector<int>& nums, int target) {
    int first = findFirst(nums, target);
    int last = findLast(nums, target);
    return {first, last};
}

int findFirst(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    int first = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            first = mid;
            right = mid - 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return first;
}

int findLast(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    int last = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            last = mid;
            left = mid + 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return last;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the size of the input array `nums`, because we are using a modified binary search algorithm to find the first and last occurrences of `target`.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the indices.
> - **Optimality proof:** The modified binary search algorithm has a logarithmic time complexity, which is optimal for searching in a sorted array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Modified binary search algorithm for finding the first and last occurrences of an element in a sorted array.
- Problem-solving patterns identified: Using a helper function to simplify the solution and improve readability.
- Optimization techniques learned: Modifying the binary search algorithm to find the first and last occurrences of an element.
- Similar problems to practice: Finding the first and last occurrences of an element in an unsorted array, finding the median of a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when the `target` is not present in the array.
- Edge cases to watch for: When the `target` is present at the beginning or end of the array, when the `target` is present multiple times in the array.
- Performance pitfalls: Using a linear search algorithm instead of a modified binary search algorithm.
- Testing considerations: Testing the solution with different input cases, including edge cases and boundary cases.