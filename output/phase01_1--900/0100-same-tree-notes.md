## Same Tree
**Problem Link:** https://leetcode.com/problems/same-tree/description

**Problem Statement:**
- Input format and constraints: Given the roots of two binary trees `p` and `q`, determine if the two trees are the same.
- Expected output format: Return `true` if the trees are the same, and `false` otherwise.
- Key requirements and edge cases to consider: 
  - The definition of "same" implies that the trees must have the same structure and the same values in corresponding nodes.
  - Empty trees (null roots) are considered the same.
- Example test cases with explanations:
  - If `p` and `q` both have the same structure and node values, return `true`.
  - If `p` and `q` have different structures or node values, return `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if two binary trees are the same, we can compare each node's value and structure recursively.
- Step-by-step breakdown of the solution:
  1. Start with the root nodes of both trees. If both are `null`, the trees are the same.
  2. If one root is `null` and the other is not, the trees are not the same.
  3. Compare the values of the current nodes. If they are different, the trees are not the same.
  4. Recursively apply the comparison to the left and right subtrees of the current nodes.
- Why this approach comes to mind first: It's a straightforward, recursive approach that checks all nodes and their values, ensuring a comprehensive comparison.

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Base case: If both trees are empty, they are the same.
        if (p == nullptr && q == nullptr) return true;
        
        // If one tree is empty and the other is not, they are not the same.
        if (p == nullptr || q == nullptr) return false;
        
        // If the values of the current nodes are different, the trees are not the same.
        if (p->val != q->val) return false;
        
        // Recursively compare the left and right subtrees.
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of nodes in both trees, since we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the deeper tree, due to the recursive call stack. In the worst case (when the tree is skewed), $h = n$, and in the best case (when the tree is balanced), $h = \log(n)$.
> - **Why these complexities occur:** The time complexity is linear because we potentially visit every node in both trees. The space complexity depends on the maximum depth of the recursive calls, which corresponds to the height of the trees.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same recursive approach used in the brute force solution is already optimal because it only visits each node once and uses a minimal amount of extra space for the recursive call stack.
- Detailed breakdown of the approach: The solution remains the same as the brute force approach because it already achieves the optimal time complexity of $O(n)$ and optimal space complexity of $O(h)$.
- Proof of optimality: Any solution must at least visit each node once to compare the trees, so the time complexity cannot be better than $O(n)$. The space complexity is also optimal because we only use a recursive call stack that, in the worst case, is as deep as the height of the tree.

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Base case: If both trees are empty, they are the same.
        if (p == nullptr && q == nullptr) return true;
        
        // If one tree is empty and the other is not, they are not the same.
        if (p == nullptr || q == nullptr) return false;
        
        // If the values of the current nodes are different, the trees are not the same.
        if (p->val != q->val) return false;
        
        // Recursively compare the left and right subtrees.
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of nodes in both trees, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the deeper tree, due to the recursive call stack.
> - **Optimality proof:** The solution is optimal because it achieves the minimum possible time complexity by only visiting each node once and uses the minimum necessary space for the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, tree traversal.
- Problem-solving patterns identified: Checking for base cases, comparing structures recursively.
- Optimization techniques learned: Minimizing the number of node visits and using an efficient data structure (the recursive call stack).
- Similar problems to practice: Other tree comparison problems, such as checking if two trees are mirror images of each other.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for `null` nodes, incorrectly comparing node values.
- Edge cases to watch for: Empty trees, trees with different structures but the same values.
- Performance pitfalls: Using an inefficient traversal method or data structure.
- Testing considerations: Ensure to test with various tree structures, including empty trees, single-node trees, and trees with different values and structures.