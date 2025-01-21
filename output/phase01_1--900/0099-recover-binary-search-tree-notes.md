## Recover Binary Search Tree

**Problem Link:** [https://leetcode.com/problems/recover-binary-search-tree/description](https://leetcode.com/problems/recover-binary-search-tree/description)

**Problem Statement:**
- Input format: The root of a binary tree, where two nodes are swapped.
- Constraints: The number of nodes in the tree is in the range `[2, 100]`.
- Expected output format: Modify the binary tree in-place to recover the correct binary search tree.
- Key requirements: 
    - The input tree is a binary search tree where exactly two nodes were swapped.
    - The goal is to recover the original binary search tree by swapping the two nodes back.
- Example test cases:
    - Input: `[1,3,null,null,2]`, where the tree is `    1
    / \
   null  3
  /
 2`
    - Output: `[3,1,null,null,2]`, where the tree is `    3
    / \
   null  1
  /
 2`

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible pairs of nodes in the tree and swapping them to see if the resulting tree is a valid binary search tree.
- Step-by-step breakdown:
    1. Perform an in-order traversal of the tree to get a list of node values in ascending order.
    2. Identify the two nodes that are out of order in the list.
    3. Swap the two nodes in the original tree.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has high time complexity due to the need to check all possible pairs of nodes.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void recoverTree(TreeNode* root) {
        vector<int> inOrder;
        getInOrder(root, inOrder);
        
        vector<int> sortedInOrder = inOrder;
        sort(sortedInOrder.begin(), sortedInOrder.end());
        
        unordered_map<int, int> wrongNodes;
        for (int i = 0; i < inOrder.size(); i++) {
            if (inOrder[i] != sortedInOrder[i]) {
                wrongNodes[inOrder[i]] = sortedInOrder[i];
            }
        }
        
        recoverTreeHelper(root, wrongNodes);
    }
    
    void getInOrder(TreeNode* root, vector<int>& inOrder) {
        if (root == nullptr) {
            return;
        }
        getInOrder(root->left, inOrder);
        inOrder.push_back(root->val);
        getInOrder(root->right, inOrder);
    }
    
    void recoverTreeHelper(TreeNode* root, unordered_map<int, int>& wrongNodes) {
        if (root == nullptr) {
            return;
        }
        recoverTreeHelper(root->left, wrongNodes);
        
        if (wrongNodes.find(root->val) != wrongNodes.end()) {
            root->val = wrongNodes[root->val];
        }
        
        recoverTreeHelper(root->right, wrongNodes);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting step, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$ for storing the in-order traversal of the tree and the sorted in-order traversal.
> - **Why these complexities occur:** The time complexity is dominated by the sorting step, and the space complexity is due to the need to store the in-order traversal of the tree.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all possible pairs of nodes, we can use the fact that a binary search tree has a specific order property to identify the two nodes that are out of order.
- Detailed breakdown:
    1. Perform an in-order traversal of the tree and keep track of the previous node.
    2. If the current node's value is less than the previous node's value, it means we have found one of the two nodes that are out of order.
    3. Keep track of the first and second nodes that are out of order.
    4. Swap the values of the first and second nodes.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is optimal because we need to visit each node at least once to check if it is out of order.

```cpp
class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode* first = nullptr;
        TreeNode* second = nullptr;
        TreeNode* prev = nullptr;
        
        while (root) {
            if (root->left == nullptr) {
                if (prev != nullptr && prev->val > root->val) {
                    if (first == nullptr) {
                        first = prev;
                    }
                    second = root;
                }
                prev = root;
                root = root->right;
            } else {
                TreeNode* temp = root->left;
                while (temp->right != nullptr && temp->right != root) {
                    temp = temp->right;
                }
                if (temp->right == nullptr) {
                    temp->right = root;
                    root = root->left;
                } else {
                    temp->right = nullptr;
                    if (prev != nullptr && prev->val > root->val) {
                        if (first == nullptr) {
                            first = prev;
                        }
                        second = root;
                    }
                    prev = root;
                    root = root->right;
                }
            }
        }
        
        swap(first->val, second->val);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it only visits each node once and uses a constant amount of extra space to store the previous node and the two nodes that are out of order.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal, binary search tree properties.
- Problem-solving patterns identified: Using the order property of a binary search tree to identify nodes that are out of order.
- Optimization techniques learned: Reducing the time complexity by avoiding unnecessary operations.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as an empty tree or a tree with only one node.
- Edge cases to watch for: A tree with two nodes that are swapped, a tree with more than two nodes that are out of order.
- Performance pitfalls: Using a brute force approach that has high time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.