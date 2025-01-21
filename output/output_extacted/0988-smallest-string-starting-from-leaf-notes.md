## Smallest String Starting From Leaf
**Problem Link:** https://leetcode.com/problems/smallest-string-starting-from-leaf/description

**Problem Statement:**
- Input: A binary tree where each node has a unique `val` between 0 and 25 representing the letters 'a' to 'z'.
- Constraints: The number of nodes in the tree is between 1 and 8500.
- Expected output: The lexicographically smallest string that starts at a leaf and ends at the root.
- Key requirements: The string should be constructed by concatenating the node values in the path from a leaf to the root, and the lexicographically smallest string should be returned.
- Example test cases:
  - Input: `[0,1,2,3,4,3,4]`
    - Output: `"dba"`
  - Input: `[25,1,3,1,3,0,2]`
    - Output: `"adz"`
  - Input: `[2,2,1,null,1,null,0,null,0]`
    - Output: `"abc"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Traverse the tree using a depth-first search (DFS) approach, exploring all possible paths from each leaf node to the root.
- Step-by-step breakdown:
  1. Define a recursive function to perform DFS.
  2. In each recursive call, append the current node's value to the path.
  3. If the current node is a leaf, construct the string by concatenating the node values in the path.
  4. Compare the constructed string with the current smallest string and update it if necessary.
- Why this approach comes to mind first: It's a straightforward way to explore all possible paths and find the lexicographically smallest string.

```cpp
class Solution {
public:
    string smallestFromLeaf(TreeNode* root) {
        string smallest = "";
        string path = "";
        dfs(root, path, smallest);
        return smallest;
    }
    
    void dfs(TreeNode* node, string& path, string& smallest) {
        if (!node) return;
        path += (char)('a' + node->val);
        if (!node->left && !node->right) {
            string curr = path;
            reverse(curr.begin(), curr.end());
            if (smallest.empty() || curr < smallest) {
                smallest = curr;
            }
        }
        dfs(node->left, path, smallest);
        dfs(node->right, path, smallest);
        path.pop_back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of nodes in the tree, because in the worst case, we might need to explore all possible paths, and each path can have up to $n$ nodes.
> - **Space Complexity:** $O(n)$, for the recursion stack and the path string.
> - **Why these complexities occur:** The brute force approach explores all possible paths, leading to exponential time complexity. The space complexity is due to the recursion stack and the path string.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of exploring all possible paths and constructing the string at each leaf node, we can construct the string as we backtrack from the leaf node to the root.
- Detailed breakdown:
  1. Perform a DFS traversal of the tree.
  2. At each node, append the current node's value to the path.
  3. If the current node is a leaf, compare the constructed path with the current smallest path and update it if necessary.
  4. Backtrack by removing the last node's value from the path.
- Proof of optimality: This approach ensures that we explore all possible paths and find the lexicographically smallest string in a single pass.

```cpp
class Solution {
public:
    string smallestFromLeaf(TreeNode* root) {
        string smallest = "~";
        string path = "";
        dfs(root, path, smallest);
        return smallest;
    }
    
    void dfs(TreeNode* node, string& path, string& smallest) {
        if (!node) return;
        path += (char)('a' + node->val);
        if (!node->left && !node->right) {
            if (path < smallest) {
                smallest = path;
            }
        } else {
            dfs(node->left, path, smallest);
            dfs(node->right, path, smallest);
        }
        path.pop_back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, for the recursion stack and the path string.
> - **Optimality proof:** This approach ensures that we explore all possible paths and find the lexicographically smallest string in a single pass, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) and backtracking.
- Problem-solving patterns identified: Exploring all possible paths and finding the lexicographically smallest string.
- Optimization techniques learned: Constructing the string as we backtrack from the leaf node to the root.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly or not updating the smallest string correctly.
- Edge cases to watch for: Empty tree or tree with a single node.
- Performance pitfalls: Exploring all possible paths without optimizing the search.
- Testing considerations: Testing the solution with different tree structures and node values.