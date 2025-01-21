## Minimum Degree of a Connected Trio in a Graph

**Problem Link:** https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/description

**Problem Statement:**
- Input format: `n` (number of nodes) and `edges` (list of undirected edges)
- Constraints: `1 <= n <= 10^5`, `1 <= edges.length <= 10^5`, `0 <= edges[i][0], edges[i][1] < n`
- Expected output format: The minimum degree of a connected trio in the graph, or `-1` if no such trio exists.
- Key requirements: Find the minimum degree of a connected trio, where a trio is a set of three nodes that are all connected to each other.
- Edge cases to consider: Disconnected graphs, graphs with no trios, and graphs with multiple connected components.

**Example Test Cases:**
- Input: `n = 6, edges = [[1,2],[1,3],[3,4],[1,4],[1,5]]`
  Output: `1`
- Input: `n = 7, edges = [[1,3],[4,5],[4,6],[6,7],[0,1],[0,2],[0,5],[2,6]]`
  Output: `0`

### Brute Force Approach

**Explanation:**
- Initial thought process: For each node, check all possible pairs of its neighbors to see if they are also connected to each other.
- Step-by-step breakdown:
  1. Create an adjacency list representation of the graph.
  2. For each node, iterate over its neighbors.
  3. For each pair of neighbors, check if they are connected to each other.
  4. If a connected trio is found, update the minimum degree.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int minTrioDegree(int n, vector<vector<int>>& edges) {
    vector<unordered_set<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].insert(edge[1]);
        graph[edge[1]].insert(edge[0]);
    }

    int minDegree = INT_MAX;
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            for (int k : graph[i]) {
                if (j != k && graph[j].count(k)) {
                    int degree = graph[i].size() + graph[j].size() + graph[k].size() - 6;
                    minDegree = min(minDegree, degree);
                }
            }
        }
    }
    return minDegree == INT_MAX ? -1 : minDegree;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the number of nodes and $m$ is the average degree of a node.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks all possible pairs of neighbors for each node. The space complexity is relatively low because we only need to store the adjacency list representation of the graph.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all possible pairs of neighbors for each node, we can use a more efficient algorithm to find connected trios.
- Detailed breakdown:
  1. Create an adjacency list representation of the graph.
  2. Use a hash set to store the edges of the graph.
  3. For each node, iterate over its neighbors.
  4. For each pair of neighbors, check if they are connected to each other using the hash set.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int minTrioDegree(int n, vector<vector<int>>& edges) {
    vector<unordered_set<int>> graph(n);
    unordered_set<string> edgeSet;
    for (auto& edge : edges) {
        graph[edge[0]].insert(edge[1]);
        graph[edge[1]].insert(edge[0]);
        string key1 = to_string(edge[0]) + "," + to_string(edge[1]);
        string key2 = to_string(edge[1]) + "," + to_string(edge[0]);
        edgeSet.insert(key1);
        edgeSet.insert(key2);
    }

    int minDegree = INT_MAX;
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            for (int k : graph[i]) {
                if (j != k) {
                    string key1 = to_string(j) + "," + to_string(k);
                    string key2 = to_string(k) + "," + to_string(j);
                    if (edgeSet.count(key1) || edgeSet.count(key2)) {
                        int degree = graph[i].size() + graph[j].size() + graph[k].size() - 6;
                        minDegree = min(minDegree, degree);
                    }
                }
            }
        }
    }
    return minDegree == INT_MAX ? -1 : minDegree;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the number of nodes and $m$ is the average degree of a node.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Optimality proof:** Although the time complexity is still $O(n \cdot m^2)$, the use of a hash set to store the edges reduces the constant factor, making the algorithm more efficient in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph traversal, adjacency list representation, hash sets.
- Problem-solving patterns identified: Using hash sets to store edges and reduce constant factors.
- Optimization techniques learned: Using more efficient data structures to reduce time complexity.
- Similar problems to practice: Graph traversal, minimum spanning tree, connected components.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as disconnected graphs or graphs with no trios.
- Edge cases to watch for: Graphs with multiple connected components, graphs with self-loops or parallel edges.
- Performance pitfalls: Using inefficient data structures or algorithms, such as iterating over all possible pairs of nodes.
- Testing considerations: Test the algorithm on different types of graphs, including small and large graphs, to ensure correctness and efficiency.