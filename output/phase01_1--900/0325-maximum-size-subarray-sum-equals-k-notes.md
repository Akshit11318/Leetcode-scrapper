## Maximum Size Subarray Sum Equals K
**Problem Link:** https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 2 * 10^4`, `-1000 <= nums[i] <= 1000`, `-1 * 10^7 <= k <= 10^7`.
- Expected output format: The length of the longest subarray whose sum equals `k`. If no such subarray exists, return `0`.
- Key requirements and edge cases to consider:
  - Empty array
  - Array with a single element
  - Array with all elements equal to `k`
  - Array with all elements less than `k`
  - Array with all elements greater than `k`
- Example test cases with explanations:
  - `[1, -1, 5, 2, -3], k = 3`: The longest subarray whose sum equals `3` is `[1, 2]`.
  - `[-2, -1, 2, 1], k = 1`: The longest subarray whose sum equals `1` is `[-1, 2]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible subarrays and check if their sum equals `k`.
- Step-by-step breakdown of the solution:
  1. Iterate over the array to generate all possible subarrays.
  2. Calculate the sum of each subarray.
  3. Check if the sum equals `k`.
  4. Keep track of the maximum length of subarrays whose sum equals `k`.
- Why this approach comes to mind first: It's a straightforward and intuitive solution.

```cpp
int maxSubArrayLen(vector<int>& nums, int k) {
    int maxLength = 0;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        for (int j = i; j < nums.size(); j++) {
            sum += nums[j];
            if (sum == k) {
                maxLength = max(maxLength, j - i + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array. This is because we're generating all possible subarrays, which has a quadratic time complexity.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the maximum length and the current sum.
> - **Why these complexities occur:** The quadratic time complexity occurs because we're using two nested loops to generate all possible subarrays.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a `HashMap` to store the cumulative sum and its corresponding index.
- Detailed breakdown of the approach:
  1. Initialize a `HashMap` to store the cumulative sum and its index.
  2. Initialize the cumulative sum to `0`.
  3. Iterate over the array and update the cumulative sum.
  4. Check if the difference between the current cumulative sum and `k` exists in the `HashMap`.
  5. If it exists, update the maximum length.
- Proof of optimality: This approach has a linear time complexity, which is the best possible complexity for this problem.

```cpp
int maxSubArrayLen(vector<int>& nums, int k) {
    unordered_map<int, int> sumIndexMap;
    sumIndexMap[0] = -1; // Base case for sum = 0
    int cumulativeSum = 0;
    int maxLength = 0;
    for (int i = 0; i < nums.size(); i++) {
        cumulativeSum += nums[i];
        if (sumIndexMap.find(cumulativeSum - k) != sumIndexMap.end()) {
            maxLength = max(maxLength, i - sumIndexMap[cumulativeSum - k]);
        }
        if (sumIndexMap.find(cumulativeSum) == sumIndexMap.end()) {
            sumIndexMap[cumulativeSum] = i;
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array. This is because we're iterating over the array once.
> - **Space Complexity:** $O(n)$, as we're using a `HashMap` to store the cumulative sum and its index.
> - **Optimality proof:** This approach has a linear time complexity, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `HashMap` to store the cumulative sum and its index.
- Problem-solving patterns identified: Using a `HashMap` to store intermediate results and avoid redundant calculations.
- Optimization techniques learned: Using a `HashMap` to reduce the time complexity from quadratic to linear.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case for `sum = 0`.
- Edge cases to watch for: Empty array, array with a single element, array with all elements equal to `k`.
- Performance pitfalls: Using a brute force approach with a quadratic time complexity.
- Testing considerations: Testing with different input sizes and edge cases to ensure the solution is correct and efficient.