## Maximum Strength of K Disjoint Subarrays

**Problem Link:** https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/description

**Problem Statement:**
- Input: An array `nums` and an integer `k`.
- Constraints: `1 <= k <= nums.length`.
- Expected output: The maximum strength of `k` disjoint subarrays.
- Key requirements: Find the maximum sum of `k` disjoint subarrays within the given array.
- Example test cases:
  - Input: `nums = [1,1,1,1,1], k = 2`, Output: `2`
  - Input: `nums = [1,-2,1,-2,1], k = 1`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible combinations of disjoint subarrays.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, calculate its sum.
  3. Select `k` disjoint subarrays that maximize the total sum.
- Why this approach comes to mind first: It's a straightforward way to consider all possibilities, but it's inefficient due to its high complexity.

```cpp
int maxStrength(vector<int>& nums, int k) {
    int n = nums.size();
    vector<vector<int>> sums(n + 1, vector<int>(n + 1));
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            sums[i][j] = accumulate(nums.begin() + i, nums.begin() + j, 0);
        }
    }
    vector<vector<int>> dp(n + 1, vector<int>(k + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= min(i, k); ++j) {
            for (int m = 0; m < i; ++m) {
                dp[i][j] = max(dp[i][j], dp[m][j - 1] + sums[m][i]);
            }
        }
    }
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot k)$, where $n$ is the length of `nums`, because we're using three nested loops.
> - **Space Complexity:** $O(n^2 + n \cdot k)$, for storing the `sums` and `dp` arrays.
> - **Why these complexities occur:** The brute force approach involves generating all possible subarrays and then selecting the best `k` disjoint ones, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to efficiently calculate the maximum sum of `k` disjoint subarrays.
- Detailed breakdown:
  1. Calculate the prefix sum array to efficiently get the sum of any subarray.
  2. Use a dynamic programming table `dp` to store the maximum sum of `j` disjoint subarrays ending at index `i`.
  3. Iterate over the array and update `dp` based on the maximum sum of `j - 1` disjoint subarrays ending at a previous index `m`, plus the sum of the subarray from `m` to `i`.
- Proof of optimality: This approach considers all possible disjoint subarrays and selects the ones with the maximum sum, ensuring optimality.

```cpp
int maxStrength(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1);
    for (int i = 0; i < n; ++i) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    vector<vector<int>> dp(n + 1, vector<int>(k + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= min(i, k); ++j) {
            for (int m = 0; m < i; ++m) {
                dp[i][j] = max(dp[i][j], dp[m][j - 1] + prefixSum[i] - prefixSum[m]);
            }
        }
    }
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the length of `nums`, because we're using three nested loops.
> - **Space Complexity:** $O(n \cdot k)$, for storing the `dp` array.
> - **Optimality proof:** This approach considers all possible disjoint subarrays and selects the ones with the maximum sum, ensuring optimality.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, prefix sum array.
- Problem-solving patterns identified: Using dynamic programming to efficiently calculate the maximum sum of disjoint subarrays.
- Optimization techniques learned: Reducing time and space complexities by using prefix sum array and dynamic programming.
- Similar problems to practice: Maximum subarray sum, minimum window subarray.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the prefix sum array or updating the dynamic programming table.
- Edge cases to watch for: Handling cases where `k` is greater than the length of `nums`.
- Performance pitfalls: Using inefficient algorithms with high time complexities.
- Testing considerations: Testing the solution with different input sizes and values of `k`.