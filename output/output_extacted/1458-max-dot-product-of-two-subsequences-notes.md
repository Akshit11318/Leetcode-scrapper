## Max Dot Product of Two Subsequences

**Problem Link:** https://leetcode.com/problems/max-dot-product-of-two-subsequences/description

**Problem Statement:**
- Input: Two arrays of integers, `nums1` and `nums2`.
- Output: The maximum dot product of two subsequences of `nums1` and `nums2`.
- Key requirements: Find the maximum dot product by considering all possible subsequences.
- Edge cases: Handle cases where one or both arrays are empty.

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of both arrays and calculate their dot products.
- Step-by-step breakdown:
  1. Generate all possible subsequences of `nums1` and `nums2`.
  2. For each subsequence of `nums1`, calculate the dot product with each subsequence of `nums2`.
  3. Keep track of the maximum dot product found.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach to ensure no possible solution is missed.

```cpp
#include <vector>
#include <algorithm>

int maxDotProduct(std::vector<int>& nums1, std::vector<int>& nums2) {
    int n = nums1.size();
    int m = nums2.size();
    int maxProduct = -1e9; // Initialize with a very small number

    // Generate all possible subsequences
    for (int mask1 = 0; mask1 < (1 << n); ++mask1) {
        for (int mask2 = 0; mask2 < (1 << m); ++mask2) {
            std::vector<int> subseq1, subseq2;
            for (int i = 0; i < n; ++i) {
                if ((mask1 & (1 << i)) != 0) {
                    subseq1.push_back(nums1[i]);
                }
            }
            for (int j = 0; j < m; ++j) {
                if ((mask2 & (1 << j)) != 0) {
                    subseq2.push_back(nums2[j]);
                }
            }

            // Calculate dot product of current subsequences
            if (!subseq1.empty() && !subseq2.empty()) {
                int dotProduct = 0;
                for (int k = 0; k < std::min(subseq1.size(), subseq2.size()); ++k) {
                    dotProduct += subseq1[k] * subseq2[k];
                }
                maxProduct = std::max(maxProduct, dotProduct);
            }
        }
    }

    return maxProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot 2^m \cdot \min(n, m))$ because we generate all possible subsequences (each of length up to $n$ or $m$) and calculate their dot products.
> - **Space Complexity:** $O(n + m)$ for storing the subsequences.
> - **Why these complexities occur:** The brute force approach requires generating all possible subsequences and calculating their dot products, leading to exponential time complexity due to the number of subsequences and linear space complexity for storing the subsequences.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store and reuse the results of subproblems, reducing the computational complexity.
- Detailed breakdown:
  1. Initialize a 2D DP table `dp` where `dp[i][j]` represents the maximum dot product of the first `i` elements of `nums1` and the first `j` elements of `nums2`.
  2. Fill the DP table by considering whether to include the current elements in the dot product or not.
  3. The final answer is stored in `dp[n][m]`.

```cpp
int maxDotProduct(std::vector<int>& nums1, std::vector<int>& nums2) {
    int n = nums1.size();
    int m = nums2.size();
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, -1e9));

    // Base case: Empty subsequences have a dot product of 0
    for (int i = 0; i <= n; ++i) {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= m; ++j) {
        dp[0][j] = 0;
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            // Consider including the current elements in the dot product
            int include = dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1];
            // Consider excluding the current elements from the dot product
            int exclude1 = dp[i - 1][j];
            int exclude2 = dp[i][j - 1];
            // Choose the maximum of the three options
            dp[i][j] = std::max({include, exclude1, exclude2, 0});
        }
    }

    return dp[n][m];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ because we fill a 2D DP table of size $(n + 1) \times (m + 1)$.
> - **Space Complexity:** $O(n \cdot m)$ for the DP table.
> - **Optimality proof:** This approach is optimal because it considers all possible subsequences and their dot products in a systematic way, avoiding redundant calculations through dynamic programming.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, dot product calculation.
- Problem-solving patterns: Breaking down problems into subproblems and reusing their solutions.
- Optimization techniques: Avoiding redundant calculations through memoization or dynamic programming.

**Mistakes to Avoid:**
- Not considering all possible subsequences.
- Not using dynamic programming to optimize the solution.
- Incorrectly calculating the dot product of subsequences.