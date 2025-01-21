## Check if a String is a Valid Sequence from Root to Leaves Path in a Binary Tree
**Problem Link:** https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/description

**Problem Statement:**
- Input format: A binary tree `root` and a string `sequence`.
- Constraints: The number of nodes in the tree is in the range `[1, 100]`, and the length of `sequence` is in the range `[1, 100]`.
- Expected output format: A boolean indicating whether `sequence` is a valid sequence from root to leaves path in the binary tree.
- Key requirements and edge cases to consider:
  - The binary tree can be empty.
  - The `sequence` can be longer than the number of nodes in the tree.
  - The `sequence` can be shorter than the number of nodes in the tree.
- Example test cases with explanations:
  - If the tree is `[0,1,0,0,1,0,null,null,1,0,0]` and the `sequence` is `"110"`, return `true`.
  - If the tree is `[0,1,0,0,1,0,null,null,1,0,0]` and the `sequence` is `"1100"`, return `false`.

### Brute Force Approach
**Explanation:**
- Initial thought process: To check if a string is a valid sequence from root to leaves path in a binary tree, we can perform a depth-first search (DFS) traversal of the tree and compare the node values with the characters in the sequence.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes a node and the current index in the sequence as parameters.
  2. If the node is `null`, return whether the current index is equal to the length of the sequence.
  3. If the current index is greater than or equal to the length of the sequence, return `false`.
  4. If the node's value is not equal to the character at the current index in the sequence, return `false`.
  5. Recursively call the function for the left and right child nodes, incrementing the current index by 1.

```cpp
class Solution {
public:
    bool isValidSequence(TreeNode* root, string sequence) {
        return dfs(root, sequence, 0);
    }
    
    bool dfs(TreeNode* node, string& sequence, int index) {
        if (node == nullptr) {
            return index == sequence.length();
        }
        if (index >= sequence.length() || node->val != sequence[index]) {
            return false;
        }
        return dfs(node->left, sequence, index + 1) || dfs(node->right, sequence, index + 1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of nodes in the tree. This is because in the worst case, we are performing two recursive calls for each node.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity due to the recursive calls, and the space complexity is linear due to the recursive call stack.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The brute force approach can be optimized by returning as soon as we find a mismatch between the node values and the characters in the sequence.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes a node and the current index in the sequence as parameters.
  2. If the node is `null`, return whether the current index is equal to the length of the sequence.
  3. If the current index is greater than or equal to the length of the sequence, return `false`.
  4. If the node's value is not equal to the character at the current index in the sequence, return `false`.
  5. If the node is a leaf node, return whether the current index is equal to the length of the sequence minus 1.
  6. Recursively call the function for the left and right child nodes, incrementing the current index by 1.

```cpp
class Solution {
public:
    bool isValidSequence(TreeNode* root, string sequence) {
        return dfs(root, sequence, 0);
    }
    
    bool dfs(TreeNode* node, string& sequence, int index) {
        if (node == nullptr) {
            return index == sequence.length();
        }
        if (index >= sequence.length() || node->val != sequence[index]) {
            return false;
        }
        if (node->left == nullptr && node->right == nullptr) {
            return index == sequence.length() - 1;
        }
        return dfs(node->left, sequence, index + 1) || dfs(node->right, sequence, index + 1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because in the worst case, we are visiting each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the recursive call stack.
> - **Optimality proof:** The optimal approach has a linear time complexity because we are visiting each node once and returning as soon as we find a mismatch.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) traversal of a binary tree.
- Problem-solving patterns identified: Using recursion to traverse a tree and compare node values with a sequence.
- Optimization techniques learned: Returning as soon as a mismatch is found to reduce the number of recursive calls.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for `null` nodes before accessing their values.
- Edge cases to watch for: Handling sequences that are longer or shorter than the number of nodes in the tree.
- Performance pitfalls: Using an exponential time complexity approach when a linear time complexity approach is possible.
- Testing considerations: Testing the function with different tree structures and sequences to ensure it handles all edge cases correctly.