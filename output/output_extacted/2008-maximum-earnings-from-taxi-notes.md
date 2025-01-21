## Maximum Earnings from Taxi
**Problem Link:** https://leetcode.com/problems/maximum-earnings-from-taxi/description

**Problem Statement:**
- Input format and constraints: The problem takes in a list of `n` trips, where each trip is represented by a tuple `(t, a, b)`, denoting the time `t`, and the start and end points `a` and `b`. The goal is to find the maximum earnings possible.
- Expected output format: The maximum earnings as an integer.
- Key requirements and edge cases to consider: The taxi can only take one trip at a time, and it cannot be in two places at once. The earnings for each trip are calculated as the distance between the start and end points.
- Example test cases with explanations:
  - For example, given the trips `[(2,1,5),(3,3,7),(2,10,11),(3,5,8),(3,4,6),(2,5,7)]`, the maximum earnings would be 20.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the maximum earnings, we could try all possible combinations of trips and calculate the earnings for each combination.
- Step-by-step breakdown of the solution: 
  1. Generate all permutations of trips.
  2. For each permutation, calculate the earnings by summing the distances of the trips that can be taken without any conflicts.
  3. Keep track of the maximum earnings found so far.
- Why this approach comes to mind first: It's a straightforward approach that tries all possibilities, which is often the first step in solving a problem.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxEarnings(vector<vector<int>>& trips) {
    int maxEarnings = 0;
    sort(trips.begin(), trips.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    int n = trips.size();
    for (int mask = 0; mask < (1 << n); ++mask) {
        int earnings = 0;
        int lastTime = 0;
        bool valid = true;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                if (trips[i][0] < lastTime) {
                    valid = false;
                    break;
                }
                earnings += trips[i][2] - trips[i][1];
                lastTime = trips[i][0];
            }
        }
        if (valid) {
            maxEarnings = max(maxEarnings, earnings);
        }
    }
    return maxEarnings;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot log(n))$ due to the sorting and the iteration over all permutations of trips.
> - **Space Complexity:** $O(n)$ for storing the trips and the permutation.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of trips, resulting in an exponential time complexity. The sorting step adds a logarithmic factor to the time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The trips can be sorted by their end times, and then we can use dynamic programming to find the maximum earnings.
- Detailed breakdown of the approach: 
  1. Sort the trips by their end times.
  2. Create a dynamic programming table `dp` where `dp[i]` represents the maximum earnings that can be obtained by taking trips up to the `i-th` trip.
  3. For each trip, find the maximum earnings that can be obtained by not taking the current trip and the maximum earnings that can be obtained by taking the current trip.
  4. Update the `dp` table accordingly.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of trips and find the maximum earnings.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxEarnings(vector<vector<int>>& trips) {
    sort(trips.begin(), trips.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    int n = trips.size();
    vector<int> dp(n);
    dp[0] = trips[0][2] - trips[0][1];
    for (int i = 1; i < n; ++i) {
        int maxEarnings = 0;
        for (int j = 0; j < i; ++j) {
            if (trips[j][0] <= trips[i][0]) {
                maxEarnings = max(maxEarnings, dp[j]);
            }
        }
        dp[i] = max(maxEarnings + trips[i][2] - trips[i][1], dp[i-1]);
    }
    return dp[n-1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ due to the nested loops.
> - **Space Complexity:** $O(n)$ for storing the dynamic programming table.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of trips and find the maximum earnings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, sorting.
- Problem-solving patterns identified: Using dynamic programming to find the maximum earnings.
- Optimization techniques learned: Using sorting to reduce the time complexity.
- Similar problems to practice: Other dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible combinations of trips.
- Edge cases to watch for: Trips with the same end time.
- Performance pitfalls: Using a brute force approach with an exponential time complexity.
- Testing considerations: Testing the solution with different inputs and edge cases.