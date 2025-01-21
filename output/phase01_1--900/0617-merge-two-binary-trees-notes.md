## Merge Two Binary Trees

**Problem Link:** https://leetcode.com/problems/merge-two-binary-trees/description

**Problem Statement:**
- Input: Two binary trees `root1` and `root2`.
- Constraints: Each tree has at most `10^4` nodes, and each node has a unique value between `0` and `10^4`.
- Expected Output: The root of the merged binary tree.
- Key Requirements: If both trees have a node at the same position, then the values of the nodes are added together. Otherwise, the tree with a node at that position has its node copied to the merged tree.
- Example Test Cases:
  - Input: `root1 = [1,3,2,5]`, `root2 = [2,1,3,null,null,4,null,7]`
  - Output: `[3,4,5,5,4,null,7]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves recursively traversing both trees and merging them based on the presence of nodes at the same positions.
- This approach comes to mind first because it directly addresses the problem statement by comparing and merging nodes at corresponding positions in both trees.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        // Base case: If both trees are empty, return nullptr
        if (!root1 && !root2) return nullptr;
        
        // If one tree is empty, return the other tree
        if (!root1) return root2;
        if (!root2) return root1;
        
        // Merge the values of the current nodes
        TreeNode* merged = new TreeNode(root1->val + root2->val);
        
        // Recursively merge the left and right subtrees
        merged->left = mergeTrees(root1->left, root2->left);
        merged->right = mergeTrees(root1->right, root2->right);
        
        return merged;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the total number of nodes in both trees. This is because we visit each node once.
> - **Space Complexity:** $O(N)$, as in the worst case, we might need to store all nodes in the merged tree, and the recursion stack can grow up to the height of the tree, which is $N$ in the case of an unbalanced tree.
> - **Why these complexities occur:** The time complexity is linear because we process each node exactly once. The space complexity is also linear due to the potential need to store all nodes in the merged tree and the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach because the nature of the problem requires visiting each node in both trees to merge them correctly.
- The key insight is recognizing that the problem inherently requires a recursive or iterative traversal of both trees, and thus, the optimal solution is already presented in the brute force approach.

```cpp
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if (!root1) return root2;
        if (!root2) return root1;
        
        TreeNode* merged = new TreeNode(root1->val + root2->val);
        merged->left = mergeTrees(root1->left, root2->left);
        merged->right = mergeTrees(root1->right, root2->right);
        
        return merged;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the total number of nodes in both trees.
> - **Space Complexity:** $O(N)$, due to the storage of the merged tree and the recursion stack.
> - **Optimality proof:** This is optimal because we must at least visit each node once to merge the trees, and the approach does so with minimal overhead.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, merging of binary trees.
- Problem-solving patterns identified: Handling of edge cases (empty trees), recursive problem solving.
- Optimization techniques learned: Recognizing the inherent complexity of a problem and optimizing within those constraints.
- Similar problems to practice: Other tree traversal and merging problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, incorrect recursive calls.
- Edge cases to watch for: Empty trees, trees of different sizes.
- Performance pitfalls: Unnecessary node creations or traversals.
- Testing considerations: Thoroughly testing with various tree configurations and sizes.