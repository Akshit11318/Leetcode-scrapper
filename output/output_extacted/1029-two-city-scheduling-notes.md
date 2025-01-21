## Two City Scheduling

**Problem Link:** https://leetcode.com/problems/two-city-scheduling/description

**Problem Statement:**
- Input format: A 2D vector `costs` where `costs[i][0]` is the cost of sending the `i-th` person to city A, and `costs[i][1]` is the cost of sending the `i-th` person to city B.
- Constraints: `2 <= costs.length <= 100`, `costs[i].length == 2`, `1 <= costs[i][j] <= 1000`.
- Expected output format: The minimum cost to send exactly `n/2` people to each city.
- Key requirements: Minimize the total cost by deciding which people to send to city A and which to city B.
- Edge cases: When the number of people is odd, it's not possible to divide them evenly between two cities. However, the problem states that `n` is even.

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of sending people to city A and city B.
- We can use a recursive approach or bit manipulation to generate all possible subsets of people to send to city A.
- Calculate the total cost for each subset and return the minimum cost found.

```cpp
int twoCitySchedCost(vector<vector<int>>& costs) {
    int n = costs.size();
    int minCost = INT_MAX;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (__builtin_popcount(mask) == n / 2) {
            int cost = 0;
            for (int i = 0; i < n; i++) {
                if ((mask >> i) & 1) {
                    cost += costs[i][0];
                } else {
                    cost += costs[i][1];
                }
            }
            minCost = min(minCost, cost);
        }
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of people. This is because we're generating all possible subsets of people.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost and the current subset.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, leading to exponential time complexity. The space complexity is constant because we only use a fixed amount of space to store the minimum cost and the current subset.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we should send the people with the largest difference between the cost of city A and city B to city A.
- We can calculate the difference for each person and sort them in descending order.
- Then, we send the top `n/2` people to city A and the rest to city B.

```cpp
int twoCitySchedCost(vector<vector<int>>& costs) {
    int n = costs.size();
    int minCost = 0;
    vector<int> diff(n);
    for (int i = 0; i < n; i++) {
        diff[i] = costs[i][0] - costs[i][1];
    }
    sort(diff.begin(), diff.end(), greater<int>());
    for (int i = 0; i < n; i++) {
        if (i < n / 2) {
            minCost += costs[i][0];
        } else {
            minCost += costs[i][1];
        }
    }
    return minCost;
}
```

However, the above code has an issue as we are not considering the original index of the costs array after sorting the difference array. Here is the correct code:

```cpp
int twoCitySchedCost(vector<vector<int>>& costs) {
    int n = costs.size();
    int minCost = 0;
    vector<pair<int, int>> diff(n);
    for (int i = 0; i < n; i++) {
        diff[i] = {costs[i][0] - costs[i][1], i};
    }
    sort(diff.begin(), diff.end(), greater<pair<int, int>>());
    for (int i = 0; i < n; i++) {
        if (i < n / 2) {
            minCost += costs[diff[i].second][0];
        } else {
            minCost += costs[diff[i].second][1];
        }
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of people. This is because we're sorting the differences.
> - **Space Complexity:** $O(n)$, as we need to store the differences and their original indices.
> - **Optimality proof:** This is the optimal solution because we're sending the people with the largest difference between the cost of city A and city B to city A, which minimizes the total cost.

### Final Notes

**Learning Points:**
- The importance of sorting and greedy algorithms in solving optimization problems.
- How to calculate the difference between two costs and use it to make decisions.
- The use of `pair` to store the difference and the original index.

**Mistakes to Avoid:**
- Not considering the original index of the costs array after sorting the difference array.
- Not using the correct data structure to store the differences and their original indices.
- Not using the greedy approach to minimize the total cost.