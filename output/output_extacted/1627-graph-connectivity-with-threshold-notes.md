## Graph Connectivity With Threshold

**Problem Link:** [https://leetcode.com/problems/graph-connectivity-with-threshold/description](https://leetcode.com/problems/graph-connectivity-with-threshold/description)

**Problem Statement:**
- Input: An integer `n`, a list of `edges` where each edge is represented as an array of two integers, and an integer `threshold`.
- Constraints: $1 \leq n \leq 10^4$, $1 \leq edges.length \leq n(n-1)/2$, $1 \leq threshold \leq n$.
- Expected output: Return a list of all possible values of `label` that satisfy the condition: for every pair of nodes `(u, v)` with a label `label`, if there exists a path from `u` to `v` with all edges having a weight greater than or equal to `threshold`, then `u` and `v` have the same label.
- Key requirements and edge cases to consider: Handling disconnected graphs, ensuring all nodes are labeled, and optimizing the algorithm for large inputs.

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a brute force approach to generate all possible label assignments for the nodes and check each assignment against the given condition.
- Step-by-step breakdown of the solution:
  1. Generate all possible label assignments for the nodes.
  2. For each label assignment, iterate over all pairs of nodes and check if there exists a path with all edges having a weight greater than or equal to `threshold`.
  3. If a pair of nodes with different labels has a path satisfying the condition, discard the current label assignment.
- Why this approach comes to mind first: It is straightforward and guarantees finding all valid label assignments but is inefficient for large inputs.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> findValidLabels(int n, vector<vector<int>>& edges, int threshold) {
    // Generate all possible label assignments
    vector<int> labels(n);
    vector<int> validLabels;
    
    // Iterate over all possible label assignments
    for (int label = 1; label <= n; ++label) {
        bool isValid = true;
        
        // Check if the current label assignment satisfies the condition
        for (int u = 0; u < n; ++u) {
            for (int v = u + 1; v < n; ++v) {
                // Check if there exists a path from u to v with all edges having a weight greater than or equal to threshold
                if (hasPath(u, v, edges, threshold)) {
                    // If u and v have different labels, discard the current label assignment
                    if (labels[u] != labels[v]) {
                        isValid = false;
                        break;
                    }
                }
            }
            if (!isValid) break;
        }
        
        if (isValid) validLabels.push_back(label);
    }
    
    return validLabels;
}

// Helper function to check if there exists a path from u to v with all edges having a weight greater than or equal to threshold
bool hasPath(int u, int v, vector<vector<int>>& edges, int threshold) {
    // Implement a pathfinding algorithm (e.g., DFS or BFS) to check if there exists a path from u to v
    // For simplicity, this implementation is omitted
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot 2^n)$, where $n$ is the number of nodes. This is because we generate all possible label assignments and check each assignment against the condition.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we need to store the label assignments and the edges.
> - **Why these complexities occur:** The brute force approach has high time complexity due to generating all possible label assignments and checking each assignment against the condition. The space complexity is relatively low since we only need to store the label assignments and the edges.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a Union-Find algorithm to group nodes that are connected by edges with weights greater than or equal to `threshold`.
- Detailed breakdown of the approach:
  1. Initialize a Union-Find data structure with each node as its own group.
  2. Iterate over the edges and union the nodes that are connected by edges with weights greater than or equal to `threshold`.
  3. Assign a unique label to each group of nodes.
- Proof of optimality: This approach is optimal because it ensures that all nodes in the same group are connected by edges with weights greater than or equal to `threshold`, and it assigns a unique label to each group.

```cpp
#include <vector>

using namespace std;

vector<int> findValidLabels(int n, vector<vector<int>>& edges, int threshold) {
    // Initialize a Union-Find data structure
    vector<int> parent(n);
    vector<int> rank(n, 0);
    
    // Initialize each node as its own group
    for (int i = 0; i < n; ++i) {
        parent[i] = i;
    }
    
    // Iterate over the edges and union the nodes that are connected by edges with weights greater than or equal to threshold
    for (auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int weight = edge[2];
        
        if (weight >= threshold) {
            unionNodes(u, v, parent, rank);
        }
    }
    
    // Assign a unique label to each group of nodes
    vector<int> labels(n);
    int label = 1;
    
    for (int i = 0; i < n; ++i) {
        if (parent[i] == i) {
            labels[i] = label++;
        } else {
            labels[i] = labels[findParent(i, parent)];
        }
    }
    
    // Return the unique labels
    vector<int> uniqueLabels;
    for (int label : labels) {
        if (find(uniqueLabels.begin(), uniqueLabels.end(), label) == uniqueLabels.end()) {
            uniqueLabels.push_back(label);
        }
    }
    
    return uniqueLabels;
}

// Helper function to union two nodes
void unionNodes(int u, int v, vector<int>& parent, vector<int>& rank) {
    int rootU = findParent(u, parent);
    int rootV = findParent(v, parent);
    
    if (rootU != rootV) {
        if (rank[rootU] < rank[rootV]) {
            parent[rootU] = rootV;
        } else if (rank[rootU] > rank[rootV]) {
            parent[rootV] = rootU;
        } else {
            parent[rootV] = rootU;
            rank[rootU]++;
        }
    }
}

// Helper function to find the parent of a node
int findParent(int node, vector<int>& parent) {
    if (parent[node] != node) {
        parent[node] = findParent(parent[node], parent);
    }
    
    return parent[node];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \alpha(n))$, where $n$ is the number of nodes and $m$ is the number of edges. The $\alpha(n)$ term represents the inverse Ackermann function, which grows very slowly.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we need to store the Union-Find data structure and the labels.
> - **Optimality proof:** This approach is optimal because it ensures that all nodes in the same group are connected by edges with weights greater than or equal to `threshold`, and it assigns a unique label to each group. The time complexity is optimal because we only need to iterate over the edges and union the nodes that are connected by edges with weights greater than or equal to `threshold`. The space complexity is optimal because we only need to store the Union-Find data structure and the labels.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-Find algorithm, graph traversal.
- Problem-solving patterns identified: Using a Union-Find algorithm to group connected nodes, assigning unique labels to each group.
- Optimization techniques learned: Using a Union-Find algorithm to reduce the time complexity of the algorithm.
- Similar problems to practice: Graph connectivity problems, Union-Find algorithm problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the Union-Find algorithm, not handling edge cases correctly.
- Edge cases to watch for: Handling disconnected graphs, ensuring all nodes are labeled.
- Performance pitfalls: Using a brute force approach, not optimizing the algorithm for large inputs.
- Testing considerations: Testing the algorithm with different inputs, including edge cases and large inputs.