## Search in a Binary Search Tree
**Problem Link:** https://leetcode.com/problems/search-in-a-binary-search-tree/description

**Problem Statement:**
- Input: The root of a binary search tree and a `val` to be searched.
- Constraints: Each node has a unique value in the range `[1, 100]`, and the tree will not exceed `100` nodes.
- Expected Output: The node with `val` if found; otherwise, return `nullptr`.
- Key Requirements: The solution should utilize the properties of a binary search tree.
- Example Test Cases:
  - Example 1: Given the tree `[4,2,7,1,3]` and `val = 2`, return the node `[2,1,3]`.
  - Example 2: Given the tree `[4,2,7,1,3]` and `val = 5`, return `nullptr`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the entire tree and check each node's value.
- Step-by-step breakdown: Start at the root, visit each node, and compare its value with `val`.
- Why this approach comes to mind first: It's the most straightforward way to ensure every node is checked.

```cpp
// Brute Force Approach
TreeNode* searchBST(TreeNode* root, int val) {
    if (root == nullptr) return nullptr;
    if (root->val == val) return root;
    
    TreeNode* left = searchBST(root->left, val);
    if (left != nullptr) return left;
    
    return searchBST(root->right, val);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, because in the worst case, we might visit every node.
> - **Space Complexity:** $O(N)$ due to the recursion stack in the worst case (when the tree is skewed).
> - **Why these complexities occur:** The brute force approach checks every node without leveraging the properties of the binary search tree.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Binary search trees have the property that all elements to the left of a node are smaller, and all elements to the right are larger.
- Detailed breakdown: Start at the root. If the node's value is equal to `val`, return the node. If `val` is less than the node's value, search in the left subtree; otherwise, search in the right subtree.
- Proof of optimality: This approach minimizes the number of nodes to visit by always moving towards the subtree that could potentially contain `val`.

```cpp
// Optimal Approach
TreeNode* searchBST(TreeNode* root, int val) {
    while (root != nullptr && root->val != val) {
        if (val < root->val) {
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return root;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the tree. In the worst case (a skewed tree), this is $O(N)$, but for a balanced binary search tree, it's $O(\log N)$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the current node.
> - **Optimality proof:** This is optimal because we take advantage of the BST property to minimize the number of nodes we need to visit.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Utilizing the properties of data structures (in this case, binary search trees) to optimize solutions.
- Problem-solving pattern: Identifying the key characteristics of a problem that can lead to more efficient solutions.
- Optimization technique: Leveraging the structure of the input data to reduce the complexity of the algorithm.

**Mistakes to Avoid:**
- Not considering the properties of the data structure.
- Failing to analyze the worst-case and average-case scenarios for time and space complexity.
- Not optimizing the solution based on the characteristics of the input data.