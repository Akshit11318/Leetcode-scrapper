## Partition Equal Subset Sum

**Problem Link:** https://leetcode.com/problems/partition-equal-subset-sum/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: $1 \leq nums.length \leq 200$, $1 \leq nums[i] \leq 100$.
- Expected output format: A boolean indicating whether the array can be partitioned into two subsets with equal sum.
- Key requirements: The sum of the elements in each subset should be equal.
- Example test cases:
  - Input: `nums = [1,5,11,5]`, Output: `true`, Explanation: The array can be partitioned as `[1,5,5]` and `[11]`.
  - Input: `nums = [1,2,3,5]`, Output: `false`, Explanation: The array cannot be partitioned into two subsets with equal sum.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of subsets and check if any of them have equal sums.
- Step-by-step breakdown:
  1. Calculate the total sum of the array.
  2. If the total sum is odd, return `false` as it's impossible to partition the array into two subsets with equal sum.
  3. Generate all possible subsets of the array.
  4. For each subset, calculate its sum and check if it's equal to half of the total sum.
  5. If such a subset is found, return `true`.
- Why this approach comes to mind first: It's a straightforward approach that considers all possibilities.

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 2 != 0) return false;
        sum /= 2;
        int n = nums.size();
        for (int i = 0; i < (1 << n); i++) {
            int subsetSum = 0;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) subsetSum += nums[j];
            }
            if (subsetSum == sum) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in the array. This is because we generate all possible subsets and calculate their sums.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the total sum and the subset sum.
> - **Why these complexities occur:** The time complexity is high because we consider all possible subsets, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to store the sums of subsets and avoid recalculating them.
- Detailed breakdown:
  1. Calculate the total sum of the array.
  2. If the total sum is odd, return `false`.
  3. Initialize a dynamic programming table `dp` of size `sum / 2 + 1`, where `dp[i]` is `true` if a subset with sum `i` can be formed.
  4. Iterate over the array and update the `dp` table.
  5. Return `dp[sum / 2]`.
- Proof of optimality: This approach has a lower time complexity than the brute force approach and is guaranteed to find a solution if one exists.

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 2 != 0) return false;
        sum /= 2;
        vector<bool> dp(sum + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int i = sum; i >= num; i--) {
                if (dp[i - num]) dp[i] = true;
            }
        }
        return dp[sum];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot sum)$, where $n$ is the number of elements in the array and $sum$ is the total sum of the array.
> - **Space Complexity:** $O(sum)$, as we use a dynamic programming table of size `sum / 2 + 1`.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the sums of subsets and avoid recalculating them, resulting in a lower time complexity than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, subset sum problem.
- Problem-solving patterns: Using dynamic programming to store intermediate results and avoid recalculating them.
- Optimization techniques: Avoiding recalculations by storing intermediate results.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: An array with a total sum that is odd, an array with a single element.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.