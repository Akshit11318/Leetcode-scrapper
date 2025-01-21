## Binary Tree Longest Consecutive Sequence II
**Problem Link:** https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description

**Problem Statement:**
- Input: The root of a binary tree where each node has a unique integer value.
- Constraints: The number of nodes in the tree is in the range $[1, 2 \times 10^5]$.
- Expected Output: The length of the longest consecutive sequence in the binary tree.
- Key Requirements:
  - The sequence can start and end at any node.
  - All nodes in the sequence must have consecutive integer values.
- Edge Cases:
  - Empty tree (though not applicable here due to the constraint of having at least one node).
  - Single-node tree.
  - Tree with multiple nodes but no consecutive sequences.

**Example Test Cases:**
- For a tree with nodes valued 1, 3, and 2, where 1 is the root, 3 is the left child, and 2 is the right child, the longest sequence is 3 (1 -> 2 -> 3 or 3 -> 2 -> 1).
- For a tree with nodes valued 4, 3, 5, where 4 is the root, 3 is the left child, and 5 is the right child, the longest sequence is 2 (4 -> 3 or 4 -> 5).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible sequence of nodes to see if they form a consecutive sequence.
- This approach involves generating all possible paths from the root to every other node, then checking each path and its reversals to see if they represent a consecutive sequence.
- This comes to mind first because it ensures we consider all possibilities, but it's highly inefficient.

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void traverse(TreeNode* node, vector<int>& path, vector<vector<int>>& allPaths) {
    if (!node) return;
    path.push_back(node->val);
    if (!node->left && !node->right) {
        allPaths.push_back(path);
    } else {
        traverse(node->left, path, allPaths);
        traverse(node->right, path, allPaths);
    }
    path.pop_back();
}

bool isConsecutive(vector<int>& seq) {
    sort(seq.begin(), seq.end());
    for (int i = 0; i < seq.size() - 1; ++i) {
        if (seq[i + 1] - seq[i] != 1) return false;
    }
    return true;
}

int longestConsecutive(TreeNode* root) {
    if (!root) return 0;
    vector<vector<int>> allPaths;
    vector<int> path;
    traverse(root, path, allPaths);
    int maxLen = 0;
    for (auto& path : allPaths) {
        if (isConsecutive(path)) {
            maxLen = max(maxLen, (int)path.size());
        }
        // Also check the reverse path
        reverse(path.begin(), path.end());
        if (isConsecutive(path)) {
            maxLen = max(maxLen, (int)path.size());
        }
        reverse(path.begin(), path.end()); // Restore original order
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot H \cdot log(H))$, where $N$ is the number of nodes and $H$ is the height of the tree. The $log(H)$ factor comes from sorting each path.
> - **Space Complexity:** $O(N \cdot H)$ for storing all paths.
> - **Why these complexities occur:** The brute force approach generates all paths, sorts them, and checks for consecutiveness, leading to high time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a depth-first search (DFS) approach but focus on sequences that are increasing or decreasing by 1, rather than generating all paths.
- We keep track of the longest increasing and decreasing sequences ending at each node.
- This approach is optimal because it avoids unnecessary path generation and sorting.

```cpp
int longestConsecutive(TreeNode* root) {
    int maxLen = 0;
    dfs(root, maxLen);
    return maxLen;
}

void dfs(TreeNode* node, int& maxLen) {
    if (!node) return;
    int inc = 1, dec = 1; // Lengths of increasing and decreasing sequences
    if (node->left) {
        dfs(node->left, maxLen);
        if (node->left->val == node->val + 1) inc = node->left->inc + 1;
        if (node->left->val == node->val - 1) dec = node->left->dec + 1;
    }
    if (node->right) {
        dfs(node->right, maxLen);
        if (node->right->val == node->val + 1) inc = max(inc, node->right->inc + 1);
        if (node->right->val == node->val - 1) dec = max(dec, node->right->dec + 1);
    }
    node->inc = inc;
    node->dec = dec;
    maxLen = max(maxLen, inc);
    maxLen = max(maxLen, dec);
    maxLen = max(maxLen, inc + dec - 1); // For sequences that go through the current node
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes, since we visit each node once.
> - **Space Complexity:** $O(H)$ for the recursion stack, where $H$ is the height of the tree.
> - **Optimality proof:** This approach is optimal because it visits each node exactly once and keeps track of the necessary information to compute the longest consecutive sequence, avoiding unnecessary work.

---

### Final Notes

**Learning Points:**
- The importance of identifying the key characteristics of the problem (consecutive sequences).
- How to apply DFS to solve problems involving tree traversals and sequence identification.
- The value of optimizing the solution by focusing on the essential aspects of the problem.

**Mistakes to Avoid:**
- Generating all possible paths without considering the specific requirements of the problem.
- Not optimizing the solution for the given constraints and requirements.
- Failing to consider all edge cases and scenarios.