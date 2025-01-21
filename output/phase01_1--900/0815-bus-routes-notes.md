## Bus Routes
**Problem Link:** https://leetcode.com/problems/bus-routes/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `routes` where each `routes[i]` is a list of distinct integers representing bus stop IDs where a bus travels, and two integers `source` and `target` representing the starting and ending bus stop IDs. The task is to find the least number of buses you must take to travel from `source` to `target`, and return it. If it is not possible to reach the target from the source, return -1.
- Expected output format: The minimum number of buses required to reach the target from the source.
- Key requirements and edge cases to consider: 
  - The input will contain at least 1 and at most 500 buses.
  - Each bus route will contain at least 1 and at most 10^5 bus stops.
  - The total number of bus stops will not exceed 10^5.
  - The `source` and `target` bus stop IDs will be between 1 and 10^6 (inclusive).
- Example test cases with explanations: 
  - Input: `routes = [[1, 2, 7], [3, 6, 7]], source = 1, target = 6`
    Output: `2`
    Explanation: The best strategy is to take the first bus to bus stop 7, then take the second bus to bus stop 6.
  - Input: `routes = [[2], [3], [1]], source = 3, target = 1`
    Output: `-1`
    Explanation: There is no way to reach bus stop 1 from bus stop 3.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves checking every possible combination of bus routes to find the minimum number of buses required to reach the target from the source.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of bus routes.
  2. For each combination, check if the source bus stop is in the first route and the target bus stop is in the last route.
  3. If a valid combination is found, update the minimum number of buses required.
- Why this approach comes to mind first: This approach is straightforward and ensures that all possible combinations are considered.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        int minBuses = INT_MAX;
        for (int i = 0; i < routes.size(); i++) {
            for (int j = i; j < routes.size(); j++) {
                if (find(routes[i].begin(), routes[i].end(), source) != routes[i].end() &&
                    find(routes[j].begin(), routes[j].end(), target) != routes[j].end()) {
                    minBuses = min(minBuses, (int)routes.size() - i + j);
                }
            }
        }
        return minBuses == INT_MAX ? -1 : minBuses;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of bus routes and $m$ is the maximum number of bus stops in a route. This is because we are generating all possible combinations of bus routes and checking each combination.
> - **Space Complexity:** $O(1)$, as we are not using any additional data structures that scale with the input size.
> - **Why these complexities occur:** The time complexity is high because we are checking every possible combination of bus routes, and the space complexity is low because we are only using a constant amount of space to store the minimum number of buses required.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a breadth-first search (BFS) algorithm to find the minimum number of buses required to reach the target from the source.
- Detailed breakdown of the approach:
  1. Create a graph where each bus stop is a node, and two nodes are connected if they are on the same bus route.
  2. Perform a BFS traversal from the source node to find the shortest path to the target node.
- Proof of optimality: The BFS algorithm ensures that we find the shortest path to the target node, which corresponds to the minimum number of buses required.

```cpp
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) return 0;
        
        unordered_map<int, vector<int>> stopToBus;
        for (int i = 0; i < routes.size(); i++) {
            for (int stop : routes[i]) {
                stopToBus[stop].push_back(i);
            }
        }
        
        queue<pair<int, int>> q;
        q.push({source, 0});
        unordered_set<int> visited;
        visited.insert(source);
        
        while (!q.empty()) {
            int stop = q.front().first;
            int bus = q.front().second;
            q.pop();
            
            for (int nextBus : stopToBus[stop]) {
                for (int nextStop : routes[nextBus]) {
                    if (nextStop == target) return bus + 1;
                    if (visited.find(nextStop) == visited.end()) {
                        q.push({nextStop, bus + 1});
                        visited.insert(nextStop);
                    }
                }
            }
        }
        
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of bus routes and $m$ is the maximum number of bus stops in a route. This is because we are performing a BFS traversal over the graph.
> - **Space Complexity:** $O(n \cdot m)$, as we are storing the graph and the visited nodes.
> - **Optimality proof:** The BFS algorithm ensures that we find the shortest path to the target node, which corresponds to the minimum number of buses required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, graph traversal.
- Problem-solving patterns identified: Using a graph to represent the problem, performing a BFS traversal to find the shortest path.
- Optimization techniques learned: Using a BFS algorithm to reduce the time complexity.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path in a weighted graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where the source and target nodes are the same, not handling the case where there is no path from the source to the target.
- Edge cases to watch for: The input may contain duplicate bus stops, the source and target nodes may not be in the graph.
- Performance pitfalls: Using a brute force approach, not optimizing the graph traversal algorithm.
- Testing considerations: Test the algorithm with different input sizes, test the edge cases and performance pitfalls.