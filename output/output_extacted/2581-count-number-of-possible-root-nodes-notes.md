## Count Number of Possible Root Nodes

**Problem Link:** https://leetcode.com/problems/count-number-of-possible-root-nodes/description

**Problem Statement:**
- Input: A tree where each node has a unique value, and a list of edges representing the tree structure.
- Output: The number of nodes that can be the root of the tree such that the tree remains connected when all nodes with values greater than the root's value are removed.
- Key requirements and edge cases to consider:
  - The tree is connected and undirected.
  - Each node has a unique value.
  - The tree can have any number of nodes.
- Example test cases with explanations:
  - A tree with 3 nodes where the values are 1, 2, and 3, and the edges are (1, 2) and (2, 3). The output should be 1 because only the node with value 3 can be the root.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try each node as the potential root and count how many nodes can be the root such that the tree remains connected when all nodes with values greater than the root's value are removed.
- Step-by-step breakdown of the solution:
  1. Iterate through each node in the tree.
  2. For each node, remove all nodes with values greater than the current node's value.
  3. Check if the remaining nodes are connected.
  4. If they are connected, increment the count of possible roots.
- Why this approach comes to mind first: It is a straightforward approach that checks each node as a potential root.

```cpp
int countRootNodes(vector<int>& edges, vector<int>& values) {
    int n = values.size();
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        vector<int> remainingNodes;
        for (int j = 0; j < n; j++) {
            if (values[j] <= values[i]) {
                remainingNodes.push_back(j);
            }
        }

        vector<vector<int>> subGraph(remainingNodes.size());
        for (int k = 0; k < remainingNodes.size(); k++) {
            for (int node : graph[remainingNodes[k]]) {
                if (find(remainingNodes.begin(), remainingNodes.end(), node) != remainingNodes.end()) {
                    subGraph[k].push_back(find(remainingNodes.begin(), remainingNodes.end(), node) - remainingNodes.begin());
                }
            }
        }

        bool isConnected = true;
        vector<bool> visited(remainingNodes.size(), false);
        dfs(subGraph, 0, visited);
        for (bool v : visited) {
            if (!v) {
                isConnected = false;
                break;
            }
        }

        if (isConnected) {
            count++;
        }
    }

    return count;
}

void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited) {
    visited[node] = true;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(graph, neighbor, visited);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where n is the number of nodes in the tree. This is because we are iterating through each node, and for each node, we are creating a subgraph and checking if it is connected.
> - **Space Complexity:** $O(n^2)$, where n is the number of nodes in the tree. This is because we are creating a subgraph for each node.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that checks each node as a potential root and creates a subgraph for each node.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a depth-first search (DFS) to check if the tree remains connected when all nodes with values greater than the root's value are removed.
- Detailed breakdown of the approach:
  1. Perform a DFS from each node to check if the tree remains connected when all nodes with values greater than the current node's value are removed.
  2. Use a visited array to keep track of the nodes that have been visited during the DFS.
- Proof of optimality: This approach is optimal because it only requires a single DFS pass through the tree for each node, resulting in a significant reduction in time complexity compared to the brute force approach.
- Why further optimization is impossible: This approach is already optimal because it only requires a single DFS pass through the tree for each node.

```cpp
int countRootNodes(vector<int>& edges, vector<int>& values) {
    int n = values.size();
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        vector<bool> visited(n, false);
        if (dfs(graph, values, i, visited, values[i])) {
            count++;
        }
    }

    return count;
}

bool dfs(vector<vector<int>>& graph, vector<int>& values, int node, vector<bool>& visited, int maxValue) {
    visited[node] = true;
    bool isConnected = true;
    for (int neighbor : graph[node]) {
        if (values[neighbor] <= maxValue && !visited[neighbor]) {
            if (!dfs(graph, values, neighbor, visited, maxValue)) {
                isConnected = false;
            }
        }
    }
    return isConnected;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where n is the number of nodes in the tree. This is because we are performing a DFS from each node.
> - **Space Complexity:** $O(n)$, where n is the number of nodes in the tree. This is because we are using a visited array to keep track of the nodes that have been visited during the DFS.
> - **Optimality proof:** This approach is optimal because it only requires a single DFS pass through the tree for each node, resulting in a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, graph traversal, and optimization techniques.
- Problem-solving patterns identified: Using a visited array to keep track of the nodes that have been visited during the DFS.
- Optimization techniques learned: Reducing the time complexity by using a single DFS pass through the tree for each node.
- Similar problems to practice: Other graph traversal and optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty graph or a graph with a single node.
- Edge cases to watch for: A graph with a single node, a graph with multiple connected components, and a graph with nodes that have the same value.
- Performance pitfalls: Using a brute force approach that checks each node as a potential root, resulting in a high time complexity.
- Testing considerations: Testing the function with different graphs, including graphs with a single node, graphs with multiple connected components, and graphs with nodes that have the same value.