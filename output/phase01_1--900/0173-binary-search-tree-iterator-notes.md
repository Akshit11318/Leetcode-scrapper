## Binary Search Tree Iterator

**Problem Link:** https://leetcode.com/problems/binary-search-tree-iterator/description

**Problem Statement:**
- Input: A binary search tree (BST) and a root node.
- Output: An iterator that can traverse the BST in an in-order manner (left-root-right).
- Key requirements and edge cases:
  - The iterator should support `next()` and `hasNext()` operations.
  - If the BST is empty, the iterator should return `false` for `hasNext()`.
  - The iterator should be able to handle large BSTs.

**Example Test Cases:**

- Test case 1: A sample BST with multiple nodes.
- Test case 2: An empty BST.
- Test case 3: A BST with a single node.

### Brute Force Approach

**Explanation:**
- The initial thought process is to perform an in-order traversal of the BST and store the results in a vector.
- Then, create an iterator that returns the elements from the vector one by one.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
class BSTIterator {
public:
    vector<int> nodes;
    int index = 0;
    void inOrder(TreeNode* root) {
        if (!root) return;
        inOrder(root->left);
        nodes.push_back(root->val);
        inOrder(root->right);
    }
    BSTIterator(TreeNode* root) {
        inOrder(root);
    }
    int next() {
        return nodes[index++];
    }
    bool hasNext() {
        return index < nodes.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the BST. This is because we are performing an in-order traversal of the BST.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the BST. This is because we are storing all the nodes in a vector.
> - **Why these complexities occur:** The time complexity occurs because we are visiting each node once during the in-order traversal. The space complexity occurs because we are storing all the nodes in a vector.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a stack to store the nodes that need to be visited.
- We start by pushing the root node onto the stack.
- Then, we enter a loop where we keep pushing the left child of the top node onto the stack until the top node has no left child.
- Once we have pushed all the left children onto the stack, we pop the top node, return its value, and push its right child onto the stack if it exists.
- This approach is optimal because it only uses a constant amount of space (for the stack) and only visits each node once.

```cpp
class BSTIterator {
public:
    stack<TreeNode*> st;
    BSTIterator(TreeNode* root) {
        pushLeft(root);
    }
    int next() {
        TreeNode* top = st.top();
        st.pop();
        if (top->right) pushLeft(top->right);
        return top->val;
    }
    bool hasNext() {
        return !st.empty();
    }
    void pushLeft(TreeNode* node) {
        while (node) {
            st.push(node);
            node = node->left;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `next()` and `O(h)` for `hasNext()`, where $h$ is the height of the BST. This is because we are only pushing and popping nodes from the stack.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the BST. This is because we are storing the nodes in the stack.
> - **Optimality proof:** This approach is optimal because it only uses a constant amount of space (for the stack) and only visits each node once. The time complexity is also optimal because we are only performing a constant amount of work for each node.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: in-order traversal, stack-based traversal.
- Problem-solving patterns identified: using a stack to store nodes that need to be visited.
- Optimization techniques learned: reducing space complexity by using a stack instead of a vector.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases (e.g., empty BST).
- Edge cases to watch for: empty BST, BST with a single node.
- Performance pitfalls: using a vector to store all nodes, which can lead to high space complexity.
- Testing considerations: testing with different types of BSTs (e.g., balanced, unbalanced).