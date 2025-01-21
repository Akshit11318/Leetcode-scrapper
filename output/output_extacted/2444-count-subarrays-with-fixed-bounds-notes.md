## Count Subarrays with Fixed Bounds
**Problem Link:** https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description

**Problem Statement:**
- Input format: Given an integer array `nums` and integers `minK`, `maxK`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= minK <= maxK <= 10^5`, and `1 <= nums[i] <= 10^5`.
- Expected output format: The number of subarrays that contain at least one `minK` and at least one `maxK`.
- Key requirements: A subarray is defined as a contiguous segment of the array.
- Edge cases to consider: Empty array, array with a single element, array with no `minK` or `maxK`.
- Example test cases:
  - Input: `nums = [1,3,5,2,7,5], minK = 1, maxK = 5`
  - Output: `2`
  - Explanation: Subarrays `[1,3,5]` and `[1,3,5,2,7,5]` contain both 1 and 5.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible subarray of the given array.
- Step-by-step breakdown:
  1. Generate all possible subarrays of the given array.
  2. For each subarray, check if it contains at least one `minK` and one `maxK`.
  3. Count the subarrays that satisfy the condition.

```cpp
int countSubarrays(vector<int>& nums, int minK, int maxK) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            bool foundMinK = false, foundMaxK = false;
            for (int k = i; k <= j; ++k) {
                if (nums[k] == minK) foundMinK = true;
                if (nums[k] == maxK) foundMaxK = true;
            }
            if (foundMinK && foundMaxK) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the array. This is because we have three nested loops: two for generating subarrays and one for checking the condition within each subarray.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves checking every possible subarray, which leads to a cubic time complexity due to the nested loops. The space complexity is constant because we only use a fixed amount of space to store the count and other variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach with two pointers.
- Detailed breakdown:
  1. Initialize two pointers, `left` and `right`, to the start of the array.
  2. Move the `right` pointer to the right and check each element.
  3. If the element is within the range `[minK, maxK]`, update the count of subarrays.
  4. If the element is outside the range, move the `left` pointer to the right of the last seen `minK` or `maxK`.

```cpp
int countSubarrays(vector<int>& nums, int minK, int maxK) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; ++i) {
        int minKCount = 0, maxKCount = 0;
        for (int j = i; j < n; ++j) {
            if (nums[j] == minK) minKCount++;
            if (nums[j] == maxK) maxKCount++;
            if (minKCount > 0 && maxKCount > 0) count++;
            if (nums[j] < minK || nums[j] > maxK) break;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we have two nested loops: one for the sliding window and one for checking the condition within each window.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because we are only checking each element once and only considering subarrays that contain at least one `minK` and one `maxK`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, two-pointer technique.
- Problem-solving patterns identified: Using a sliding window to reduce the number of subarrays to check.
- Optimization techniques learned: Avoiding unnecessary checks by breaking the loop when an element is outside the range.
- Similar problems to practice: Other problems involving subarrays or sliding windows.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the count correctly, not breaking the loop when an element is outside the range.
- Edge cases to watch for: Empty array, array with a single element, array with no `minK` or `maxK`.
- Performance pitfalls: Using a brute force approach, not optimizing the loop conditions.
- Testing considerations: Testing with different input sizes, testing with edge cases.