## Number of Subarrays with Bounded Maximum
**Problem Link:** https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` and two integers `left` and `right`, find the number of non-empty subarrays such that the value of the maximum element in the subarray is in the range `[left, right]`.
- Expected output format: The number of subarrays that satisfy the condition.
- Key requirements and edge cases to consider: Handle edge cases where `left` is greater than `right`, or when the input array is empty.
- Example test cases with explanations:
  - For `nums = [2, 1, 4, 3]`, `left = 2`, and `right = 3`, the output should be `3` because the subarrays `[2]`, `[2, 1]`, and `[3]` satisfy the condition.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Check every possible subarray to see if the maximum element falls within the given range.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, find the maximum element.
  3. Check if the maximum element is within the range `[left, right]`.
  4. Count the subarrays that satisfy the condition.

```cpp
int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            int maxVal = INT_MIN;
            for (int k = i; k <= j; k++) {
                maxVal = max(maxVal, nums[k]);
            }
            if (maxVal >= left && maxVal <= right) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we are generating all possible subarrays ($O(n^2)$) and for each subarray, we are finding the maximum element ($O(n)$).
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves checking every possible subarray and finding the maximum element in each, leading to cubic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every subarray, we can maintain a window of elements that satisfy the condition and slide this window over the array.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `start` and `end`, to represent the window.
  2. Initialize a variable `count` to store the number of subarrays that satisfy the condition.
  3. Iterate over the array with the `end` pointer.
  4. For each element, check if it is within the range `[left, right]`. If it is, update the `count` by adding the number of subarrays that can be formed with this element as the maximum.
  5. If the element is greater than `right`, move the `start` pointer to the right until the maximum element in the window is within the range `[left, right]`.
- Proof of optimality: This approach is optimal because it only requires a single pass over the array, reducing the time complexity significantly.

```cpp
int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
    int count = 0, start = 0, end = 0, lastRight = -1;
    while (end < nums.size()) {
        if (nums[end] > right) {
            start = end + 1;
            lastRight = end;
        } else if (nums[end] >= left && nums[end] <= right) {
            lastRight = end;
        }
        if (lastRight != -1) {
            count += lastRight - start + 1;
        }
        end++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we are making a single pass over the array.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the number of subarrays that satisfy the condition.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, optimization of brute force approaches.
- Problem-solving patterns identified: Looking for ways to reduce the number of operations by maintaining a window of relevant data.
- Optimization techniques learned: Using a single pass over the data instead of generating all possible subarrays.
- Similar problems to practice: Other problems that involve finding the number of subarrays that satisfy certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the `start` pointer correctly when an element greater than `right` is encountered.
- Edge cases to watch for: Handling the case where `left` is greater than `right`, or when the input array is empty.
- Performance pitfalls: Using the brute force approach for large inputs, which can lead to cubic time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it produces the correct output.