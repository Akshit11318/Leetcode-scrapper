## Partition to K Equal Sum Subsets

**Problem Link:** https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description

**Problem Statement:**
- Input format: `nums` (a list of integers) and `k` (the number of subsets)
- Constraints: `1 <= k <= nums.size()`, `1 <= nums.size() <= 16`, `1 <= nums[i] <= 10^4`
- Expected output format: `true` if it is possible to divide the array into `k` subsets with equal sum, `false` otherwise
- Key requirements: The sum of all elements in `nums` must be divisible by `k`.
- Example test cases:
  - `nums = [4, 3, 2, 3, 5, 2, 1], k = 4` returns `true` because it is possible to divide the array into 4 subsets with equal sum.
  - `nums = [1, 2, 3, 4], k = 3` returns `false` because it is not possible to divide the array into 3 subsets with equal sum.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of subsets and check if the sum of each subset is equal.
- Step-by-step breakdown:
  1. Calculate the total sum of the array and check if it is divisible by `k`. If not, return `false`.
  2. Generate all possible combinations of subsets.
  3. For each combination, calculate the sum of each subset and check if all sums are equal. If so, return `true`.
- Why this approach comes to mind first: It is a straightforward solution that checks all possibilities.

```cpp
#include <vector>

class Solution {
public:
    bool canPartitionKSubsets(std::vector<int>& nums, int k) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % k != 0) {
            return false;
        }
        int target = sum / k;
        std::vector<bool> visited(nums.size(), false);
        return dfs(nums, k, target, 0, 0, visited);
    }
    
    bool dfs(std::vector<int>& nums, int k, int target, int index, int currentSum, std::vector<bool>& visited) {
        if (k == 0) {
            return true;
        }
        if (currentSum == target) {
            return dfs(nums, k - 1, target, 0, 0, visited);
        }
        for (int i = index; i < nums.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                if (dfs(nums, k, target, i + 1, currentSum + nums[i], visited)) {
                    return true;
                }
                visited[i] = false;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \times 2^n)$ where $n$ is the number of elements in the array. This is because we are generating all possible combinations of subsets.
> - **Space Complexity:** $O(n)$ for the recursion stack and the `visited` array.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible combinations of subsets, and the space complexity occurs because we need to store the recursion stack and the `visited` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible combinations of subsets, we can use a backtracking approach to try all possible assignments of numbers to subsets.
- Detailed breakdown:
  1. Calculate the total sum of the array and check if it is divisible by `k`. If not, return `false`.
  2. Initialize an array `groups` to store the sum of each subset.
  3. Use a backtracking function to try all possible assignments of numbers to subsets.
- Proof of optimality: This approach is optimal because it tries all possible assignments of numbers to subsets in a systematic way, without generating all possible combinations of subsets.

```cpp
class Solution {
public:
    bool canPartitionKSubsets(std::vector<int>& nums, int k) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % k != 0) {
            return false;
        }
        int target = sum / k;
        std::vector<int> groups(k, 0);
        std::sort(nums.rbegin(), nums.rend());
        return backtrack(nums, groups, target, 0);
    }
    
    bool backtrack(std::vector<int>& nums, std::vector<int>& groups, int target, int index) {
        if (index == nums.size()) {
            for (int group : groups) {
                if (group != target) {
                    return false;
                }
            }
            return true;
        }
        for (int i = 0; i < groups.size(); i++) {
            if (groups[i] + nums[index] <= target) {
                groups[i] += nums[index];
                if (backtrack(nums, groups, target, index + 1)) {
                    return true;
                }
                groups[i] -= nums[index];
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \times 2^n)$ where $n$ is the number of elements in the array. This is because we are trying all possible assignments of numbers to subsets.
> - **Space Complexity:** $O(n + k)$ for the recursion stack and the `groups` array.
> - **Optimality proof:** This approach is optimal because it tries all possible assignments of numbers to subsets in a systematic way, without generating all possible combinations of subsets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, recursion, and subset sum problem.
- Problem-solving patterns identified: using a systematic approach to try all possible assignments of numbers to subsets.
- Optimization techniques learned: using a backtracking approach to try all possible assignments of numbers to subsets.
- Similar problems to practice: subset sum problem, partition problem.

**Mistakes to Avoid:**
- Common implementation errors: not checking if the total sum is divisible by `k`, not initializing the `groups` array correctly.
- Edge cases to watch for: when the total sum is not divisible by `k`, when the input array is empty.
- Performance pitfalls: using a brute force approach to generate all possible combinations of subsets.
- Testing considerations: testing the function with different inputs, including edge cases.