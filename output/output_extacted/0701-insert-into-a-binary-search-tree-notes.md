## Insert into a Binary Search Tree

**Problem Link:** https://leetcode.com/problems/insert-into-a-binary-search-tree/description

**Problem Statement:**
- Input format and constraints: The input is a binary search tree (`root`) and a value (`val`) to be inserted into the tree. The tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`.
- Expected output format: The function should return the root of the modified binary search tree after inserting the given value.
- Key requirements and edge cases to consider: The function must maintain the properties of a binary search tree, i.e., for every node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node. The function should also handle the case where the input tree is empty (i.e., `root` is `NULL`).
- Example test cases with explanations:
  - Example 1:
    - Input: `root = [4,2,7,1,3]`, `val = 5`
    - Output: `[4,2,7,1,3,5]`
    - Explanation: The value `5` is inserted into the tree, and the resulting tree maintains the binary search tree properties.
  - Example 2:
    - Input: `root = [40,20,60,10,30,50,70]`, `val = 25`
    - Output: `[40,20,60,10,30,50,70,null,null,25]`
    - Explanation: The value `25` is inserted into the tree, and the resulting tree maintains the binary search tree properties.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to traverse the tree, find the correct location for the new value, and then insert it. This can be done using a recursive or iterative approach.
- Step-by-step breakdown of the solution:
  1. Start at the root of the tree.
  2. Compare the value to be inserted with the current node's value.
  3. If the value is less than the current node's value, move to the left subtree.
  4. If the value is greater than the current node's value, move to the right subtree.
  5. Repeat steps 2-4 until an empty spot is found (i.e., a leaf node is reached).
  6. Insert the new value at the empty spot.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves a simple traversal of the tree and comparison of values.

```cpp
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        // Base case: if the tree is empty, create a new node
        if (root == NULL) {
            return new TreeNode(val);
        }

        // Recursive case: traverse the tree to find the correct location
        if (val < root->val) {
            root->left = insertIntoBST(root->left, val);
        } else if (val > root->val) {
            root->right = insertIntoBST(root->right, val);
        }

        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the tree. In the worst case, the tree is skewed, and $h = n$, where $n$ is the number of nodes in the tree. Therefore, the time complexity is $O(n)$.
> - **Space Complexity:** $O(h)$, as the recursive call stack can go up to the height of the tree. In the worst case, the space complexity is $O(n)$.
> - **Why these complexities occur:** The time and space complexities occur because of the recursive traversal of the tree. The height of the tree determines the maximum number of recursive calls, and therefore, the time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is similar to the brute force approach, as it also involves a recursive or iterative traversal of the tree. However, the optimal solution can be implemented more efficiently using an iterative approach.
- Detailed breakdown of the approach:
  1. Start at the root of the tree.
  2. Compare the value to be inserted with the current node's value.
  3. If the value is less than the current node's value, move to the left subtree.
  4. If the value is greater than the current node's value, move to the right subtree.
  5. Repeat steps 2-4 until an empty spot is found (i.e., a leaf node is reached).
  6. Insert the new value at the empty spot.
- Proof of optimality: The optimal solution has a time complexity of $O(h)$, where $h$ is the height of the tree. This is because the solution involves a single traversal of the tree, and the height of the tree determines the maximum number of nodes that need to be visited. The space complexity is $O(1)$, as the solution only uses a constant amount of space to store the current node and the value to be inserted.

```cpp
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        // Base case: if the tree is empty, create a new node
        if (root == NULL) {
            return new TreeNode(val);
        }

        // Initialize a pointer to the current node
        TreeNode* curr = root;

        // Traverse the tree to find the correct location
        while (true) {
            if (val < curr->val) {
                // If the left child is empty, insert the new value
                if (curr->left == NULL) {
                    curr->left = new TreeNode(val);
                    break;
                }
                // Otherwise, move to the left subtree
                curr = curr->left;
            } else {
                // If the right child is empty, insert the new value
                if (curr->right == NULL) {
                    curr->right = new TreeNode(val);
                    break;
                }
                // Otherwise, move to the right subtree
                curr = curr->right;
            }
        }

        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the tree. In the worst case, the tree is skewed, and $h = n$, where $n$ is the number of nodes in the tree. Therefore, the time complexity is $O(n)$.
> - **Space Complexity:** $O(1)$, as the solution only uses a constant amount of space to store the current node and the value to be inserted.
> - **Optimality proof:** The solution is optimal because it involves a single traversal of the tree, and the height of the tree determines the maximum number of nodes that need to be visited. The space complexity is also optimal, as the solution only uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive and iterative tree traversal, comparison of values, and insertion of nodes.
- Problem-solving patterns identified: the problem can be solved using a recursive or iterative approach, and the optimal solution involves a single traversal of the tree.
- Optimization techniques learned: the optimal solution uses a constant amount of space, and the time complexity is determined by the height of the tree.
- Similar problems to practice: insertion into a binary search tree, deletion from a binary search tree, and searching in a binary search tree.

**Mistakes to Avoid:**
- Common implementation errors: incorrect handling of edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: the tree may be skewed, and the height of the tree may be equal to the number of nodes in the tree.
- Performance pitfalls: the solution may have a high time complexity if the tree is very large, and the space complexity may be high if the solution uses a recursive approach.
- Testing considerations: the solution should be tested with different types of input, including empty trees, trees with a single node, and large trees.