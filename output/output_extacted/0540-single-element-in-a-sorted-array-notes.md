## Single Element in a Sorted Array
**Problem Link:** https://leetcode.com/problems/single-element-in-a-sorted-array/description

**Problem Statement:**
- Input: A sorted array of integers where every element appears twice except one.
- Constraints: The array is sorted, and there is exactly one element that appears only once.
- Expected Output: The single element that appears only once in the array.
- Key Requirements: The solution must find the single element efficiently, considering the array's sorted nature.
- Edge Cases: Empty array, array with only one element, and array with all elements appearing twice except one.

Example Test Cases:
- `[1, 1, 2, 3, 3, 4, 4, 8, 8]` returns `2`.
- `[3, 3, 7, 7, 10, 11, 11]` returns `10`.
- `[1]` returns `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each element in the array to see if it appears only once.
- This approach comes to mind first because it's straightforward and easy to implement.
- However, it's inefficient due to its linear search nature and the need to potentially scan the entire array for each element.

```cpp
int singleNonDuplicate(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) {
        bool found = false;
        for (int j = 0; j < nums.size(); j++) {
            if (i != j && nums[i] == nums[j]) {
                found = true;
                break;
            }
        }
        if (!found) return nums[i];
    }
    return -1; // Should not reach here
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because for each element, we potentially scan the entire array again.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the result and loop counters.
> - **Why these complexities occur:** The brute force approach involves nested loops, leading to quadratic time complexity, but it doesn't require additional space that scales with input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a binary search approach, taking advantage of the array's sorted nature.
- We divide the array into two halves and determine which half the single element is likely to be in by comparing the middle element with its adjacent one.
- This approach is optimal because it reduces the search space by half at each step, similar to binary search in a sorted array.

```cpp
int singleNonDuplicate(vector<int>& nums) {
    int low = 0, high = nums.size() - 1;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (mid % 2 == 1) mid--; // Ensure mid is even for comparison
        if (nums[mid] == nums[mid + 1]) low = mid + 2;
        else high = mid;
    }
    return nums[low];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ because with each iteration, we halve the search space.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the result and loop counters.
> - **Optimality proof:** This is the best possible time complexity for this problem because we must at least look at each element once to ensure we find the single one, and binary search allows us to do this in logarithmic time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of binary search for efficient searching in sorted arrays.
- Problem-solving patterns identified include exploiting the properties of the input (sorted array with a single unique element) to reduce the problem's complexity.
- Optimization techniques learned include reducing the search space by half at each step.
- Similar problems to practice include other binary search problems and finding unique elements in arrays.

**Mistakes to Avoid:**
- Common implementation errors include incorrect handling of edge cases (like an empty array or an array with a single element) and failure to initialize variables properly.
- Edge cases to watch for include arrays with duplicate elements at the beginning or end and arrays with an odd number of elements.
- Performance pitfalls include using inefficient algorithms (like the brute force approach for large inputs) and not considering the input's properties to optimize the solution.
- Testing considerations include testing with various input sizes, including edge cases, to ensure the solution's correctness and efficiency.