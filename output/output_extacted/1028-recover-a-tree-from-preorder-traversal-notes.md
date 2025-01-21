## Recover a Tree from Preorder Traversal
**Problem Link:** https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description

**Problem Statement:**
- Input: A string `traversal` representing the preorder traversal of a binary tree, where each node is represented by a lowercase letter.
- Expected output: The root of the recovered binary tree.
- Key requirements and edge cases to consider:
  - The input string is non-empty and only contains lowercase letters.
  - The length of the input string is between 1 and 10^5.
- Example test cases with explanations:
  - For the input "aa", the output should be a tree with two nodes labeled 'a'.
  - For the input "ab", the output should be a tree with two nodes labeled 'a' and 'b', where 'b' is the right child of 'a'.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the string and try to construct the tree by creating nodes for each character.
- Step-by-step breakdown of the solution:
  1. Initialize a stack to store the nodes.
  2. Iterate over the string, and for each character, create a new node.
  3. If the stack is not empty and the top node of the stack has no left child, set the new node as the left child of the top node and pop the top node from the stack.
  4. If the stack is not empty and the top node of the stack has a left child but no right child, set the new node as the right child of the top node and pop the top node from the stack.
  5. Push the new node onto the stack.
- Why this approach comes to mind first: It's a straightforward way to construct the tree by iterating over the string and creating nodes for each character.

```cpp
// Brute force approach
struct TreeNode {
    char val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(char x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* recoverFromPreorder(string traversal) {
    stack<TreeNode*> st;
    int i = 0;
    while (i < traversal.size()) {
        string val;
        val += traversal[i];
        i++;
        string depth;
        while (i < traversal.size() && traversal[i] == '-') {
            depth += traversal[i];
            i++;
        }
        TreeNode* node = new TreeNode(val[0]);
        while (!st.empty() && st.size() > depth.size()) {
            st.pop();
        }
        if (!st.empty()) {
            if (!st.top()->left) {
                st.top()->left = node;
            } else {
                st.top()->right = node;
            }
        }
        st.push(node);
    }
    while (st.size() > 1) {
        st.pop();
    }
    return st.top();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate over the string once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to push all characters onto the stack.
> - **Why these complexities occur:** The time complexity occurs because we need to process each character in the input string, and the space complexity occurs because we need to store the nodes in the stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to store the nodes and their corresponding depths.
- Detailed breakdown of the approach:
  1. Initialize a stack to store the nodes and their corresponding depths.
  2. Iterate over the string, and for each character, create a new node.
  3. While the stack is not empty and the top node of the stack has a depth greater than the current depth, pop the top node from the stack.
  4. If the stack is not empty, set the new node as the left or right child of the top node of the stack based on whether the top node has a left child.
  5. Push the new node onto the stack with its corresponding depth.
- Proof of optimality: This approach is optimal because we only iterate over the string once and use a stack to store the nodes, which reduces the time complexity to $O(n)$.

```cpp
// Optimal approach
TreeNode* recoverFromPreorder(string traversal) {
    stack<pair<TreeNode*, int>> st;
    int i = 0;
    while (i < traversal.size()) {
        string val;
        val += traversal[i];
        i++;
        string depth;
        while (i < traversal.size() && traversal[i] == '-') {
            depth += traversal[i];
            i++;
        }
        TreeNode* node = new TreeNode(val[0]);
        while (!st.empty() && st.top().second > depth.size()) {
            st.pop();
        }
        if (!st.empty()) {
            if (!st.top().first->left) {
                st.top().first->left = node;
            } else {
                st.top().first->right = node;
            }
        }
        st.push({node, depth.size()});
    }
    return st.top().first;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate over the string once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to push all characters onto the stack.
> - **Optimality proof:** This approach is optimal because we only iterate over the string once and use a stack to store the nodes, which reduces the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to store nodes and their corresponding depths.
- Problem-solving patterns identified: Constructing a tree from a preorder traversal.
- Optimization techniques learned: Using a stack to reduce time complexity.
- Similar problems to practice: Constructing a tree from an inorder traversal, constructing a tree from a postorder traversal.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input string.
- Edge cases to watch for: An input string with only one character, an input string with all characters being the same.
- Performance pitfalls: Using a recursive approach instead of an iterative approach, which can lead to a stack overflow.
- Testing considerations: Testing the function with different input strings, including edge cases.