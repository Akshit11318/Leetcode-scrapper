## Delete Columns to Make Sorted III

**Problem Link:** https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description

**Problem Statement:**
- Input format: A 2D array `strs` of strings, each representing a row in a table.
- Constraints: `1 <= strs.length <= 100`, `1 <= strs[i].length <= 100`.
- Expected output format: The minimum number of columns to delete to make the table sorted.
- Key requirements and edge cases to consider: The table is sorted if the entries in each row are in non-decreasing order from left to right. If there are multiple possible answers, any of them is accepted.
- Example test cases with explanations:
  - Input: `strs = ["abc","bce","cae"]`, Output: `1`.
  - Input: `strs = ["a","b"]`, Output: `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subset of columns to see if deleting them would make the table sorted.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of columns.
  2. For each subset, delete the corresponding columns from the table.
  3. Check if the resulting table is sorted.
  4. If it is, update the minimum number of columns to delete.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach to solving the problem.

```cpp
#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    int minDeletionSize(std::vector<std::string>& strs) {
        int minDeletions = INT_MAX;
        int n = strs.size();
        int m = strs[0].size();
        
        for (int mask = 0; mask < (1 << m); mask++) {
            bool isSorted = true;
            std::vector<std::string> tempStrs(n);
            
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (!(mask & (1 << j))) {
                        tempStrs[i] += strs[i][j];
                    }
                }
            }
            
            for (int i = 0; i < n - 1; i++) {
                if (tempStrs[i] > tempStrs[i + 1]) {
                    isSorted = false;
                    break;
                }
            }
            
            if (isSorted) {
                int deletions = __builtin_popcount(mask);
                minDeletions = std::min(minDeletions, deletions);
            }
        }
        
        return minDeletions;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \cdot n \cdot m)$, where $m$ is the number of columns and $n$ is the number of rows. This is because we generate all possible subsets of columns ($2^m$) and for each subset, we create a temporary table and check if it's sorted ($n \cdot m$).
> - **Space Complexity:** $O(n \cdot m)$, for storing the temporary table.
> - **Why these complexities occur:** The brute force approach is exhaustive, leading to high time complexity due to generating all subsets and checking each one.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to build up a solution. The idea is to maintain a `dp` array where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`.
- Detailed breakdown of the approach:
  1. Initialize a `dp` array of size `m`, where `dp[i]` is initially set to 1 (since a single column is always sorted).
  2. Iterate over each column. For each column, compare it with all previous columns.
  3. If the current column is not less than the previous column in any row, update `dp[i]` to be `dp[j] + 1` if it's greater than the current `dp[i]`.
  4. The minimum number of columns to delete is `m - max(dp)`, where `max(dp)` is the maximum value in the `dp` array.

```cpp
class Solution {
public:
    int minDeletionSize(std::vector<std::string>& strs) {
        int m = strs[0].size();
        std::vector<int> dp(m, 1);
        
        for (int j = 1; j < m; j++) {
            for (int i = 0; i < j; i++) {
                bool isIncreasing = true;
                int n = strs.size();
                
                for (int k = 0; k < n - 1; k++) {
                    if (strs[k][i] > strs[k][j] || strs[k][j] < strs[k + 1][j]) {
                        isIncreasing = false;
                        break;
                    }
                }
                
                if (isIncreasing) {
                    dp[j] = std::max(dp[j], dp[i] + 1);
                }
            }
        }
        
        return m - *std::max_element(dp.begin(), dp.end());
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n)$, where $m$ is the number of columns and $n$ is the number of rows. This is because for each column, we compare it with all previous columns and check if the subsequence is increasing.
> - **Space Complexity:** $O(m)$, for storing the `dp` array.
> - **Optimality proof:** This approach is optimal because it considers all possible increasing subsequences of columns and finds the longest one, which directly corresponds to the minimum number of columns that need to be deleted to make the table sorted.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, longest increasing subsequence.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving them using dynamic programming.
- Optimization techniques learned: Using dynamic programming to avoid redundant computation and improve time complexity.
- Similar problems to practice: Longest Increasing Subsequence, Edit Distance.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` array, incorrect update logic for `dp[i]`.
- Edge cases to watch for: Empty input, single column input.
- Performance pitfalls: Using a brute force approach for large inputs, not using dynamic programming to optimize the solution.
- Testing considerations: Test the solution with different inputs, including edge cases and large inputs.