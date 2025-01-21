## Largest Divisible Subset

**Problem Link:** https://leetcode.com/problems/largest-divisible-subset/description

**Problem Statement:**
- Input format: an integer array `nums` containing distinct positive integers.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected output format: a list of integers representing the largest subset of `nums` where every pair `(i, j)` of indices of this subset satisfies that `nums[i] % nums[j] == 0` or `nums[j] % nums[i] == 0`.
- Key requirements and edge cases to consider:
  - The subset must be non-empty.
  - If there are multiple subsets of the same size, any of them can be returned.
  - The input array `nums` is guaranteed to contain distinct elements.

Example test cases with explanations:
- For `nums = [1,2,3]`, one possible answer is `[1,2]` because `2 % 1 == 0`.
- For `nums = [1,2,4,8]`, one possible answer is `[1,2,4,8]` because each number can be divided by the previous one.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subset of the input array `nums` to find the largest one where each pair of elements satisfies the divisibility condition.
- Step-by-step breakdown:
  1. Generate all possible subsets of `nums`.
  2. For each subset, check if every pair of elements satisfies the condition `nums[i] % nums[j] == 0` or `nums[j] % nums[i] == 0`.
  3. Keep track of the largest subset that satisfies the condition.
- Why this approach comes to mind first: It's a straightforward way to ensure that all possibilities are considered, but it's inefficient due to the exponential number of subsets.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> largestDivisibleSubset(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    int n = nums.size();
    std::vector<std::vector<int>> dp(n);
    std::vector<int> maxLen(n, 1);
    std::vector<int> prev(n, -1);

    for (int i = 0; i < n; i++) {
        dp[i].push_back(nums[i]);
        for (int j = 0; j < i; j++) {
            if (nums[i] % nums[j] == 0 && maxLen[j] + 1 > maxLen[i]) {
                maxLen[i] = maxLen[j] + 1;
                prev[i] = j;
                dp[i] = dp[j];
                dp[i].push_back(nums[i]);
            }
        }
    }

    int maxIndex = 0;
    for (int i = 1; i < n; i++) {
        if (maxLen[i] > maxLen[maxIndex]) {
            maxIndex = i;
        }
    }

    return dp[maxIndex];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ because in the worst case, we generate all subsets of `nums`.
> - **Space Complexity:** $O(2^n)$ because we store all subsets.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsets, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to avoid redundant computations and to efficiently find the largest divisible subset.
- Detailed breakdown:
  1. Sort the input array `nums`.
  2. Create a dynamic programming table `dp` where `dp[i]` represents the largest divisible subset ending at index `i`.
  3. For each element in `nums`, check all previous elements to see if they can be part of the subset.
  4. Update `dp[i]` if a larger subset is found.
- Proof of optimality: This approach ensures that all possible subsets are considered without redundant computations, leading to an optimal solution.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> largestDivisibleSubset(std::vector<int>& nums) {
    if (nums.empty()) return {};
    std::sort(nums.begin(), nums.end());
    int n = nums.size();
    std::vector<int> dp(n, 1);
    std::vector<int> prev(n, -1);

    int maxLen = 1, maxIndex = 0;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
        if (dp[i] > maxLen) {
            maxLen = dp[i];
            maxIndex = i;
        }
    }

    std::vector<int> result;
    while (maxIndex != -1) {
        result.push_back(nums[maxIndex]);
        maxIndex = prev[maxIndex];
    }
    std::reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we iterate through `nums` and for each element, we potentially check all previous elements.
> - **Space Complexity:** $O(n)$ because we store the dynamic programming table and the previous indices.
> - **Optimality proof:** This approach is optimal because it efficiently considers all possible subsets without redundant computations, achieving a polynomial time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming and subset generation.
- Problem-solving patterns identified: using sorting to simplify the problem and applying dynamic programming to avoid redundant computations.
- Optimization techniques learned: reducing the problem size by sorting and using dynamic programming to efficiently find the solution.
- Similar problems to practice: other dynamic programming problems involving subset selection or optimization.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty input array, and not properly initializing dynamic programming tables.
- Edge cases to watch for: handling duplicate elements, if allowed, and ensuring that the solution works for arrays with a single element.
- Performance pitfalls: using brute force approaches for large inputs and not optimizing the solution for the given constraints.
- Testing considerations: thoroughly testing the solution with various input sizes, including edge cases, to ensure correctness and efficiency.