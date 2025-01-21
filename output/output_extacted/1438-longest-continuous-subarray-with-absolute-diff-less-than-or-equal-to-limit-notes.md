## Longest Continuous Subarray with Absolute Diff Less Than or Equal to Limit

**Problem Link:** https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and an integer `limit`, find the length of the longest subarray in which the absolute difference between any two elements is less than or equal to `limit`.
- Expected output format: Return the length of the longest subarray.
- Key requirements and edge cases to consider: The array can be empty, and the limit can be any integer.
- Example test cases with explanations:
  - `nums = [8,2,4,7]`, `limit = 4` => The longest subarray is `[2,4,7]`.
  - `nums = [10,1,2,4,7,2]`, `limit = 5` => The longest subarray is `[1,2,4,7,2]`.
  - `nums = [4,2,2,2,4,4,2,2]`, `limit = 0` => The longest subarray is `[2,2,2,2]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can generate all possible subarrays and check if the absolute difference between any two elements is less than or equal to the limit.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, calculate the maximum and minimum values.
  3. Check if the absolute difference between the maximum and minimum values is less than or equal to the limit.
  4. Keep track of the longest subarray that satisfies the condition.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible subarrays.

```cpp
int longestSubarray(vector<int>& nums, int limit) {
    int n = nums.size();
    int maxLength = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int maxVal = INT_MIN;
            int minVal = INT_MAX;
            for (int k = i; k <= j; k++) {
                maxVal = max(maxVal, nums[k]);
                minVal = min(minVal, nums[k]);
            }
            if (maxVal - minVal <= limit) {
                maxLength = max(maxLength, j - i + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the array. This is because we have three nested loops.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it generates all possible subarrays and checks each one. The space complexity is low because we only need to keep track of a few variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a deque to keep track of the maximum and minimum values in the current window.
- Detailed breakdown of the approach:
  1. Initialize two deques, `maxDeque` and `minDeque`, to keep track of the maximum and minimum values in the current window.
  2. Initialize the window boundaries, `left` and `right`, to 0.
  3. Move the `right` boundary to the right and update the deques accordingly.
  4. If the difference between the maximum and minimum values in the current window is greater than the limit, move the `left` boundary to the right and update the deques accordingly.
  5. Keep track of the maximum length of the subarray that satisfies the condition.
- Why further optimization is impossible: The optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
int longestSubarray(vector<int>& nums, int limit) {
    int n = nums.size();
    int maxLength = 0;
    deque<int> maxDeque;
    deque<int> minDeque;
    int left = 0;
    for (int right = 0; right < n; right++) {
        while (!maxDeque.empty() && nums[right] >= nums[maxDeque.back()]) {
            maxDeque.pop_back();
        }
        maxDeque.push_back(right);
        while (!minDeque.empty() && nums[right] <= nums[minDeque.back()]) {
            minDeque.pop_back();
        }
        minDeque.push_back(right);
        while (nums[maxDeque.front()] - nums[minDeque.front()] > limit) {
            left++;
            if (maxDeque.front() < left) {
                maxDeque.pop_front();
            }
            if (minDeque.front() < left) {
                minDeque.pop_front();
            }
        }
        maxLength = max(maxLength, right - left + 1);
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array. This is because we only iterate through the array once.
> - **Space Complexity:** $O(n)$, as we use two deques to keep track of the maximum and minimum values in the current window.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem. This is because we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a deque to keep track of the maximum and minimum values in a window.
- Problem-solving patterns identified: Using a sliding window approach to solve problems that involve finding a subarray that satisfies a certain condition.
- Optimization techniques learned: Using a deque to reduce the time complexity of the algorithm.
- Similar problems to practice: Finding the longest subarray with a sum less than or equal to a certain limit.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the deques correctly when moving the window boundaries.
- Edge cases to watch for: Handling the case where the input array is empty.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the algorithm with different input arrays and limits to ensure that it works correctly.