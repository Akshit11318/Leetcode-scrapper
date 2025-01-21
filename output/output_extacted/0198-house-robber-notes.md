## House Robber
**Problem Link:** [https://leetcode.com/problems/house-robber/description](https://leetcode.com/problems/house-robber/description)

**Problem Statement:**
- Input format: An array of integers `nums` representing the amount of money in each house.
- Constraints: `1 <= nums.length <= 100`, `0 <= nums[i] <= 1000`.
- Expected output format: The maximum amount of money that can be stolen.
- Key requirements: The robber cannot steal from adjacent houses.
- Edge cases: If the input array is empty or contains only one element, return 0 or the single element respectively.
- Example test cases:
  - Input: `nums = [1,2,3,1]`, Output: `4` (Steal from the first and third houses).
  - Input: `nums = [2,7,9,3,1]`, Output: `12` (Steal from the first, third, and fifth houses).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of stealing from houses and calculate the maximum amount that can be stolen without stealing from adjacent houses.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the input array.
  2. For each subset, check if any two houses are adjacent.
  3. If not, calculate the sum of the amounts in the subset.
  4. Keep track of the maximum sum found.

```cpp
#include <iostream>
#include <vector>

int rob(std::vector<int>& nums) {
    int n = nums.size();
    int max_amount = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int current_amount = 0;
        bool is_valid = true;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                if (i > 0 && (mask & (1 << (i - 1))) != 0) {
                    is_valid = false;
                    break;
                }
                current_amount += nums[i];
            }
        }
        if (is_valid) {
            max_amount = std::max(max_amount, current_amount);
        }
    }
    return max_amount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of houses. The reason is that we generate all possible subsets of the input array, which takes $O(2^n)$ time, and for each subset, we check if any two houses are adjacent, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the maximum amount and the current amount.
> - **Why these complexities occur:** The brute force approach is inefficient because it tries all possible combinations of stealing from houses, which results in an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to solve this problem efficiently. The idea is to keep track of the maximum amount that can be stolen up to each house.
- Detailed breakdown of the approach:
  1. Initialize an array `dp` of size `n`, where `dp[i]` represents the maximum amount that can be stolen up to the `i-th` house.
  2. For the first house, `dp[0] = nums[0]`.
  3. For the second house, `dp[1] = std::max(nums[0], nums[1])`.
  4. For each house from the third to the last, `dp[i] = std::max(dp[i-1], dp[i-2] + nums[i])`.
  5. The maximum amount that can be stolen is `dp[n-1]`.

```cpp
int rob(std::vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    std::vector<int> dp(n);
    dp[0] = nums[0];
    dp[1] = std::max(nums[0], nums[1]);
    for (int i = 2; i < n; i++) {
        dp[i] = std::max(dp[i-1], dp[i-2] + nums[i]);
    }
    return dp[n-1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of houses. The reason is that we only need to iterate through the input array once to fill up the `dp` array.
> - **Space Complexity:** $O(n)$, since we need to store the `dp` array of size `n`.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid redundant calculations and has a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, memoization.
- Problem-solving patterns: Breaking down the problem into smaller subproblems, using a bottom-up approach to solve the problem.
- Optimization techniques: Avoiding redundant calculations using dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not handling the base cases correctly.
- Edge cases: Not handling the case where the input array is empty or contains only one element.
- Performance pitfalls: Using a brute force approach that has an exponential time complexity.