## Find Number of Coins to Place in Tree Nodes
**Problem Link:** https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary tree, return the minimum number of coins to place in the tree nodes such that the tree becomes a valid binary search tree (BST).
- Expected output format: The output should be an integer representing the minimum number of coins required.
- Key requirements and edge cases to consider:
  - Each node in the tree has a unique value.
  - The tree may not be a valid BST initially.
  - The coins can only be placed at the nodes.
- Example test cases with explanations:
  - For a tree with nodes having values 2, 3, and 1, the output should be 1 because we can place a coin at the root node with value 2 to make the tree a valid BST.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of placing coins at the nodes and check if the resulting tree is a valid BST.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of placing coins at the nodes.
  2. For each combination, create a copy of the original tree and place the coins accordingly.
  3. Check if the resulting tree is a valid BST by performing an in-order traversal.
  4. If the tree is a valid BST, count the number of coins used and update the minimum count if necessary.
- Why this approach comes to mind first: This approach is straightforward and tries to solve the problem by brute force, but it is inefficient due to the large number of possible combinations.

```cpp
class Solution {
public:
    int minCoins = INT_MAX;
    int minCameraCover(TreeNode* root) {
        dfs(root);
        return minCoins;
    }
    
    int dfs(TreeNode* node) {
        if (!node) return 0;
        
        int left = dfs(node->left);
        int right = dfs(node->right);
        
        if (left == -1 || right == -1) {
            minCoins++;
            return 0;
        }
        
        if (left == 0 && right == 0) return -1;
        
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the tree, because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a depth-first search (DFS) approach to traverse the tree and count the number of coins required to make the tree a valid BST.
- Detailed breakdown of the approach:
  1. Perform a DFS traversal of the tree.
  2. For each node, check if the left and right subtrees are valid BSTs.
  3. If either subtree is not a valid BST, increment the coin count and mark the current node as a coin.
  4. Return the minimum coin count.
- Proof of optimality: This approach is optimal because it visits each node only once and uses a constant amount of space for each recursive call.

```cpp
class Solution {
public:
    int minCoins = 0;
    int minCameraCover(TreeNode* root) {
        dfs(root);
        if (root->val == -1) minCoins++;
        return minCoins;
    }
    
    int dfs(TreeNode* node) {
        if (!node) return 0;
        
        int left = dfs(node->left);
        int right = dfs(node->right);
        
        if (left == -1 || right == -1) {
            minCoins++;
            return 0;
        }
        
        if (left == 0 && right == 0) return -1;
        
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the tree, because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because it visits each node only once and uses a constant amount of space for each recursive call.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, recursive approach.
- Problem-solving patterns identified: Using a recursive approach to solve a tree-related problem.
- Optimization techniques learned: Using a single pass to count the number of coins required.
- Similar problems to practice: Other tree-related problems that require a recursive approach.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null nodes, not handling edge cases.
- Edge cases to watch for: Empty tree, tree with a single node.
- Performance pitfalls: Using an inefficient algorithm, not optimizing the recursive approach.
- Testing considerations: Test the solution with different tree structures and edge cases.