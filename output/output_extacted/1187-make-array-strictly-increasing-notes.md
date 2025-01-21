## Make Array Strictly Increasing
**Problem Link:** https://leetcode.com/problems/make-array-strictly-increasing/description

**Problem Statement:**
- Input: Two integer arrays `arr1` and `arr2` of the same length `n`, and an integer `k`.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= n`, `1 <= arr1[i], arr2[i] <= 10^5`.
- Expected Output: Determine if it's possible to make `arr1` strictly increasing by replacing elements in `arr1` with elements from `arr2` at most `k` times.
- Key Requirements:
  - The order of elements in `arr1` must be maintained.
  - An element from `arr2` can only replace an element at the same index in `arr1`.
- Edge Cases:
  - When `k` is equal to the length of `arr1`, it's always possible to make `arr1` strictly increasing.
  - When `arr1` is already strictly increasing, no replacements are needed.
- Example Test Cases:
  - `arr1 = [1, 2, 3], arr2 = [1, 2, 3], k = 0`: Return `True` because `arr1` is already strictly increasing.
  - `arr1 = [1, 2, 1], arr2 = [1, 2, 3], k = 1`: Return `True` because replacing the last element in `arr1` with the last element in `arr2` makes `arr1` strictly increasing.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking all possible combinations of replacing elements in `arr1` with elements from `arr2` up to `k` times and verifying if the resulting array is strictly increasing.
- This approach involves generating all possible combinations and checking each one, which leads to a high time complexity.

```cpp
#include <vector>
#include <algorithm>

bool canBeIncreasing(std::vector<int>& arr1, std::vector<int>& arr2, int k) {
    // Generate all possible combinations of replacements
    std::vector<bool> mask(arr1.size(), false);
    std::function<void(int)> dfs = [&](int idx) {
        if (idx == arr1.size()) {
            // Check if the current combination makes arr1 strictly increasing
            std::vector<int> temp = arr1;
            for (int i = 0; i < arr1.size(); ++i) {
                if (mask[i]) temp[i] = arr2[i];
            }
            bool increasing = true;
            for (int i = 1; i < temp.size(); ++i) {
                if (temp[i] <= temp[i - 1]) {
                    increasing = false;
                    break;
                }
            }
            if (increasing && std::count(mask.begin(), mask.end(), true) <= k) {
                return true;
            }
        } else {
            // Try replacing the current element
            mask[idx] = true;
            if (dfs(idx + 1)) return true;
            mask[idx] = false;
            if (dfs(idx + 1)) return true;
        }
        return false;
    };
    return dfs(0);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of `arr1`, because we generate all possible combinations of replacements.
> - **Space Complexity:** $O(n)$, for the recursion stack and the `mask` vector.
> - **Why these complexities occur:** The high time complexity is due to generating all possible combinations of replacements, which grows exponentially with the size of the input arrays.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use dynamic programming to keep track of the minimum number of replacements needed to make the array strictly increasing up to each position.
- We maintain two arrays, `dp` and `prev`, where `dp[i]` stores the minimum number of replacements needed to make the array strictly increasing up to position `i`, and `prev[i]` stores the previous element that leads to the minimum number of replacements.

```cpp
bool canBeIncreasing(std::vector<int>& arr1, std::vector<int>& arr2, int k) {
    int n = arr1.size();
    std::vector<int> dp(n, INT_MAX);
    dp[0] = 0;
    for (int i = 1; i < n; ++i) {
        // Check if we can make the array strictly increasing without replacing the current element
        if (arr1[i] > arr1[i - 1]) {
            dp[i] = dp[i - 1];
        }
        // Check if replacing the current element with the corresponding element from arr2 makes the array strictly increasing
        if (arr2[i] > arr1[i - 1] && dp[i - 1] + 1 <= k) {
            dp[i] = std::min(dp[i], dp[i - 1] + 1);
        }
    }
    return dp[n - 1] <= k;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `arr1`, because we iterate through the arrays once.
> - **Space Complexity:** $O(n)$, for the `dp` array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to keep track of the minimum number of replacements needed to make the array strictly increasing up to each position, which avoids the exponential time complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems that involve finding the minimum or maximum value of a function subject to certain constraints.
- How to use dynamic programming to avoid the exponential time complexity of brute force approaches.
- The trade-off between time and space complexity in dynamic programming approaches.

**Mistakes to Avoid:**
- Failing to consider all possible combinations of replacements in the brute force approach.
- Not using dynamic programming to keep track of the minimum number of replacements needed to make the array strictly increasing up to each position.
- Not checking the constraints of the problem, such as the length of the input arrays and the value of `k`.