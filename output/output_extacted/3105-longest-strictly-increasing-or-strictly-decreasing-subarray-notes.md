## Longest Strictly Increasing or Strictly Decreasing Subarray
**Problem Link:** https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description

**Problem Statement:**
- Input: An integer array `nums`.
- Output: The length of the longest subarray that is either strictly increasing or strictly decreasing.
- Key requirements: The subarray must be strictly increasing or strictly decreasing, meaning each element is greater than (or less than) the previous one without equality.
- Example test cases:
  - Input: `nums = [1,3,5,4,7]`
    - Output: `2`
    - Explanation: The longest strictly increasing subarray is `[1,3]` or `[3,5]`, and the longest strictly decreasing subarray is `[5,4]`.
  - Input: `nums = [1,27,27,3,5]`
    - Output: `3`
    - Explanation: The longest strictly increasing subarray is `[3,5]`, and the longest strictly decreasing subarray is `[27,3]`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray to see if it's strictly increasing or decreasing.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, check if it's strictly increasing or decreasing.
  3. Keep track of the longest subarray that meets the criteria.
- Why this approach comes to mind first: It's straightforward and ensures all possibilities are considered.

```cpp
int longestSubarray(vector<int>& nums) {
    int n = nums.size();
    int maxLength = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            vector<int> subarray(nums.begin() + i, nums.begin() + j);
            if (isStrictlyIncreasing(subarray) || isStrictlyDecreasing(subarray)) {
                maxLength = max(maxLength, (int)subarray.size());
            }
        }
    }
    return maxLength;
}

bool isStrictlyIncreasing(vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] <= arr[i - 1]) return false;
    }
    return true;
}

bool isStrictlyDecreasing(vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] >= arr[i - 1]) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ because for each subarray, we check if it's strictly increasing or decreasing, which takes linear time.
> - **Space Complexity:** $O(n)$ because we generate subarrays.
> - **Why these complexities occur:** The brute force approach generates all possible subarrays and checks each one, leading to high time complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all subarrays, we can maintain two variables, one for the length of the longest strictly increasing subarray ending at the current position and one for the longest strictly decreasing subarray.
- Detailed breakdown:
  1. Initialize `increasing` and `decreasing` arrays to store the lengths of the longest strictly increasing and decreasing subarrays ending at each position.
  2. Iterate through the array, updating `increasing` and `decreasing` based on whether the current element can extend the previous strictly increasing or decreasing subarray.
  3. Keep track of the maximum length seen so far.
- Why further optimization is impossible: We must examine each element at least once to determine if it can be part of a strictly increasing or decreasing subarray.

```cpp
int findLengthOfLCIS(vector<int>& nums) {
    if (nums.empty()) return 0;
    int n = nums.size();
    int maxLength = 1;
    int increasing = 1, decreasing = 1;
    for (int i = 1; i < n; i++) {
        if (nums[i] > nums[i - 1]) {
            increasing = decreasing + 1;
            decreasing = 1;
        } else if (nums[i] < nums[i - 1]) {
            decreasing = increasing + 1;
            increasing = 1;
        } else {
            increasing = 1;
            decreasing = 1;
        }
        maxLength = max(maxLength, max(increasing, decreasing));
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we make a single pass through the array.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space.
> - **Optimality proof:** This is optimal because we must at least read the input once, and our algorithm does so in a single pass.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and maintaining running statistics.
- Problem-solving patterns identified: Looking for ways to avoid brute force by maintaining relevant statistics.
- Optimization techniques learned: Reducing time complexity by avoiding redundant work.
- Similar problems to practice: Other dynamic programming problems involving sequences or arrays.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the `increasing` and `decreasing` variables.
- Edge cases to watch for: Handling empty input or input with a single element.
- Performance pitfalls: Failing to recognize the opportunity to use dynamic programming to reduce time complexity.
- Testing considerations: Ensure the solution works correctly for both strictly increasing and strictly decreasing subarrays, as well as for arrays that contain both types of subarrays.