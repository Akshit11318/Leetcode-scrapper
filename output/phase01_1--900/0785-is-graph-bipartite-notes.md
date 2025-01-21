## Is Graph Bipartite
**Problem Link:** https://leetcode.com/problems/is-graph-bipartite/description

**Problem Statement:**
- Input format and constraints: The problem takes as input a graph represented as an adjacency list `graph`, where `graph[i]` is a list of indices `j` such that there is an edge between `i` and `j`. The graph has `n` nodes.
- Expected output format: The function should return `true` if the graph is bipartite and `false` otherwise.
- Key requirements and edge cases to consider: A graph is bipartite if it can be colored using two colors such that no two adjacent nodes have the same color. The graph can have multiple connected components.
- Example test cases with explanations: 
    - Example 1: 
        - Input: `graph = [[1,3],[0,2],[1,3],[0,2]]`
        - Output: `true`
        - Explanation: The graph is bipartite because we can color the nodes with two colors such that no two adjacent nodes have the same color.
    - Example 2: 
        - Input: `graph = [[1,2,3],[0,2],[0,1,3],[0,2]]`
        - Output: `false`
        - Explanation: The graph is not bipartite because we cannot color the nodes with two colors such that no two adjacent nodes have the same color.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible colorings of the graph and check if any of them satisfy the condition of being bipartite.
- Step-by-step breakdown of the solution: 
    1. Generate all possible colorings of the graph using two colors.
    2. For each coloring, check if any two adjacent nodes have the same color.
    3. If we find a coloring where no two adjacent nodes have the same color, return `true`.
    4. If we try all colorings and none of them satisfy the condition, return `false`.
- Why this approach comes to mind first: This approach is straightforward and involves checking all possible colorings of the graph.

```cpp
#include <vector>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1);
    
    // Function to check if a coloring is valid
    bool isValid(int node, int c) {
        if (color[node] != -1) {
            return color[node] == c;
        }
        color[node] = c;
        for (int neighbor : graph[node]) {
            if (!isValid(neighbor, 1 - c)) {
                return false;
            }
        }
        return true;
    }
    
    // Try all possible colorings
    for (int i = 0; i < n; i++) {
        if (color[i] == -1) {
            if (!isValid(i, 0)) {
                return false;
            }
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of nodes in the graph. This is because we try all possible colorings of the graph, and for each coloring, we check if it is valid.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the graph. This is because we need to store the color of each node.
> - **Why these complexities occur:** The time complexity occurs because we try all possible colorings of the graph, and the space complexity occurs because we need to store the color of each node.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible colorings of the graph, we can use a depth-first search (DFS) to assign colors to the nodes.
- Detailed breakdown of the approach: 
    1. Initialize an array `color` to store the color of each node.
    2. Iterate over all nodes in the graph. If a node has not been assigned a color, perform a DFS from that node.
    3. During the DFS, assign a color to the current node and recursively assign colors to its neighbors.
    4. If we encounter a node that has already been assigned a color and the color is different from the expected color, return `false`.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges in the graph. This is because we visit each node and edge once during the DFS.

```cpp
#include <vector>
using namespace std;

bool isBipartite(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1);
    
    // Function to perform DFS
    bool dfs(int node, int c) {
        if (color[node] != -1) {
            return color[node] == c;
        }
        color[node] = c;
        for (int neighbor : graph[node]) {
            if (!dfs(neighbor, 1 - c)) {
                return false;
            }
        }
        return true;
    }
    
    // Perform DFS from each uncolored node
    for (int i = 0; i < n; i++) {
        if (color[i] == -1) {
            if (!dfs(i, 0)) {
                return false;
            }
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges in the graph. This is because we visit each node and edge once during the DFS.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the graph. This is because we need to store the color of each node.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n + m)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, graph coloring.
- Problem-solving patterns identified: Using DFS to solve graph problems.
- Optimization techniques learned: Avoiding unnecessary work by using DFS instead of trying all possible colorings.
- Similar problems to practice: Other graph problems, such as finding connected components or testing whether a graph is connected.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a node has already been assigned a color before assigning a new color.
- Edge cases to watch for: Graphs with multiple connected components.
- Performance pitfalls: Trying all possible colorings of the graph instead of using DFS.
- Testing considerations: Testing the function with graphs of different sizes and structures.