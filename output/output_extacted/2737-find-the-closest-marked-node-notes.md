## Find the Closest Marked Node
**Problem Link:** https://leetcode.com/problems/find-the-closest-marked-node/description

**Problem Statement:**
- Input: An array `n` representing the number of nodes in the graph, and an array `edges` representing the edges in the graph, and an array `marked` representing the marked nodes.
- Output: An array where the value at each index `i` is the closest marked node to node `i`.
- Key requirements and edge cases to consider:
  - The graph is undirected and connected.
  - There are no self-loops or parallel edges.
  - The marked array contains at least one marked node.
- Example test cases with explanations:
  - For example, if the input is `n = 6`, `edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]`, and `marked = [1]`, then the output should be `[1,1,1,1,1,1]`, because node `1` is the closest marked node to all other nodes.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can use a **Breadth-First Search (BFS)** algorithm to find the shortest distance from each node to the closest marked node.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the graph.
  2. Perform BFS from each node to find the shortest distance to the closest marked node.
  3. Store the result in an array.
- Why this approach comes to mind first: It is a straightforward solution that uses a well-known algorithm (BFS) to solve the problem.

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> closestMarkedNodes(int n, vector<vector<int>>& edges, vector<int>& marked) {
    // Create adjacency list
    vector<vector<int>> adj(n + 1);
    for (auto& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }

    // Perform BFS from each node
    vector<int> result(n);
    for (int i = 1; i <= n; i++) {
        queue<pair<int, int>> q; // node, distance
        vector<bool> visited(n + 1, false);
        q.push({i, 0});
        visited[i] = true;
        int closest = -1;
        while (!q.empty()) {
            int node = q.front().first;
            int dist = q.front().second;
            q.pop();
            if (find(marked.begin(), marked.end(), node) != marked.end()) {
                closest = node;
                break;
            }
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    q.push({neighbor, dist + 1});
                    visited[neighbor] = true;
                }
            }
        }
        result[i - 1] = closest;
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we perform BFS from each node.
> - **Space Complexity:** $O(n + m)$, because we store the adjacency list and the result array.
> - **Why these complexities occur:** The time complexity is high because we perform BFS from each node, and the space complexity is moderate because we store the adjacency list and the result array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a single BFS traversal to find the closest marked node to all other nodes.
- Detailed breakdown of the approach:
  1. Perform BFS from all marked nodes simultaneously.
  2. Store the result in an array.
- Proof of optimality: This solution has a lower time complexity than the brute force approach because we only perform a single BFS traversal.
- Why further optimization is impossible: This solution has the lowest possible time complexity because we must visit all nodes at least once to find the closest marked node.

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> closestMarkedNodes(int n, vector<vector<int>>& edges, vector<int>& marked) {
    // Create adjacency list
    vector<vector<int>> adj(n + 1);
    for (auto& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }

    // Perform BFS from all marked nodes
    vector<int> result(n, -1);
    queue<pair<int, int>> q; // node, distance
    vector<bool> visited(n + 1, false);
    for (int node : marked) {
        q.push({node, 0});
        visited[node] = true;
    }
    while (!q.empty()) {
        int node = q.front().first;
        int dist = q.front().second;
        q.pop();
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                q.push({neighbor, dist + 1});
                visited[neighbor] = true;
                result[neighbor - 1] = node;
            }
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we perform a single BFS traversal.
> - **Space Complexity:** $O(n + m)$, because we store the adjacency list and the result array.
> - **Optimality proof:** This solution has the lowest possible time complexity because we must visit all nodes at least once to find the closest marked node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, adjacency list representation, and simultaneous BFS traversal.
- Problem-solving patterns identified: Using a single BFS traversal to find the closest marked node to all other nodes.
- Optimization techniques learned: Reducing the number of BFS traversals to improve time complexity.
- Similar problems to practice: Finding the shortest path between two nodes in a graph, finding the closest unmarked node to all marked nodes.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty graph or no marked nodes.
- Edge cases to watch for: Handling nodes with no marked neighbors, handling nodes with multiple marked neighbors.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Testing the solution with different graph sizes, edge densities, and marked node configurations.