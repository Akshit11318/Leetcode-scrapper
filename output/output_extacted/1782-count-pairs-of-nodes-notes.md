## Count Pairs of Nodes
**Problem Link:** https://leetcode.com/problems/count-pairs-of-nodes/description

**Problem Statement:**
- Input format: A directed graph represented as an adjacency list `edges` and a list of nodes `n`.
- Constraints: `1 <= n <= 10^5`, `0 <= edges.length <= 5 * 10^5`.
- Expected output format: The number of pairs of nodes that are not reachable from each other.
- Key requirements and edge cases to consider: 
    - A node is reachable from itself.
    - The graph is directed.
- Example test cases with explanations:
    - For `n = 3` and `edges = [[0, 1], [1, 2], [2, 0]]`, the output should be `0` because every node is reachable from every other node.
    - For `n = 4` and `edges = [[0, 1], [1, 2], [2, 0], [3, 3]]`, the output should be `2` because the only pairs of nodes that are not reachable from each other are `(0, 3)` and `(3, 0)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each pair of nodes, perform a depth-first search (DFS) to check if one node is reachable from the other.
- Step-by-step breakdown of the solution:
    1. Create an adjacency list representation of the graph.
    2. For each pair of nodes `(i, j)`, perform a DFS from node `i` to check if node `j` is reachable.
    3. If node `j` is not reachable from node `i`, perform a DFS from node `j` to check if node `i` is reachable from node `j`.
    4. If neither node is reachable from the other, increment the count of pairs.
- Why this approach comes to mind first: This approach is straightforward and checks all possible pairs of nodes for reachability.

```cpp
class Solution {
public:
    int countPairs(int n, vector<vector<int>>& edges) {
        // Create an adjacency list representation of the graph
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
        }

        int count = 0;
        // For each pair of nodes, check if one node is reachable from the other
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                bool reachableItoJ = dfs(graph, i, j);
                bool reachableJtoI = dfs(graph, j, i);
                if (!reachableItoJ && !reachableJtoI) {
                    count++;
                }
            }
        }

        return count;
    }

    bool dfs(vector<vector<int>>& graph, int start, int target) {
        vector<bool> visited(graph.size(), false);
        return dfsHelper(graph, start, target, visited);
    }

    bool dfsHelper(vector<vector<int>>& graph, int current, int target, vector<bool>& visited) {
        if (current == target) return true;
        visited[current] = true;
        for (int neighbor : graph[current]) {
            if (!visited[neighbor] && dfsHelper(graph, neighbor, target, visited)) {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \times (n + m))$, where $n$ is the number of nodes and $m$ is the number of edges. This is because for each pair of nodes, we perform a DFS that takes $O(n + m)$ time in the worst case.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we need to store the adjacency list representation of the graph.
> - **Why these complexities occur:** The time complexity occurs because we are checking all possible pairs of nodes for reachability, and for each pair, we are performing a DFS that takes $O(n + m)$ time. The space complexity occurs because we need to store the adjacency list representation of the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible pairs of nodes for reachability, we can use a `tarjan` algorithm to find strongly connected components (SCCs) in the graph. Two nodes are reachable from each other if and only if they are in the same SCC.
- Detailed breakdown of the approach:
    1. Implement the `tarjan` algorithm to find SCCs in the graph.
    2. For each SCC, calculate the number of pairs of nodes that are not reachable from each other.
    3. Sum up the counts from all SCCs to get the total count.
- Proof of optimality: This approach is optimal because it only needs to traverse the graph once to find all SCCs, and then it can calculate the count of pairs in $O(n)$ time.

```cpp
class Solution {
public:
    int countPairs(int n, vector<vector<int>>& edges) {
        // Create an adjacency list representation of the graph
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
        }

        int count = 0;
        // Use tarjan algorithm to find strongly connected components
        vector<vector<int>> sccs = tarjan(graph);
        // For each SCC, calculate the number of pairs of nodes that are not reachable from each other
        for (auto& scc : sccs) {
            for (int node : scc) {
                for (int otherNode = 0; otherNode < n; otherNode++) {
                    if (find(scc.begin(), scc.end(), otherNode) == scc.end()) {
                        count++;
                    }
                }
            }
        }

        return count / 2;
    }

    vector<vector<int>> tarjan(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> index(n, -1);
        vector<int> low(n);
        vector<int> stack;
        vector<vector<int>> sccs;
        int idx = 0;

        for (int i = 0; i < n; i++) {
            if (index[i] == -1) {
                strongConnect(graph, i, index, low, stack, sccs, idx);
            }
        }

        return sccs;
    }

    void strongConnect(vector<vector<int>>& graph, int node, vector<int>& index, vector<int>& low, vector<int>& stack, vector<vector<int>>& sccs, int& idx) {
        index[node] = idx;
        low[node] = idx;
        idx++;
        stack.push_back(node);

        for (int neighbor : graph[node]) {
            if (index[neighbor] == -1) {
                strongConnect(graph, neighbor, index, low, stack, sccs, idx);
                low[node] = min(low[node], low[neighbor]);
            } else if (find(stack.begin(), stack.end(), neighbor) != stack.end()) {
                low[node] = min(low[node], index[neighbor]);
            }
        }

        if (low[node] == index[node]) {
            vector<int> scc;
            while (true) {
                int w = stack.back();
                stack.pop_back();
                scc.push_back(w);
                if (w == node) break;
            }
            sccs.push_back(scc);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we only need to traverse the graph once to find all SCCs.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we need to store the adjacency list representation of the graph.
> - **Optimality proof:** This approach is optimal because it only needs to traverse the graph once to find all SCCs, and then it can calculate the count of pairs in $O(n)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tarjan's algorithm for finding strongly connected components, DFS for checking reachability.
- Problem-solving patterns identified: Using a `tarjan` algorithm to find SCCs in a graph to solve reachability problems.
- Optimization techniques learned: Reducing the time complexity from $O(n^2 \times (n + m))$ to $O(n + m)$ by using a `tarjan` algorithm.
- Similar problems to practice: Finding the number of connected components in a graph, checking if a graph is strongly connected.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where a node is not reachable from any other node.
- Edge cases to watch for: Graphs with self-loops, graphs with multiple edges between the same pair of nodes.
- Performance pitfalls: Using a brute force approach that checks all possible pairs of nodes for reachability.
- Testing considerations: Testing the solution with graphs of different sizes and structures to ensure correctness and performance.