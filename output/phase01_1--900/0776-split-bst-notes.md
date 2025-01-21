## Split BST

**Problem Link:** https://leetcode.com/problems/split-bst/description

**Problem Statement:**
- Input format: The function takes in a binary tree `root` and an integer `target`.
- Constraints: The binary tree is a BST (Binary Search Tree).
- Expected output format: The function should return two BSTs, `root1` and `root2`, where `root1` contains all values less than or equal to `target`, and `root2` contains all values greater than `target`.
- Key requirements and edge cases to consider:
  - The input tree may be empty.
  - The target value may not exist in the tree.
  - The tree may contain duplicate values.
- Example test cases with explanations:
  - If the input tree is `[2,1,3]` and the target is `2`, the output should be `[2,1]` and `[3]`.
  - If the input tree is `[2,1,3]` and the target is `1`, the output should be `[1]` and `[2,null,3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree and store all values in a vector. Then, create two new BSTs by iterating over the vector and inserting values into the corresponding tree.
- Step-by-step breakdown of the solution:
  1. Traverse the input tree using inorder traversal and store all values in a vector.
  2. Create two new BSTs, `root1` and `root2`.
  3. Iterate over the vector and insert values into the corresponding tree based on the target value.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it involves simple tree traversal and insertion operations.

```cpp
TreeNode* insert(TreeNode* root, int val) {
    if (!root) return new TreeNode(val);
    if (val < root->val) root->left = insert(root->left, val);
    else root->right = insert(root->right, val);
    return root;
}

vector<int> inorder(TreeNode* root) {
    vector<int> res;
    if (root) {
        res = inorder(root->left);
        res.push_back(root->val);
        vector<int> tmp = inorder(root->right);
        res.insert(res.end(), tmp.begin(), tmp.end());
    }
    return res;
}

vector<TreeNode*> splitBST(TreeNode* root, int target) {
    vector<int> vals = inorder(root);
    TreeNode* root1 = nullptr;
    TreeNode* root2 = nullptr;
    for (int val : vals) {
        if (val <= target) root1 = insert(root1, val);
        else root2 = insert(root2, val);
    }
    return {root1, root2};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of nodes in the tree. This is because we perform inorder traversal, which takes $O(n)$ time, and then insert values into the new trees, which takes $O(\log n)$ time per insertion.
> - **Space Complexity:** $O(n)$, as we store all values in a vector and create two new trees.
> - **Why these complexities occur:** The time complexity is dominated by the insertion operations, which take $O(\log n)$ time per insertion. The space complexity is due to the storage of all values in a vector and the creation of two new trees.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can split the tree in-place by traversing the tree and updating the child pointers of the nodes.
- Detailed breakdown of the approach:
  1. Traverse the tree using a recursive function.
  2. If the current node's value is less than or equal to the target, recursively traverse the left subtree and update the right child pointer of the current node to the root of the right subtree.
  3. If the current node's value is greater than the target, recursively traverse the right subtree and update the left child pointer of the current node to the root of the left subtree.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we must visit each node at least once to split the tree.
- Why further optimization is impossible: We cannot avoid visiting each node, so the time complexity is bounded by the number of nodes in the tree.

```cpp
TreeNode* splitBST(TreeNode* root, int target) {
    if (!root) return {nullptr, nullptr};
    if (root->val <= target) {
        auto right_split = splitBST(root->right, target);
        root->right = right_split.first;
        return {root, right_split.second};
    } else {
        auto left_split = splitBST(root->left, target);
        root->left = left_split.second;
        return {left_split.first, root};
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node exactly once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because we use recursive function calls to traverse the tree.
> - **Optimality proof:** The time complexity is optimal because we must visit each node at least once to split the tree. The space complexity is optimal because we only use a constant amount of space per recursive function call.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, recursive function calls, and in-place modification of tree structures.
- Problem-solving patterns identified: Splitting a tree into two subtrees based on a target value.
- Optimization techniques learned: Avoiding unnecessary memory allocations and using recursive function calls to simplify the solution.
- Similar problems to practice: Splitting a linked list into two lists based on a target value.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update child pointers of nodes during tree traversal.
- Edge cases to watch for: Handling empty trees and trees with duplicate values.
- Performance pitfalls: Using inefficient data structures or algorithms that result in high time or space complexity.
- Testing considerations: Testing the solution with different input trees and target values to ensure correctness.