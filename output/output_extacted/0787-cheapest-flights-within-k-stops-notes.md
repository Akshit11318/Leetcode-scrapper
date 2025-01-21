## Cheapest Flights Within K Stops
**Problem Link:** https://leetcode.com/problems/cheapest-flights-within-k-stops/description

**Problem Statement:**
- Input format and constraints: The function takes four parameters: `n` (the number of cities), `flights` (a list of flights where each flight is a list of three integers `[from, to, price]`), `src` (the source city), and `dst` (the destination city), and `K` (the maximum number of stops).
- Expected output format: The function returns the cheapest price to fly from `src` to `dst` with at most `K` stops. If it is impossible to fly from `src` to `dst` with at most `K` stops, return `-1`.
- Key requirements and edge cases to consider: The graph is represented as a list of edges, and the weights are the prices of the flights.
- Example test cases with explanations:
  - `n = 3`, `flights = [[0,1,100],[1,2,100],[0,2,500]]`, `src = 0`, `dst = 2`, `K = 1`. The output should be `200`.
  - `n = 3`, `flights = [[0,1,100],[1,2,100],[0,2,500]]`, `src = 0`, `dst = 2`, `K = 0`. The output should be `500`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves trying all possible paths from the source city to the destination city and keeping track of the minimum cost.
- Step-by-step breakdown of the solution:
  1. Generate all possible paths from the source city to the destination city.
  2. For each path, calculate the total cost.
  3. Keep track of the minimum cost.
- Why this approach comes to mind first: It is a straightforward approach that tries all possibilities.

```cpp
#include <vector>
using namespace std;

int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
    // Generate all possible paths
    vector<vector<int>> paths;
    vector<int> path;
    dfs(flights, src, dst, K, path, paths);
    
    // Initialize minimum cost to infinity
    int minCost = INT_MAX;
    
    // Calculate the minimum cost
    for (const auto& path : paths) {
        int cost = 0;
        for (int i = 0; i < path.size() - 1; ++i) {
            // Find the cost of the flight from city i to city i+1
            for (const auto& flight : flights) {
                if (flight[0] == path[i] && flight[1] == path[i + 1]) {
                    cost += flight[2];
                    break;
                }
            }
        }
        // Update the minimum cost
        minCost = min(minCost, cost);
    }
    
    // Return the minimum cost if it is not infinity, otherwise return -1
    return minCost == INT_MAX ? -1 : minCost;
}

void dfs(vector<vector<int>>& flights, int src, int dst, int K, vector<int>& path, vector<vector<int>>& paths) {
    // Add the current city to the path
    path.push_back(src);
    
    // If the current city is the destination city and the number of stops is not exceeded
    if (src == dst && path.size() - 1 <= K + 1) {
        paths.push_back(path);
    } else if (path.size() - 1 <= K + 1) {
        // For each neighboring city that has not been visited
        for (const auto& flight : flights) {
            if (flight[0] == src && find(path.begin(), path.end(), flight[1]) == path.end()) {
                // Recursively call the dfs function
                dfs(flights, flight[1], dst, K, path, paths);
            }
        }
    }
    
    // Remove the current city from the path
    path.pop_back();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^{K+1})$ where $n$ is the number of cities and $K$ is the maximum number of stops. This is because in the worst case, we need to try all possible paths of length up to $K+1$.
> - **Space Complexity:** $O(n^{K+1})$ where $n$ is the number of cities and $K$ is the maximum number of stops. This is because we need to store all possible paths.
> - **Why these complexities occur:** The brute force approach involves trying all possible paths, which results in exponential time and space complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a modified version of Dijkstra's algorithm with a priority queue.
- Detailed breakdown of the approach:
  1. Create a priority queue to store the cities to be visited, where the priority is the minimum cost to reach each city.
  2. Initialize the priority queue with the source city and a cost of 0.
  3. While the priority queue is not empty, extract the city with the minimum cost and update the costs of its neighboring cities.
  4. If the destination city is reached and the number of stops is not exceeded, return the minimum cost.
- Proof of optimality: The modified Dijkstra's algorithm is optimal because it always chooses the city with the minimum cost to visit next, which ensures that the minimum cost to reach the destination city is found.

```cpp
#include <queue>
#include <vector>
using namespace std;

struct Node {
    int city;
    int cost;
    int stops;
};

struct Compare {
    bool operator()(const Node& a, const Node& b) {
        return a.cost > b.cost;
    }
};

int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
    // Create a priority queue
    priority_queue<Node, vector<Node>, Compare> pq;
    
    // Initialize the priority queue with the source city
    pq.push({src, 0, 0});
    
    // Initialize the minimum cost to infinity
    int minCost = INT_MAX;
    
    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        
        // If the current city is the destination city and the number of stops is not exceeded
        if (node.city == dst && node.stops <= K + 1) {
            // Update the minimum cost
            minCost = min(minCost, node.cost);
        }
        
        // If the number of stops is exceeded, skip the current city
        if (node.stops > K + 1) {
            continue;
        }
        
        // For each neighboring city
        for (const auto& flight : flights) {
            if (flight[0] == node.city) {
                // Push the neighboring city into the priority queue
                pq.push({flight[1], node.cost + flight[2], node.stops + 1});
            }
        }
    }
    
    // Return the minimum cost if it is not infinity, otherwise return -1
    return minCost == INT_MAX ? -1 : minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log n)$ where $n$ is the number of cities and $m$ is the number of flights. This is because we use a priority queue to store the cities to be visited.
> - **Space Complexity:** $O(n + m)$ where $n$ is the number of cities and $m$ is the number of flights. This is because we need to store the cities and flights.
> - **Optimality proof:** The modified Dijkstra's algorithm is optimal because it always chooses the city with the minimum cost to visit next, which ensures that the minimum cost to reach the destination city is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dijkstra's algorithm, priority queue.
- Problem-solving patterns identified: Using a priority queue to solve the problem efficiently.
- Optimization techniques learned: Modifying Dijkstra's algorithm to solve the problem with a limited number of stops.
- Similar problems to practice: Other problems that involve finding the minimum cost or shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the destination city is not reachable.
- Edge cases to watch for: The case where the number of stops is exceeded.
- Performance pitfalls: Using an inefficient algorithm that has a high time complexity.
- Testing considerations: Testing the function with different inputs to ensure that it works correctly in all cases.