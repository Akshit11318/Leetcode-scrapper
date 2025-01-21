## Flip Binary Tree To Match Preorder Traversal
**Problem Link:** https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary tree and an array `voyage` which consists of node values in the **preorder** traversal of the tree, return `true` if the tree can be flipped to match `voyage`, otherwise return `false`. 
- Expected output format: A boolean indicating whether the tree can be flipped to match the preorder traversal.
- Key requirements and edge cases to consider: The tree can be flipped at any node. The tree is not guaranteed to be a binary search tree.
- Example test cases with explanations: 
    - Example 1: 
        - Input: `root = [1,2], voyage = [1,2]`
        - Output: `true`
    - Example 2: 
        - Input: `root = [1,2], voyage = [1,3]`
        - Output: `false`
    - Example 3: 
        - Input: `root = [1,2], voyage = [1]`
        - Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible flip of the binary tree and verifying if the preorder traversal matches the given `voyage`.
- Step-by-step breakdown of the solution:
    1. Generate all possible flips of the binary tree.
    2. For each flipped tree, perform a preorder traversal.
    3. Compare the preorder traversal with the given `voyage`.
    4. If a match is found, return `true`. If no match is found after checking all flips, return `false`.
- Why this approach comes to mind first: This approach is straightforward and involves systematically checking all possibilities.

```cpp
class Solution {
public:
    bool flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        // Base case: if the tree is empty
        if (!root) return true;
        
        // If the current node's value does not match the next value in voyage
        if (root->val != voyage[0]) return false;
        
        // Remove the current node's value from voyage
        voyage.erase(voyage.begin());
        
        // Recursively check the left and right subtrees
        return flipMatchVoyage(root->left, voyage) && flipMatchVoyage(root->right, voyage);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$ due to the recursive call stack and the modification of the `voyage` vector.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node in the tree. The space complexity is also linear due to the recursive call stack and the modification of the `voyage` vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible flips of the binary tree, we can determine whether a flip is needed at each node based on the preorder traversal.
- Detailed breakdown of the approach:
    1. Initialize an index to keep track of the current position in the `voyage`.
    2. Recursively traverse the tree, checking if the current node's value matches the next value in `voyage`.
    3. If the current node's value matches, increment the index and continue the traversal.
    4. If the current node's value does not match, return `false`.
    5. If the traversal completes without finding a mismatch, return `true`.
- Proof of optimality: This approach is optimal because it only visits each node once and performs a constant amount of work for each node.

```cpp
class Solution {
public:
    bool flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        int index = 0;
        return flipMatchVoyageHelper(root, voyage, index);
    }
    
    bool flipMatchVoyageHelper(TreeNode* node, vector<int>& voyage, int& index) {
        if (!node) return true;
        
        if (node->val != voyage[index++]) return false;
        
        if (node->left && node->left->val != voyage[index]) {
            swap(node->left, node->right);
        }
        
        return flipMatchVoyageHelper(node->left, voyage, index) && flipMatchVoyageHelper(node->right, voyage, index);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$ due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it only visits each node once and performs a constant amount of work for each node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, preorder traversal, and tree manipulation.
- Problem-solving patterns identified: Using indices to keep track of positions in arrays or vectors.
- Optimization techniques learned: Avoiding unnecessary computations by only visiting each node once.
- Similar problems to practice: Other tree traversal problems, such as inorder and postorder traversal.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null nodes before accessing their values.
- Edge cases to watch for: Empty trees, trees with a single node, and trees with duplicate values.
- Performance pitfalls: Using inefficient algorithms or data structures, such as generating all possible flips of the tree.
- Testing considerations: Test the solution with different types of trees, including empty trees, trees with a single node, and trees with multiple nodes.