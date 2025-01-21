## Minimum Cost to Merge Stones

**Problem Link:** https://leetcode.com/problems/minimum-cost-to-merge-stones/description

**Problem Statement:**
- Input format and constraints: The problem involves merging stones represented by an array of integers, `stones`, where each integer represents the weight of a stone. The goal is to merge the stones in a way that minimizes the total cost. The input array is guaranteed to have a length that is a power of 2 (i.e., `n = 2^k`), and the total number of stones `k` is given.
- Expected output format: The function should return the minimum cost to merge all stones into one.
- Key requirements and edge cases to consider: The cost of merging two piles of stones is the sum of the weights of the stones in the two piles. The problem requires finding the minimum cost to merge all stones into one pile.
- Example test cases with explanations: For example, given `stones = [3, 5, 1, 2, 6]` and `k = 3`, the minimum cost to merge all stones into one is `25`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible ways to merge the stones and calculating the cost for each way.
- Step-by-step breakdown of the solution:
  1. Generate all possible ways to merge the stones.
  2. For each way, calculate the cost by summing the weights of the stones in each merge operation.
  3. Keep track of the minimum cost found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is inefficient due to the large number of possible ways to merge the stones.

```cpp
int minCost(vector<int>& stones) {
    int n = stones.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + stones[i];
    }

    int k = 3; // number of piles to merge into
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
    dp[0][0] = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            for (int m = 0; m < i; m++) {
                int cost = dp[m][j - 1] + prefixSum[i] - prefixSum[m];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }

    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k \cdot n)$, where $n$ is the number of stones and $k$ is the number of piles to merge into. This is because we generate all possible ways to merge the stones and calculate the cost for each way.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the number of stones and $k$ is the number of piles to merge into. This is because we need to store the minimum cost for each way to merge the stones.
> - **Why these complexities occur:** The brute force approach has high time and space complexities due to the large number of possible ways to merge the stones and the need to store the minimum cost for each way.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using dynamic programming. We can divide the problem into smaller sub-problems and store the minimum cost for each sub-problem to avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Define a 2D array `dp` where `dp[i][j]` represents the minimum cost to merge the stones from index `i` to `j`.
  2. Initialize the `dp` array by setting `dp[i][i] = 0` for all `i`, since the cost to merge a single stone is 0.
  3. Fill the `dp` array in a bottom-up manner by considering all possible ways to merge the stones from index `i` to `j`.
  4. For each way to merge the stones, calculate the cost by summing the weights of the stones in each merge operation and add the minimum cost to merge the remaining stones.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible ways to merge the stones and store the minimum cost for each sub-problem, resulting in an optimal solution.
- Why further optimization is impossible: The dynamic programming approach has a time complexity of $O(n^2 \cdot k)$, which is optimal for this problem.

```cpp
int minCost(vector<int>& stones) {
    int n = stones.size();
    int k = 3; // number of piles to merge into

    // Calculate prefix sum
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + stones[i];
    }

    // Initialize dp array
    vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(n + 1, vector<int>(k + 1, INT_MAX)));
    for (int i = 0; i < n; i++) {
        dp[i][i][1] = 0;
    }

    // Fill dp array in a bottom-up manner
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;
            for (int m = 2; m <= k; m++) {
                for (int mid = i; mid < j; mid++) {
                    int cost = dp[i][mid][m - 1] + dp[mid + 1][j][1] + prefixSum[j + 1] - prefixSum[i];
                    dp[i][j][m] = min(dp[i][j][m], cost);
                }
            }
            dp[i][j][1] = prefixSum[j + 1] - prefixSum[i];
        }
    }

    return dp[0][n - 1][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the number of stones and $k$ is the number of piles to merge into.
> - **Space Complexity:** $O(n^2 \cdot k)$, where $n$ is the number of stones and $k$ is the number of piles to merge into.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible ways to merge the stones and store the minimum cost for each sub-problem, resulting in an optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, divide and conquer.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and storing the minimum cost for each sub-problem.
- Optimization techniques learned: Using dynamic programming to avoid redundant calculations.
- Similar problems to practice: Other dynamic programming problems, such as the 0/1 knapsack problem and the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` array, incorrect calculation of the cost.
- Edge cases to watch for: Handling the case where the number of stones is 1, handling the case where the number of piles to merge into is 1.
- Performance pitfalls: Using a brute force approach, which can result in high time and space complexities.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it produces the correct output.