## Find a Corresponding Node of a Binary Tree in a Clone of That Tree

**Problem Link:** https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description

**Problem Statement:**
- Given two binary trees `original` and `cloned`, and a reference to a node `target` in the `original` tree, return the corresponding node in the `cloned` tree.
- The input trees are not guaranteed to be balanced or complete.
- The target node is guaranteed to exist in the `original` tree.
- The `original` and `cloned` trees are identical in structure and values.

**Expected Output Format:**
- The function should return a pointer to the corresponding node in the `cloned` tree.

**Key Requirements and Edge Cases to Consider:**
- The input trees can be empty.
- The target node can be any node in the `original` tree, including the root.
- The function should handle edge cases where the `original` or `cloned` tree is empty.

**Example Test Cases with Explanations:**

*   Input: `original = [1,2,3,4,5,6,7]`, `cloned = [1,2,3,4,5,6,7]`, `target = 4`
    Output: Node with value `4` in the `cloned` tree
*   Input: `original = [1,2,3,4,5,6,7]`, `cloned = [1,2,3,4,5,6,7]`, `target = 7`
    Output: Node with value `7` in the `cloned` tree

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the `original` tree and find the target node.
- Once the target node is found, we can traverse the `cloned` tree and find the corresponding node with the same value.
- We can use a recursive or iterative approach to traverse the trees.

```cpp
// Brute Force Approach
TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
    if (original == nullptr || cloned == nullptr) return nullptr;
    
    if (original->val == target->val) {
        return cloned;
    }
    
    TreeNode* leftResult = getTargetCopy(original->left, cloned->left, target);
    if (leftResult != nullptr) return leftResult;
    
    TreeNode* rightResult = getTargetCopy(original->right, cloned->right, target);
    if (rightResult != nullptr) return rightResult;
    
    return nullptr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we are traversing the tree recursively.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The recursive approach causes the time complexity to be linear with respect to the number of nodes, and the space complexity is dependent on the height of the tree due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to traverse the `original` and `cloned` trees simultaneously, using the same recursive or iterative approach.
- By doing so, we can find the corresponding node in the `cloned` tree as soon as we find the target node in the `original` tree.
- This approach avoids the need to traverse the `cloned` tree separately and reduces the time complexity.

```cpp
// Optimal Approach
TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
    if (original == nullptr || cloned == nullptr) return nullptr;
    
    if (original == target) {
        return cloned;
    }
    
    TreeNode* leftResult = getTargetCopy(original->left, cloned->left, target);
    if (leftResult != nullptr) return leftResult;
    
    TreeNode* rightResult = getTargetCopy(original->right, cloned->right, target);
    if (rightResult != nullptr) return rightResult;
    
    return nullptr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we are traversing the tree recursively.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because we are traversing the tree only once and finding the corresponding node in the `cloned` tree as soon as we find the target node in the `original` tree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive tree traversal, simultaneous traversal of two trees.
- Problem-solving patterns identified: finding a node in a tree, traversing two trees simultaneously.
- Optimization techniques learned: reducing the number of tree traversals.
- Similar problems to practice: finding a node in a tree, traversing a tree recursively or iteratively.

**Mistakes to Avoid:**
- Common implementation errors: not checking for null pointers, not handling edge cases.
- Edge cases to watch for: empty trees, target node not found.
- Performance pitfalls: traversing the tree multiple times, not using simultaneous traversal.
- Testing considerations: testing with different tree structures, testing with different target nodes.