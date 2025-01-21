## Minimum Flips in Binary Tree to Get Result
**Problem Link:** https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/description

**Problem Statement:**
- Input: A binary tree where each node has a value of either 0 or 1, and a target binary string.
- Constraints: The binary tree is not empty, and the target string has the same length as the number of nodes in the binary tree.
- Expected Output: The minimum number of flips (i.e., changing a 0 to a 1 or a 1 to a 0) needed to make the binary representation of the tree match the target string.
- Key Requirements: The binary representation of the tree is obtained by performing a pre-order traversal of the tree.
- Example Test Cases:
  - Example 1:
    - Input: root = [1,1,0], target = "101"
    - Output: 1
    - Explanation: Flip the node with value 0 to get the target string "101".
  - Example 2:
    - Input: root = [1,0,1], target = "001"
    - Output: 3
    - Explanation: Flip all three nodes to get the target string "001".

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to consider all possible combinations of flips for the nodes in the binary tree.
- Step-by-step breakdown:
  1. Generate all possible binary strings of the same length as the number of nodes in the tree.
  2. For each binary string, flip the corresponding nodes in the tree to match the string.
  3. Perform a pre-order traversal of the tree to get its binary representation.
  4. Compare the binary representation with the target string and count the number of differences.
  5. Keep track of the minimum number of differences found.
- This approach comes to mind first because it considers all possible scenarios, but it's inefficient due to its exponential time complexity.

```cpp
int minFlips(TreeNode* root, string target) {
    int minFlips = INT_MAX;
    int n = countNodes(root);
    for (int i = 0; i < (1 << n); i++) {
        string binaryString = "";
        for (int j = 0; j < n; j++) {
            binaryString += (i & (1 << j)) ? '1' : '0';
        }
        int flips = 0;
        TreeNode* node = root;
        string treeBinary = preOrderTraversal(node);
        for (int j = 0; j < n; j++) {
            if (treeBinary[j] != binaryString[j]) {
                flips++;
            }
        }
        minFlips = min(minFlips, flips);
    }
    return minFlips;
}

int countNodes(TreeNode* root) {
    if (!root) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}

string preOrderTraversal(TreeNode* root) {
    if (!root) return "";
    string result = "";
    result += root->val + '0';
    result += preOrderTraversal(root->left);
    result += preOrderTraversal(root->right);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of nodes in the tree. This is because we generate all possible binary strings of length $n$ and perform a pre-order traversal for each string.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the binary string and the result of the pre-order traversal.
> - **Why these complexities occur:** The exponential time complexity occurs because we consider all possible binary strings, and the linear space complexity occurs because we need to store the binary string and the result of the pre-order traversal.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a depth-first search (DFS) to traverse the tree and compare the node values with the target string.
- Detailed breakdown:
  1. Perform a DFS traversal of the tree, and for each node, compare its value with the corresponding character in the target string.
  2. If the values are different, increment the flip count.
  3. Return the total flip count after the traversal.
- Proof of optimality: This approach is optimal because it only requires a single pass through the tree, resulting in a linear time complexity.

```cpp
int minFlips(TreeNode* root, string target) {
    int flips = 0;
    dfs(root, target, flips, 0);
    return flips;
}

void dfs(TreeNode* node, string& target, int& flips, int index) {
    if (!node) return;
    if (node->val != (target[index] - '0')) {
        flips++;
    }
    dfs(node->left, target, flips, 2 * index + 1);
    dfs(node->right, target, flips, 2 * index + 2);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we perform a single pass through the tree.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tree, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, binary tree manipulation.
- Problem-solving patterns identified: using DFS to traverse the tree and compare node values with a target string.
- Optimization techniques learned: reducing the time complexity from exponential to linear by using a single pass through the tree.
- Similar problems to practice: other problems involving binary trees and string comparisons.

**Mistakes to Avoid:**
- Common implementation errors: not handling the base case correctly in the recursive DFS function.
- Edge cases to watch for: empty trees, trees with a single node, and trees with multiple nodes.
- Performance pitfalls: using an exponential-time approach instead of a linear-time approach.
- Testing considerations: testing the function with different tree structures and target strings to ensure correctness.