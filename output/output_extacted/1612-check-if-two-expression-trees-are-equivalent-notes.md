## Check If Two Expression Trees Are Equivalent

**Problem Link:** https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/description

**Problem Statement:**
- Input format: Two `TreeNode` objects representing the roots of two expression trees.
- Constraints: Each `TreeNode` has a `val` attribute representing the value of the node, and `left` and `right` attributes representing the left and right child nodes, respectively.
- Expected output format: A boolean indicating whether the two expression trees are equivalent.
- Key requirements and edge cases to consider:
  - The trees are considered equivalent if they have the same structure and the same values at corresponding nodes.
  - The trees can contain null nodes, which should be handled accordingly.
- Example test cases with explanations:
  - Example 1: Two trees with the same structure and values should return `true`.
  - Example 2: Two trees with different structures or values should return `false`.
  - Example 3: Two trees with null nodes should be handled correctly.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To compare two expression trees, we can recursively compare the values and structures of the trees.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes two `TreeNode` objects as input.
  2. If both trees are null, return `true` since they are equivalent.
  3. If one tree is null and the other is not, return `false` since they are not equivalent.
  4. If the values at the current nodes are different, return `false` since the trees are not equivalent.
  5. Recursively compare the left and right subtrees.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to compare the trees recursively.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Base case: If both trees are null, they are equivalent
        if (p == nullptr && q == nullptr) {
            return true;
        }
        // If one tree is null and the other is not, they are not equivalent
        if (p == nullptr || q == nullptr) {
            return false;
        }
        // If the values at the current nodes are different, the trees are not equivalent
        if (p->val != q->val) {
            return false;
        }
        // Recursively compare the left and right subtrees
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of nodes in the trees, since we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the trees, since we need to store the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is dependent on the height of the trees because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal, as we need to visit each node at least once to compare the trees.
- Detailed breakdown of the approach: The approach remains the same as the brute force approach.
- Proof of optimality: Since we need to visit each node at least once, the time complexity of $O(n)$ is optimal.
- Why further optimization is impossible: We cannot avoid visiting each node, so further optimization is not possible.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Base case: If both trees are null, they are equivalent
        if (p == nullptr && q == nullptr) {
            return true;
        }
        // If one tree is null and the other is not, they are not equivalent
        if (p == nullptr || q == nullptr) {
            return false;
        }
        // If the values at the current nodes are different, the trees are not equivalent
        if (p->val != q->val) {
            return false;
        }
        // Recursively compare the left and right subtrees
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of nodes in the trees, since we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the trees, since we need to store the recursive call stack.
> - **Optimality proof:** The time complexity is optimal because we need to visit each node at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, comparison of tree structures.
- Problem-solving patterns identified: Divide-and-conquer approach, recursive function calls.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other tree-related problems, such as tree traversal, tree construction, and tree manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Not handling null nodes correctly, not comparing values at corresponding nodes.
- Edge cases to watch for: Null nodes, trees with different structures or values.
- Performance pitfalls: Not optimizing the recursive function calls, not using a divide-and-conquer approach.
- Testing considerations: Test cases with null nodes, trees with different structures or values, large trees to test performance.