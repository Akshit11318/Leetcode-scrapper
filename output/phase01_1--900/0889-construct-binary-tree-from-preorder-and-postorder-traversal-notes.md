## Construct Binary Tree from Preorder and Postorder Traversal

**Problem Link:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description

**Problem Statement:**
- Input format: Two integer arrays `preorder` and `postorder` where `preorder` is the preorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree.
- Constraints: `1 <= preorder.length == postorder.length <= 30`, `0 <= preorder[i], postorder[i] <= 100`, and both `preorder` and `postorder` represent the same binary tree.
- Expected output format: The root of the constructed binary tree.
- Key requirements and edge cases to consider: The input arrays represent valid preorder and postorder traversals of a binary tree, and the tree is not guaranteed to be balanced.

**Example Test Cases:**
- Given `preorder = [1,2,4,5,3,6,7]` and `postorder = [4,5,2,6,7,3,1]`, return the root of the binary tree represented by these traversals.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of nodes to form a binary tree and then checking if the preorder and postorder traversals of the constructed tree match the given arrays.
- This approach is impractical due to its exponential time complexity.

```cpp
class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        // Base case
        if (preorder.empty()) return nullptr;
        
        // Create the root node
        TreeNode* root = new TreeNode(preorder[0]);
        
        // If there's only one node, return it
        if (preorder.size() == 1) return root;
        
        // Find the index of the left child in the preorder traversal
        int leftChildIndex = 1;
        
        // Find the index of the right child in the postorder traversal
        int rightChildIndex = postorder.size() - 2;
        
        // Recursively construct the left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + leftChildIndex + 1);
        vector<int> leftPostorder(postorder.begin(), postorder.begin() + leftChildIndex);
        vector<int> rightPreorder(preorder.begin() + leftChildIndex + 1, preorder.end());
        vector<int> rightPostorder(postorder.begin() + leftChildIndex, postorder.end() - 1);
        
        root->left = constructFromPrePost(leftPreorder, leftPostorder);
        root->right = constructFromPrePost(rightPreorder, rightPostorder);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the number of nodes in the tree, due to trying all possible combinations of nodes.
> - **Space Complexity:** $O(n)$ for storing the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the properties of preorder and postorder traversals to construct the binary tree.
- In a preorder traversal, the root node is visited first, followed by the left subtree and then the right subtree.
- In a postorder traversal, the left subtree is visited first, followed by the right subtree and then the root node.
- We can use these properties to recursively construct the left and right subtrees.

```cpp
class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        int preIndex = 0;
        int postIndex = 0;
        return construct(preorder, postorder, preIndex, postIndex);
    }
    
    TreeNode* construct(vector<int>& preorder, vector<int>& postorder, int& preIndex, int& postIndex) {
        if (preIndex >= preorder.size() || postIndex >= postorder.size()) {
            return nullptr;
        }
        
        TreeNode* root = new TreeNode(preorder[preIndex++]);
        
        if (preIndex >= preorder.size() || postIndex >= postorder.size()) {
            return root;
        }
        
        if (preorder[preIndex] == postorder[postIndex]) {
            root->left = construct(preorder, postorder, preIndex, postIndex);
        } else {
            root->left = construct(preorder, postorder, preIndex, postIndex);
            root->right = construct(preorder, postorder, preIndex, postIndex);
        }
        
        return root;
    }
};
```

However, this code has an issue in the `construct` method where it checks if `preorder[preIndex] == postorder[postIndex]`. The correct approach should utilize the fact that the first element in the preorder traversal is the root, and then find the index of the left child in the postorder traversal to determine the size of the left subtree.

Here is the corrected optimal approach:

```cpp
class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        int preIndex = 0;
        int postIndex = 0;
        return construct(preorder, postorder, preIndex, postIndex);
    }
    
    TreeNode* construct(vector<int>& preorder, vector<int>& postorder, int& preIndex, int& postIndex) {
        if (preIndex >= preorder.size() || postIndex >= postorder.size()) {
            return nullptr;
        }
        
        TreeNode* root = new TreeNode(preorder[preIndex++]);
        
        if (preIndex >= preorder.size() || postIndex >= postorder.size()) {
            return root;
        }
        
        // Find the index of the left child in the postorder traversal
        int leftChildIndex = postIndex;
        while (postorder[leftChildIndex] != preorder[preIndex]) {
            leftChildIndex++;
        }
        
        int leftSize = leftChildIndex - postIndex + 1;
        
        // Construct the left subtree
        root->left = construct(preorder, postorder, preIndex, postIndex);
        
        // Move the postIndex to the end of the left subtree
        postIndex += leftSize;
        
        // Construct the right subtree
        root->right = construct(preorder, postorder, preIndex, postIndex);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$ for storing the recursive call stack.
> - **Optimality proof:** This is the optimal solution because we only visit each node once, resulting in linear time complexity.

---

### Final Notes

**Learning Points:**
- The key insight is to use the properties of preorder and postorder traversals to construct the binary tree.
- We can use these properties to recursively construct the left and right subtrees.
- The optimal approach has a time complexity of $O(n)$, where $n$ is the number of nodes in the tree.

**Mistakes to Avoid:**
- Trying all possible combinations of nodes, which results in exponential time complexity.
- Not utilizing the properties of preorder and postorder traversals to construct the binary tree.
- Not handling the base case correctly, where the input arrays are empty.