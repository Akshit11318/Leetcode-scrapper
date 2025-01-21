## Path Sum IV
**Problem Link:** https://leetcode.com/problems/path-sum-iv/description

**Problem Statement:**
- Input: A binary tree where each node has a unique value and at most two children (left and right).
- Constraints: The number of nodes in the tree is between 1 and 1000, and each node's value is between 1 and 1000.
- Expected Output: The total number of paths where the sum of the node values equals a given target sum.
- Key Requirements and Edge Cases:
  - The path must start at the root node.
  - Each node can only be used once in a path.
  - The path can be any length, but it must start at the root and end at any node.
- Example Test Cases:
  - Given a binary tree with the root node having a value of 1, and its left child having a value of 2, and its right child having a value of 3, and the target sum being 3, the output should be 2 because there are two paths that sum up to 3: [1, 2] and [1, 3].

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to perform a depth-first search (DFS) on the binary tree, calculating the sum of each path and checking if it equals the target sum.
- We can use recursion to implement the DFS.
- This approach comes to mind first because it is a straightforward way to explore all possible paths in the tree.

```cpp
class Solution {
public:
    int pathSum(vector<vector<int>>& nums) {
        // Create a map to store the tree nodes
        unordered_map<int, TreeNode*> tree;
        for (auto& num : nums) {
            int depth = num[0], pos = num[1], val = num[2];
            tree[depth * 100 + pos] = new TreeNode(val);
        }
        
        // Build the tree
        for (auto& num : nums) {
            int depth = num[0], pos = num[1];
            if (2 * pos - 1 <= 1000 * (depth + 1) - 1) {
                tree[depth * 100 + pos]->left = tree[(depth + 1) * 100 + 2 * pos - 1];
            }
            if (2 * pos <= 1000 * (depth + 1) - 1) {
                tree[depth * 100 + pos]->right = tree[(depth + 1) * 100 + 2 * pos];
            }
        }
        
        // Perform DFS
        int res = 0;
        dfs(tree[101], 0, nums[0][2]);
        return res;
    }
    
    void dfs(TreeNode* node, int sum, int target) {
        if (!node) return;
        sum += node->val;
        if (sum == target) res++;
        dfs(node->left, sum, target);
        dfs(node->right, sum, target);
    }
};

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot h)$, where $n$ is the number of nodes in the tree and $h$ is the height of the tree. This is because in the worst case, we visit each node and perform a DFS from each node.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we store each node in the `tree` map.
> - **Why these complexities occur:** The time complexity occurs because we perform a DFS from each node, and the space complexity occurs because we store each node in the `tree` map.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a hash map to store the prefix sum of each path and its frequency.
- We can use a DFS to calculate the prefix sum of each path and update the frequency in the hash map.
- This approach is optimal because it avoids recalculating the prefix sum of each path and reduces the time complexity to $O(n)$.

```cpp
class Solution {
public:
    int pathSum(vector<vector<int>>& nums) {
        unordered_map<int, int> sumCount;
        sumCount[0] = 1;
        int res = 0;
        for (auto& num : nums) {
            int depth = num[0], pos = num[1], val = num[2];
            unordered_map<int, int> nextSumCount;
            for (auto& sumCountPair : sumCount) {
                int sum = sumCountPair.first + val;
                nextSumCount[sum]++;
                if (sum == num[2]) res += sumCountPair.second;
            }
            sumCount = nextSumCount;
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node once and update the frequency in the hash map.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we store the prefix sum of each path and its frequency in the hash map.
> - **Optimality proof:** This approach is optimal because it avoids recalculating the prefix sum of each path and reduces the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a hash map to store the prefix sum of each path and its frequency.
- The problem-solving pattern identified is to use a DFS to calculate the prefix sum of each path and update the frequency in the hash map.
- The optimization technique learned is to avoid recalculating the prefix sum of each path and reduce the time complexity to $O(n)$.

**Mistakes to Avoid:**
- A common implementation error is to recalculate the prefix sum of each path, which increases the time complexity to $O(n \cdot h)$.
- An edge case to watch for is when the tree is empty, in which case the function should return 0.
- A performance pitfall is to use a recursive approach without memoization, which can cause a stack overflow for large trees.