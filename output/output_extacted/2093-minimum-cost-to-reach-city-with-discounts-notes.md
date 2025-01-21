## Minimum Cost to Reach City with Discounts
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/description

**Problem Statement:**
- Given a `graph` representing the cities and their connections with costs, a `start` city, and a `target` city, find the minimum cost to reach the target city from the start city. The graph is represented as an adjacency list where each element is a tuple of `(city, cost)`.
- Input format: `graph`, `start`, `target`
- Constraints: The graph is guaranteed to be connected, and there are no self-loops or multiple edges between the same pair of cities.
- Expected output format: The minimum cost to reach the target city from the start city.
- Key requirements: The solution should handle the case where there are no discounts and the case where there are discounts.
- Edge cases: The start city is the same as the target city, or there is no path from the start city to the target city.

**Example Test Cases:**
- `graph = [[0, 1, 5], [1, 0, 3], [2, 0, 2]]`, `start = 0`, `target = 2`. The minimum cost is `5`.
- `graph = [[0, 1, 10], [1, 0, 2], [2, 0, 3]]`, `start = 0`, `target = 2`. The minimum cost is `3`.

### Brute Force Approach

**Explanation:**
- The brute force approach involves trying all possible paths from the start city to the target city and calculating the cost for each path.
- We can use a recursive depth-first search (DFS) to explore all possible paths.
- For each path, we calculate the cost by summing up the costs of all edges in the path.

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

int minCost(vector<vector<int>>& graph, int start, int target) {
    unordered_set<int> visited;
    int minCost = INT_MAX;
    dfs(graph, start, target, 0, visited, minCost);
    return minCost;
}

void dfs(vector<vector<int>>& graph, int currentCity, int target, int currentCost, unordered_set<int>& visited, int& minCost) {
    if (currentCity == target) {
        minCost = min(minCost, currentCost);
        return;
    }
    visited.insert(currentCity);
    for (auto& neighbor : graph[currentCity]) {
        int city = neighbor[0];
        int cost = neighbor[1];
        if (visited.find(city) == visited.end()) {
            dfs(graph, city, target, currentCost + cost, visited, minCost);
        }
    }
    visited.erase(currentCity);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$ where $n$ is the number of cities and $m$ is the average number of neighbors for each city. This is because we are trying all possible paths, and for each path, we are iterating over all neighbors of each city.
> - **Space Complexity:** $O(n)$ where $n$ is the number of cities. This is because we are using a recursive call stack to store the current path, and the maximum depth of the call stack is $n$.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible paths, which results in an exponential number of iterations. The space complexity is relatively low because we are only using a recursive call stack to store the current path.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using Dijkstra's algorithm with a priority queue to find the shortest path from the start city to the target city.
- We can use a `priority_queue` to store the cities to be visited, where the priority of each city is its current minimum cost.
- We can use a `unordered_map` to store the minimum cost for each city.

```cpp
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

int minCost(vector<vector<int>>& graph, int start, int target) {
    unordered_map<int, int> minCost;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    while (!pq.empty()) {
        int currentCost = pq.top().first;
        int currentCity = pq.top().second;
        pq.pop();
        if (currentCity == target) {
            return currentCost;
        }
        if (minCost.find(currentCity) != minCost.end() && minCost[currentCity] <= currentCost) {
            continue;
        }
        minCost[currentCity] = currentCost;
        for (auto& neighbor : graph[currentCity]) {
            int city = neighbor[0];
            int cost = neighbor[1];
            pq.push({currentCost + cost, city});
        }
    }
    return -1; // no path found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((n + m) \cdot log(n))$ where $n$ is the number of cities and $m$ is the total number of edges. This is because we are using a priority queue to store the cities to be visited, and the priority queue operations take $O(log(n))$ time.
> - **Space Complexity:** $O(n + m)$ where $n$ is the number of cities and $m$ is the total number of edges. This is because we are using a priority queue to store the cities to be visited, and an unordered map to store the minimum cost for each city.
> - **Optimality proof:** The optimal approach is guaranteed to find the shortest path from the start city to the target city because it uses Dijkstra's algorithm, which is a well-known algorithm for finding the shortest path in a graph.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dijkstra's algorithm, priority queue, unordered map.
- Problem-solving patterns identified: using a priority queue to store the cities to be visited, using an unordered map to store the minimum cost for each city.
- Optimization techniques learned: using a priority queue to reduce the time complexity, using an unordered map to reduce the space complexity.
- Similar problems to practice: finding the shortest path in a weighted graph, finding the minimum cost to reach a target city with discounts.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where there are no discounts, not handling the case where there is no path from the start city to the target city.
- Edge cases to watch for: the start city is the same as the target city, there is no path from the start city to the target city.
- Performance pitfalls: using a brute force approach, not using a priority queue to store the cities to be visited.
- Testing considerations: testing the case where there are no discounts, testing the case where there is no path from the start city to the target city.