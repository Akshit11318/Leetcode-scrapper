## Binary Tree Paths

**Problem Link:** https://leetcode.com/problems/binary-tree-paths/description

**Problem Statement:**
- Input format: The input is a binary tree where each node has a value and two children (left and right).
- Constraints: The binary tree is not empty.
- Expected output format: A list of strings representing all root-to-leaf paths in the binary tree.
- Key requirements and edge cases to consider: The solution should handle trees with varying depths and node values. If a node is a leaf node, its path should be included in the result.
- Example test cases with explanations:
  - Example 1:
    - Input: `root = [1,2,3,null,5]`
    - Output: `["1->2->5","1->3"]`
    - Explanation: The paths from the root node to all leaf nodes are `1->2->5` and `1->3`.
  - Example 2:
    - Input: `root = [1]`
    - Output: `["1"]`
    - Explanation: The path from the root node to the only leaf node is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves traversing the binary tree and checking each node to see if it's a leaf node. If a node is a leaf node, its path from the root is added to the result.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to traverse the binary tree.
  2. In the recursive function, check if the current node is `NULL`. If it is, return.
  3. If the current node is not `NULL`, append its value to the current path.
  4. If the current node is a leaf node, add the current path to the result.
  5. Recursively call the function on the left and right children of the current node.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a natural first step in solving the problem.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        dfs(root, "", result);
        return result;
    }
    
    void dfs(TreeNode* node, string path, vector<string>& result) {
        if (node == nullptr) return;
        
        path += to_string(node->val);
        
        if (node->left == nullptr && node->right == nullptr) {
            result.push_back(path);
        } else {
            path += "->";
            dfs(node->left, path, result);
            path = path.substr(0, path.find("->") + 2);
            dfs(node->right, path, result);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree, since we visit each node once.
> - **Space Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree, since in the worst case, the tree is completely unbalanced, e.g., each node has only left child node, the recursion call would occur N times (the height of the tree), and the space required to store the recursion stack would be $O(N)$.
> - **Why these complexities occur:** The time complexity is $O(N)$ because we visit each node once. The space complexity is $O(N)$ because in the worst case, the recursion call stack can go as high as $N$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of passing the path as a string and then modifying it, we can pass the path as a vector of integers and then convert it to a string when we reach a leaf node. This approach avoids the extra work of string manipulation.
- Detailed breakdown of the approach:
  1. Define a recursive function to traverse the binary tree.
  2. In the recursive function, check if the current node is `NULL`. If it is, return.
  3. If the current node is not `NULL`, append its value to the current path.
  4. If the current node is a leaf node, convert the current path to a string and add it to the result.
  5. Recursively call the function on the left and right children of the current node.
- Proof of optimality: This approach is optimal because it visits each node once and does not perform any unnecessary work.

```cpp
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        vector<int> path;
        dfs(root, path, result);
        return result;
    }
    
    void dfs(TreeNode* node, vector<int>& path, vector<string>& result) {
        if (node == nullptr) return;
        
        path.push_back(node->val);
        
        if (node->left == nullptr && node->right == nullptr) {
            string str;
            for (int i = 0; i < path.size(); i++) {
                str += to_string(path[i]);
                if (i < path.size() - 1) str += "->";
            }
            result.push_back(str);
        } else {
            dfs(node->left, path, result);
            dfs(node->right, path, result);
        }
        
        path.pop_back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree, since we visit each node once.
> - **Space Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree, since in the worst case, the tree is completely unbalanced, e.g., each node has only left child node, the recursion call would occur N times (the height of the tree), and the space required to store the recursion stack would be $O(N)$.
> - **Optimality proof:** This approach is optimal because it visits each node once and does not perform any unnecessary work.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, path construction.
- Problem-solving patterns identified: Using recursion to solve problems that have a recursive structure.
- Optimization techniques learned: Avoiding unnecessary string manipulation.
- Similar problems to practice: Other tree traversal problems, such as finding the maximum depth of a binary tree or finding all paths in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case in a recursive function, not checking for `NULL` nodes.
- Edge cases to watch for: Empty trees, trees with only one node.
- Performance pitfalls: Using inefficient data structures or algorithms, such as using a string to store the path and modifying it repeatedly.
- Testing considerations: Test the function with different types of trees, including empty trees and trees with only one node.