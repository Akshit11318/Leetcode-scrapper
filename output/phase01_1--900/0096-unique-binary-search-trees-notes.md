## Unique Binary Search Trees

**Problem Link:** https://leetcode.com/problems/unique-binary-search-trees/description

**Problem Statement:**
- Input: An integer `n`, which represents the number of nodes in a binary search tree.
- Constraints: `1 <= n <= 19`.
- Expected Output: The number of unique binary search trees that can be formed with `n` nodes.
- Key Requirements: Each node in the binary search tree must have a unique value, and the left subtree of a node must contain only values less than the node's value, while the right subtree must contain only values greater than the node's value.
- Example Test Cases:
  - Input: `n = 3`
  - Output: `5`
  - Explanation: There are five unique binary search trees that can be formed with three nodes.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible binary trees and then filtering out those that do not satisfy the binary search tree property.
- Step-by-step breakdown:
  1. Generate all possible binary trees with `n` nodes.
  2. For each binary tree, check if it satisfies the binary search tree property.
  3. Count the number of binary trees that satisfy the property.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible solutions and then filtering out the invalid ones.

```cpp
class Solution {
public:
    int numTrees(int n) {
        // Generate all possible binary trees
        vector<TreeNode*> trees = generateTrees(n);
        
        // Count the number of unique binary search trees
        int count = 0;
        for (TreeNode* tree : trees) {
            if (isBST(tree)) {
                count++;
            }
        }
        
        return count;
    }
    
    // Function to generate all possible binary trees
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) {
            return {nullptr};
        }
        
        vector<TreeNode*> trees;
        for (int i = 1; i <= n; i++) {
            vector<TreeNode*> leftTrees = generateTrees(i - 1);
            vector<TreeNode*> rightTrees = generateTrees(n - i);
            
            for (TreeNode* left : leftTrees) {
                for (TreeNode* right : rightTrees) {
                    TreeNode* root = new TreeNode(i);
                    root->left = left;
                    root->right = right;
                    trees.push_back(root);
                }
            }
        }
        
        return trees;
    }
    
    // Function to check if a binary tree is a binary search tree
    bool isBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        
        if (root->left != nullptr && root->left->val >= root->val) {
            return false;
        }
        
        if (root->right != nullptr && root->right->val <= root->val) {
            return false;
        }
        
        return isBST(root->left) && isBST(root->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of nodes. This is because we generate all possible binary trees, which has a time complexity of $O(2^n)$.
> - **Space Complexity:** $O(2^n)$, where $n$ is the number of nodes. This is because we store all possible binary trees in memory.
> - **Why these complexities occur:** The brute force approach involves generating all possible binary trees and then filtering out the invalid ones, which results in a high time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that the number of unique binary search trees with `n` nodes can be calculated using dynamic programming.
- Detailed breakdown:
  1. Create a dynamic programming table `dp` of size `n + 1`, where `dp[i]` represents the number of unique binary search trees with `i` nodes.
  2. Initialize `dp[0] = 1` and `dp[1] = 1`, since there is only one way to construct a binary search tree with 0 or 1 nodes.
  3. For each `i` from 2 to `n`, calculate `dp[i]` by summing up the number of unique binary search trees with `j` nodes in the left subtree and `i - j - 1` nodes in the right subtree, for all `j` from 0 to `i - 1`.
- Proof of optimality: The dynamic programming approach ensures that we calculate the number of unique binary search trees with `n` nodes in a bottom-up manner, avoiding the need to generate all possible binary trees.

```cpp
class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                dp[i] += dp[j] * dp[i - j - 1];
            }
        }
        
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes. This is because we use a nested loop to calculate the number of unique binary search trees with `n` nodes.
> - **Space Complexity:** $O(n)$, where $n` is the number of nodes. This is because we use a dynamic programming table of size `n + 1` to store the number of unique binary search trees with `i` nodes.
> - **Optimality proof:** The dynamic programming approach ensures that we calculate the number of unique binary search trees with `n` nodes in a bottom-up manner, avoiding the need to generate all possible binary trees. This results in a significant reduction in time and space complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the use of dynamic programming to solve a combinatorial problem.
- The key insight is to recognize that the number of unique binary search trees with `n` nodes can be calculated using a bottom-up approach.
- The dynamic programming approach avoids the need to generate all possible binary trees, resulting in a significant reduction in time and space complexity.

**Mistakes to Avoid:**
- Failing to recognize the dynamic programming pattern in the problem.
- Attempting to generate all possible binary trees, which results in a high time and space complexity.
- Not initializing the dynamic programming table correctly, which can lead to incorrect results.

Note: The problem can also be solved using the `Catalan number` formula, which is given by $C_n = \frac{1}{n+1} \cdot \binom{2n}{n}$. However, the dynamic programming approach is more intuitive and easier to understand.