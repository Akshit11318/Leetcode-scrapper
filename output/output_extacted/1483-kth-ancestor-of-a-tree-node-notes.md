## Kth Ancestor of a Tree Node
**Problem Link:** https://leetcode.com/problems/kth-ancestor-of-a-tree-node/description

**Problem Statement:**
- Given a tree where each node has a unique integer `node_id` and a `parent_id` (the parent node's id), find the kth ancestor of a given node.
- The tree is represented as a list of nodes where each node is an array `[node_id, parent_id]`.
- The `node_id` is unique for each node and ranges from 0 to n-1 (where n is the number of nodes).
- The `parent_id` is the id of the parent node, or -1 if the node is the root.
- The function `getKthAncestor` takes three parameters: `tree`, `node`, and `k`, and returns the id of the kth ancestor of the given node, or -1 if the kth ancestor does not exist.
- The function should handle edge cases such as when the node does not exist, or when k is greater than the number of ancestors.

**Example Test Cases:**
- `tree = [[0, -1], [0, -1], [1, 0]]`, `node = 1`, `k = 1`: Returns -1 because node 1 does not have a parent.
- `tree = [[0, -1], [0, -1], [1, 0]]`, `node = 0`, `k = 2`: Returns -1 because node 0 does not have a grandparent.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to recursively traverse the tree to find the kth ancestor of a given node.
- We start at the given node and move up the tree by following the parent pointers until we find the kth ancestor or reach the root.
- If we reach the root before finding the kth ancestor, we return -1.

```cpp
class TreeAncestor {
public:
    vector<vector<int>> tree;
    TreeAncestor(vector<vector<int>>& tree) : tree(tree) {}

    int getKthAncestor(int node, int k) {
        // Base case: if k is 0, return the node itself
        if (k == 0) return node;
        
        // Find the parent of the node
        int parent = -1;
        for (auto& n : tree) {
            if (n[0] == node) {
                parent = n[1];
                break;
            }
        }
        
        // If the node does not have a parent, return -1
        if (parent == -1) return -1;
        
        // Recursively find the kth ancestor of the parent
        return getKthAncestor(parent, k - 1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of nodes and $k$ is the number of ancestors to traverse. This is because in the worst case, we need to traverse the entire tree to find the kth ancestor.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes. This is because we need to store the tree in memory.
> - **Why these complexities occur:** The brute force approach has high time complexity because it uses recursive function calls to traverse the tree, which can lead to a lot of repeated work. The space complexity is high because we need to store the entire tree in memory.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a binary lifting approach to find the kth ancestor of a given node.
- We precompute the ancestors of each node up to a certain depth (e.g., $\log n$) and store them in a table.
- When we need to find the kth ancestor of a node, we use the precomputed table to quickly find the answer.

```cpp
class TreeAncestor {
public:
    vector<vector<int>> tree;
    vector<vector<int>> ancestors;
    TreeAncestor(vector<vector<int>>& tree) : tree(tree) {
        int n = tree.size();
        ancestors.resize(n, vector<int>(20, -1));
        
        // Precompute the ancestors of each node
        for (int i = 0; i < n; i++) {
            for (auto& node : tree) {
                if (node[0] == i) {
                    ancestors[i][0] = node[1];
                    break;
                }
            }
        }
        
        // Compute the ancestors up to depth 20
        for (int j = 1; j < 20; j++) {
            for (int i = 0; i < n; i++) {
                if (ancestors[i][j - 1] != -1) {
                    ancestors[i][j] = ancestors[ancestors[i][j - 1]][j - 1];
                }
            }
        }
    }

    int getKthAncestor(int node, int k) {
        // Use the precomputed table to find the kth ancestor
        for (int i = 19; i >= 0; i--) {
            if ((k >> i) & 1) {
                if (ancestors[node][i] == -1) return -1;
                node = ancestors[node][i];
            }
        }
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of nodes. This is because we use a binary lifting approach to find the kth ancestor.
> - **Space Complexity:** $O(n \log n)$, where $n$ is the number of nodes. This is because we need to store the precomputed table of ancestors.
> - **Optimality proof:** The optimal approach has a time complexity of $O(\log n)$ because we use a binary lifting approach to find the kth ancestor. This is the best possible time complexity because we need to traverse at least $\log n$ levels of the tree to find the kth ancestor.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is binary lifting, which is a technique for finding the kth ancestor of a node in a tree.
- The problem-solving pattern identified is to use precomputation to speed up the query time.
- The optimization technique learned is to use a binary lifting approach to reduce the time complexity.

**Mistakes to Avoid:**
- A common implementation error is to use a recursive approach without memoization, which can lead to a high time complexity.
- An edge case to watch for is when the node does not exist in the tree, or when k is greater than the number of ancestors.
- A performance pitfall is to use a brute force approach without considering the time complexity, which can lead to slow performance for large inputs.