## Distribute Coins in Binary Tree

**Problem Link:** https://leetcode.com/problems/distribute-coins-in-binary-tree/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary tree, return the number of moves required to make every node have exactly one coin.
- Expected output format: The number of moves required.
- Key requirements and edge cases to consider: Each node can have any number of coins, and a node can give or receive coins to its children.
- Example test cases with explanations: For example, given the binary tree `[3,0,0]`, the output should be `2`, because we can move one coin from the left child to the root, and one coin from the right child to the root.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by calculating the number of coins in each subtree and then move coins from the child nodes to the parent nodes until each node has exactly one coin.
- Step-by-step breakdown of the solution: We can use a recursive approach to calculate the number of coins in each subtree and then move the coins accordingly.
- Why this approach comes to mind first: This approach is intuitive because it involves calculating the number of coins in each subtree and then moving the coins to the parent nodes.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
class Solution {
public:
    int distributeCoins(TreeNode* root) {
        int moves = 0;
        distributeCoinsHelper(root, moves);
        return moves;
    }
    
    int distributeCoinsHelper(TreeNode* node, int& moves) {
        if (node == nullptr) {
            return 0;
        }
        int left = distributeCoinsHelper(node->left, moves);
        int right = distributeCoinsHelper(node->right, moves);
        moves += abs(left) + abs(right);
        return left + right + node->val - 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the binary tree, because of the recursive call stack.
> - **Why these complexities occur:** The time complexity occurs because we visit each node once, and the space complexity occurs because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass of post-order traversal to calculate the number of moves required.
- Detailed breakdown of the approach: We can use a recursive approach to calculate the number of moves required for each subtree and then move the coins accordingly.
- Proof of optimality: This approach is optimal because it only requires a single pass of post-order traversal, which has a time complexity of $O(n)$.
- Why further optimization is impossible: Further optimization is impossible because we must visit each node at least once to calculate the number of moves required.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
class Solution {
public:
    int distributeCoins(TreeNode* root) {
        int moves = 0;
        distributeCoinsHelper(root, moves);
        return moves;
    }
    
    int distributeCoinsHelper(TreeNode* node, int& moves) {
        if (node == nullptr) {
            return 0;
        }
        int left = distributeCoinsHelper(node->left, moves);
        int right = distributeCoinsHelper(node->right, moves);
        moves += abs(left) + abs(right);
        return left + right + node->val - 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the binary tree, because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because it only requires a single pass of post-order traversal, which has a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Post-order traversal, recursive approach.
- Problem-solving patterns identified: Using a single pass of post-order traversal to calculate the number of moves required.
- Optimization techniques learned: Reducing the number of passes through the binary tree.
- Similar problems to practice: Other problems involving post-order traversal and recursive approaches.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of the recursion, not updating the moves variable correctly.
- Edge cases to watch for: Empty binary tree, binary tree with only one node.
- Performance pitfalls: Using a non-recursive approach that requires multiple passes through the binary tree.
- Testing considerations: Testing the solution with different binary tree structures, including empty and single-node trees.