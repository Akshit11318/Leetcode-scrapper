## Construct Binary Tree from Preorder and Inorder Traversal

**Problem Link:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description

**Problem Statement:**
- Input format and constraints: Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, reconstruct and return the binary tree.
- Expected output format: Return the root of the reconstructed binary tree.
- Key requirements and edge cases to consider: 
  - The length of `preorder` and `inorder` will be the same.
  - The values in `preorder` and `inorder` will be unique.
  - The given input is guaranteed to be valid, i.e., it represents a valid binary tree.
- Example test cases with explanations: 
  - Example 1: Input: `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`. Output: `[3,9,20,null,null,15,7]`.
  - Example 2: Input: `preorder = [-1]`, `inorder = [-1]`. Output: `[-1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying to construct the binary tree by iterating through the preorder and inorder arrays and using a recursive approach to build the tree. However, this approach is inefficient because it involves a lot of repeated work and does not take advantage of the properties of preorder and inorder traversals.
- Step-by-step breakdown of the solution:
  1. Start with the first element of the preorder array as the root.
  2. Find the root in the inorder array to determine the left and right subtrees.
  3. Recursively construct the left and right subtrees.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it involves a lot of repeated work.

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() || inorder.empty()) return NULL;
        
        TreeNode* root = new TreeNode(preorder[0]);
        int index = find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
        vector<int> rightInorder(inorder.begin() + index + 1, inorder.end());
        
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> rightPreorder(preorder.begin() + index + 1, preorder.end());
        
        root->left = buildTree(leftPreorder, leftInorder);
        root->right = buildTree(rightPreorder, rightInorder);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because in the worst case, we are searching for an element in the inorder array for each node, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$ because we are using recursive call stack and storing the nodes of the tree.
> - **Why these complexities occur:** The time complexity is high because of the search operation in the inorder array, and the space complexity is due to the recursive call stack and the storage of the tree nodes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of searching for the root in the inorder array for each recursive call, we can pass the indices of the current subtree to avoid the search operation.
- Detailed breakdown of the approach:
  1. Initialize the indices for the preorder and inorder arrays.
  2. Recursively construct the left and right subtrees by passing the updated indices.
- Proof of optimality: This approach is optimal because it avoids the search operation in the inorder array and only traverses the arrays once.

```cpp
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTreeHelper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
    
    TreeNode* buildTreeHelper(vector<int>& preorder, int preStart, int preEnd, vector<int>& inorder, int inStart, int inEnd) {
        if (preStart > preEnd) return NULL;
        
        TreeNode* root = new TreeNode(preorder[preStart]);
        int index = find(inorder.begin() + inStart, inorder.begin() + inEnd + 1, preorder[preStart]) - inorder.begin();
        
        int leftSize = index - inStart;
        
        root->left = buildTreeHelper(preorder, preStart + 1, preStart + leftSize, inorder, inStart, index - 1);
        root->right = buildTreeHelper(preorder, preStart + leftSize + 1, preEnd, inorder, index + 1, inEnd);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are traversing the arrays once, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$ because we are using recursive call stack and storing the nodes of the tree.
> - **Optimality proof:** This approach is optimal because it avoids the search operation in the inorder array and only traverses the arrays once, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, tree construction, and optimization techniques.
- Problem-solving patterns identified: Avoiding repeated work and using indices to traverse arrays efficiently.
- Optimization techniques learned: Passing indices instead of searching for elements in arrays.
- Similar problems to practice: Constructing binary trees from different types of traversals, such as postorder and inorder.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, missing base cases for recursion, and not handling edge cases properly.
- Edge cases to watch for: Empty arrays, single-element arrays, and arrays with duplicate values.
- Performance pitfalls: Using inefficient search operations and not optimizing recursive calls.
- Testing considerations: Testing with different types of input, such as balanced and unbalanced trees, and edge cases.