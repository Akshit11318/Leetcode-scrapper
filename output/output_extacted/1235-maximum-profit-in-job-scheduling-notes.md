## Maximum Profit in Job Scheduling
**Problem Link:** https://leetcode.com/problems/maximum-profit-in-job-scheduling/description

**Problem Statement:**
- Input: An array of `jobs` where each job is an array `[startTime, endTime, profit]`.
- Constraints: `1 <= startTime < endTime <= 10^5`, `1 <= profit <= 10^4`, and `1 <= jobs.length <= 500`.
- Expected Output: The maximum possible profit that can be achieved by scheduling jobs without conflicts.
- Key Requirements and Edge Cases:
  - Jobs cannot overlap in time.
  - The goal is to maximize the total profit.

**Example Test Cases:**
- For `jobs = [[1,2,50],[1,5,100],[2,100,200],[2,20,50]]`, the maximum profit is `250`.
- For `jobs = [[1,2,50],[1,5,50],[2,3,100]]`, the maximum profit is `100`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of jobs and select the combination that gives the maximum profit without any conflicts.
- Step-by-step breakdown:
  1. Generate all permutations of jobs.
  2. For each permutation, check for conflicts (overlapping jobs).
  3. For conflict-free permutations, calculate the total profit.
  4. Keep track of the maximum profit found.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int jobScheduling(vector<vector<int>>& jobs) {
    // Sort jobs by end time
    sort(jobs.begin(), jobs.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    
    int maxProfit = 0;
    for (int i = 0; i < (1 << jobs.size()); i++) {
        int profit = 0;
        int lastEndTime = 0;
        for (int j = 0; j < jobs.size(); j++) {
            if ((i & (1 << j)) && jobs[j][0] >= lastEndTime) {
                profit += jobs[j][2];
                lastEndTime = jobs[j][1];
            }
        }
        maxProfit = max(maxProfit, profit);
    }
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ where $n$ is the number of jobs. The reason is that we generate all permutations of jobs (which is $2^n$) and for each permutation, we potentially iterate through all jobs once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we only use a constant amount of space to store the maximum profit and other variables.
> - **Why these complexities occur:** The exponential time complexity is due to generating all permutations of jobs, which leads to an inefficient algorithm for large inputs.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use dynamic programming to store the maximum profit that can be achieved up to each job, considering only non-conflicting jobs.
- Detailed breakdown:
  1. Sort jobs by end time.
  2. Initialize a dynamic programming (DP) array `dp` where `dp[i]` represents the maximum profit achievable up to the `i-th` job.
  3. For each job, find the last non-conflicting job and update `dp[i]` with the maximum of its current value and the profit of the current job plus the profit of the last non-conflicting job.
  4. The final answer is the maximum value in the `dp` array.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int jobScheduling(vector<vector<int>>& jobs) {
    sort(jobs.begin(), jobs.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    
    int n = jobs.size();
    vector<int> dp(n);
    dp[0] = jobs[0][2];
    
    for (int i = 1; i < n; i++) {
        int incl = jobs[i][2];
        int lastNonConflict = -1;
        for (int j = i - 1; j >= 0; j--) {
            if (jobs[j][1] <= jobs[i][0]) {
                lastNonConflict = j;
                break;
            }
        }
        if (lastNonConflict != -1) {
            incl += dp[lastNonConflict];
        }
        dp[i] = max(dp[i - 1], incl);
    }
    
    return dp[n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because for each job, we potentially iterate through all previous jobs to find the last non-conflicting one.
> - **Space Complexity:** $O(n)$ for the DP array.
> - **Optimality proof:** This approach is optimal because it considers all possible non-conflicting combinations of jobs and keeps track of the maximum profit achievable up to each job, ensuring that no better solution is overlooked.

---

### Final Notes

**Learning Points:**
- Dynamic programming can be used to solve problems that have overlapping subproblems and optimal substructure.
- Sorting jobs by end time helps in efficiently finding non-conflicting jobs.
- The key to solving such problems lies in identifying the correct DP state and transition.

**Mistakes to Avoid:**
- Not considering all possible non-conflicting combinations of jobs.
- Incorrectly updating the DP array, leading to suboptimal solutions.
- Not handling edge cases properly, such as an empty input array.