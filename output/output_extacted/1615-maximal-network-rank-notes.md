## Maximal Network Rank
**Problem Link:** https://leetcode.com/problems/maximal-network-rank/description

**Problem Statement:**
- Input format: `n` (number of cities), `roads` (list of roads between cities)
- Constraints: `2 <= n <= 5 * 10^4`, `0 <= roads.length <= n * (n - 1) / 2`, `roads[i].length == 2`, `0 <= u_i, v_i <= n - 1`, `u_i != v_i`, `0 <= roads.length <= n * (n - 1) / 2`
- Expected output: Maximum possible network rank
- Key requirements: Calculate the maximum possible network rank by considering all possible pairs of cities and their connections
- Example test cases:
  - Input: `n = 4`, `roads = [[0,1],[0,3],[1,2],[1,3]]`
  - Output: `4`
  - Explanation: The maximum possible network rank is achieved when we consider the cities `1` and `3`. The city `1` has roads to cities `0`, `2`, and `3`, while the city `3` has roads to cities `0`, `1`. The total number of roads is `4`, which is the maximum possible network rank.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible pairs of cities and calculate the network rank for each pair by considering the roads between them.
- Step-by-step breakdown:
  1. Initialize the maximum network rank to `0`.
  2. Iterate through all possible pairs of cities.
  3. For each pair of cities, calculate the network rank by considering the roads between them.
  4. Update the maximum network rank if the current network rank is higher.

```cpp
int maximalNetworkRank(int n, vector<vector<int>>& roads) {
    int maxRank = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int rank = 0;
            for (auto& road : roads) {
                if (road[0] == i || road[0] == j || road[1] == i || road[1] == j) {
                    rank++;
                }
            }
            maxRank = max(maxRank, rank);
        }
    }
    return maxRank;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of cities and $m$ is the number of roads. This is because we iterate through all possible pairs of cities and for each pair, we iterate through all roads.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum network rank and the current rank.
> - **Why these complexities occur:** The time complexity occurs because we use nested loops to iterate through all possible pairs of cities and roads. The space complexity is constant because we only use a fixed amount of space to store the maximum network rank and the current rank.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of iterating through all roads for each pair of cities, we can use a more efficient data structure to store the roads for each city.
- Detailed breakdown:
  1. Create an adjacency list to store the roads for each city.
  2. Iterate through all possible pairs of cities.
  3. For each pair of cities, calculate the network rank by considering the roads between them using the adjacency list.
  4. Update the maximum network rank if the current network rank is higher.

```cpp
int maximalNetworkRank(int n, vector<vector<int>>& roads) {
    vector<unordered_set<int>> graph(n);
    for (auto& road : roads) {
        graph[road[0]].insert(road[1]);
        graph[road[1]].insert(road[0]);
    }
    int maxRank = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int rank = graph[i].size() + graph[j].size();
            if (graph[i].count(j)) {
                rank--;
            }
            maxRank = max(maxRank, rank);
        }
    }
    return maxRank;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 + m)$, where $n$ is the number of cities and $m$ is the number of roads. This is because we create an adjacency list and then iterate through all possible pairs of cities.
> - **Space Complexity:** $O(n + m)$, as we use an adjacency list to store the roads for each city.
> - **Optimality proof:** This approach is optimal because we use a more efficient data structure to store the roads for each city, reducing the time complexity from $O(n^2 \cdot m)$ to $O(n^2 + m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a more efficient data structure to store the roads for each city.
- Problem-solving patterns identified: Iterating through all possible pairs of cities and using a more efficient data structure to calculate the network rank.
- Optimization techniques learned: Using an adjacency list to store the roads for each city.
- Similar problems to practice: Other graph-related problems that require finding the maximum or minimum value for a given set of nodes or edges.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the case where two cities are connected by a road.
- Edge cases to watch for: The case where there are no roads between any cities.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the code with different inputs to ensure it works correctly for all possible cases.