## Minimum Difficulty of a Job Schedule
**Problem Link:** https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description

**Problem Statement:**
- Input: A list of integers `jobDifficulty` representing the difficulty levels of jobs, and an integer `d` representing the number of days to schedule the jobs.
- Constraints: $1 \leq jobDifficulty.length \leq 300$, $1 \leq jobDifficulty[i] \leq 1000$, $1 \leq d \leq jobDifficulty.length$.
- Expected Output: The minimum difficulty of a job schedule.
- Key Requirements: The minimum difficulty of a job schedule is the sum of the maximum difficulty of each day.
- Edge Cases: When `d` equals the length of `jobDifficulty`, the minimum difficulty is the sum of all difficulties. When `d` is 1, the minimum difficulty is the maximum difficulty of all jobs.

**Example Test Cases:**
- `jobDifficulty = [6, 5, 4, 3, 2, 1]`, `d = 2`. The minimum difficulty is `max(6, 5) + max(4, 3, 2, 1) = 6 + 4 = 10`.
- `jobDifficulty = [9, 9, 9]`, `d = 4`. The minimum difficulty is `-1` because it's impossible to schedule the jobs into 4 days.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations of scheduling the jobs into `d` days.
- We use recursion to try all possible combinations and calculate the minimum difficulty for each combination.
- This approach comes to mind first because it's straightforward and easy to implement.

```cpp
class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        int n = jobDifficulty.size();
        if (n < d) return -1;
        return dfs(jobDifficulty, d, 0);
    }

    int dfs(vector<int>& jobDifficulty, int d, int start) {
        if (d == 1) {
            int maxVal = 0;
            for (int i = start; i < jobDifficulty.size(); i++) {
                maxVal = max(maxVal, jobDifficulty[i]);
            }
            return maxVal;
        }
        int minVal = INT_MAX;
        int maxVal = 0;
        for (int i = start; i <= jobDifficulty.size() - d; i++) {
            maxVal = max(maxVal, jobDifficulty[i]);
            int val = maxVal + dfs(jobDifficulty, d - 1, i + 1);
            minVal = min(minVal, val);
        }
        return minVal;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ because we're trying all possible combinations of scheduling the jobs.
> - **Space Complexity:** $O(n)$ because of the recursion stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, resulting in exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use dynamic programming to store the minimum difficulty for each subproblem.
- We use a memoization table to store the minimum difficulty for each subproblem and avoid redundant calculations.
- The optimal solution is to use a bottom-up dynamic programming approach to calculate the minimum difficulty for each subproblem.

```cpp
class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        int n = jobDifficulty.size();
        if (n < d) return -1;
        vector<vector<int>> memo(n + 1, vector<int>(d + 1, INT_MAX));
        return dfs(jobDifficulty, d, 0, memo);
    }

    int dfs(vector<int>& jobDifficulty, int d, int start, vector<vector<int>>& memo) {
        if (d == 1) {
            int maxVal = 0;
            for (int i = start; i < jobDifficulty.size(); i++) {
                maxVal = max(maxVal, jobDifficulty[i]);
            }
            return maxVal;
        }
        if (memo[start][d] != INT_MAX) return memo[start][d];
        int minVal = INT_MAX;
        int maxVal = 0;
        for (int i = start; i <= jobDifficulty.size() - d; i++) {
            maxVal = max(maxVal, jobDifficulty[i]);
            int val = maxVal + dfs(jobDifficulty, d - 1, i + 1, memo);
            minVal = min(minVal, val);
        }
        memo[start][d] = minVal;
        return minVal;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot d)$ because we're using dynamic programming to store the minimum difficulty for each subproblem.
> - **Space Complexity:** $O(n \cdot d)$ because of the memoization table.
> - **Optimality proof:** The optimal approach uses dynamic programming to avoid redundant calculations and has a polynomial time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, memoization, and recursion.
- Problem-solving patterns identified: breaking down the problem into subproblems and using dynamic programming to store the minimum difficulty for each subproblem.
- Optimization techniques learned: using memoization to avoid redundant calculations and reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not using memoization to avoid redundant calculations.
- Edge cases to watch for: when `d` equals the length of `jobDifficulty`, when `d` is 1.
- Performance pitfalls: using a brute force approach with exponential time complexity.
- Testing considerations: testing the solution with different inputs, including edge cases, to ensure correctness and efficiency.