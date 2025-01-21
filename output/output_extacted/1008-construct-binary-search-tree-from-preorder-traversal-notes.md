## Construct Binary Search Tree from Preorder Traversal

**Problem Link:** https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description

**Problem Statement:**
- Input: An array of distinct integers `preorder`, representing a preorder traversal of a binary search tree (BST).
- Output: The root node of the constructed BST.
- Key requirements:
  - The input array represents a valid preorder traversal of a BST.
  - The constructed BST must satisfy the BST property: for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
- Edge cases:
  - An empty input array represents an empty BST.
  - A single-element input array represents a BST with one node.

**Example Test Cases:**
- Input: `preorder = [8,5,1,7,10,12]`
  - Output: The root node of the constructed BST, which can be visualized as:
        ```
        8
       / \
      5   10
     / \    \
    1   7   12
        ```
- Input: `preorder = [1]`
  - Output: The root node of the constructed BST, which is a single node with value 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a recursive approach to construct the BST. For each node, we find the first element in the preorder traversal that is greater than the current node's value. This element becomes the right child of the current node.
- Step-by-step breakdown:
  1. Start with the first element of the preorder traversal as the root node.
  2. For each subsequent element in the preorder traversal, find the first node in the current BST that has a value greater than the current element.
  3. If such a node is found, insert the current element as the right child of that node.
  4. If no such node is found, insert the current element as the left child of the last node that was inserted.

```cpp
// Brute force approach
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        if (preorder.empty()) return nullptr;
        TreeNode* root = new TreeNode(preorder[0]);
        for (int i = 1; i < preorder.size(); i++) {
            TreeNode* current = root;
            while (true) {
                if (preorder[i] < current->val) {
                    if (!current->left) {
                        current->left = new TreeNode(preorder[i]);
                        break;
                    }
                    current = current->left;
                } else {
                    if (!current->right) {
                        current->right = new TreeNode(preorder[i]);
                        break;
                    }
                    current = current->right;
                }
            }
        }
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the preorder traversal. This is because in the worst case, we may need to traverse the entire BST for each element in the preorder traversal.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the preorder traversal. This is because we need to store all the nodes of the constructed BST.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the repeated traversal of the BST for each element in the preorder traversal.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a recursive approach with a lower bound to efficiently construct the BST. For each node, we find the range of values that can be in its left and right subtrees.
- Step-by-step breakdown:
  1. Start with the first element of the preorder traversal as the root node.
  2. For each subsequent element in the preorder traversal, find the range of values that can be in the left subtree of the current node.
  3. If the current element is within the range of values for the left subtree, recursively construct the left subtree.
  4. Otherwise, the current element becomes the root of the right subtree.

```cpp
// Optimal approach
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        return bstFromPreorder(preorder, 0, preorder.size(), INT_MIN, INT_MAX);
    }
    
    TreeNode* bstFromPreorder(vector<int>& preorder, int start, int end, int lower, int upper) {
        if (start == end) return nullptr;
        if (preorder[start] < lower || preorder[start] > upper) return nullptr;
        TreeNode* root = new TreeNode(preorder[start]);
        int rightStart = start + 1;
        while (rightStart < end && preorder[rightStart] < root->val) rightStart++;
        root->left = bstFromPreorder(preorder, start + 1, rightStart, lower, root->val);
        root->right = bstFromPreorder(preorder, rightStart, end, root->val, upper);
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the preorder traversal. This is because we only visit each element once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the preorder traversal. This is because we need to store all the nodes of the constructed BST.
> - **Optimality proof:** The optimal approach has linear time complexity because we only visit each element once and use a recursive approach to construct the BST.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive approach, lower bound, range of values for left and right subtrees.
- Problem-solving patterns identified: using a recursive approach to construct a BST from a preorder traversal.
- Optimization techniques learned: using a lower bound to efficiently construct the BST.
- Similar problems to practice: constructing a BST from an inorder traversal, constructing a BST from a postorder traversal.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not handling the case where the input array is empty.
- Edge cases to watch for: empty input array, single-element input array.
- Performance pitfalls: using a brute force approach with high time complexity.
- Testing considerations: testing the implementation with different input arrays, including edge cases.