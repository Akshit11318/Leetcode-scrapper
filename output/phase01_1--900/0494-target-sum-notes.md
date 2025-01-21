## Target Sum

**Problem Link:** [https://leetcode.com/problems/target-sum/description](https://leetcode.com/problems/target-sum/description)

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `target`.
- Constraints: $1 \leq \text{length of } nums \leq 20$ and $1 \leq \text{each element in } nums \leq 1000$.
- Expected output format: The number of ways to assign `+` or `-` to each element in `nums` such that the sum of the resulting array equals `target`.
- Key requirements and edge cases to consider: The array can contain duplicate elements, and the target sum can be positive, negative, or zero.
- Example test cases with explanations:
  - Example 1: `nums = [1,1,1,1,1], target = 3`, output: `5`. There are 5 ways to assign `+` or `-` to each element in `nums` such that the sum of the resulting array equals `3`.
  - Example 2: `nums = [1], target = 1`, output: `1`. There is 1 way to assign `+` or `-` to each element in `nums` such that the sum of the resulting array equals `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of assigning `+` or `-` to each element in `nums`.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `+` and `-` for each element in `nums`.
  2. For each combination, calculate the sum of the resulting array.
  3. Count the number of combinations where the sum equals `target`.
- Why this approach comes to mind first: It is a straightforward way to solve the problem by trying all possible solutions.

```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int count = 0;
        int n = nums.size();
        for (int mask = 0; mask < (1 << n); mask++) {
            int sum = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) {
                    sum += nums[i];
                } else {
                    sum -= nums[i];
                }
            }
            if (sum == target) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `nums`. This is because we generate $2^n$ combinations and calculate the sum for each combination in $O(n)$ time.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we only use a constant amount of space to store the count and the sum.
> - **Why these complexities occur:** The time complexity occurs because we try all possible combinations of assigning `+` or `-` to each element in `nums`. The space complexity occurs because we only use a constant amount of space to store the count and the sum.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the count of ways to reach each possible sum.
- Detailed breakdown of the approach:
  1. Initialize a map to store the count of ways to reach each possible sum.
  2. For each element in `nums`, update the map by adding the count of ways to reach each possible sum minus the current element.
  3. Return the count of ways to reach the target sum.
- Proof of optimality: This approach is optimal because it avoids trying all possible combinations of assigning `+` or `-` to each element in `nums`.
- Why further optimization is impossible: This approach is already optimal because it uses dynamic programming to store the count of ways to reach each possible sum.

```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        map<int, int> dp;
        dp[0] = 1;
        for (int i = 0; i < n; i++) {
            map<int, int> next;
            for (auto& pair : dp) {
                next[pair.first + nums[i]] += pair.second;
                next[pair.first - nums[i]] += pair.second;
            }
            dp = next;
        }
        return dp[target];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot sum)$, where $n$ is the length of `nums` and $sum$ is the sum of all elements in `nums`. This is because we update the map for each element in `nums` and the size of the map is at most $sum$.
> - **Space Complexity:** $O(sum)$, excluding the space required for the input array. This is because we store the count of ways to reach each possible sum in the map.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the count of ways to reach each possible sum, avoiding trying all possible combinations of assigning `+` or `-` to each element in `nums`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and bit manipulation.
- Problem-solving patterns identified: Using dynamic programming to store the count of ways to reach each possible sum.
- Optimization techniques learned: Using a map to store the count of ways to reach each possible sum.
- Similar problems to practice: Other dynamic programming problems, such as the knapsack problem or the Fibonacci sequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the map correctly or not updating the map correctly.
- Edge cases to watch for: The array can contain duplicate elements, and the target sum can be positive, negative, or zero.
- Performance pitfalls: Trying all possible combinations of assigning `+` or `-` to each element in `nums` can lead to exponential time complexity.
- Testing considerations: Test the solution with different input arrays and target sums to ensure it works correctly.