## Delete and Earn

**Problem Link:** https://leetcode.com/problems/delete-and-earn/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 20000`, `1 <= nums[i] <= 10000`.
- Expected output format: The maximum number of points that can be earned.
- Key requirements and edge cases to consider: 
  - The points earned for each number `x` is `x * frequency(x)`, where `frequency(x)` is the number of times `x` appears in `nums`.
  - If `x` is deleted, all occurrences of `x-1` and `x+1` must also be deleted.
- Example test cases with explanations:
  - For `nums = [3,4,2]`, the maximum points that can be earned is `6` by deleting `2` and `4`, then earning `3 * 1 = 3` for `3`, and `4 * 1 = 3` for `4` is not possible because `3` and `4` cannot be deleted together, so we delete `2` and keep `3` and `4`, then the maximum points that can be earned is `3 * 1 + 4 * 1 = 7`.
  - For `nums = [2,2,3,3,3,4]`, the maximum points that can be earned is `9` by deleting `2` and `4`, then earning `3 * 3 = 9` for `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsets of `nums`, then for each subset, calculate the total points earned.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of `nums`.
  2. For each subset, calculate the total points earned by summing up `x * frequency(x)` for each `x` in the subset.
  3. Check if the subset is valid by ensuring that if `x` is in the subset, then `x-1` and `x+1` are not in the subset.
  4. Update the maximum points earned if the current subset is valid and earns more points.
- Why this approach comes to mind first: This approach is straightforward and ensures that all possible solutions are considered.

```cpp
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int maxNum = *max_element(nums.begin(), nums.end());
        vector<int> freq(maxNum + 1, 0);
        for (int num : nums) {
            freq[num]++;
        }
        int maxPoints = 0;
        vector<bool> visited(maxNum + 1, false);
        function<void(int, int)> dfs = [&](int index, int points) {
            if (index > maxNum) {
                maxPoints = max(maxPoints, points);
                return;
            }
            if (!visited[index]) {
                visited[index] = true;
                if (index > 1 && freq[index - 1] > 0) {
                    freq[index - 1] = 0;
                }
                if (index < maxNum && freq[index + 1] > 0) {
                    freq[index + 1] = 0;
                }
                dfs(index + 1, points + index * freq[index]);
                if (index > 1 && freq[index - 1] == 0) {
                    freq[index - 1] = 1;
                }
                if (index < maxNum && freq[index + 1] == 0) {
                    freq[index + 1] = 1;
                }
                visited[index] = false;
            }
            dfs(index + 1, points);
        };
        dfs(1, 0);
        return maxPoints;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of unique elements in `nums`, because we generate all possible subsets of `nums`.
> - **Space Complexity:** $O(n)$, because we use a recursive call stack to store the subsets.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of `nums`, which results in exponential time complexity. The space complexity is linear because we only need to store the current subset being processed.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the maximum points earned for each number up to `i`.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming array `dp` of size `maxNum + 1`, where `dp[i]` stores the maximum points earned for each number up to `i`.
  2. Initialize `dp[1]` to `freq[1]`, because we can earn `1 * freq[1]` points for `1`.
  3. For each number `i` from `2` to `maxNum`, calculate `dp[i]` as the maximum of `dp[i-1]` and `dp[i-2] + i * freq[i]`, because we can either skip `i` and earn `dp[i-1]` points, or include `i` and earn `dp[i-2] + i * freq[i]` points.
  4. The maximum points earned is stored in `dp[maxNum]`.
- Why further optimization is impossible: This approach has a linear time complexity and space complexity, which is optimal because we need to process each number in `nums` at least once.

```cpp
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int maxNum = *max_element(nums.begin(), nums.end());
        vector<int> freq(maxNum + 1, 0);
        for (int num : nums) {
            freq[num]++;
        }
        vector<int> dp(maxNum + 1, 0);
        dp[1] = freq[1];
        for (int i = 2; i <= maxNum; i++) {
            dp[i] = max(dp[i-1], dp[i-2] + i * freq[i]);
        }
        return dp[maxNum];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the maximum number in `nums`, because we process each number in `nums` once.
> - **Space Complexity:** $O(n)$, because we use a dynamic programming array of size `maxNum + 1`.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and space complexity, which is the minimum required to process each number in `nums` at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive approach.
- Problem-solving patterns identified: Using dynamic programming to store intermediate results and avoid redundant calculations.
- Optimization techniques learned: Using a bottom-up approach to fill up the dynamic programming array, avoiding unnecessary recursive calls.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the dynamic programming array, incorrect calculation of the maximum points earned.
- Edge cases to watch for: Handling the case where `nums` is empty, handling the case where `maxNum` is 0.
- Performance pitfalls: Using an exponential time complexity approach, using an excessive amount of memory to store the dynamic programming array.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.