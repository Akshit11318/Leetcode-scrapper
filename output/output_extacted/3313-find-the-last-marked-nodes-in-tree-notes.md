## Find the Last Marked Nodes in Tree
**Problem Link:** https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/description

**Problem Statement:**
- Input format and constraints: Given a tree with `n` nodes, where each node is initially unmarked, and an array `edges` representing the edges of the tree, and an array `marked` representing the nodes to be marked.
- Expected output format: Return an array containing the last marked node in each subtree.
- Key requirements and edge cases to consider: The tree is not necessarily a binary tree, and a node can have any number of children.
- Example test cases with explanations:
  - Example 1:
    - Input: `n = 5`, `edges = [[0, 1], [0, 2], [1, 3], [1, 4]]`, `marked = [1, 1, 0, 0, 0]`
    - Output: `[1, 1, 0, 0, 0]`
  - Example 2:
    - Input: `n = 3`, `edges = [[0, 1], [0, 2]]`, `marked = [1, 0, 1]`
    - Output: `[1, 0, 1]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can perform a depth-first search (DFS) traversal of the tree and mark each node as we visit it. We can keep track of the last marked node in each subtree by using a recursive approach.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the tree.
  2. Perform a DFS traversal of the tree, starting from each node.
  3. As we visit each node, mark it and update the last marked node in the subtree.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
#include <vector>
using namespace std;

vector<int> lastMarkedNodes(int n, vector<vector<int>>& edges, vector<int>& marked) {
    // Create adjacency list representation of the tree
    vector<vector<int>> tree(n);
    for (auto& edge : edges) {
        tree[edge[0]].push_back(edge[1]);
        tree[edge[1]].push_back(edge[0]);
    }

    // Perform DFS traversal and mark each node
    vector<int> lastMarked(n, -1);
    for (int i = 0; i < n; i++) {
        if (marked[i]) {
            lastMarked[i] = i;
            dfs(tree, i, marked, lastMarked);
        }
    }

    return lastMarked;
}

void dfs(vector<vector<int>>& tree, int node, vector<int>& marked, vector<int>& lastMarked) {
    // Mark each node as we visit it
    marked[node] = 1;
    lastMarked[node] = node;

    // Recursively visit each child node
    for (int child : tree[node]) {
        if (!marked[child]) {
            dfs(tree, child, marked, lastMarked);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because we perform a DFS traversal of the tree for each node.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the adjacency list representation of the tree and the last marked node in each subtree.
> - **Why these complexities occur:** The time complexity is high because we perform a DFS traversal of the tree for each node, and the space complexity is moderate because we need to store the adjacency list representation of the tree and the last marked node in each subtree.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can perform a single DFS traversal of the tree and mark each node as we visit it. We can keep track of the last marked node in each subtree by using a recursive approach with a return value.
- Detailed breakdown of the approach:
  1. Create an adjacency list representation of the tree.
  2. Perform a DFS traversal of the tree, starting from the root node.
  3. As we visit each node, mark it and update the last marked node in the subtree.
  4. Return the last marked node in the subtree.
- Proof of optimality: This approach is optimal because we only need to perform a single DFS traversal of the tree, and we can keep track of the last marked node in each subtree using a recursive approach.

```cpp
#include <vector>
using namespace std;

vector<int> lastMarkedNodes(int n, vector<vector<int>>& edges, vector<int>& marked) {
    // Create adjacency list representation of the tree
    vector<vector<int>> tree(n);
    for (auto& edge : edges) {
        tree[edge[0]].push_back(edge[1]);
        tree[edge[1]].push_back(edge[0]);
    }

    // Perform DFS traversal and mark each node
    vector<int> lastMarked(n, -1);
    dfs(tree, 0, marked, lastMarked);
    return lastMarked;
}

int dfs(vector<vector<int>>& tree, int node, vector<int>& marked, vector<int>& lastMarked) {
    // Mark each node as we visit it
    marked[node] = 1;

    // Initialize last marked node in subtree
    int lastNode = -1;

    // Recursively visit each child node
    for (int child : tree[node]) {
        if (!marked[child]) {
            int childLastNode = dfs(tree, child, marked, lastMarked);
            if (childLastNode != -1) {
                lastNode = childLastNode;
            }
        }
    }

    // Update last marked node in subtree
    if (lastNode == -1) {
        lastNode = node;
    }
    lastMarked[node] = lastNode;
    return lastNode;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we only need to perform a single DFS traversal of the tree.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the adjacency list representation of the tree and the last marked node in each subtree.
> - **Optimality proof:** This approach is optimal because we only need to perform a single DFS traversal of the tree, and we can keep track of the last marked node in each subtree using a recursive approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, recursive approach with return value.
- Problem-solving patterns identified: Using a recursive approach to keep track of the last marked node in each subtree.
- Optimization techniques learned: Reducing the number of DFS traversals from $n$ to $1$.

**Mistakes to Avoid:**
- Common implementation errors: Not marking each node as we visit it, not updating the last marked node in each subtree correctly.
- Edge cases to watch for: Handling the case where a node has no children, handling the case where a node is already marked.
- Performance pitfalls: Performing multiple DFS traversals of the tree, not using a recursive approach to keep track of the last marked node in each subtree.
- Testing considerations: Testing the solution with different input cases, including cases where a node has no children, cases where a node is already marked, and cases where the tree is empty.