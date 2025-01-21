## Pseudo-Palindromic Paths in a Binary Tree

**Problem Link:** https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description

**Problem Statement:**
- Input: A binary tree where each node has a unique value between `1` and `9`.
- Output: The number of pseudo-palindromic paths in the binary tree. A pseudo-palindromic path is a path from the root to a leaf node that contains at most one node with an odd number of occurrences.
- Key requirements and edge cases to consider:
  - Handling leaf nodes.
  - Counting node values along the path.
  - Checking for pseudo-palindromic properties.
- Example test cases with explanations:
  - Test case 1: A binary tree with a single node.
  - Test case 2: A binary tree with two nodes.
  - Test case 3: A binary tree with multiple levels.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) from the root node and check each path to see if it's pseudo-palindromic.
- Step-by-step breakdown of the solution:
  1. Define a recursive DFS function that traverses the tree and counts the occurrences of each node value.
  2. When a leaf node is reached, check if the path is pseudo-palindromic by counting the number of nodes with an odd number of occurrences.
  3. If the path is pseudo-palindromic, increment the count of pseudo-palindromic paths.
- Why this approach comes to mind first: It's a straightforward way to explore all possible paths in the tree and check their pseudo-palindromic properties.

```cpp
class Solution {
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        int count = 0;
        unordered_map<int, int> freq;
        dfs(root, freq, count);
        return count;
    }

    void dfs(TreeNode* node, unordered_map<int, int>& freq, int& count) {
        if (!node) return;
        freq[node->val]++;
        if (!node->left && !node->right) {
            int oddCount = 0;
            for (auto& pair : freq) {
                if (pair.second % 2 != 0) oddCount++;
            }
            if (oddCount <= 1) count++;
        }
        dfs(node->left, freq, count);
        dfs(node->right, freq, count);
        freq[node->val]--;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot 9)$ where $N$ is the number of nodes in the tree, because in the worst case, we might need to traverse all nodes and update the frequency map for each node.
> - **Space Complexity:** $O(H + 9)$ where $H$ is the height of the tree, because we need to store the recursive call stack and the frequency map.
> - **Why these complexities occur:** The time complexity is due to the recursive DFS traversal and the frequency map updates, while the space complexity is due to the recursive call stack and the frequency map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using a frequency map, we can use a bitmask to keep track of the node values along the path. This allows us to quickly check if a path is pseudo-palindromic.
- Detailed breakdown of the approach:
  1. Define a recursive DFS function that traverses the tree and updates the bitmask.
  2. When a leaf node is reached, check if the path is pseudo-palindromic by counting the number of bits set in the bitmask.
  3. If the path is pseudo-palindromic, increment the count of pseudo-palindromic paths.
- Proof of optimality: This approach has the same time complexity as the brute force approach but uses less space, making it more efficient.

```cpp
class Solution {
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        int count = 0;
        int bitmask = 0;
        dfs(root, bitmask, count);
        return count;
    }

    void dfs(TreeNode* node, int& bitmask, int& count) {
        if (!node) return;
        bitmask ^= (1 << (node->val - 1));
        if (!node->left && !node->right) {
            int oddCount = 0;
            for (int i = 0; i < 9; i++) {
                if ((bitmask >> i) & 1) oddCount++;
            }
            if (oddCount <= 1) count++;
        }
        dfs(node->left, bitmask, count);
        dfs(node->right, bitmask, count);
        bitmask ^= (1 << (node->val - 1));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot 9)$ where $N$ is the number of nodes in the tree, because in the worst case, we might need to traverse all nodes and update the bitmask.
> - **Space Complexity:** $O(H)$ where $H$ is the height of the tree, because we need to store the recursive call stack.
> - **Optimality proof:** This approach is optimal because it uses a bitmask to keep track of the node values along the path, which allows for quick checking of pseudo-palindromic properties and reduces the space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search, bitmasking, and pseudo-palindromic checking.
- Problem-solving patterns identified: Using bitmasks to keep track of node values and counting the number of bits set to check for pseudo-palindromic properties.
- Optimization techniques learned: Reducing space complexity by using a bitmask instead of a frequency map.
- Similar problems to practice: Other problems involving tree traversals and bitmasking.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the bitmask or count correctly.
- Edge cases to watch for: Handling leaf nodes and checking for pseudo-palindromic properties correctly.
- Performance pitfalls: Using a frequency map instead of a bitmask, which can increase space complexity.
- Testing considerations: Testing the solution with different tree structures and node values to ensure correctness.