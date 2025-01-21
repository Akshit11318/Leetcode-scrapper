## Number of Subarrays with Bounded Maximum
**Problem Link:** https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description

**Problem Statement:**
- Input: An array of integers `nums` and two integers `left` and `right`.
- Output: The number of contiguous subarrays such that the maximum of the subarray is in the range `[left, right]`.
- Key Requirements:
  - The subarray must be contiguous.
  - The maximum of the subarray must be within the given range `[left, right]`.
- Example Test Cases:
  - `nums = [2, 1, 4, 3], left = 2, right = 3` should return `3` because the subarrays are `[2], [2, 1], [3]`.
  - `nums = [2, 9, 2, 5, 6], left = 2, right = 8` should return `7` because the subarrays are `[2], [2, 9], [2, 9, 2], [2, 9, 2, 5], [2], [2, 5], [2, 5, 6]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible subarray to see if its maximum falls within the given range.
- This involves iterating over the array with two nested loops to generate all possible subarrays, and then checking each subarray's maximum.
- This approach comes to mind first because it's straightforward and directly addresses the problem statement.

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
> - **Time Complexity:** $O(n^3)$ where $n$ is the size of the input array `nums`. This is because we have three nested loops.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we only use a constant amount of space to store the count and the maximum value.
> - **Why these complexities occur:** The cubic time complexity arises from generating all possible subarrays and then finding the maximum of each, which involves iterating over the subarray. The constant space complexity is due to only using a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a sliding window approach, maintaining two pointers, `start` and `end`, to represent the current subarray.
- We also keep track of the maximum value within the current window.
- When the maximum value exceeds `right`, we move the `start` pointer to the right until the maximum value is within the range `[left, right]`.
- We count the number of valid subarrays ending at the `end` pointer.
- This approach is optimal because it reduces the time complexity significantly by avoiding redundant calculations and only considering valid subarrays.

```cpp
int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
    int res = 0, start = 0, end = 0, count = 0, maxVal = INT_MIN;
    while (end < nums.size()) {
        maxVal = max(maxVal, nums[end]);
        while (maxVal > right && start <= end) {
            if (nums[start] == maxVal) maxVal = INT_MIN;
            start++;
        }
        count = end - start + 1;
        if (maxVal >= left) {
            res += count;
        }
        end++;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the size of the input array `nums`. This is because we only make one pass through the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we only use a constant amount of space to store the pointers, count, and maximum value.
> - **Optimality proof:** This is the best possible time complexity because we must at least look at each element once to determine the number of valid subarrays.

---

### Final Notes

**Learning Points:**
- The importance of the sliding window technique in array and string problems.
- How to optimize brute force solutions by reducing redundant calculations and focusing on the critical aspects of the problem.
- The use of two pointers to efficiently scan through the array and maintain a window of interest.

**Mistakes to Avoid:**
- Not considering the edge cases where the maximum value of the subarray is exactly `left` or `right`.
- Failing to update the maximum value correctly when moving the window.
- Not accounting for the count of valid subarrays ending at each position correctly.