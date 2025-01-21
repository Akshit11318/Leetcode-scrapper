## Minimum Fuel Cost to Report to the Capital
**Problem Link:** https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description

**Problem Statement:**
- Input format: The problem takes in a tree represented as a list of edges `edges` where each edge is a list `[u, v]` and a list of `n` nodes. The goal is to find the minimum fuel cost to report to the capital.
- Expected output format: The function should return the minimum fuel cost.
- Key requirements and edge cases to consider: The tree is connected, and all nodes are reachable from the capital (node 0).
- Example test cases with explanations:
  - For `edges = [[0,1],[0,2],[0,3]]` and `seats = [5,1,1,1]`, the minimum fuel cost is 3 because we need to send 1 person from node 1, 1 person from node 2, and 1 person from node 3 to the capital.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves calculating the minimum fuel cost by simulating all possible ways to send people from each node to the capital.
- Step-by-step breakdown of the solution:
  1. Build an adjacency list representation of the tree.
  2. Perform a depth-first search (DFS) from each node to calculate the number of people that need to be sent to the capital.
  3. For each node, calculate the fuel cost by dividing the number of people by the number of seats available and rounding up to the nearest integer.
  4. Sum up the fuel costs from all nodes to get the total minimum fuel cost.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
#include <vector>
#include <cmath>
using namespace std;

int minimumFuelCost(vector<vector<int>>& edges, int seats) {
    int n = edges.size() + 1;
    vector<vector<int>> adj(n);
    for (auto& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }

    int totalFuelCost = 0;
    function<int(int, int)> dfs = [&](int node, int parent) {
        int people = 1;
        for (int child : adj[node]) {
            if (child != parent) {
                people += dfs(child, node);
            }
        }
        if (node != 0) {
            totalFuelCost += (people + seats - 1) / seats;
        }
        return people;
    };

    dfs(0, -1);
    return totalFuelCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we perform a DFS traversal of the tree.
> - **Space Complexity:** $O(n + m)$, because we store the adjacency list representation of the tree.
> - **Why these complexities occur:** The time complexity occurs because we visit each node and edge once during the DFS traversal, and the space complexity occurs because we store the adjacency list representation of the tree.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a DFS traversal to calculate the minimum fuel cost by summing up the fuel costs from each node to the capital.
- Detailed breakdown of the approach:
  1. Build an adjacency list representation of the tree.
  2. Perform a DFS traversal from each node to calculate the number of people that need to be sent to the capital.
  3. For each node, calculate the fuel cost by dividing the number of people by the number of seats available and rounding up to the nearest integer.
  4. Sum up the fuel costs from all nodes to get the total minimum fuel cost.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n + m)$ and a space complexity of $O(n + m)$, which is the best possible complexity for this problem.
- Why further optimization is impossible: Further optimization is impossible because we need to visit each node and edge at least once to calculate the minimum fuel cost.

```cpp
#include <vector>
#include <cmath>
using namespace std;

int minimumFuelCost(vector<vector<int>>& edges, int seats) {
    int n = edges.size() + 1;
    vector<vector<int>> adj(n);
    for (auto& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }

    int totalFuelCost = 0;
    function<int(int, int)> dfs = [&](int node, int parent) {
        int people = 1;
        for (int child : adj[node]) {
            if (child != parent) {
                people += dfs(child, node);
            }
        }
        if (node != 0) {
            totalFuelCost += (people + seats - 1) / seats;
        }
        return people;
    };

    dfs(0, -1);
    return totalFuelCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we perform a DFS traversal of the tree.
> - **Space Complexity:** $O(n + m)$, because we store the adjacency list representation of the tree.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n + m)$ and a space complexity of $O(n + m)$, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, adjacency list representation of a tree.
- Problem-solving patterns identified: Using DFS traversal to calculate the minimum fuel cost.
- Optimization techniques learned: Using a recursive DFS function to calculate the minimum fuel cost.
- Similar problems to practice: Problems involving tree traversals and graph algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case in the recursive DFS function.
- Edge cases to watch for: Handling the case where a node has no children.
- Performance pitfalls: Using a naive approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs and edge cases to ensure it works correctly.