## Minimum Distance Between BST Nodes

**Problem Link:** https://leetcode.com/problems/minimum-distance-between-bst-nodes/description

**Problem Statement:**
- Given the root of a Binary Search Tree (BST), find the minimum difference between the values of any two different nodes in the tree.
- Input format: The root of a BST.
- Constraints: The number of nodes in the tree is in the range [2, 100].
- Expected output format: The minimum difference between any two different nodes in the tree.
- Key requirements and edge cases to consider: The tree is not empty, and there are at least two nodes.

**Example Test Cases:**
- Example 1:
  - Input: `root = [4,2,6,1,3]`
  - Output: `1`
  - Explanation: The minimum difference between any two different nodes in the tree is `1`, which is the difference between `1` and `2` or between `3` and `4`.
- Example 2:
  - Input: `root = [1,0,48,1,null,27,50,1,null,2,null,null,45]`
  - Output: `1`
  - Explanation: The minimum difference between any two different nodes in the tree is `1`, which is the difference between several pairs of nodes.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree and store all node values in a list or array.
- Then, sort the list of node values.
- Finally, iterate through the sorted list to find the minimum difference between any two adjacent values.

```cpp
class Solution {
public:
    int minDiffInBST(TreeNode* root) {
        vector<int> values;
        inorderTraversal(root, values);
        sort(values.begin(), values.end());
        int minDiff = INT_MAX;
        for (int i = 1; i < values.size(); i++) {
            minDiff = min(minDiff, values[i] - values[i - 1]);
        }
        return minDiff;
    }
    
    void inorderTraversal(TreeNode* root, vector<int>& values) {
        if (root) {
            inorderTraversal(root->left, values);
            values.push_back(root->val);
            inorderTraversal(root->right, values);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of nodes in the tree. This is because we are sorting the list of node values, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(n)$, as we need to store all node values in the list.
> - **Why these complexities occur:** The sorting operation is the main contributor to the time complexity, while the space complexity is due to storing all node values.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the properties of a Binary Search Tree (BST) to find the minimum difference without sorting.
- We can perform an in-order traversal of the BST and keep track of the previous node's value.
- The minimum difference will be found by comparing the current node's value with the previous node's value during the traversal.

```cpp
class Solution {
public:
    int minDiffInBST(TreeNode* root) {
        int minDiff = INT_MAX;
        int prevVal = -1;
        inorderTraversal(root, minDiff, prevVal);
        return minDiff;
    }
    
    void inorderTraversal(TreeNode* root, int& minDiff, int& prevVal) {
        if (root) {
            inorderTraversal(root->left, minDiff, prevVal);
            if (prevVal != -1) {
                minDiff = min(minDiff, root->val - prevVal);
            }
            prevVal = root->val;
            inorderTraversal(root->right, minDiff, prevVal);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are performing a single pass through the tree.
> - **Space Complexity:** $O(n)$, as in the worst case, the recursive call stack can go up to the height of the tree, which is $n$ for an unbalanced tree.
> - **Optimality proof:** This approach is optimal because we are only visiting each node once and using a constant amount of extra space to store the previous node's value, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal of a Binary Search Tree (BST) and keeping track of the previous node's value to find the minimum difference.
- Problem-solving patterns identified: Using the properties of a BST to avoid sorting and reduce the time complexity.
- Optimization techniques learned: Avoiding unnecessary operations like sorting and using a single pass through the tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where the previous node's value is not initialized.
- Edge cases to watch for: Empty trees or trees with a single node.
- Performance pitfalls: Using sorting or other inefficient methods to find the minimum difference.
- Testing considerations: Testing with different tree structures, including balanced and unbalanced trees, to ensure the solution works correctly in all cases.