## Find the Maximum Achievable Number
**Problem Link:** https://leetcode.com/problems/find-the-maximum-achievable-number/description

**Problem Statement:**
- Given a list of integers and a limit, find the maximum achievable number that can be formed by adding or subtracting the integers in the list without exceeding the limit.
- Input format and constraints: The input is a list of integers and an integer limit. The list can be empty, and the limit can be any positive integer.
- Expected output format: The maximum achievable number that can be formed without exceeding the limit.
- Key requirements and edge cases to consider: Handle cases where the list is empty or the limit is 0.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of adding or subtracting the integers in the list and check if the result exceeds the limit.
- Step-by-step breakdown:
  1. Generate all possible combinations of adding or subtracting the integers in the list.
  2. For each combination, calculate the sum.
  3. Check if the sum exceeds the limit.
  4. If it does not exceed the limit, update the maximum achievable number.

```cpp
#include <iostream>
#include <vector>

int findMaxAchievableNumber(std::vector<int>& nums, int limit) {
    int maxAchievable = 0;
    int n = nums.size();
    // Generate all possible combinations of adding or subtracting the integers in the list
    for (int i = 0; i < (1 << n); i++) {
        int sum = 0;
        for (int j = 0; j < n; j++) {
            // Check if the jth bit is set in the binary representation of i
            if ((i & (1 << j)) != 0) {
                sum += nums[j];
            } else {
                sum -= nums[j];
            }
        }
        // Check if the sum exceeds the limit
        if (sum <= limit && sum > maxAchievable) {
            maxAchievable = sum;
        }
    }
    return maxAchievable;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of integers in the list. This is because we generate all possible combinations of adding or subtracting the integers in the list, which has a time complexity of $O(2^n)$. For each combination, we calculate the sum, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input, making it constant. This is because we only use a fixed amount of space to store the maximum achievable number and the sum.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that tries all possible combinations of adding or subtracting the integers in the list.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the maximum achievable number for each possible sum.
- Detailed breakdown:
  1. Create a dynamic programming table `dp` of size `limit + 1`, where `dp[i]` stores the maximum achievable number that can be formed with a sum of `i`.
  2. Initialize `dp[0] = 0`, because the maximum achievable number with a sum of 0 is 0.
  3. For each integer `num` in the list, update the `dp` table by iterating from `limit` down to `num`.
  4. For each `i` in the range `[num, limit]`, update `dp[i] = max(dp[i], dp[i - num] + num)`.

```cpp
#include <iostream>
#include <vector>

int findMaxAchievableNumber(std::vector<int>& nums, int limit) {
    std::vector<int> dp(limit + 1, -1);
    dp[0] = 0;
    for (int num : nums) {
        for (int i = limit; i >= num; i--) {
            if (dp[i - num] != -1) {
                dp[i] = std::max(dp[i], dp[i - num] + num);
            }
        }
    }
    int maxAchievable = 0;
    for (int i = 0; i <= limit; i++) {
        if (dp[i] != -1 && dp[i] > maxAchievable) {
            maxAchievable = dp[i];
        }
    }
    return maxAchievable;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot limit)$, where $n$ is the number of integers in the list. This is because we iterate over the list and update the `dp` table for each integer.
> - **Space Complexity:** $O(limit)$, which means the space required grows linearly with the size of the limit.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the maximum achievable number for each possible sum, avoiding the need to try all possible combinations of adding or subtracting the integers in the list.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming and brute force approach.
- Problem-solving patterns identified: using dynamic programming to store the maximum achievable number for each possible sum.
- Optimization techniques learned: avoiding the need to try all possible combinations of adding or subtracting the integers in the list.
- Similar problems to practice: problems that involve finding the maximum achievable number or sum with certain constraints.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` table correctly or not updating the `dp` table correctly.
- Edge cases to watch for: handling cases where the list is empty or the limit is 0.
- Performance pitfalls: using a brute force approach that tries all possible combinations of adding or subtracting the integers in the list.
- Testing considerations: testing the function with different inputs and edge cases to ensure it works correctly.