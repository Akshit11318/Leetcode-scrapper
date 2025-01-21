## Find Largest Value in Each Tree Row

**Problem Link:** https://leetcode.com/problems/find-largest-value-in-each-tree-row/description

**Problem Statement:**
- Input format and constraints: You are given a binary tree, and you need to find the largest value in each row of the tree.
- Expected output format: Return a vector of integers where the `i-th` element is the largest value in the `i-th` row.
- Key requirements and edge cases to consider: The input tree is not empty, and the tree may have a large number of nodes.
- Example test cases with explanations:
  - Example 1:
    - Input: `root = [1,3,2,5,3,null,9]`
    - Output: `[1,3,9]`
  - Example 2:
    - Input: `root = [1]`
    - Output: `[1]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can traverse the tree level by level, and for each level, we can find the maximum value.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the root node and its level (0).
  2. Initialize an empty vector to store the maximum values for each level.
  3. While the queue is not empty, dequeue a node and its level.
  4. If the level is equal to the size of the result vector, add a new element to the vector with the value of the current node.
  5. Otherwise, update the value at the current level in the result vector if the value of the current node is greater.
  6. Enqueue the children of the current node with their levels.
- Why this approach comes to mind first: It is a straightforward way to traverse the tree level by level and find the maximum value at each level.

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
    vector<int> largestValues(TreeNode* root) {
        if (!root) return {};
        
        vector<int> result;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            auto [node, level] = q.front();
            q.pop();
            
            if (level == result.size()) {
                result.push_back(node->val);
            } else {
                result[level] = max(result[level], node->val);
            }
            
            if (node->left) q.push({node->left, level + 1});
            if (node->right) q.push({node->right, level + 1});
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, the queue will store all nodes at the last level, which is $n/2$ nodes.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is linear because we need to store all nodes at the last level in the queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because it already has a linear time complexity and is easy to implement.
- Detailed breakdown of the approach: The approach is the same as the brute force approach.
- Proof of optimality: The time complexity is optimal because we need to visit each node at least once to find the maximum value at each level.
- Why further optimization is impossible: Further optimization is impossible because we need to visit each node at least once, and the current approach already does that in linear time.

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
    vector<int> largestValues(TreeNode* root) {
        if (!root) return {};
        
        vector<int> result;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            auto [node, level] = q.front();
            q.pop();
            
            if (level == result.size()) {
                result.push_back(node->val);
            } else {
                result[level] = max(result[level], node->val);
            }
            
            if (node->left) q.push({node->left, level + 1});
            if (node->right) q.push({node->right, level + 1});
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, the queue will store all nodes at the last level, which is $n/2$ nodes.
> - **Optimality proof:** The time complexity is optimal because we need to visit each node at least once to find the maximum value at each level.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Breadth-First Search (BFS), queue data structure.
- Problem-solving patterns identified: Level order traversal, finding maximum values.
- Optimization techniques learned: None, because the brute force approach is already optimal.
- Similar problems to practice: `102. Binary Tree Level Order Traversal`, `107. Binary Tree Level Order Traversal II`.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the node is null before accessing its children.
- Edge cases to watch for: Empty tree, tree with only one node.
- Performance pitfalls: Using a recursive approach, which can cause a stack overflow for very large trees.
- Testing considerations: Test with different tree structures, including empty tree, tree with only one node, and tree with multiple levels.