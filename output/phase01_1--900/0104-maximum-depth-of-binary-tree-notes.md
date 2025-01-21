## Maximum Depth of Binary Tree

**Problem Link:** https://leetcode.com/problems/maximum-depth-of-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [0, 10^4].
- Expected output: The maximum depth of the binary tree.
- Key requirements and edge cases to consider: 
    - Handling an empty tree (i.e., the root is null).
    - Single-node trees.
    - Balanced and unbalanced trees.
- Example test cases with explanations:
    - Example 1: Input: root = [3,9,20,null,null,15,7], Output: 3
    - Example 2: Input: root = [1,null,2], Output: 2

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might start by thinking of traversing the tree and calculating the depth of each node from the root.
- Step-by-step breakdown of the solution: 
    1. Traverse the tree using any traversal method (e.g., DFS or BFS).
    2. For each node, keep track of its depth from the root.
    3. Update the maximum depth whenever a deeper node is encountered.
- Why this approach comes to mind first: It's straightforward and doesn't require much insight into the problem's structure, making it a natural first attempt.

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0; // Base case: empty tree
        return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack. In the worst case (an unbalanced tree), $h = n$.
> - **Why these complexities occur:** The time complexity is linear because we visit each node exactly once. The space complexity is dependent on the height of the tree due to the recursive nature of the solution.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem doesn't require visiting nodes in any particular order (like in-order, pre-order, or post-order), so we can simply use a depth-first search (DFS) approach to calculate the maximum depth.
- Detailed breakdown of the approach: 
    1. If the tree is empty (root is null), return 0 as there are no nodes.
    2. Otherwise, recursively calculate the maximum depth of the left and right subtrees.
    3. Return 1 (for the current node) plus the maximum of the depths of the left and right subtrees.
- Proof of optimality: This solution is optimal because it visits each node exactly once and uses a minimal amount of extra space (for the recursive call stack), achieving a time complexity of $O(n)$ and a space complexity of $O(h)$.

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0; // Base case: empty tree
        return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** This solution is optimal because it visits each node once and uses minimal extra space, resulting in the best possible time and space complexities for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive DFS, handling base cases (like an empty tree), and calculating maximum depth in a tree structure.
- Problem-solving patterns identified: Breaking down a problem into smaller sub-problems (e.g., calculating the depth of left and right subtrees).
- Optimization techniques learned: Minimizing the number of node visits and using recursive calls efficiently to reduce space complexity.
- Similar problems to practice: Minimum Depth of Binary Tree, Diameter of Binary Tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case (empty tree), incorrectly calculating the maximum depth.
- Edge cases to watch for: Empty trees, single-node trees, and trees with a large difference in the number of nodes between the left and right subtrees.
- Performance pitfalls: Using an inefficient traversal method or not optimizing the recursive calls, leading to higher time or space complexities.
- Testing considerations: Ensure to test with various tree structures, including balanced and unbalanced trees, and edge cases like empty or single-node trees.