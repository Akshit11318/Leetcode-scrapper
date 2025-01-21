## Largest Color Value in a Directed Graph

**Problem Link:** [https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description)

**Problem Statement:**
- Given a directed graph with `n` nodes, where each node has a color and a list of neighboring nodes.
- The goal is to find the largest possible color value for each node such that:
  - For each node, its color value is at least as large as its neighboring nodes.
  - The color values are integers between 1 and `n`.
- The input format consists of an adjacency list representation of the graph, where each node is associated with a list of its neighboring nodes.
- The expected output is a list of integers representing the largest possible color values for each node.
- Key requirements include ensuring that the color values are valid integers and handling potential cycles in the graph.
- Edge cases to consider include graphs with no nodes, graphs with a single node, and graphs with multiple connected components.

**Example Test Cases:**
- For a graph with nodes [1, 2, 3] and edges [(1, 2), (2, 3)], the largest color values would be [3, 2, 1].
- For a graph with nodes [1, 2, 3] and edges [(1, 2), (1, 3)], the largest color values would be [3, 1, 1].

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over all possible color assignments for each node and checking if the assignment satisfies the condition that each node's color value is at least as large as its neighboring nodes.
- The step-by-step breakdown involves generating all permutations of color values, checking each permutation against the graph's constraints, and keeping track of the largest valid color values.
- This approach comes to mind first because it is a straightforward enumeration of possibilities.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void dfs(int node, vector<int>& colors, vector<vector<int>>& graph) {
    for (int neighbor : graph[node]) {
        if (colors[neighbor] >= colors[node]) {
            colors[neighbor]++;
            dfs(neighbor, colors, graph);
        }
    }
}

vector<int> largestColorValues(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
    }
    
    vector<int> colors(n, 1);
    for (int i = 0; i < n; i++) {
        dfs(i, colors, graph);
    }
    
    return colors;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot n!)$, where $n$ is the number of nodes and $m$ is the number of edges. The $n!$ factor comes from generating all permutations of color values.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Why these complexities occur:** The brute force approach involves generating all possible permutations of color values, which leads to the $n!$ factor in the time complexity. The space complexity comes from storing the graph and the color values.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a topological sorting approach to assign color values to nodes in a way that satisfies the condition.
- The detailed breakdown involves performing a depth-first search (DFS) on the graph to detect cycles and assign color values based on the DFS traversal order.
- This approach is optimal because it avoids the need to generate all permutations of color values and instead uses the graph structure to guide the assignment of color values.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> largestColorValues(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
    }
    
    vector<int> in_degree(n, 0);
    for (const auto& neighbors : graph) {
        for (int neighbor : neighbors) {
            in_degree[neighbor]++;
        }
    }
    
    vector<int> colors(n, 1);
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (in_degree[i] == 0) {
            q.push(i);
        }
    }
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        
        for (int neighbor : graph[node]) {
            colors[neighbor] = max(colors[neighbor], colors[node] + 1);
            in_degree[neighbor]--;
            if (in_degree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    return colors;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Optimality proof:** This approach is optimal because it uses a topological sorting to assign color values in a way that satisfies the condition, avoiding the need to generate all permutations of color values.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the importance of using graph algorithms to solve problems involving graph structures.
- The optimal approach shows how to use a topological sorting to assign color values in a way that satisfies the condition.
- The problem highlights the importance of considering the graph structure when solving problems involving graph traversal.

**Mistakes to Avoid:**
- Failing to consider the graph structure and instead using a brute force approach.
- Not using a topological sorting to assign color values.
- Not handling cycles in the graph correctly.
- Not considering the time and space complexity of the solution.