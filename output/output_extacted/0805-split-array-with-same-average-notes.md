## Split Array with Same Average
**Problem Link:** https://leetcode.com/problems/split-array-with-same-average/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `k`.
- Constraints: `1 <= k <= nums.size()` and `nums.size()` will be in the range `[1, 20]`.
- Expected output format: A boolean indicating whether it is possible to split the array into `k` non-empty subsets such that the sum of the elements in each subset is equal.
- Key requirements and edge cases to consider:
  - The array may contain duplicate elements.
  - The array may contain negative numbers.
  - The array may contain zero.
- Example test cases with explanations:
  - Input: `nums = [1,2,3,4,5,6,7,8,9], k = 3`
    Output: `true`
    Explanation: The sum of the array is `45`. We can split the array into three subsets with equal sum: `[1,2,3,4,5,6,7,8,9] -> [1,2,3] + [4,5,6] + [7,8,9]`.
  - Input: `nums = [1,2,3,4,5,6,7,8,9], k = 4`
    Output: `false`
    Explanation: The sum of the array is `45`. We cannot split the array into four subsets with equal sum.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of splitting the array into `k` non-empty subsets.
- Step-by-step breakdown of the solution:
  1. Calculate the total sum of the array.
  2. Try all possible combinations of splitting the array into `k` non-empty subsets.
  3. For each combination, check if the sum of the elements in each subset is equal to the average sum.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations.

```cpp
class Solution {
public:
    bool splitArraySameAverage(vector<int>& nums, int k) {
        int n = nums.size();
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        vector<bool> visited(n, false);
        return dfs(nums, k, 0, 0, totalSum, visited, 0);
    }

    bool dfs(vector<int>& nums, int k, int index, int currentSum, int totalSum, vector<bool>& visited, int count) {
        if (count == k - 1) {
            int remainingSum = 0;
            for (int i = 0; i < nums.size(); i++) {
                if (!visited[i]) {
                    remainingSum += nums[i];
                }
            }
            return remainingSum * k == totalSum;
        }
        for (int i = index; i < nums.size(); i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            if (dfs(nums, k, i + 1, currentSum + nums[i], totalSum, visited, count + 1)) {
                return true;
            }
            visited[i] = false;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the size of the input array. This is because we try all possible combinations of splitting the array into `k` non-empty subsets.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we use a recursive call stack to store the current subset.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of splitting the array into `k` non-empty subsets, resulting in an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We only need to consider subsets with a sum that is a multiple of the average sum.
- Detailed breakdown of the approach:
  1. Calculate the total sum of the array.
  2. Calculate the average sum by dividing the total sum by `k`.
  3. Try all possible combinations of splitting the array into `k` non-empty subsets, but only consider subsets with a sum that is a multiple of the average sum.
- Proof of optimality: This approach is optimal because we only consider subsets with a sum that is a multiple of the average sum, which reduces the number of combinations to try.

```cpp
class Solution {
public:
    bool splitArraySameAverage(vector<int>& nums, int k) {
        int n = nums.size();
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        if (totalSum % k != 0) {
            return false;
        }
        int averageSum = totalSum / k;
        vector<bool> visited(n, false);
        return dfs(nums, k, 0, 0, averageSum, visited, 0);
    }

    bool dfs(vector<int>& nums, int k, int index, int currentSum, int averageSum, vector<bool>& visited, int count) {
        if (count == k - 1) {
            int remainingSum = 0;
            for (int i = 0; i < nums.size(); i++) {
                if (!visited[i]) {
                    remainingSum += nums[i];
                }
            }
            return remainingSum == averageSum;
        }
        for (int i = index; i < nums.size(); i++) {
            if (visited[i]) {
                continue;
            }
            if (currentSum + nums[i] > averageSum) {
                continue;
            }
            visited[i] = true;
            if (dfs(nums, k, i + 1, currentSum + nums[i], averageSum, visited, count + (currentSum + nums[i] == averageSum ? 1 : 0))) {
                return true;
            }
            visited[i] = false;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, but with a reduced number of combinations to try due to the optimization.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array.
> - **Optimality proof:** This approach is optimal because we only consider subsets with a sum that is a multiple of the average sum, which reduces the number of combinations to try.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, subset sum problem.
- Problem-solving patterns identified: Reducing the problem size by considering only subsets with a sum that is a multiple of the average sum.
- Optimization techniques learned: Pruning branches in the recursive call tree by considering only subsets with a sum that is a multiple of the average sum.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the case where the total sum is not divisible by `k`.
- Edge cases to watch for: The input array may contain duplicate elements or negative numbers.
- Performance pitfalls: Trying all possible combinations of splitting the array into `k` non-empty subsets without optimization.
- Testing considerations: Test the solution with different input arrays and values of `k`.