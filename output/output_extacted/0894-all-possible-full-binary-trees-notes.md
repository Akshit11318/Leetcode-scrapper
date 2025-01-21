## All Possible Full Binary Trees

**Problem Link:** https://leetcode.com/problems/all-possible-full-binary-trees/description

**Problem Statement:**
- Input: An integer `N`, representing the number of nodes.
- Constraints: `1 <= N <= 20`
- Output: A list of all possible full binary trees with `N` nodes.
- Key requirements: Each node in the tree should have either 0 or 2 children.
- Example test cases:
  - For `N = 1`, there's only one possible full binary tree, which is a single node.
  - For `N = 3`, there's one possible full binary tree, which has one root node and two child nodes.
  - For `N = 5`, there are two possible full binary trees.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start with the root node and try to construct all possible full binary trees by recursively adding left and right child nodes.
- Step-by-step breakdown:
  1. Create a recursive function to generate all possible full binary trees.
  2. In each recursive call, try to add left and right child nodes to the current node.
  3. If the total number of nodes exceeds `N`, backtrack and try a different combination.
- Why this approach comes to mind first: It's a straightforward and intuitive way to generate all possible full binary trees.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<TreeNode*> allPossibleFBT(int N) {
        vector<TreeNode*> result;
        if (N % 2 == 0) return result; // Full binary tree must have odd number of nodes
        generateFBT(N, result);
        return result;
    }

    void generateFBT(int N, vector<TreeNode*>& result) {
        if (N == 1) {
            result.push_back(new TreeNode(0));
            return;
        }
        for (int i = 1; i < N; i += 2) {
            vector<TreeNode*> left = allPossibleFBT(i);
            vector<TreeNode*> right = allPossibleFBT(N - i - 1);
            for (auto& l : left) {
                for (auto& r : right) {
                    TreeNode* root = new TreeNode(0);
                    root->left = l;
                    root->right = r;
                    result.push_back(root);
                }
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{N/2})$, because in the worst case, we're generating all possible full binary trees with `N/2` nodes.
> - **Space Complexity:** $O(2^{N/2})$, because we need to store all generated full binary trees.
> - **Why these complexities occur:** The recursive approach and the need to store all generated trees lead to exponential time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use memoization to store the results of subproblems and avoid redundant calculations.
- Detailed breakdown:
  1. Create a recursive function with memoization to generate all possible full binary trees.
  2. Store the results of subproblems in a map to avoid recalculating them.
- Proof of optimality: This approach avoids redundant calculations and has a lower time complexity than the brute force approach.

```cpp
class Solution {
public:
    vector<TreeNode*> allPossibleFBT(int N) {
        if (N % 2 == 0) return {}; // Full binary tree must have odd number of nodes
        unordered_map<int, vector<TreeNode*>> memo;
        return generateFBT(N, memo);
    }

    vector<TreeNode*> generateFBT(int N, unordered_map<int, vector<TreeNode*>>& memo) {
        if (N == 1) {
            return {new TreeNode(0)};
        }
        if (memo.count(N)) {
            return memo[N];
        }
        vector<TreeNode*> result;
        for (int i = 1; i < N; i += 2) {
            vector<TreeNode*> left = generateFBT(i, memo);
            vector<TreeNode*> right = generateFBT(N - i - 1, memo);
            for (auto& l : left) {
                for (auto& r : right) {
                    TreeNode* root = new TreeNode(0);
                    root->left = l;
                    root->right = r;
                    result.push_back(root);
                }
            }
        }
        memo[N] = result;
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{N/2})$, because we're generating all possible full binary trees with `N/2` nodes.
> - **Space Complexity:** $O(2^{N/2})$, because we need to store all generated full binary trees and the memoization map.
> - **Optimality proof:** This approach has the best possible time complexity for generating all possible full binary trees, and the memoization technique avoids redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Recursive functions, memoization, and tree generation.
- Problem-solving patterns: Divide-and-conquer approach and avoiding redundant calculations.
- Optimization techniques: Memoization and storing subproblem results.
- Similar problems to practice: Generating all possible binary trees, full binary trees with specific properties, and other combinatorial problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for base cases, not handling edge cases, and not optimizing recursive functions.
- Edge cases to watch for: Handling cases with `N = 1` and ensuring the generated trees have the correct number of nodes.
- Performance pitfalls: Not using memoization and not avoiding redundant calculations.
- Testing considerations: Testing with different input values, checking the correctness of the generated trees, and ensuring the function handles edge cases correctly.