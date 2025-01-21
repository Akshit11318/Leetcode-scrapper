## Verify Preorder Sequence in Binary Search Tree

**Problem Link:** https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description

**Problem Statement:**
- Input format and constraints: Given an array of integers representing a preorder traversal of a binary search tree (BST), verify if the sequence is valid.
- Expected output format: Return `true` if the sequence is valid, `false` otherwise.
- Key requirements and edge cases to consider: 
    - The sequence must adhere to BST properties: for every node, all elements in its left subtree must be less than the node, and all elements in its right subtree must be greater.
    - Handle sequences that could represent an empty tree or a tree with a single node.
- Example test cases with explanations:
    - `[40, 10, 20, 60, 50, 70]` is valid because it can represent a BST where 40 is the root, 10 is the left child of 40, 20 is the right child of 10, and so on.
    - `[40, 10, 20, 60, 50, 70, 8]` is not valid because after 40, 10, and 20, the next element 60 is larger than 20 but the sequence includes 8 which is smaller than 10, violating the BST property.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try to reconstruct the BST from the preorder sequence and then verify if the reconstructed tree satisfies the BST properties.
- Step-by-step breakdown of the solution:
    1. Start with the first element as the root.
    2. Iterate through the rest of the sequence. For each element, compare it with the root and decide whether it should go to the left subtree or the right subtree based on the BST property.
    3. If an element cannot be placed without violating the BST property, return `false`.
- Why this approach comes to mind first: It directly addresses the problem statement by attempting to build a BST and then verify its correctness.

```cpp
#include <iostream>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool verifyPreorder(std::vector<int>& preorder) {
    if (preorder.size() == 0) return true;
    
    TreeNode* root = new TreeNode(preorder[0]);
    std::vector<TreeNode*> nodes;
    nodes.push_back(root);
    
    for (int i = 1; i < preorder.size(); ++i) {
        int val = preorder[i];
        TreeNode* newNode = new TreeNode(val);
        
        bool placed = false;
        for (auto node : nodes) {
            if (val < node->val) {
                if (node->left) {
                    continue;
                } else {
                    node->left = newNode;
                    nodes.push_back(newNode);
                    placed = true;
                    break;
                }
            } else if (val > node->val) {
                if (node->right) {
                    continue;
                } else {
                    node->right = newNode;
                    nodes.push_back(newNode);
                    placed = true;
                    break;
                }
            }
        }
        if (!placed) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the preorder sequence. This is because in the worst case, for each new node, we might have to traverse through all existing nodes to find a place for it.
> - **Space Complexity:** $O(n)$, for storing the nodes of the tree.
> - **Why these complexities occur:** The brute force approach involves potentially checking every node for each new node added, leading to quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a stack to keep track of the nodes that we've seen so far but haven't yet found a larger number to be their right child. We also keep track of the lower bound for the next number in the sequence.
- Detailed breakdown of the approach:
    1. Initialize an empty stack and a lower bound of negative infinity.
    2. Iterate through the preorder sequence. For each number:
        - If the number is less than the top of the stack, it means this number should be the left child of the top of the stack. So, we push this number onto the stack.
        - If the number is greater than the top of the stack but less than the upper bound, it means this number should be the right child of some node in the stack. We update the upper bound for the next number to be the current top of the stack and pop the stack until we find a node that is smaller than the current number or the stack is empty.
        - If the number is greater than or equal to the upper bound, return false because it violates the BST property.
    3. After iterating through the entire sequence, if we haven't returned false, it means the sequence is valid.
- Proof of optimality: This approach ensures that we only need to iterate through the sequence once, resulting in a linear time complexity.

```cpp
bool verifyPreorder(std::vector<int>& preorder) {
    std::vector<int> stack;
    int lower = INT_MIN;
    
    for (int val : preorder) {
        if (val < lower) return false;
        
        while (!stack.empty() && val > stack.back()) {
            lower = stack.back();
            stack.pop_back();
        }
        
        stack.push_back(val);
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the preorder sequence. This is because we make a single pass through the sequence.
> - **Space Complexity:** $O(n)$, for the stack used to keep track of nodes.
> - **Optimality proof:** This approach is optimal because it achieves linear time complexity by only requiring a single pass through the input sequence and using a stack to efficiently manage the nodes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to efficiently manage a sequence of elements and keep track of bounds.
- Problem-solving patterns identified: Iterating through a sequence and using a data structure (like a stack) to keep track of intermediate results.
- Optimization techniques learned: Reducing time complexity from quadratic to linear by using a more efficient data structure and algorithm.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the bounds or not properly updating the stack.
- Edge cases to watch for: Empty sequences, sequences with a single element, and sequences that represent an unbalanced tree.
- Performance pitfalls: Using a naive approach that results in quadratic time complexity.
- Testing considerations: Ensure to test with various sequences, including valid and invalid ones, and edge cases.