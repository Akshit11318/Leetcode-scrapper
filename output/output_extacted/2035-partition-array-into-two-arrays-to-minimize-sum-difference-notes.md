## Partition Array into Two Arrays to Minimize Sum Difference

**Problem Link:** https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 15`.
- Expected Output: The minimum possible difference between the sum of the elements in the two arrays.
- Key Requirements: The input array must be partitioned into two non-empty, non-overlapping arrays.
- Edge Cases: Handling arrays of length 1, arrays with all elements being equal, and arrays with large differences in element values.
- Example Test Cases:
  - Input: `nums = [1,2,3,9]`
  - Output: `3`
  - Explanation: One optimal partition is `[1,9]` and `[2,3]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible partitions of the input array and calculating the difference in sums for each partition.
- Step-by-step breakdown:
  1. Generate all possible subsets of the input array.
  2. For each subset, calculate the sum of its elements and the sum of the elements not in the subset.
  3. Calculate the absolute difference between these two sums.
  4. Keep track of the minimum difference found across all subsets.

```cpp
#include <vector>
#include <algorithm>
#include <climits>

int minimumDifference(std::vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    for (int num : nums) totalSum += num;
    
    int minDiff = INT_MAX;
    for (int mask = 1; mask < (1 << n); ++mask) {
        int subsetSum = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                subsetSum += nums[i];
            }
        }
        int diff = abs(subsetSum - (totalSum - subsetSum));
        minDiff = std::min(minDiff, diff);
    }
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in the input array. This is because we generate all possible subsets (which is $2^n$) and for each subset, we calculate the sum of its elements (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, not counting the space needed for the input and output. This is because we only use a constant amount of space to store the minimum difference and other variables.
> - **Why these complexities occur:** The time complexity is dominated by generating all possible subsets and calculating sums for each, while the space complexity is low because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is recognizing that we can use dynamic programming to efficiently calculate the minimum difference.
- Detailed breakdown:
  1. Calculate the total sum of the input array.
  2. Initialize a dynamic programming table `dp` where `dp[i][j]` represents whether it is possible to get a sum of `j` using the first `i` elements.
  3. Fill the `dp` table by iterating over each element and each possible sum from 0 to half of the total sum.
  4. The minimum difference is the minimum absolute difference between any achievable sum and the total sum minus that achievable sum.

```cpp
#include <vector>
#include <algorithm>
#include <climits>

int minimumDifference(std::vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    for (int num : nums) totalSum += num;
    
    std::vector<std::vector<bool>> dp(n + 1, std::vector<bool>(totalSum / 2 + 1, false));
    dp[0][0] = true;
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= totalSum / 2; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j >= nums[i - 1]) {
                dp[i][j] = dp[i][j] || dp[i - 1][j - nums[i - 1]];
            }
        }
    }
    
    int minDiff = INT_MAX;
    for (int j = 0; j <= totalSum / 2; ++j) {
        if (dp[n][j]) {
            minDiff = std::min(minDiff, abs(j - (totalSum - j)));
        }
    }
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot totalSum)$, where $n$ is the number of elements and $totalSum$ is the sum of all elements. This is because we fill a dynamic programming table of size $n \times totalSum$.
> - **Space Complexity:** $O(n \cdot totalSum)$, for the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it considers all possible subsets and their sums in an efficient manner, ensuring that the minimum difference is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, subset generation, and sum calculations.
- Problem-solving patterns identified: breaking down problems into smaller sub-problems and using dynamic programming to avoid redundant calculations.
- Optimization techniques learned: using dynamic programming to reduce time complexity.
- Similar problems to practice: partition problems, subset sum problems, and other dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of dynamic programming tables, incorrect bounds for loops.
- Edge cases to watch for: arrays of length 1, arrays with all elements being equal.
- Performance pitfalls: using brute force approaches for large inputs, not optimizing dynamic programming solutions.
- Testing considerations: testing with small and large inputs, testing with edge cases.