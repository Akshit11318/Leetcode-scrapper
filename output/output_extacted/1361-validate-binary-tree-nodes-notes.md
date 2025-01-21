## Validate Binary Tree Nodes
**Problem Link:** https://leetcode.com/problems/validate-binary-tree-nodes/description

**Problem Statement:**
- Input: `n` (number of nodes), `leftChild` (array of left child indices), `rightChild` (array of right child indices)
- Output: `true` if the binary tree is valid, `false` otherwise
- Key requirements: 
  - Each node must have at most two children (left and right).
  - There must be exactly one root node (node 0).
  - All nodes must be reachable from the root node.
- Example test cases:
  - `n = 4`, `leftChild = [1, -1, 3, -1]`, `rightChild = [2, -1, -1, -1]`. Expected output: `true`.
  - `n = 4`, `leftChild = [1, -1, 3, -1]`, `rightChild = [2, 3, -1, -1]`. Expected output: `false`.

---

### Brute Force Approach
**Explanation:**
- We start by identifying the root node and then perform a depth-first search (DFS) to traverse the tree.
- We keep track of visited nodes to ensure all nodes are reachable from the root.
- We also verify that each node has at most two children.

```cpp
#include <iostream>
#include <vector>

bool validateBinaryTreeNodes(int n, std::vector<int>& leftChild, std::vector<int>& rightChild) {
    std::vector<bool> visited(n, false);
    int root = 0; // Assuming node 0 is the root

    // Perform DFS from the root node
    if (!dfs(root, leftChild, rightChild, visited)) {
        return false;
    }

    // Check if all nodes are reachable from the root
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            return false;
        }
    }

    return true;
}

bool dfs(int node, std::vector<int>& leftChild, std::vector<int>& rightChild, std::vector<bool>& visited) {
    if (node == -1) { // Base case: null node
        return true;
    }

    if (visited[node]) { // Cycle detected
        return false;
    }

    visited[node] = true;

    // Recursively traverse left and right subtrees
    if (!dfs(leftChild[node], leftChild, rightChild, visited)) {
        return false;
    }

    if (!dfs(rightChild[node], leftChild, rightChild, visited)) {
        return false;
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes. Each node is visited once during the DFS traversal.
> - **Space Complexity:** $O(n)$, due to the recursive call stack and the `visited` array.
> - **Why these complexities occur:** The brute force approach involves a recursive DFS traversal, which has a linear time complexity. The space complexity is also linear due to the recursive call stack and the additional `visited` array.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using a `parent` array to keep track of the parent node for each node.
- We then perform a single pass through the `leftChild` and `rightChild` arrays to populate the `parent` array.
- We verify that each node has at most two children and that there is exactly one root node.

```cpp
#include <iostream>
#include <vector>

bool validateBinaryTreeNodes(int n, std::vector<int>& leftChild, std::vector<int>& rightChild) {
    std::vector<int> parent(n, -1); // Initialize parent array with -1

    // Populate parent array
    for (int i = 0; i < n; i++) {
        if (leftChild[i] != -1) {
            if (parent[leftChild[i]] != -1) { // Node already has a parent
                return false;
            }
            parent[leftChild[i]] = i;
        }

        if (rightChild[i] != -1) {
            if (parent[rightChild[i]] != -1) { // Node already has a parent
                return false;
            }
            parent[rightChild[i]] = i;
        }
    }

    int rootCount = 0;
    for (int i = 0; i < n; i++) {
        if (parent[i] == -1) { // Node is a root
            rootCount++;
        }
    }

    return rootCount == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes. We perform a single pass through the `leftChild` and `rightChild` arrays.
> - **Space Complexity:** $O(n)$, due to the `parent` array.
> - **Optimality proof:** This approach is optimal because we only need to perform a single pass through the input arrays to verify the binary tree structure. We avoid the overhead of recursive function calls and achieve a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: depth-first search (DFS), parent array, and tree traversal.
- Problem-solving patterns identified: using a `parent` array to keep track of node relationships and verifying tree structure constraints.
- Optimization techniques learned: avoiding recursive function calls and using a single pass through input arrays.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `parent` array correctly, not handling null nodes properly.
- Edge cases to watch for: nodes with multiple parents, nodes with no parents (multiple roots).
- Performance pitfalls: using recursive function calls instead of a single pass through input arrays.
- Testing considerations: test cases with different tree structures, including empty trees, single-node trees, and trees with multiple levels.