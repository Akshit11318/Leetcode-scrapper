## Maximum Sum Obtained of Any Permutation

**Problem Link:** https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description

**Problem Statement:**
- Input: An array of integers `arr` and an array of integers `multipliers`.
- Constraints: `1 <= arr.length <= 1000`, `1 <= multipliers.length <= 1000`, and `multipliers.length <= arr.length`.
- Expected Output: The maximum sum that can be obtained from any permutation of `arr` with the given `multipliers`.
- Key Requirements: Find the optimal permutation of `arr` to maximize the sum of products between each element in `arr` and its corresponding multiplier in `multipliers`.
- Example Test Cases:
  - Example 1: Input `arr = [1, 2, 3]`, `multipliers = [3, 2, 1]`. Output: `14`. Explanation: `3 * 3 + 2 * 2 + 1 * 1 = 14`.
  - Example 2: Input `arr = [-5, -3, -3, -2, 7, 1]`, `multipliers = [-10, -10, 6, 2, -10, 9]`. Output: `102`. Explanation: The optimal permutation yields the maximum sum.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible permutations of `arr` and calculating the sum of products for each permutation.
- For each permutation, multiply each element in `arr` by its corresponding multiplier in `multipliers` and sum these products.
- The brute force approach considers all possible arrangements of `arr`, which leads to an exponential number of permutations.

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int maximumSum(int* arr, int arrSize, int* multipliers, int multipliersSize) {
    int maxSum = INT_MIN;
    // Generate all permutations of arr
    do {
        int sum = 0;
        for (int i = 0; i < multipliersSize; i++) {
            sum += arr[i] * multipliers[i];
        }
        maxSum = max(maxSum, sum);
    } while (next_permutation(arr, arr + arrSize));
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the size of `arr`. This is due to generating all permutations of `arr`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum and temporary variables.
> - **Why these complexities occur:** The brute force approach generates all permutations, leading to an exponential time complexity. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves using dynamic programming to store and reuse the results of subproblems.
- The key insight is to realize that the problem can be solved by considering the maximum sum that can be obtained by either including or excluding the current element from the permutation.
- We use a `dp` table to store the maximum sum for each subproblem, where `dp[i][j]` represents the maximum sum that can be obtained by considering the first `i` elements of `arr` and the first `j` multipliers.
- We fill the `dp` table in a bottom-up manner, considering all possible permutations and choosing the one that yields the maximum sum.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maximumSum(vector<int>& arr, vector<int>& multipliers) {
    int n = arr.size();
    int m = multipliers.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            dp[i][j] = max(dp[i - 1][j - 1] + arr[i - 1] * multipliers[j - 1], dp[i - 1][j]);
        }
    }
    return dp[n][m];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `arr` and $m$ is the size of `multipliers`. This is due to filling the `dp` table.
> - **Space Complexity:** $O(n \cdot m)$, as we use a `dp` table to store the results of subproblems.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible permutations and choose the one that yields the maximum sum. This is the optimal solution because it has a polynomial time complexity and uses a reasonable amount of space.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the use of dynamic programming to solve a complex problem efficiently.
- The key insight is to realize that the problem can be solved by considering the maximum sum that can be obtained by either including or excluding the current element from the permutation.
- The optimal solution has a polynomial time complexity, making it much faster than the brute force approach.

**Mistakes to Avoid:**
- Failing to consider all possible permutations of `arr`.
- Not using dynamic programming to store and reuse the results of subproblems.
- Not choosing the permutation that yields the maximum sum.
- Not handling edge cases, such as when `arr` or `multipliers` is empty.