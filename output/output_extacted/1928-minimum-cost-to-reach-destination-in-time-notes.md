## Minimum Cost to Reach Destination in Time
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/description

**Problem Statement:**
- Input format: You are given `n` cities and `flights` representing the cost and time for each flight between two cities. You also have `start` and `end` cities, and a `maxTime` constraint.
- Constraints: `1 <= n <= 100`, `1 <= flights.length <= 500`, `1 <= start, end <= n`, `1 <= maxTime <= 1000`.
- Expected output format: The minimum cost to reach the destination within the given time limit.
- Key requirements and edge cases to consider:
  - Handling cases where there are no flights from the start city or to the end city.
  - Ensuring that the total time for the path does not exceed `maxTime`.
- Example test cases with explanations:
  - A simple case with direct flights from start to end.
  - A case where the optimal path involves multiple flights with varying costs and times.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Enumerate all possible paths from the start city to the end city and calculate their total cost and time.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of flights that could lead from the start city to the end city.
  2. For each permutation, calculate the total cost and time.
  3. Check if the total time does not exceed `maxTime`.
  4. Among valid paths, find the one with the minimum cost.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that considers all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int findCheapestPrice(int n, vector<vector<int>>& flights, int start, int end, int maxTime) {
    // Define a helper function to perform DFS
    function<int(int, int, int)> dfs = [&](int city, int time, int cost) {
        // Base case: If we've reached the end city, return the current cost
        if (city == end) return cost;
        
        // Initialize minimum cost to infinity
        int minCost = INT_MAX;
        
        // Iterate over all flights from the current city
        for (auto& flight : flights) {
            if (flight[0] == city) {
                int newTime = time + flight[2];
                int newCost = cost + flight[1];
                
                // If the new time does not exceed maxTime, perform DFS from the next city
                if (newTime <= maxTime) {
                    minCost = min(minCost, dfs(flight[1], newTime, newCost));
                }
            }
        }
        
        return minCost;
    };
    
    // Call the DFS function from the start city
    int result = dfs(start, 0, 0);
    
    // If no valid path is found, return -1
    return result == INT_MAX ? -1 : result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ due to generating all permutations of flights, where $n$ is the number of flights. This is because in the worst case, we might have to explore all possible paths.
> - **Space Complexity:** $O(n)$ for the recursion stack in the worst case.
> - **Why these complexities occur:** The brute force approach is inherently inefficient because it explores all possible solutions without any optimization.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a priority queue to efficiently explore paths with the lowest cost and time.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the start city, a cost of 0, and a time of 0.
  2. Iterate until the queue is empty:
     - Dequeue the city with the lowest cost.
     - If the dequeued city is the end city, return its cost.
     - For each neighboring city that can be reached within `maxTime`, calculate the new cost and time, and enqueue it if it's not already in the queue or if the new cost is lower.
- Proof of optimality: This approach ensures that we always explore the path with the lowest cost first, thus finding the optimal solution efficiently.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

struct City {
    int id, cost, time;
    City(int id, int cost, int time) : id(id), cost(cost), time(time) {}
};

struct Compare {
    bool operator()(const City& a, const City& b) {
        return a.cost > b.cost;
    }
};

int findCheapestPrice(int n, vector<vector<int>>& flights, int start, int end, int maxTime) {
    unordered_map<int, vector<pair<int, int>>> graph;
    for (auto& flight : flights) {
        graph[flight[0]].emplace_back(flight[1], flight[2]);
    }
    
    priority_queue<City, vector<City>, Compare> pq;
    pq.emplace(start, 0, 0);
    unordered_map<int, int> minCost;
    
    while (!pq.empty()) {
        auto city = pq.top(); pq.pop();
        
        if (city.id == end) return city.cost;
        
        if (minCost.count(city.id) && minCost[city.id] <= city.cost) continue;
        minCost[city.id] = city.cost;
        
        for (auto& neighbor : graph[city.id]) {
            int newCost = city.cost + neighbor.second;
            int newTime = city.time + neighbor.second;
            
            if (newTime <= maxTime) {
                pq.emplace(neighbor.first, newCost, newTime);
            }
        }
    }
    
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(E \log V)$, where $E$ is the number of edges (flights) and $V$ is the number of vertices (cities), due to using a priority queue to efficiently select the next city to visit.
> - **Space Complexity:** $O(V + E)$ for storing the graph and the priority queue.
> - **Optimality proof:** This approach is optimal because it uses a priority queue to always explore the path with the lowest cost first, ensuring that the minimum cost path to the destination within the given time limit is found efficiently.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, graph traversal (specifically, a variant of Dijkstra's algorithm adapted for time and cost constraints).
- Problem-solving patterns identified: The importance of selecting the most promising path to explore next, based on a heuristic (in this case, the cost).
- Optimization techniques learned: Using data structures like priority queues to efficiently manage and select the next item to process based on a priority (cost).
- Similar problems to practice: Other graph traversal problems with constraints, such as finding the shortest path in a weighted graph or the minimum spanning tree.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the cost or time when exploring neighbors, or failing to handle cases where a city is visited multiple times with different costs.
- Edge cases to watch for: Ensuring that the start and end cities are valid, handling the case where there are no flights from the start city or to the end city, and checking for negative cost cycles (though not applicable in this specific problem due to its nature).
- Performance pitfalls: Using an inefficient data structure for the priority queue or not properly pruning the search space based on the time constraint.
- Testing considerations: Thoroughly testing with various inputs, including edge cases like an empty graph, a graph with a single node, or a graph where the start and end cities are the same.