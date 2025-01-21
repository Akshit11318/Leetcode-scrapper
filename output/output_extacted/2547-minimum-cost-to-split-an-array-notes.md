## Minimum Cost to Split an Array
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-split-an-array/description

**Problem Statement:**
- Input: An integer array `nums` and a function `op`.
- Constraints: $1 \leq nums.length \leq 1000$ and $0 \leq nums[i] \leq 10^6$ for all $i$.
- Expected Output: The minimum cost to split the array into non-empty subarrays such that the cost of each subarray is the result of applying `op` to all elements in the subarray.
- Key Requirements: Find the minimum cost by considering all possible splits.
- Edge Cases: Consider arrays with a single element, arrays with all elements being the same, and arrays with distinct elements.

Example Test Cases:
- For `nums = [1, 2, 3, 4]` and `op(x) = x * x`, the minimum cost is `1 * 1 + 2 * 2 + 3 * 3 + 4 * 4 = 30`.
- For `nums = [1, 2, 3, 4]` and `op(x) = x + x`, the minimum cost is `(1 + 2 + 3 + 4) * 2 = 20`.

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible splits of the array and calculate the cost for each split.
- We use a recursive approach to generate all possible splits.
- For each split, we calculate the cost by applying the `op` function to each subarray and summing up the costs.

```cpp
#include <vector>
#include <functional>

int minCost(std::vector<int>& nums, std::function<int(std::vector<int>)> op) {
    int n = nums.size();
    std::vector<int> costs(n + 1, INT_MAX);
    costs[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            std::vector<int> subarray(nums.begin() + j, nums.begin() + i);
            costs[i] = std::min(costs[i], costs[j] + op(subarray));
        }
    }

    return costs[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible splits of the array, and for each split, we calculate the cost.
> - **Space Complexity:** $O(n)$, as we need to store the costs for each prefix of the array.
> - **Why these complexities occur:** The exponential time complexity is due to the recursive generation of all possible splits, while the linear space complexity is due to the need to store the costs for each prefix.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use dynamic programming to store the minimum cost for each prefix of the array.
- We use a bottom-up approach to fill up the `costs` array, where `costs[i]` represents the minimum cost for the first `i` elements.
- For each `i`, we consider all possible splits of the first `i` elements and calculate the minimum cost.

```cpp
#include <vector>
#include <functional>

int minCost(std::vector<int>& nums, std::function<int(std::vector<int>)> op) {
    int n = nums.size();
    std::vector<int> costs(n + 1, INT_MAX);
    costs[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            std::vector<int> subarray(nums.begin() + j, nums.begin() + i);
            costs[i] = std::min(costs[i], costs[j] + op(subarray));
        }
    }

    return costs[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the length of the input array and $m$ is the maximum size of a subarray. This is because we use a bottom-up approach to fill up the `costs` array.
> - **Space Complexity:** $O(n)$, as we need to store the costs for each prefix of the array.
> - **Optimality proof:** This approach is optimal because it considers all possible splits of the array and calculates the minimum cost for each split.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursion, and memoization.
- Problem-solving patterns identified: breaking down the problem into smaller subproblems and solving them recursively.
- Optimization techniques learned: using dynamic programming to store the minimum cost for each prefix of the array.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases correctly, not using memoization to store intermediate results.
- Edge cases to watch for: arrays with a single element, arrays with all elements being the same, and arrays with distinct elements.
- Performance pitfalls: using an exponential-time algorithm instead of a dynamic programming approach.
- Testing considerations: testing the function with different input arrays and `op` functions to ensure correctness.