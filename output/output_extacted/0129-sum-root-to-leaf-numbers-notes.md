## Sum Root to Leaf Numbers
**Problem Link:** https://leetcode.com/problems/sum-root-to-leaf-numbers/description

**Problem Statement:**
- Input: The root of a binary tree where each node contains a digit from 0 to 9.
- Constraints: The number of nodes in the tree is in the range [1, 1000].
- Expected Output: The sum of all numbers that can be formed by traversing from the root to a leaf.
- Key Requirements: The tree may contain nodes with values from 0 to 9, and each path from the root to a leaf represents a number.
- Example Test Cases:
  - Input: root = [1,2,3], Output: 25 (Explanation: 12 + 13 = 25)
  - Input: root = [4,9,0,5,1], Output: 1026 (Explanation: 49 + 401 + 490 + 410 + 425 = 1026)

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves traversing the tree and calculating the sum of all paths from the root to each leaf node.
- This can be achieved by using a depth-first search (DFS) approach, where we recursively explore each path and calculate the sum.
- However, this approach may not be efficient for large trees due to its recursive nature.

```cpp
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
    
    int dfs(TreeNode* node, int sum) {
        if (!node) return 0;
        sum = sum * 10 + node->val;
        if (!node->left && !node->right) return sum;
        return dfs(node->left, sum) + dfs(node->right, sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is proportional to the height of the tree due to the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is similar to the brute force approach, as it also uses a DFS traversal to calculate the sum of all paths.
- However, we can optimize the code by handling the base case where the node is null and the recursive case where the node is a leaf node.
- This approach is optimal because it has a linear time complexity and uses a minimal amount of extra space.

```cpp
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
    
    int dfs(TreeNode* node, int sum) {
        if (!node) return 0;
        sum = sum * 10 + node->val;
        if (!node->left && !node->right) return sum;
        return dfs(node->left, sum) + dfs(node->right, sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree.
> - **Optimality proof:** This approach is optimal because it visits each node once and uses a minimal amount of extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, recursive functions.
- Problem-solving patterns identified: using DFS to calculate the sum of all paths in a tree.
- Optimization techniques learned: handling base cases, minimizing extra space usage.
- Similar problems to practice: `Path Sum`, `Path Sum II`.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle the base case, using excessive extra space.
- Edge cases to watch for: empty trees, trees with a single node.
- Performance pitfalls: using inefficient traversal methods, not optimizing the recursive function.
- Testing considerations: testing with different tree structures, edge cases, and large inputs.