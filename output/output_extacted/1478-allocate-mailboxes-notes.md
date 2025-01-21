## Allocate Mailboxes
**Problem Link:** [https://leetcode.com/problems/allocate-mailboxes/description](https://leetcode.com/problems/allocate-mailboxes/description)

**Problem Statement:**
- Input: `houses` - a list of integers representing house locations, `k` - the number of mailboxes to allocate.
- Output: The minimum distance between each house and its nearest mailbox.
- Key requirements: Allocate `k` mailboxes to minimize the maximum distance between each house and its nearest mailbox.
- Edge cases: `houses` may be empty, `k` may be greater than the number of houses.

Example test cases:
- `houses = [1,4,8,10,20], k = 3`
- `houses = [2,3,5,12,18,23,38,41,42,47], k = 4`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of mailbox allocations and calculate the maximum distance for each combination.
- We will use a recursive approach to try all possible allocations.
- This approach comes to mind first because it ensures we consider all possibilities.

```cpp
class Solution {
public:
    int minDistance(vector<int>& houses, int k) {
        sort(houses.begin(), houses.end());
        int n = houses.size();
        vector<vector<int>> dist(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int sum = 0;
                for (int x = i; x <= j; x++) {
                    sum += abs(houses[x] - houses[(i + j) / 2]);
                }
                dist[i][j] = sum;
            }
        }
        return dfs(houses, k, 0, dist);
    }
    
    int dfs(vector<int>& houses, int k, int start, vector<vector<int>>& dist) {
        int n = houses.size();
        if (k == 0) {
            if (start == n) return 0;
            else return INT_MAX;
        }
        int res = INT_MAX;
        for (int i = start; i < n; i++) {
            int val = dfs(houses, k - 1, i + 1, dist);
            if (val != INT_MAX) {
                res = min(res, max(dist[start][i], val));
            }
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k \cdot n^2)$, where $n$ is the number of houses and $k$ is the number of mailboxes. The recursive function is called $2^k$ times, and for each call, we iterate over the houses.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of houses. We store the distances between each pair of houses in a 2D array.
> - **Why these complexities occur:** The recursive approach tries all possible allocations, resulting in exponential time complexity. The space complexity is due to the storage of distances between each pair of houses.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the minimum distance for each subproblem.
- We will use a 2D array `dp` to store the minimum distance for each subproblem, where `dp[i][j]` represents the minimum distance for the first `i` houses and `j` mailboxes.
- We will iterate over the houses and mailboxes, and for each subproblem, we will try all possible allocations and update the minimum distance.

```cpp
class Solution {
public:
    int minDistance(vector<int>& houses, int k) {
        sort(houses.begin(), houses.end());
        int n = houses.size();
        vector<vector<int>> dist(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int sum = 0;
                for (int x = i; x <= j; x++) {
                    sum += abs(houses[x] - houses[(i + j) / 2]);
                }
                dist[i][j] = sum;
            }
        }
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= min(i, k); j++) {
                for (int x = 0; x < i; x++) {
                    dp[i][j] = min(dp[i][j], max(dp[x][j - 1], dist[x][i - 1]));
                }
            }
        }
        return dp[n][k];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the number of houses and $k$ is the number of mailboxes. We iterate over the houses and mailboxes, and for each subproblem, we try all possible allocations.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the number of houses and $k$ is the number of mailboxes. We store the minimum distance for each subproblem in a 2D array.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible allocations and store the minimum distance for each subproblem, resulting in the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursive approach.
- Problem-solving patterns identified: trying all possible allocations, storing minimum distance for each subproblem.
- Optimization techniques learned: using dynamic programming to reduce time complexity.
- Similar problems to practice: problems involving dynamic programming and recursive approach.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of arrays, incorrect update of minimum distance.
- Edge cases to watch for: empty input array, `k` greater than the number of houses.
- Performance pitfalls: using recursive approach without memoization, resulting in exponential time complexity.
- Testing considerations: testing with different input sizes, testing with edge cases.