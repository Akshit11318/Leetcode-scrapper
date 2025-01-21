## Largest Sum of Averages

**Problem Link:** https://leetcode.com/problems/largest-sum-of-averages/description

**Problem Statement:**
- Input format: `nums` (a list of integers) and `k` (an integer representing the number of partitions)
- Constraints: $1 \leq k \leq n \leq 100$, where $n$ is the length of `nums`
- Expected output format: The maximum sum of `k` averages
- Key requirements and edge cases to consider: Handling cases where `k` is 1 or equal to `n`, and ensuring the sum of averages is maximized
- Example test cases with explanations:
  - For `nums = [9, 1, 2, 3, 9]` and `k = 3`, the output should be `20.0`, because the optimal partition is `[9], [1, 2, 3], [9]`, resulting in averages of `9.0, 2.0, 9.0`, summing to `20.0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible partitions of the array and calculate the sum of averages for each partition
- Step-by-step breakdown of the solution:
  1. Generate all possible partitions of the array
  2. For each partition, calculate the average of each subset
  3. Sum the averages of each subset
  4. Keep track of the maximum sum found
- Why this approach comes to mind first: It is a straightforward, exhaustive approach that guarantees finding the maximum sum of averages by considering every possible partition.

```cpp
#include <vector>
#include <numeric>

double largestSumOfAverages(vector<int>& nums, int k) {
    int n = nums.size();
    vector<double> prefixSum(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }

    double maxSum = 0.0;
    // Generate all possible partitions
    vector<int> partition;
    function<void(int)> backtrack = [&](int start) {
        if (partition.size() == k - 1) {
            // Calculate sum of averages for this partition
            double sum = 0.0;
            int prev = 0;
            for (int i = 0; i < partition.size(); ++i) {
                sum += (prefixSum[partition[i]] - prefixSum[prev]) / (partition[i] - prev);
                prev = partition[i];
            }
            sum += (prefixSum[n] - prefixSum[prev]) / (n - prev);
            maxSum = max(maxSum, sum);
            return;
        }
        for (int i = start; i < n; ++i) {
            partition.push_back(i);
            backtrack(i + 1);
            partition.pop_back();
        }
    };
    backtrack(1);
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n^{k})$, where $n$ is the length of `nums`, because we generate all possible partitions and calculate the sum of averages for each
> - **Space Complexity:** $O(n)$, for storing the prefix sum array and the recursion stack
> - **Why these complexities occur:** The time complexity is high due to generating all possible partitions, and the space complexity is moderate due to the need for storing the prefix sum array and recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using dynamic programming to store and reuse the results of subproblems, specifically the maximum sum of averages for each prefix of the array and each number of partitions
- Detailed breakdown of the approach:
  1. Initialize a 2D table `dp` where `dp[i][j]` represents the maximum sum of averages for the first `i` elements and `j` partitions
  2. Fill the table in a bottom-up manner, considering each possible partition and calculating the maximum sum of averages
  3. The final result is stored in `dp[n][k]`
- Proof of optimality: This approach is optimal because it avoids redundant calculations by storing and reusing the results of subproblems, ensuring that each subproblem is solved only once.

```cpp
double largestSumOfAverages(vector<int>& nums, int k) {
    int n = nums.size();
    vector<double> prefixSum(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }

    vector<vector<double>> dp(n + 1, vector<double>(k + 1, 0.0));
    for (int i = 1; i <= n; ++i) {
        dp[i][1] = prefixSum[i] / i;
    }

    for (int j = 2; j <= k; ++j) {
        for (int i = j; i <= n; ++i) {
            for (int x = j - 1; x < i; ++x) {
                dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefixSum[i] - prefixSum[x]) / (i - x));
            }
        }
    }

    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n^2)$, because we fill the 2D table in a bottom-up manner, considering each possible partition
> - **Space Complexity:** $O(k \cdot n)$, for storing the 2D table
> - **Optimality proof:** This approach is optimal because it avoids redundant calculations by storing and reusing the results of subproblems, ensuring that each subproblem is solved only once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, partitioning, and calculation of averages
- Problem-solving patterns identified: Breaking down the problem into subproblems, storing and reusing results, and considering all possible partitions
- Optimization techniques learned: Avoiding redundant calculations and using dynamic programming to store and reuse results
- Similar problems to practice: Other dynamic programming problems, such as the `Partition Equal Subset Sum` problem

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize the 2D table correctly, not considering all possible partitions, and not storing and reusing results correctly
- Edge cases to watch for: Handling cases where `k` is 1 or equal to `n`, and ensuring the sum of averages is maximized
- Performance pitfalls: Failing to avoid redundant calculations, resulting in high time complexity
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure correctness and performance.