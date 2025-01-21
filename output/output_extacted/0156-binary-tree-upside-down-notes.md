## Binary Tree Upside Down
**Problem Link:** https://leetcode.com/problems/binary-tree-upside-down/description

**Problem Statement:**
- Input format and constraints: The input is the root of a binary tree, and the task is to return the root of the upside-down binary tree.
- Expected output format: The output should be the root of the transformed binary tree.
- Key requirements and edge cases to consider: The tree can be empty (i.e., the input root can be `NULL`), and the tree nodes have a `val`, `left`, and `right` child.
- Example test cases with explanations:
  - Test case 1: An empty tree (`NULL`) should return `NULL`.
  - Test case 2: A tree with a single node should return the same tree.
  - Test case 3: A tree with multiple nodes should be transformed correctly.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial approach is to traverse the tree and create a new tree with the left and right children swapped for each node.
- Step-by-step breakdown of the solution:
  1. Create a new node for each node in the original tree.
  2. Traverse the original tree and create the new tree by swapping the left and right children of each node.
  3. Update the root of the new tree to be the leftmost node in the original tree.
- Why this approach comes to mind first: This approach is straightforward and involves a simple traversal of the tree.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        if (!root || !root->left) {
            return root;
        }
        
        TreeNode* newRoot = upsideDownBinaryTree(root->left);
        root->left->left = root;
        root->left->right = root->right;
        root->left = NULL;
        root->right = NULL;
        
        return newRoot;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is linear due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a recursive approach to transform the tree in-place.
- Detailed breakdown of the approach:
  1. If the tree is empty or only has one node, return the root as it is.
  2. Recursively call the function on the left subtree.
  3. Update the left and right children of the current node to be the right child of the current node and the left child of the current node, respectively.
  4. Set the left and right children of the current node to `NULL`.
- Proof of optimality: This approach is optimal because it only visits each node once and performs a constant amount of work for each node.
- Why further optimization is impossible: This approach is already optimal because it has a linear time complexity and only uses a constant amount of extra space.

```cpp
class Solution {
public:
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        if (!root || !root->left) {
            return root;
        }
        
        TreeNode* newRoot = upsideDownBinaryTree(root->left);
        root->left->left = root;
        root->left->right = root->right;
        root->left = NULL;
        root->right = NULL;
        
        return newRoot;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Optimality proof:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is linear due to the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, in-place tree transformation.
- Problem-solving patterns identified: Divide-and-conquer approach, recursive function calls.
- Optimization techniques learned: Using recursive functions to simplify the solution.
- Similar problems to practice: Tree traversal, tree transformation, recursive functions.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly, not updating the left and right children correctly.
- Edge cases to watch for: Empty tree, tree with one node, tree with multiple nodes.
- Performance pitfalls: Using excessive extra space, not optimizing the recursive function calls.
- Testing considerations: Test the function with different types of input, including empty tree, tree with one node, and tree with multiple nodes.