## Minimize the Total Price of the Trips
**Problem Link:** https://leetcode.com/problems/minimize-the-total-price-of-the-trips/description

**Problem Statement:**
- Input: `n` (number of cities), `edges` (list of edges between cities, where each edge is a tuple of `(city1, city2, cost)`), and `discount` (a discount applied to the total cost after visiting a certain number of cities).
- Constraints: `1 <= n <= 10^5`, `0 <= edges.length <= 10^5`, `0 <= cost <= 10^5`, `0 <= discount <= 10^5`.
- Expected output: The minimum total cost of visiting all cities.
- Key requirements and edge cases to consider: 
    - All cities must be visited exactly once.
    - The order of visiting cities matters, as the discount is applied after visiting a certain number of cities.
    - The graph may not be fully connected.
- Example test cases with explanations:
    - For `n = 3`, `edges = [(0, 1, 10), (1, 2, 20), (2, 0, 30)]`, and `discount = 10`, the minimum total cost is `40` (visit cities in order `0 -> 1 -> 2`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible permutations of visiting cities and calculate the total cost for each permutation.
- The brute force approach generates all permutations of cities, then for each permutation, it calculates the total cost by summing the costs of edges between consecutive cities in the permutation.
- This approach comes to mind first because it is straightforward and guarantees finding the optimal solution, but it is inefficient for large inputs due to its high time complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minCost(int n, vector<vector<int>>& edges, int discount) {
    // Generate all permutations of cities
    vector<int> cities(n);
    for (int i = 0; i < n; i++) cities[i] = i;
    
    int minCost = INT_MAX;
    do {
        // Calculate the total cost for the current permutation
        int totalCost = 0;
        for (int i = 0; i < n - 1; i++) {
            // Find the edge between the current city and the next city
            for (auto& edge : edges) {
                if ((edge[0] == cities[i] && edge[1] == cities[i + 1]) || 
                    (edge[0] == cities[i + 1] && edge[1] == cities[i])) {
                    totalCost += edge[2];
                    break;
                }
            }
        }
        
        // Apply the discount
        totalCost -= discount;
        
        // Update the minimum cost
        minCost = min(minCost, totalCost);
    } while (next_permutation(cities.begin(), cities.end()));
    
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$, where $n$ is the number of cities and $m$ is the number of edges, because we generate all permutations of cities and for each permutation, we iterate over all edges to find the costs.
> - **Space Complexity:** $O(n)$, because we store the current permutation of cities.
> - **Why these complexities occur:** The high time complexity occurs because generating all permutations of cities is a factorial operation, and for each permutation, we iterate over all edges to calculate the total cost.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a more efficient algorithm that avoids generating all permutations of cities.
- We can use a variant of the Traveling Salesman Problem (TSP) algorithm, which is a classic problem in combinatorial optimization and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the original city.
- The TSP algorithm can be implemented using dynamic programming, which reduces the time complexity significantly.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int minCost(int n, vector<vector<int>>& edges, int discount) {
    // Create an adjacency matrix to represent the graph
    vector<vector<int>> graph(n, vector<int>(n, INT_MAX));
    for (auto& edge : edges) {
        graph[edge[0]][edge[1]] = edge[2];
        graph[edge[1]][edge[0]] = edge[2];
    }
    
    // Initialize the dp table
    vector<vector<int>> dp(1 << n, vector<int>(n, INT_MAX));
    dp[1][0] = 0;
    
    // Fill the dp table
    for (int mask = 1; mask < (1 << n); mask++) {
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) continue;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if ((mask & (1 << j)) == 0) continue;
                int newMask = mask ^ (1 << i);
                dp[mask][i] = min(dp[mask][i], dp[newMask][j] + graph[j][i]);
            }
        }
    }
    
    // Find the minimum cost
    int minCost = INT_MAX;
    for (int i = 0; i < n; i++) {
        minCost = min(minCost, dp[(1 << n) - 1][i]);
    }
    
    // Apply the discount
    minCost -= discount;
    
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot 2^n)$, where $n$ is the number of cities, because we fill the dp table using two nested loops, and the outer loop runs over all possible subsets of cities.
> - **Space Complexity:** $O(n \cdot 2^n)$, because we store the dp table, which has $n$ rows and $2^n$ columns.
> - **Optimality proof:** This solution is optimal because it uses dynamic programming to avoid redundant calculations and explores all possible subsets of cities, ensuring that the minimum cost is found.

---

### Final Notes

**Learning Points:**
- The Traveling Salesman Problem (TSP) is a classic problem in combinatorial optimization and operations research.
- Dynamic programming can be used to solve TSP efficiently.
- The adjacency matrix representation of a graph can be useful for solving graph problems.

**Mistakes to Avoid:**
- Generating all permutations of cities can lead to high time complexity.
- Not using dynamic programming to avoid redundant calculations can lead to inefficient solutions.
- Not considering the discount when calculating the minimum cost can lead to incorrect results.

---