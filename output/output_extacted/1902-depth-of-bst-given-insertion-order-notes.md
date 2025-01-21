## Depth of BST Given Insertion Order

**Problem Link:** https://leetcode.com/problems/depth-of-bst-given-insertion-order/description

**Problem Statement:**
- Input: An array of integers representing the insertion order of a Binary Search Tree (BST).
- Constraints: The input array will not be empty, and all integers will be unique.
- Expected Output: The minimum depth of the BST.
- Key Requirements: The BST must be constructed following the insertion order, and the minimum depth must be calculated.
- Edge Cases: The input array may contain a single element or a large number of elements.

### Brute Force Approach

**Explanation:**
- The initial thought process is to construct the BST by inserting elements one by one according to the given order and then calculate the minimum depth.
- Step-by-step breakdown:
  1. Create a `TreeNode` class to represent each node in the BST.
  2. Construct the BST by iterating through the insertion order and inserting each element into the tree.
  3. Calculate the minimum depth of the BST by performing a level-order traversal and keeping track of the minimum depth encountered.

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
    int maxDepth(TreeNode* root) {
        if (root == NULL) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }

    int minDepth(TreeNode* root) {
        if (root == NULL) return 0;
        if (root->left == NULL && root->right == NULL) return 1;
        if (root->left == NULL) return 1 + minDepth(root->right);
        if (root->right == NULL) return 1 + minDepth(root->left);
        return 1 + min(minDepth(root->left), minDepth(root->right));
    }

    int minDepth(vector<int>& order) {
        TreeNode* root = new TreeNode(order[0]);
        for (int i = 1; i < order.size(); i++) {
            TreeNode* node = root;
            while (true) {
                if (order[i] < node->val) {
                    if (node->left == NULL) {
                        node->left = new TreeNode(order[i]);
                        break;
                    }
                    node = node->left;
                } else {
                    if (node->right == NULL) {
                        node->right = new TreeNode(order[i]);
                        break;
                    }
                    node = node->right;
                }
            }
        }
        return minDepth(root);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the input array. This is because in the worst-case scenario, we need to traverse the entire tree for each insertion, resulting in quadratic time complexity.
> - **Space Complexity:** $O(n)$, as we need to store all elements in the tree.
> - **Why these complexities occur:** The brute force approach leads to inefficient insertion and depth calculation due to the recursive nature of the tree construction and the lack of optimization in the insertion process.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to construct the BST using a more efficient method, taking advantage of the properties of a BST.
- Step-by-step breakdown:
  1. Initialize the root node with the first element of the insertion order.
  2. Iterate through the remaining elements in the insertion order.
  3. For each element, start from the root node and move down the tree, choosing the left or right child based on whether the current node's value is greater than or less than the element.
  4. When a leaf node is reached, insert the element as a child of the current node.
  5. Calculate the minimum depth of the BST by performing a level-order traversal and keeping track of the minimum depth encountered.

```cpp
class Solution {
public:
    int minDepth(vector<int>& order) {
        TreeNode* root = new TreeNode(order[0]);
        for (int i = 1; i < order.size(); i++) {
            TreeNode* node = root;
            while (true) {
                if (order[i] < node->val) {
                    if (node->left == NULL) {
                        node->left = new TreeNode(order[i]);
                        break;
                    }
                    node = node->left;
                } else {
                    if (node->right == NULL) {
                        node->right = new TreeNode(order[i]);
                        break;
                    }
                    node = node->right;
                }
            }
        }
        queue<TreeNode*> q;
        q.push(root);
        int depth = 0;
        while (!q.empty()) {
            int size = q.size();
            depth++;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left == NULL && node->right == NULL) {
                    return depth;
                }
                if (node->left != NULL) q.push(node->left);
                if (node->right != NULL) q.push(node->right);
            }
        }
        return depth;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we perform a constant amount of work for each element in the array.
> - **Space Complexity:** $O(n)$, as we need to store all elements in the tree.
> - **Optimality proof:** This approach is optimal because we only visit each node once during the construction of the tree and the calculation of the minimum depth.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: tree construction, level-order traversal, and minimum depth calculation.
- Problem-solving patterns identified: using a queue to perform level-order traversal and keeping track of the minimum depth encountered.
- Optimization techniques learned: avoiding unnecessary recursive calls and using a more efficient method for tree construction.
- Similar problems to practice: constructing a BST from a sorted array, calculating the maximum depth of a BST, and finding the minimum depth of a binary tree.

**Mistakes to Avoid:**
- Common implementation errors: not checking for null pointers, not handling edge cases, and using inefficient algorithms.
- Edge cases to watch for: empty input array, single-element input array, and large input arrays.
- Performance pitfalls: using recursive functions with high time complexity, not optimizing the tree construction process, and not using efficient data structures.
- Testing considerations: testing with different input sizes, testing with edge cases, and testing with random input arrays.