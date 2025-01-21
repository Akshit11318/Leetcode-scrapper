## Range Sum of BST

**Problem Link:** https://leetcode.com/problems/range-sum-of-bst/description

**Problem Statement:**
- Input: The root of a `Binary Search Tree (BST)` and two integers `low` and `high`.
- Constraints: The number of nodes in the tree is in the range `[1, 2 * 10^4]`. 
- Expected output: The sum of the values of all nodes with a value in the range `[low, high]`.
- Key requirements and edge cases to consider: Handling nodes that are exactly on the boundaries of the range, and ensuring the solution works for both small and large input trees.

**Example Test Cases:**
- Example 1:
  - Input: `root = [10,5,15,3,7,null,18]`, `low = 7`, `high = 15`
  - Output: `32` (10 + 15 + 7 = 32)
- Example 2:
  - Input: `root = [10,5,15,3,7,13,18,1,null,6]`, `low = 6`, `high = 10`
  - Output: `23` (6 + 10 + 7 = 23)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the entire tree and check each node's value to see if it falls within the specified range.
- Step-by-step breakdown:
  1. Define a helper function to traverse the tree recursively.
  2. For each node, check if its value is within the range `[low, high]`.
  3. If it is, add the value to a running sum.
  4. Recursively call the helper function on the left and right child nodes.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement without requiring a deep understanding of the properties of a BST.

```cpp
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        int sum = 0;
        helper(root, low, high, sum);
        return sum;
    }
    
    void helper(TreeNode* node, int low, int high, int& sum) {
        if (node == nullptr) return;
        if (node->val >= low && node->val <= high) {
            sum += node->val;
        }
        helper(node->left, low, high, sum);
        helper(node->right, low, high, sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because in the worst case, we visit every node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursion stack. In the worst case (a skewed tree), this could be $O(n)$.
> - **Why these complexities occur:** The brute force approach requires checking every node, leading to linear time complexity. The space complexity is due to the recursive calls, which can go as deep as the height of the tree.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Utilize the properties of a Binary Search Tree, where all values to the left of a node are less than the node's value, and all values to the right are greater.
- Detailed breakdown:
  1. If the current node's value is less than `low`, there's no need to explore the left subtree since all values will be less than `low`.
  2. If the current node's value is greater than `high`, there's no need to explore the right subtree since all values will be greater than `high`.
  3. Recursively apply the above logic to the left and right subtrees, adjusting the bounds as necessary.
- Proof of optimality: This approach minimizes the number of nodes that need to be visited by pruning branches that are guaranteed to be outside the specified range, making it more efficient than the brute force approach.

```cpp
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (root == nullptr) return 0;
        if (root->val < low) {
            return rangeSumBST(root->right, low, high);
        }
        if (root->val > high) {
            return rangeSumBST(root->left, low, high);
        }
        return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ in the worst case (when all nodes fall within the range), but typically much less because we prune branches.
> - **Space Complexity:** $O(h)$ due to the recursion stack, with $h$ being the height of the tree after pruning.
> - **Optimality proof:** This approach is optimal because it minimizes the number of nodes visited by leveraging the BST property, reducing unnecessary traversals.

---

### Final Notes

**Learning Points:**
- Utilizing the properties of data structures (in this case, BST) can significantly optimize solutions.
- Pruning or reducing the search space can lead to more efficient algorithms.
- Recursive solutions can be elegant but require careful consideration of the base case and recursion depth.

**Mistakes to Avoid:**
- Not considering the properties of the data structure.
- Failing to prune the search space when possible.
- Not optimizing recursive calls to prevent stack overflow errors.