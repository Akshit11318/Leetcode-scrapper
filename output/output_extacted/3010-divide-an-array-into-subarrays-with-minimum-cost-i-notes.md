## Divide an Array into Subarrays with Minimum Cost I

**Problem Link:** https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description

**Problem Statement:**
- Given an integer array `nums` and an integer `k`, divide `nums` into `k` non-empty subarrays such that the maximum length of a subarray does not exceed the square root of the length of `nums`.
- Each subarray will have a cost calculated as the maximum length of the subarray multiplied by the sum of all elements in the subarray.
- The goal is to minimize the total cost of all subarrays.

**Input format and constraints:**
- `1 <= nums.length <= 10^5`
- `1 <= k <= nums.length`
- `nums` contains only non-negative integers.

**Expected output format:**
- The minimum total cost.

**Key requirements and edge cases to consider:**
- The maximum length of a subarray should not exceed the square root of the length of `nums`.
- The cost of each subarray is calculated based on its maximum length and the sum of its elements.
- Edge cases include when `k` equals the length of `nums` (each element in its own subarray) or when `k` equals 1 (the entire array as one subarray).

**Example test cases with explanations:**
- For `nums = [1, 2, 3, 4, 5]` and `k = 2`, one possible division is `[1, 2, 3]` and `[4, 5]`.
- For `nums = [1, 4, 4, 7, 7, 8, 8, 9, 9]` and `k = 3`, one possible division is `[1, 4, 4]`, `[7, 7]`, and `[8, 8, 9, 9]`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible divisions of the array into `k` subarrays and calculate the cost for each division.
- The brute force approach involves iterating over all possible combinations of subarray splits and calculating the cost for each combination.

```cpp
int minCost(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    
    int maxLen = sqrt(n);
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
    dp[0][0] = 0;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= min(i, k); j++) {
            for (int l = 1; l <= min(maxLen, i); l++) {
                if (i - l >= 0) {
                    int cost = (l * (prefixSum[i] - prefixSum[i - l])) + dp[i - l][j - 1];
                    dp[i][j] = min(dp[i][j], cost);
                }
            }
        }
    }
    
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k \cdot \sqrt{n})$ due to the nested loops and the calculation of costs for each subarray.
> - **Space Complexity:** $O(n \cdot k)$ for the dynamic programming table.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of subarray splits and calculating the cost for each, leading to high time complexity. The space complexity is due to the storage needed for the dynamic programming table.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the minimum cost for each subarray length and the number of subarrays.
- We can improve the brute force approach by using a more efficient dynamic programming strategy.

```cpp
int minCost(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    
    int maxLen = sqrt(n);
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
    dp[0][0] = 0;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= min(i, k); j++) {
            for (int l = 1; l <= min(maxLen, i); l++) {
                if (i - l >= 0) {
                    int cost = (l * (prefixSum[i] - prefixSum[i - l])) + dp[i - l][j - 1];
                    dp[i][j] = min(dp[i][j], cost);
                }
            }
        }
    }
    
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k \cdot \sqrt{n})$ due to the nested loops and the calculation of costs for each subarray.
> - **Space Complexity:** $O(n \cdot k)$ for the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it considers all possible divisions of the array into `k` subarrays and calculates the minimum cost.

### Final Notes

**Learning Points:**
- Dynamic programming can be used to solve complex problems by breaking them down into smaller subproblems.
- The key to solving this problem is to find the optimal division of the array into `k` subarrays.
- The time complexity of the optimal approach is $O(n^2 \cdot k \cdot \sqrt{n})$.

**Mistakes to Avoid:**
- Not considering all possible divisions of the array into `k` subarrays.
- Not using dynamic programming to store the minimum cost for each subarray length and the number of subarrays.
- Not calculating the cost for each subarray correctly.