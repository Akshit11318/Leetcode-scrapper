## House Robber III

**Problem Link:** [https://leetcode.com/problems/house-robber-iii/description](https://leetcode.com/problems/house-robber-iii/description)

**Problem Statement:**
- The input is the root of a binary tree where each node represents a house.
- Each node has a value representing the amount of money that can be stolen from that house.
- The goal is to find the maximum amount of money that can be stolen without stealing from adjacent houses.
- The tree is not guaranteed to be balanced, and the values in the tree are not guaranteed to be non-negative.
- The expected output is the maximum amount of money that can be stolen.

**Key Requirements and Edge Cases:**
- The tree may be empty (i.e., the root is null).
- The tree may have only one node.
- The values in the tree may be negative.
- The tree may have nodes with zero value.

**Example Test Cases:**
- Test case 1: A tree with two nodes, where the root has a value of 3 and the left child has a value of 2. The expected output is 3.
- Test case 2: A tree with three nodes, where the root has a value of 3, the left child has a value of 4, and the right child has a value of 5. The expected output is 7.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to consider all possible combinations of houses to steal from.
- We can use a recursive function to explore all possible combinations.
- For each node, we have two options: steal from the current house or not steal from the current house.
- If we steal from the current house, we cannot steal from its children.
- If we do not steal from the current house, we can steal from its children.

```cpp
class Solution {
public:
    int rob(TreeNode* root) {
        return robHelper(root);
    }
    
    int robHelper(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        
        int steal = node->val;
        if (node->left != nullptr) {
            steal += robHelper(node->left->left) + robHelper(node->left->right);
        }
        if (node->right != nullptr) {
            steal += robHelper(node->right->left) + robHelper(node->right->right);
        }
        
        int notSteal = robHelper(node->left) + robHelper(node->right);
        
        return max(steal, notSteal);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where n is the number of nodes in the tree. This is because we are exploring all possible combinations of houses to steal from.
> - **Space Complexity:** $O(n)$, where n is the number of nodes in the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity because we are exploring all possible combinations of houses to steal from. The space complexity is linear because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a recursive approach with memoization to avoid redundant calculations.
- For each node, we have two options: steal from the current house or not steal from the current house.
- If we steal from the current house, we cannot steal from its children.
- If we do not steal from the current house, we can steal from its children.
- We can use a pair of values to represent the maximum amount of money that can be stolen from a subtree: the first value represents the maximum amount of money that can be stolen if the root of the subtree is stolen, and the second value represents the maximum amount of money that can be stolen if the root of the subtree is not stolen.

```cpp
class Solution {
public:
    int rob(TreeNode* root) {
        return robHelper(root).first;
    }
    
    pair<int, int> robHelper(TreeNode* node) {
        if (node == nullptr) {
            return {0, 0};
        }
        
        pair<int, int> left = robHelper(node->left);
        pair<int, int> right = robHelper(node->right);
        
        int steal = node->val + left.second + right.second;
        int notSteal = max(left.first, left.second) + max(right.first, right.second);
        
        return {steal, notSteal};
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of nodes in the tree. This is because we are visiting each node once.
> - **Space Complexity:** $O(n)$, where n is the number of nodes in the tree. This is because of the recursive call stack.
> - **Optimality proof:** The optimal approach has a linear time complexity because we are visiting each node once and using memoization to avoid redundant calculations. The space complexity is linear because of the recursive call stack.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the use of recursive approaches with memoization to solve tree-related problems.
- The problem requires careful consideration of edge cases, such as an empty tree or a tree with only one node.
- The problem requires careful analysis of the time and space complexities of different approaches.

**Mistakes to Avoid:**
- Not considering edge cases, such as an empty tree or a tree with only one node.
- Not using memoization to avoid redundant calculations in the recursive approach.
- Not carefully analyzing the time and space complexities of different approaches.