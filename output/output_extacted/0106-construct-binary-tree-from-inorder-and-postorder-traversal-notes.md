## Construct Binary Tree from Inorder and Postorder Traversal

**Problem Link:** https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description

**Problem Statement:**
- Input format: Two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree.
- Constraints: `1 <= inorder.length <= 3000`, `postorder.length == inorder.length`, `0 <= inorder[i] <= 3000`, `0 <= postorder[i] <= 3000`, `inorder` and `postorder` represent a valid binary tree with unique values.
- Expected output: The root of the constructed binary tree.
- Key requirements: The function should construct a binary tree from the given inorder and postorder traversals and return its root.
- Edge cases: Empty input arrays, single-element arrays.

**Example Test Cases:**
- Example 1:
  - Input: `inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]`
  - Output: The root of the binary tree `[3,9,20,null,null,15,7]`
- Example 2:
  - Input: `inorder = [-1], postorder = [-1]`
  - Output: The root of the binary tree `[-1]`

### Brute Force Approach

**Explanation:**
- The initial thought process involves directly constructing the binary tree by comparing elements from the inorder and postorder traversals. However, this approach is not efficient as it involves a lot of comparisons and does not utilize the properties of inorder and postorder traversals effectively.
- A step-by-step breakdown would involve:
  1. Identifying the root node from the postorder traversal (last element).
  2. Finding the index of the root node in the inorder traversal.
  3. Recursively constructing the left and right subtrees.
- This approach comes to mind first because it directly utilizes the given traversals to construct the tree, but it's not efficient due to repeated comparisons and lack of optimization.

```cpp
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.empty() || postorder.empty()) return nullptr;
        
        TreeNode* root = new TreeNode(postorder.back());
        int rootIndex = find(inorder.begin(), inorder.end(), postorder.back()) - inorder.begin();
        
        vector<int> leftInorder(inorder.begin(), inorder.begin() + rootIndex);
        vector<int> rightInorder(inorder.begin() + rootIndex + 1, inorder.end());
        vector<int> leftPostorder(postorder.begin(), postorder.begin() + rootIndex);
        vector<int> rightPostorder(postorder.begin() + rootIndex, postorder.end() - 1);
        
        root->left = buildTree(leftInorder, leftPostorder);
        root->right = buildTree(rightInorder, rightPostorder);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because for each node, we are potentially scanning the entire inorder array to find its index.
> - **Space Complexity:** $O(n)$, due to the recursive call stack and the space needed to store the node values.
> - **Why these complexities occur:** The brute force approach involves a lot of unnecessary comparisons and scans through the input arrays, leading to high time complexity. The space complexity is due to the recursive nature of the solution and the need to store node values.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that the last element of the postorder traversal is the root of the tree, and then using this information to divide the inorder traversal into left and right subtrees.
- A detailed breakdown of the approach involves:
  1. Creating a hashmap to store the indices of elements in the inorder traversal for efficient lookup.
  2. Defining a recursive function that takes the start and end indices of the current subtree in both inorder and postorder traversals.
  3. Within the recursive function, identifying the root node from the postorder traversal and finding its index in the inorder traversal using the hashmap.
  4. Recursively constructing the left and right subtrees by adjusting the start and end indices based on the root's index.
- This approach is optimal because it utilizes a hashmap for constant time lookup of indices in the inorder traversal, significantly reducing the time complexity compared to the brute force approach.

```cpp
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        unordered_map<int, int> indexMap;
        for (int i = 0; i < n; ++i) {
            indexMap[inorder[i]] = i;
        }
        
        return buildTreeHelper(inorder, postorder, 0, n - 1, 0, n - 1, indexMap);
    }
    
    TreeNode* buildTreeHelper(vector<int>& inorder, vector<int>& postorder, int inStart, int inEnd, int postStart, int postEnd, unordered_map<int, int>& indexMap) {
        if (inStart > inEnd || postStart > postEnd) return nullptr;
        
        TreeNode* root = new TreeNode(postorder[postEnd]);
        int rootIndex = indexMap[postorder[postEnd]];
        int leftSize = rootIndex - inStart;
        
        root->left = buildTreeHelper(inorder, postorder, inStart, rootIndex - 1, postStart, postStart + leftSize - 1, indexMap);
        root->right = buildTreeHelper(inorder, postorder, rootIndex + 1, inEnd, postStart + leftSize, postEnd - 1, indexMap);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are doing a constant amount of work for each node, and the hashmap allows for constant time lookup of indices.
> - **Space Complexity:** $O(n)$, due to the recursive call stack, the space needed to store the node values, and the hashmap.
> - **Optimality proof:** This solution is optimal because it minimizes the number of operations needed to construct the binary tree from the given traversals, leveraging the properties of inorder and postorder traversals along with efficient data structures like hashmaps.

### Final Notes

**Learning Points:**
- The importance of understanding the properties of binary tree traversals (inorder, postorder, preorder).
- Utilizing hashmaps for efficient lookup and reducing time complexity.
- Recursive approaches for constructing binary trees from traversals.
- Optimizing solutions by minimizing unnecessary comparisons and scans.

**Mistakes to Avoid:**
- Not utilizing the properties of binary tree traversals effectively.
- Implementing inefficient lookup mechanisms (e.g., linear search instead of hashmap).
- Failing to handle edge cases (e.g., empty input arrays).
- Not optimizing recursive functions to minimize redundant calculations.