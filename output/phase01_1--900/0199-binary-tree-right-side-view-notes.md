## Binary Tree Right Side View

**Problem Link:** https://leetcode.com/problems/binary-tree-right-side-view/description

**Problem Statement:**
- Input format: The input is the root of a binary tree.
- Constraints: The number of nodes in the tree is in the range `[0, 100]`.
- Expected output format: Return a list of the rightmost node at each level.
- Key requirements and edge cases to consider: Handle empty trees, trees with a single node, and trees with multiple levels.
- Example test cases with explanations: 
  - Example 1: Input: `root = [1,2,3,null,5,null,4]`, Output: `[1,3,4]`
  - Example 2: Input: `root = [1,null,3]`, Output: `[1,3]`
  - Example 3: Input: `root = []`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a level-order traversal of the binary tree and store all nodes at each level. Then, extract the last node at each level to obtain the right side view.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the root node and a level counter.
  2. Perform a level-order traversal using the queue, storing nodes at each level in a separate list.
  3. Extract the last node from each level's list to obtain the right side view.
- Why this approach comes to mind first: It is a straightforward way to traverse the tree and collect nodes at each level.

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
    vector<int> rightSideView(TreeNode* root) {
        if (!root) return {};
        
        vector<int> result;
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (i == levelSize - 1) {
                    result.push_back(node->val);
                }
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, as in the worst case (when the tree is a complete binary tree), the queue will store $n/2$ nodes at the last level.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear due to the storage required for the queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can directly collect the rightmost node at each level during the level-order traversal, eliminating the need to store all nodes at each level.
- Detailed breakdown of the approach:
  1. Initialize a queue with the root node.
  2. Perform a level-order traversal, and for each level, directly add the last node to the result list.
- Proof of optimality: This approach is optimal because it only requires a single pass through the tree and uses a minimal amount of extra space to store the result.

```cpp
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (!root) return {};
        
        vector<int> result;
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (i == levelSize - 1) {
                    result.push_back(node->val);
                }
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, as in the worst case (when the tree is a complete binary tree), the queue will store $n/2$ nodes at the last level.
> - **Optimality proof:** This approach is optimal because it achieves the minimum time complexity required to traverse the tree and collect the rightmost node at each level.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level-order traversal, queue data structure.
- Problem-solving patterns identified: Directly collecting the required information during traversal to minimize extra space.
- Optimization techniques learned: Eliminating unnecessary storage to reduce space complexity.
- Similar problems to practice: Other tree traversal problems, such as finding the leftmost node at each level.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle the case where the tree is empty or only has one node.
- Edge cases to watch for: Trees with multiple levels, trees with only one node, empty trees.
- Performance pitfalls: Using excessive extra space to store unnecessary information.
- Testing considerations: Ensure that the solution works correctly for trees of different sizes and structures.