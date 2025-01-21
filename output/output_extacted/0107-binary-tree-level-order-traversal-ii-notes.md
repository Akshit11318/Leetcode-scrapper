## Binary Tree Level Order Traversal II

**Problem Link:** https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description

**Problem Statement:**
- Input format and constraints: Given a binary tree, return the bottom-up level order traversal of its nodes' values.
- Expected output format: A list of lists, where each inner list represents a level of the tree, and the levels are listed in reverse order.
- Key requirements and edge cases to consider: The input tree can be empty, and the solution should handle this case correctly. The tree can also be highly unbalanced.
- Example test cases with explanations:
    - Example 1: Input: `[3,9,20,null,null,15,7]`, Output: `[[15,7],[9,20],[3]]`
    - Example 2: Input: `[1]`, Output: `[[1]]`
    - Example 3: Input: `[]`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a level order traversal and store the nodes at each level. Then, reverse the order of the levels to get the bottom-up traversal.
- Step-by-step breakdown of the solution:
    1. Create a queue to hold the nodes at each level.
    2. Enqueue the root node and start a loop that continues until the queue is empty.
    3. In each iteration of the loop, dequeue all nodes at the current level and enqueue their children.
    4. Store the values of the nodes at each level in a separate list.
    5. After the loop, reverse the order of the lists to get the bottom-up traversal.
- Why this approach comes to mind first: It is a straightforward application of the level order traversal algorithm, with an additional step to reverse the order of the levels.

```cpp
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> levelValues;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                levelValues.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(levelValues);
        }
        
        reverse(result.begin(), result.end());
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, since in the worst case (a complete binary tree), the queue will hold $n/2$ nodes at the last level.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear because we need to store all nodes at the last level in the queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal, with a time complexity of $O(n)$ and a space complexity of $O(n)$. However, we can make a small improvement by using a more efficient data structure to store the levels.
- Detailed breakdown of the approach:
    1. Use a `deque` instead of a `vector` to store the levels, since we need to insert at the beginning of the `deque` in each iteration.
    2. Use a `queue` to perform the level order traversal.
- Proof of optimality: The time complexity of $O(n)$ is optimal because we must visit each node at least once. The space complexity of $O(n)$ is also optimal because we need to store all nodes at the last level.
- Why further optimization is impossible: We cannot reduce the time complexity below $O(n)$ because we must visit each node at least once. We cannot reduce the space complexity below $O(n)$ because we need to store all nodes at the last level.

```cpp
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> levelValues;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                levelValues.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.insert(result.begin(), levelValues);
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$, since in the worst case (a complete binary tree), the queue will hold $n/2$ nodes at the last level.
> - **Optimality proof:** The time complexity is optimal because we must visit each node at least once. The space complexity is optimal because we need to store all nodes at the last level.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level order traversal, queue data structure.
- Problem-solving patterns identified: Using a queue to perform a level order traversal, storing the levels in a separate data structure.
- Optimization techniques learned: Using a `deque` instead of a `vector` to store the levels.
- Similar problems to practice: Other tree traversal problems, such as in-order traversal or post-order traversal.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for an empty tree, not handling the case where the tree has only one node.
- Edge cases to watch for: An empty tree, a tree with only one node, a tree with a large number of nodes.
- Performance pitfalls: Using a data structure that is not efficient for the problem, such as using a `vector` instead of a `deque` to store the levels.
- Testing considerations: Test the solution with different types of trees, including empty trees, trees with only one node, and trees with a large number of nodes.