## Unique Binary Search Trees II
**Problem Link:** https://leetcode.com/problems/unique-binary-search-trees-ii/description

**Problem Statement:**
- Input format: An integer `n` representing the number of nodes in the binary search tree.
- Constraints: `1 <= n <= 8`
- Expected output format: A list of all unique binary search trees that can be constructed from `n` nodes, where each node is labeled from `1` to `n`.
- Key requirements: Each tree must be a valid binary search tree, where the left subtree of a node contains only nodes with values less than the node, and the right subtree contains only nodes with values greater than the node.
- Example test cases:
  - Input: `n = 3`
  - Output: All unique binary search trees that can be constructed from `3` nodes.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by generating all possible binary trees with `n` nodes, then filter out the ones that are not valid binary search trees.
- Step-by-step breakdown of the solution:
  1. Generate all possible binary trees with `n` nodes.
  2. For each tree, check if it is a valid binary search tree by traversing the tree and verifying that each node's value is within the correct range.
  3. If the tree is valid, add it to the list of unique binary search trees.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible solutions and then filtering out the ones that do not meet the criteria.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        return generateTrees(1, n);
    }
    
    vector<TreeNode*> generateTrees(int start, int end) {
        vector<TreeNode*> res;
        if (start > end) {
            res.push_back(NULL);
            return res;
        }
        
        for (int i = start; i <= end; i++) {
            vector<TreeNode*> left = generateTrees(start, i - 1);
            vector<TreeNode*> right = generateTrees(i + 1, end);
            
            for (auto l : left) {
                for (auto r : right) {
                    TreeNode* node = new TreeNode(i);
                    node->left = l;
                    node->right = r;
                    res.push_back(node);
                }
            }
        }
        
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n / n^{3/2})$ (due to the number of possible binary trees with `n` nodes)
> - **Space Complexity:** $O(4^n / n^{3/2})$ (due to the storage of all possible binary trees)
> - **Why these complexities occur:** The time and space complexities are dominated by the number of possible binary trees with `n` nodes, which grows exponentially with `n`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using a recursive approach, where we generate all possible left and right subtrees for each node, and then combine them to form the final trees.
- Detailed breakdown of the approach:
  1. Define a recursive function `generateTrees(start, end)` that generates all possible binary search trees with nodes labeled from `start` to `end`.
  2. If `start > end`, return a list containing `NULL`, which represents an empty tree.
  3. Otherwise, iterate over all possible root nodes from `start` to `end`, and for each root node, recursively generate all possible left and right subtrees.
  4. Combine the left and right subtrees to form the final trees, and add them to the list of unique binary search trees.
- Proof of optimality: This approach is optimal because it generates all possible binary search trees with `n` nodes, and it does so in a way that avoids redundant computation.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        return generateTrees(1, n);
    }
    
    vector<TreeNode*> generateTrees(int start, int end) {
        vector<TreeNode*> res;
        if (start > end) {
            res.push_back(NULL);
            return res;
        }
        
        for (int i = start; i <= end; i++) {
            vector<TreeNode*> left = generateTrees(start, i - 1);
            vector<TreeNode*> right = generateTrees(i + 1, end);
            
            for (auto l : left) {
                for (auto r : right) {
                    TreeNode* node = new TreeNode(i);
                    node->left = l;
                    node->right = r;
                    res.push_back(node);
                }
            }
        }
        
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n / n^{3/2})$ (due to the number of possible binary trees with `n` nodes)
> - **Space Complexity:** $O(4^n / n^{3/2})$ (due to the storage of all possible binary trees)
> - **Optimality proof:** This approach is optimal because it generates all possible binary search trees with `n` nodes, and it does so in a way that avoids redundant computation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive approach, tree generation, and combination of subtrees.
- Problem-solving patterns identified: breaking down the problem into smaller sub-problems, and solving them recursively.
- Optimization techniques learned: avoiding redundant computation by using recursive approach.
- Similar problems to practice: generating all possible binary trees with `n` nodes, generating all possible permutations of a given array.

**Mistakes to Avoid:**
- Common implementation errors: not handling the base case correctly, not initializing the recursive function correctly.
- Edge cases to watch for: handling the case where `n` is `0`, handling the case where `start > end`.
- Performance pitfalls: not optimizing the recursive function to avoid redundant computation.
- Testing considerations: testing the function with different values of `n`, testing the function with edge cases.