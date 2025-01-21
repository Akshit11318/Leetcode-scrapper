## Combination Sum IV
**Problem Link:** https://leetcode.com/problems/combination-sum-iv/description

**Problem Statement:**
- Input format and constraints: Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. The length of `nums` is between 1 and 1000, and `nums[i]` is between 1 and 1000. `target` is between 1 and 1000.
- Expected output format: The number of combinations that sum up to `target`.
- Key requirements and edge cases to consider: The order of the numbers in the combination does not matter, and each number in `nums` can be used any number of times.
- Example test cases with explanations: 
  - For `nums = [1,2,3]` and `target = 4`, the output should be `7` because the combinations that sum up to `4` are `[1,1,1,1]`, `[1,1,2]`, `[1,2,1]`, `[1,3]`, `[2,1,1]`, `[2,2]`, and `[3,1]`.
  - For `nums = [9]` and `target = 3`, the output should be `0` because there is no combination that sums up to `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a recursive approach to generate all possible combinations of numbers from `nums` that sum up to `target`.
- Step-by-step breakdown of the solution: 
  1. Start with an empty combination.
  2. For each number in `nums`, add it to the current combination and recursively generate combinations that sum up to `target - current_number`.
  3. If the sum of the current combination is equal to `target`, increment the count of combinations.
- Why this approach comes to mind first: It is a straightforward way to generate all possible combinations and check if they sum up to `target`.

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int count = 0;
        vector<int> current_combination;
        backtrack(nums, target, current_combination, count);
        return count;
    }
    
    void backtrack(vector<int>& nums, int target, vector<int>& current_combination, int& count) {
        if (target == 0) {
            count++;
            return;
        }
        if (target < 0) {
            return;
        }
        for (int num : nums) {
            current_combination.push_back(num);
            backtrack(nums, target - num, current_combination, count);
            current_combination.pop_back();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N^{target})$ where $N$ is the length of `nums` because in the worst case, we have to generate all possible combinations of numbers from `nums` that sum up to `target`.
> - **Space Complexity:** $O(target)$ because of the recursion stack.
> - **Why these complexities occur:** The time complexity occurs because of the recursive generation of all possible combinations, and the space complexity occurs because of the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of combinations that sum up to each number from `1` to `target`.
- Detailed breakdown of the approach: 
  1. Create a dynamic programming table `dp` of size `target + 1` and initialize it with `0`.
  2. Set `dp[0] = 1` because there is one way to sum up to `0`, which is to choose no numbers.
  3. For each number `i` from `1` to `target`, for each number `num` in `nums`, if `i - num >= 0`, add `dp[i - num]` to `dp[i]`.
  4. Return `dp[target]`.
- Proof of optimality: This approach is optimal because it avoids the redundant computation of the brute force approach and only computes the number of combinations that sum up to each number from `1` to `target` once.

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (i - num >= 0) {
                    dp[i] += dp[i - num];
                }
            }
        }
        return dp[target];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot target)$ where $N$ is the length of `nums` because we need to iterate over each number in `nums` for each number from `1` to `target`.
> - **Space Complexity:** $O(target)$ because of the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it avoids the redundant computation of the brute force approach and only computes the number of combinations that sum up to each number from `1` to `target` once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion.
- Problem-solving patterns identified: Avoiding redundant computation, using dynamic programming to store intermediate results.
- Optimization techniques learned: Using dynamic programming to optimize recursive solutions.
- Similar problems to practice: Combination Sum, Combination Sum II, Combination Sum III.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, not handling edge cases correctly.
- Edge cases to watch for: `target` is `0`, `nums` is empty.
- Performance pitfalls: Using a recursive solution without memoization or dynamic programming.
- Testing considerations: Test the solution with different inputs, including edge cases.