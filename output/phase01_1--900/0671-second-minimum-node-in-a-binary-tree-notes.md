## Second Minimum Node In a Binary Tree

**Problem Link:** https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description

**Problem Statement:**
- Given a non-empty special binary tree, each node has one of two possible values: either 0 or 1. Each node having a value of 0 has two children, and each node having a value of 1 has one child.
- The root of the tree is given, and we need to find the second minimum value in the tree.
- If no such node exists, return -1.

**Input Format and Constraints:**
- The number of nodes in the tree is in the range [1, 100].
- Each node has a value of either 0 or 1.

**Expected Output Format:**
- The second minimum value in the tree if it exists, otherwise -1.

**Key Requirements and Edge Cases to Consider:**
- Handling the root node with a value of 1.
- Handling nodes with a value of 0 and their children.
- Finding the minimum and second minimum values.

**Example Test Cases with Explanations:**
- Example 1:
  - Input: root = [1]
  - Output: -1
  - Explanation: Since there's only one node with a value of 1, there's no second minimum value.

- Example 2:
  - Input: root = [0,1,0]
  - Output: 1
  - Explanation: The tree structure is:
        0
       / \
      1   0
    The second minimum value is 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to perform a depth-first search (DFS) or breadth-first search (BFS) traversal of the binary tree to find all node values.
- Store the values in a data structure like a set or vector to keep track of unique values.
- Then, sort the unique values to find the second minimum value.

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
    int findSecondMinimumValue(TreeNode* root) {
        set<int> values;
        dfs(root, values);
        if (values.size() < 2) {
            return -1;
        }
        auto it = values.begin();
        ++it;
        return *it;
    }
    
    void dfs(TreeNode* node, set<int>& values) {
        if (node == nullptr) {
            return;
        }
        values.insert(node->val);
        dfs(node->left, values);
        dfs(node->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of nodes in the tree. The reason is that in the worst case, we visit each node once during the DFS traversal, and then we insert each value into a set, which takes $\log n$ time.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store all node values in the set.
> - **Why these complexities occur:** These complexities occur because we are using a set to store unique values, which has a time complexity of $\log n$ for insertion operations, and we are performing a DFS traversal of the tree.

---

### Optimal Approach (Required)

**Explanation:**
- Instead of storing all node values in a set and then sorting them, we can keep track of the minimum and second minimum values during the DFS traversal itself.
- Initialize the minimum value with the root's value and the second minimum value with a large number (e.g., INT_MAX).
- During the traversal, if we find a value less than the current second minimum value and not equal to the minimum value, we update the second minimum value.

```cpp
class Solution {
public:
    int findSecondMinimumValue(TreeNode* root) {
        int minVal = root->val;
        int secondMinVal = INT_MAX;
        dfs(root, minVal, secondMinVal);
        return secondMinVal == INT_MAX ? -1 : secondMinVal;
    }
    
    void dfs(TreeNode* node, int& minVal, int& secondMinVal) {
        if (node == nullptr) {
            return;
        }
        if (node->val > minVal && node->val < secondMinVal) {
            secondMinVal = node->val;
        }
        dfs(node->left, minVal, secondMinVal);
        dfs(node->right, minVal, secondMinVal);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. We visit each node once during the DFS traversal.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This is the optimal solution because we only visit each node once and keep track of the necessary information (minimum and second minimum values) during the traversal, without using any additional data structures that would increase the space complexity.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and using them to optimize the solution.
- The use of DFS traversal to solve tree-related problems.
- Keeping track of necessary information during the traversal to avoid additional data structures.

**Mistakes to Avoid:**
- Not considering the problem constraints and using a more general approach that might not be optimal.
- Not handling edge cases properly, such as when the tree has only one node.
- Not optimizing the solution for space complexity.