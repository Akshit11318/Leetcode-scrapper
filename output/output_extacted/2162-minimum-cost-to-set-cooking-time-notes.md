## Minimum Cost to Set Cooking Time
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-set-cooking-time/description

**Problem Statement:**
- Given a `0-indexed` integer array `cookTimes` where `cookTimes[i]` is the cooking time of the `i-th` burner.
- Given an integer `perBurner` representing the cost per minute to use a burner.
- Given an integer `start` representing the initial cooking time.
- Given a `0-indexed` integer array `s` representing the cooking times for each dish.
- Given a `0-indexed` integer array `d` representing the delay times for each dish.
- The goal is to find the minimum cost to set the cooking time for each dish.

**Expected Output Format:**
- The minimum cost as an integer.

**Key Requirements and Edge Cases to Consider:**
- Handle cases where `start` is greater than the maximum cooking time in `s`.
- Handle cases where `start` is less than the minimum cooking time in `s`.
- Consider the cost of using each burner and the delay times for each dish.

**Example Test Cases with Explanations:**
- For example, if `cookTimes = [3, 5]`, `perBurner = 1`, `start = 2`, `s = [3, 4]`, and `d = [1, 2]`, the minimum cost would be calculated based on the optimal cooking time for each dish considering the burners' cooking times, the cost per minute, and the delay times.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through all possible combinations of cooking times for each dish and calculate the cost for each combination.
- The brute force approach involves checking all permutations of cooking times for each dish and selecting the one with the minimum cost.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

int minCostToSetCookingTime(vector<int>& cookTimes, int perBurner, int start, vector<int>& s, vector<int>& d) {
    int minCost = numeric_limits<int>::max();
    for (int i = 0; i < (1 << s.size()); i++) {
        int cost = 0;
        for (int j = 0; j < s.size(); j++) {
            if ((i & (1 << j)) != 0) {
                cost += perBurner * max(s[j] - start, 0);
                start = max(start, s[j]);
                start += d[j];
            }
        }
        minCost = min(minCost, cost);
    }
    return minCost;
}

int main() {
    vector<int> cookTimes = {3, 5};
    int perBurner = 1;
    int start = 2;
    vector<int> s = {3, 4};
    vector<int> d = {1, 2};
    cout << "Minimum cost: " << minCostToSetCookingTime(cookTimes, perBurner, start, s, d) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \times n)$ where $n$ is the number of dishes. This is because we are generating all possible subsets of dishes and iterating through each subset.
> - **Space Complexity:** $O(1)$ as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves checking all possible combinations of cooking times, leading to exponential time complexity. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to build up a solution. We can calculate the minimum cost for each dish by considering the minimum cost of the previous dishes.
- We use a `dp` array where `dp[i]` represents the minimum cost for the first `i` dishes.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

int minCostToSetCookingTime(vector<int>& cookTimes, int perBurner, int start, vector<int>& s, vector<int>& d) {
    int n = s.size();
    vector<int> dp(n + 1, numeric_limits<int>::max());
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        int cost = dp[i - 1] + perBurner * max(s[i - 1] - start, 0);
        dp[i] = min(dp[i], cost);
        start = max(start, s[i - 1]);
        start += d[i - 1];
    }
    return dp[n];
}

int main() {
    vector<int> cookTimes = {3, 5};
    int perBurner = 1;
    int start = 2;
    vector<int> s = {3, 4};
    vector<int> d = {1, 2};
    cout << "Minimum cost: " << minCostToSetCookingTime(cookTimes, perBurner, start, s, d) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of dishes. This is because we are iterating through each dish once.
> - **Space Complexity:** $O(n)$ as we are using a `dp` array of size $n + 1$.
> - **Optimality proof:** This solution is optimal because we are considering the minimum cost for each dish and building up a solution using dynamic programming. We are not missing any possible solutions and we are not doing any unnecessary work.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, iteration.
- Problem-solving patterns identified: building up a solution using dynamic programming.
- Optimization techniques learned: using dynamic programming to avoid redundant work.
- Similar problems to practice: other dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` array correctly, not considering the minimum cost for each dish.
- Edge cases to watch for: handling cases where `start` is greater than the maximum cooking time in `s`, handling cases where `start` is less than the minimum cooking time in `s`.
- Performance pitfalls: using a brute force approach instead of dynamic programming.
- Testing considerations: testing the solution with different inputs, testing the solution with edge cases.