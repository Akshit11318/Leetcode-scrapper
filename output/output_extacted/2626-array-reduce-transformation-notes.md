## Array Reduce Transformation
**Problem Link:** https://leetcode.com/problems/array-reduce-transformation/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of length `n`, and two integers `left` and `right`, reduce the array to a single number using the operations `nums[i] = nums[i] + nums[i - 1]` for `left <= i <= right - 1` and `nums[i] = nums[i] - nums[i - 1]` for `right <= i <= n - 1`.
- Expected output format: Return the final reduced number.
- Key requirements and edge cases to consider: 
    - `1 <= n <= 10^5`
    - `0 <= left <= right <= n - 1`
    - `0 <= nums[i] <= 10^9`
- Example test cases with explanations: 
    - For `nums = [1, 2, 3, 4, 5]`, `left = 1`, `right = 3`, the output should be `2`.
    - For `nums = [10, 20, 30, 40, 50]`, `left = 0`, `right = 0`, the output should be `10`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach to solve this problem is to iterate over the array from `left` to `right - 1` and perform the operation `nums[i] = nums[i] + nums[i - 1]`. Then, iterate over the array from `right` to `n - 1` and perform the operation `nums[i] = nums[i] - nums[i - 1]`.
- Step-by-step breakdown of the solution:
    1. Iterate over the array from `left` to `right - 1` and perform the operation `nums[i] = nums[i] + nums[i - 1]`.
    2. Iterate over the array from `right` to `n - 1` and perform the operation `nums[i] = nums[i] - nums[i - 1]`.
    3. Return the last element of the array as the final reduced number.
- Why this approach comes to mind first: This approach directly follows the problem description and is the most intuitive way to solve the problem.

```cpp
int reduce(vector<int>& nums, int left, int right) {
    int n = nums.size();
    // Perform addition operation from left to right - 1
    for (int i = left; i < right; i++) {
        nums[i] = nums[i] + nums[i - 1];
    }
    // Perform subtraction operation from right to n - 1
    for (int i = right; i < n; i++) {
        nums[i] = nums[i] - nums[i - 1];
    }
    // Return the last element of the array
    return nums[n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array. This is because we are iterating over the array twice.
> - **Space Complexity:** $O(1)$, as we are not using any extra space.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we are iterating over the array twice, and the space complexity is $O(1)$ because we are not using any extra space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can simplify the problem by observing the pattern of the operations. The addition operation from `left` to `right - 1` can be represented as a prefix sum, and the subtraction operation from `right` to `n - 1` can be represented as a suffix sum.
- Detailed breakdown of the approach:
    1. Calculate the prefix sum from `left` to `right - 1`.
    2. Calculate the suffix sum from `right` to `n - 1`.
    3. Return the sum of the prefix sum and the suffix sum as the final reduced number.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate over the array at least once to perform the operations.

```cpp
int reduce(vector<int>& nums, int left, int right) {
    int n = nums.size();
    long long prefixSum = 0;
    long long suffixSum = 0;
    // Calculate the prefix sum from left to right - 1
    for (int i = left; i < right; i++) {
        prefixSum += nums[i];
    }
    // Calculate the suffix sum from right to n - 1
    for (int i = right; i < n; i++) {
        suffixSum += nums[i];
    }
    // Return the sum of the prefix sum and the suffix sum
    return (int)(prefixSum + suffixSum - nums[right - 1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array. This is because we are iterating over the array twice.
> - **Space Complexity:** $O(1)$, as we are not using any extra space.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum and suffix sum.
- Problem-solving patterns identified: Simplifying the problem by observing patterns.
- Optimization techniques learned: Using prefix sum and suffix sum to simplify the problem.
- Similar problems to practice: Problems involving prefix sum and suffix sum.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly.
- Edge cases to watch for: When `left` is equal to `right`, or when `left` or `right` is equal to `n`.
- Performance pitfalls: Not using prefix sum and suffix sum to simplify the problem.
- Testing considerations: Testing the function with different inputs and edge cases.