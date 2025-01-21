## Count Unreachable Pairs of Nodes in an Undirected Graph

**Problem Link:** https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description

**Problem Statement:**
- Input: An integer `n` representing the number of nodes, and an array `edges` of pairs representing the edges in the graph.
- Output: The number of unreachable pairs of nodes.
- Key requirements: The graph is undirected, and the nodes are labeled from 1 to `n`.
- Edge cases: The graph may be disconnected, and there may be multiple edges between two nodes.

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over all pairs of nodes and check if there is a path between them using a depth-first search (DFS) or breadth-first search (BFS) algorithm.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
class Solution {
public:
    long long countUnreachablePairs(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n + 1);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        long long unreachable = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                if (!isConnected(graph, i, j)) {
                    unreachable++;
                }
            }
        }

        return unreachable;
    }

    bool isConnected(vector<vector<int>>& graph, int node1, int node2) {
        vector<bool> visited(graph.size(), false);
        visited[node1] = true;
        stack<int> st;
        st.push(node1);

        while (!st.empty()) {
            int node = st.top();
            st.pop();

            for (int neighbor : graph[node]) {
                if (neighbor == node2) {
                    return true;
                }
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    st.push(neighbor);
                }
            }
        }

        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of nodes. This is because we are iterating over all pairs of nodes and performing a DFS or BFS for each pair, which takes $O(n)$ time in the worst case.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we are storing the graph and the visited nodes in memory.
> - **Why these complexities occur:** The brute force approach has high time complexity because it involves iterating over all pairs of nodes and performing a search algorithm for each pair. The space complexity is relatively low because we are only storing the graph and the visited nodes.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a union-find data structure to keep track of the connected components in the graph.
- We can iterate over the edges and union the nodes in each edge, and then count the number of nodes in each connected component.
- Finally, we can calculate the number of unreachable pairs by iterating over all pairs of connected components and multiplying the sizes of the two components.

```cpp
class Solution {
public:
    long long countUnreachablePairs(int n, vector<vector<int>>& edges) {
        vector<int> parent(n + 1);
        vector<int> size(n + 1, 1);

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        for (auto& edge : edges) {
            unionNodes(parent, size, edge[0], edge[1]);
        }

        vector<long long> componentSizes;
        for (int i = 1; i <= n; i++) {
            if (parent[i] == i) {
                componentSizes.push_back(size[i]);
            }
        }

        long long unreachable = 0;
        for (int i = 0; i < componentSizes.size(); i++) {
            for (int j = i + 1; j < componentSizes.size(); j++) {
                unreachable += componentSizes[i] * componentSizes[j];
            }
        }

        return unreachable;
    }

    int findParent(vector<int>& parent, int node) {
        if (parent[node] != node) {
            parent[node] = findParent(parent, parent[node]);
        }
        return parent[node];
    }

    void unionNodes(vector<int>& parent, vector<int>& size, int node1, int node2) {
        int parent1 = findParent(parent, node1);
        int parent2 = findParent(parent, node2);

        if (parent1 != parent2) {
            parent[parent2] = parent1;
            size[parent1] += size[parent2];
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \alpha(n))$, where $n$ is the number of nodes and $m$ is the number of edges. The $\alpha(n)$ term represents the inverse Ackermann function, which grows very slowly.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we are storing the parent and size arrays.
> - **Optimality proof:** The optimal approach has a much lower time complexity than the brute force approach because it uses a union-find data structure to keep track of the connected components in the graph. This allows us to avoid iterating over all pairs of nodes and performing a search algorithm for each pair.

### Final Notes

**Learning Points:**
- The problem requires the use of a union-find data structure to keep track of the connected components in the graph.
- The optimal approach has a much lower time complexity than the brute force approach because it avoids iterating over all pairs of nodes and performing a search algorithm for each pair.
- The problem requires careful consideration of the edge cases, such as the graph being disconnected or having multiple edges between two nodes.

**Mistakes to Avoid:**
- Failing to consider the edge cases, such as the graph being disconnected or having multiple edges between two nodes.
- Using a brute force approach that has a high time complexity.
- Failing to use a union-find data structure to keep track of the connected components in the graph.
- Failing to calculate the number of unreachable pairs correctly by iterating over all pairs of connected components and multiplying the sizes of the two components.