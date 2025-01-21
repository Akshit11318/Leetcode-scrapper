## Node with Highest Edge Score

**Problem Link:** https://leetcode.com/problems/node-with-highest-edge-score/description

**Problem Statement:**
- Given an integer `n` representing the number of nodes in a graph, and an integer array `edges` of length `n - 1` where `edges[i] = [a, b]` represents an edge between nodes `a` and `b`.
- The score of a node is defined as the sum of the absolute differences between the node and its neighbors.
- Return the node with the highest edge score.

**Key Requirements and Edge Cases:**
- The input graph is a tree.
- The nodes are labeled from 1 to `n`.
- The score of each node is calculated based on the absolute difference between the node and its neighbors.

**Example Test Cases:**
- Input: `n = 4`, `edges = [[1,2],[1,3],[1,4]]`
- Output: `1`
- Explanation: The scores are as follows:
  - Node 1: `|1-2| + |1-3| + |1-4| = 1 + 2 + 3 = 6`
  - Node 2: `|2-1| = 1`
  - Node 3: `|3-1| = 2`
  - Node 4: `|4-1| = 3`
  - Node 1 has the highest score.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the score for each node by iterating over all edges and summing the absolute differences between the node and its neighbors.
- We create an adjacency list representation of the graph to efficiently access the neighbors of each node.
- For each node, we calculate its score by summing the absolute differences between the node and its neighbors.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

int edgeScore(vector<vector<int>>& edges, int n) {
    unordered_map<int, vector<int>> graph;
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    int maxScore = 0, maxNode = 0;
    for (int i = 1; i <= n; i++) {
        int score = 0;
        for (int neighbor : graph[i]) {
            score += abs(i - neighbor);
        }
        if (score > maxScore) {
            maxScore = score;
            maxNode = i;
        }
    }
    return maxNode;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because in the worst case, we iterate over all nodes and their neighbors.
> - **Space Complexity:** $O(n)$ for storing the adjacency list representation of the graph.
> - **Why these complexities occur:** The brute force approach involves iterating over all edges and nodes, resulting in a quadratic time complexity. The space complexity is linear due to the storage of the adjacency list.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves using a similar approach to the brute force, but with a more efficient data structure and algorithm.
- We create an adjacency list representation of the graph using a vector of vectors.
- For each node, we calculate its score by summing the absolute differences between the node and its neighbors.
- We keep track of the node with the maximum score.

```cpp
#include <vector>
using namespace std;

int edgeScore(vector<vector<int>>& edges, int n) {
    vector<vector<int>> graph(n + 1);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    int maxScore = 0, maxNode = 0;
    for (int i = 1; i <= n; i++) {
        int score = 0;
        for (int neighbor : graph[i]) {
            score += abs(i - neighbor);
        }
        if (score > maxScore) {
            maxScore = score;
            maxNode = i;
        }
    }
    return maxNode;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because in the worst case, we iterate over all nodes and their neighbors.
> - **Space Complexity:** $O(n)$ for storing the adjacency list representation of the graph.
> - **Optimality proof:** The optimal solution has the same time and space complexity as the brute force approach because the problem requires calculating the score for each node by summing the absolute differences between the node and its neighbors.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: graph traversal, adjacency list representation.
- Problem-solving patterns identified: calculating scores for each node based on its neighbors.
- Optimization techniques learned: using a more efficient data structure (vector of vectors) instead of an unordered map.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases (e.g., empty graph), incorrect calculation of scores.
- Edge cases to watch for: graph with a single node, graph with no edges.
- Performance pitfalls: using an inefficient data structure (e.g., adjacency matrix) for large graphs.