## Maximum Width of Binary Tree

**Problem Link:** https://leetcode.com/problems/maximum-width-of-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [1, 2000].
- Expected Output: The maximum width of the binary tree.
- Key Requirements:
  - The width of a binary tree is the maximum width at any level.
  - The width of a level is the number of nodes in that level.
- Edge Cases:
  - An empty tree (not applicable due to the constraints).
  - A tree with a single node.

**Example Test Cases:**
- For the binary tree: 
        1
       / \
      3   2
     / \
    5   3
   / \
  9   4
- The maximum width is 4 (at the level of nodes 9, 4, 3, 5).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a level-order traversal of the binary tree and at each level, count the number of nodes. The maximum count encountered during the traversal would be the maximum width.
- Step-by-step breakdown:
  1. Initialize a queue with the root node and its level (0).
  2. Initialize variables to keep track of the maximum width and the current level's node count.
  3. Perform a level-order traversal:
     - For each node, check if it's at a new level. If so, update the current level's count to 1; otherwise, increment the count.
     - Update the maximum width if the current level's count exceeds it.
     - Add the node's children to the queue with their respective levels.
  4. Return the maximum width found.

```cpp
// Brute Force Approach
int widthOfBinaryTree(TreeNode* root) {
    if (!root) return 0;
    int maxWidth = 0;
    queue<pair<TreeNode*, int>> q;
    q.push({root, 0});
    while (!q.empty()) {
        int levelSize = q.size();
        int levelMin = q.front().second;
        int levelMax = q.front().second;
        for (int i = 0; i < levelSize; ++i) {
            auto [node, idx] = q.front(); q.pop();
            levelMax = max(levelMax, idx);
            if (node->left) q.push({node->left, 2 * idx + 1});
            if (node->right) q.push({node->right, 2 * idx + 2});
        }
        maxWidth = max(maxWidth, levelMax - levelMin + 1);
    }
    return maxWidth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. Each node is visited once.
> - **Space Complexity:** $O(N)$, as in the worst case, the queue will store all nodes at the last level, which can be $N/2$ nodes for a complete binary tree.
> - **Why these complexities occur:** The brute force approach involves visiting each node once, hence the linear time complexity. The space complexity is due to the queue used for level-order traversal.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of just keeping track of the count of nodes at each level, we can also keep track of the minimum and maximum indices at each level. This allows us to calculate the width of each level more accurately.
- Detailed breakdown:
  1. Perform a level-order traversal using a queue, where each node is associated with its index in the level (starting from 0 for the root).
  2. For each level, keep track of the minimum and maximum indices encountered.
  3. Calculate the width of the current level as the difference between the maximum and minimum indices plus one.
  4. Update the maximum width if the current level's width is greater.

```cpp
// Optimal Approach
int widthOfBinaryTree(TreeNode* root) {
    if (!root) return 0;
    int maxWidth = 0;
    queue<pair<TreeNode*, long long>> q;
    q.push({root, 0});
    while (!q.empty()) {
        int levelSize = q.size();
        long long levelMin = LLONG_MAX, levelMax = LLONG_MIN;
        for (int i = 0; i < levelSize; ++i) {
            auto [node, idx] = q.front(); q.pop();
            levelMin = min(levelMin, idx);
            levelMax = max(levelMax, idx);
            if (node->left) q.push({node->left, 2 * idx + 1});
            if (node->right) q.push({node->right, 2 * idx + 2});
        }
        maxWidth = max(maxWidth, (int)(levelMax - levelMin + 1));
    }
    return maxWidth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. Each node is visited once.
> - **Space Complexity:** $O(N)$, as in the worst case, the queue will store all nodes at the last level.
> - **Optimality proof:** This approach is optimal because it visits each node exactly once and calculates the width of each level in a single pass, making it the most efficient way to solve the problem.

---

### Final Notes

**Learning Points:**
- The importance of level-order traversal in tree problems.
- How to calculate the width of a binary tree by tracking the minimum and maximum indices at each level.
- The use of a queue to efficiently perform level-order traversal.

**Mistakes to Avoid:**
- Not considering the indices of nodes at each level, which can lead to incorrect width calculations.
- Not handling edge cases, such as an empty tree or a tree with a single node.
- Not optimizing the solution to avoid unnecessary computations.