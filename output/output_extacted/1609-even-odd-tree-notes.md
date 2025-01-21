## Even Odd Tree

**Problem Link:** https://leetcode.com/problems/even-odd-tree/description

**Problem Statement:**
- Input format and constraints: The input is a binary tree where each node has a value and two children (left and right). The tree is represented as a `TreeNode` object, where `TreeNode.val` is the value of the node, and `TreeNode.left` and `TreeNode.right` are the left and right children of the node, respectively. The tree has at most `10^4` nodes, and each node's value is between `1` and `10^8`.
- Expected output format: The function should return `true` if the binary tree is an even-odd tree, and `false` otherwise.
- Key requirements and edge cases to consider: The binary tree is an even-odd tree if all nodes at even levels have odd integer values and all nodes at odd levels have even integer values.
- Example test cases with explanations:
    - Example 1: Input: `root = [1,10,4,3,null,7,9]`. Output: `true`. Explanation: The tree is an even-odd tree because all nodes at even levels have odd integer values and all nodes at odd levels have even integer values.
    - Example 2: Input: `root = [5,4,2,3,3,7]`. Output: `false`. Explanation: The tree is not an even-odd tree because the node at level 2 (value 4) is even, but it should be odd.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to traverse the tree level by level, checking if each node's value is odd or even, and if it matches the expected parity based on its level.
- Step-by-step breakdown of the solution:
    1. Initialize a queue with the root node and its level (0).
    2. While the queue is not empty, dequeue a node and its level.
    3. Check if the node's value is odd or even.
    4. If the node's level is even, check if the node's value is odd. If it's not, return `false`.
    5. If the node's level is odd, check if the node's value is even. If it's not, return `false`.
    6. Enqueue the node's children with their levels.
- Why this approach comes to mind first: This approach is straightforward because it directly checks each node's value and level, which are the key factors in determining if the tree is an even-odd tree.

```cpp
class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        if (!root) return true;
        
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            int size = q.size();
            int prevVal = 0;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front().first;
                int level = q.front().second;
                q.pop();
                
                if (level % 2 == 0) { // even level
                    if (node->val % 2 == 0) return false; // value should be odd
                    if (prevVal != 0 && node->val <= prevVal) return false; // value should be strictly increasing
                } else { // odd level
                    if (node->val % 2 != 0) return false; // value should be even
                    if (prevVal != 0 && node->val >= prevVal) return false; // value should be strictly decreasing
                }
                
                prevVal = node->val;
                
                if (node->left) q.push({node->left, level + 1});
                if (node->right) q.push({node->right, level + 1});
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, the queue will contain all nodes at the last level of the tree.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is linear because we store all nodes at the last level in the queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a level-order traversal (BFS) to traverse the tree, which allows us to efficiently check each node's value and level.
- Detailed breakdown of the approach:
    1. Initialize a queue with the root node and its level (0).
    2. While the queue is not empty, dequeue a node and its level.
    3. Check if the node's value is odd or even.
    4. If the node's level is even, check if the node's value is odd. If it's not, return `false`.
    5. If the node's level is odd, check if the node's value is even. If it's not, return `false`.
    6. Enqueue the node's children with their levels.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible time and space complexity for this problem.

```cpp
class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        if (!root) return true;
        
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            int size = q.size();
            int prevVal = 0;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front().first;
                int level = q.front().second;
                q.pop();
                
                if (level % 2 == 0) { // even level
                    if (node->val % 2 == 0) return false; // value should be odd
                    if (prevVal != 0 && node->val <= prevVal) return false; // value should be strictly increasing
                } else { // odd level
                    if (node->val % 2 != 0) return false; // value should be even
                    if (prevVal != 0 && node->val >= prevVal) return false; // value should be strictly decreasing
                }
                
                prevVal = node->val;
                
                if (node->left) q.push({node->left, level + 1});
                if (node->right) q.push({node->right, level + 1});
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, the queue will contain all nodes at the last level of the tree.
> - **Optimality proof:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is linear because we store all nodes at the last level in the queue.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level-order traversal (BFS), queue data structure.
- Problem-solving patterns identified: Checking each node's value and level, using a queue to efficiently traverse the tree.
- Optimization techniques learned: Using a level-order traversal to reduce the time complexity.
- Similar problems to practice: Other problems that involve traversing a tree and checking node values, such as "Symmetric Tree" and "Binary Tree Level Order Traversal".

**Mistakes to Avoid:**
- Common implementation errors: Not checking the node's level correctly, not handling the case where the tree is empty.
- Edge cases to watch for: The tree is empty, the tree has only one node, the tree has multiple levels.
- Performance pitfalls: Using a recursive approach instead of an iterative approach, which can lead to a stack overflow error.
- Testing considerations: Test the function with different types of trees, including empty trees, trees with one node, and trees with multiple levels.