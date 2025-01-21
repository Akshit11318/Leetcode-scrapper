## Binary Search Tree Iterator II
**Problem Link:** https://leetcode.com/problems/binary-search-tree-iterator-ii/description

**Problem Statement:**
- Input: A Binary Search Tree (BST) with nodes having unique values.
- Output: Implement an iterator that allows you to iterate through the BST in ascending order, and also supports the `prev()` function to get the previous node in the iteration.
- Key requirements:
  - The iterator should support `next()`, `prev()`, `hasNext()`, and `hasPrev()` functions.
  - The iterator should iterate through the BST in ascending order.
- Edge cases:
  - An empty BST.
  - A BST with a single node.
- Example test cases:
  - Create a BST with nodes having values 5, 3, 7, 2, 4, 6, 8.
  - Call `next()` and `prev()` functions to iterate through the BST in ascending order.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to perform an in-order traversal of the BST and store the node values in a list.
- Then, use two pointers, one for the current node and one for the previous node, to support the `next()` and `prev()` functions.
- Why this approach comes to mind first: It's a straightforward way to iterate through the BST in ascending order, but it's not efficient for large BSTs because it requires storing all node values in a list.

```cpp
class BSTIterator {
public:
    vector<int> nodes;
    int index;
    BSTIterator(TreeNode* root) {
        // Perform in-order traversal and store node values in a list
        inorderTraversal(root);
        index = -1;
    }
    
    bool hasNext() {
        return index < nodes.size() - 1;
    }
    
    bool hasPrev() {
        return index > 0;
    }
    
    int next() {
        return nodes[++index];
    }
    
    int prev() {
        return nodes[--index];
    }
    
    void inorderTraversal(TreeNode* node) {
        if (node) {
            inorderTraversal(node->left);
            nodes.push_back(node->val);
            inorderTraversal(node->right);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the BST, because we perform an in-order traversal of the BST and store all node values in a list.
> - **Space Complexity:** $O(n)$, because we store all node values in a list.
> - **Why these complexities occur:** These complexities occur because we need to store all node values in a list to support the `next()` and `prev()` functions.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a stack to store nodes to be visited, and use two stacks, one for the next node and one for the previous node.
- We perform an in-order traversal of the BST, but instead of storing all node values in a list, we store the nodes to be visited in a stack.
- When `next()` is called, we pop the top node from the stack, and when `prev()` is called, we pop the top node from the other stack.
- Why this approach is optimal: It's more efficient than the brute force approach because we don't need to store all node values in a list.

```cpp
class BSTIterator {
public:
    stack<TreeNode*> nextStack;
    stack<TreeNode*> prevStack;
    
    BSTIterator(TreeNode* root) {
        // Perform in-order traversal and store nodes to be visited in a stack
        pushLeft(root, nextStack);
    }
    
    bool hasNext() {
        return !nextStack.empty();
    }
    
    bool hasPrev() {
        return !prevStack.empty();
    }
    
    int next() {
        TreeNode* node = nextStack.top();
        nextStack.pop();
        if (node->right) {
            pushLeft(node->right, nextStack);
        }
        prevStack.push(node);
        return node->val;
    }
    
    int prev() {
        TreeNode* node = prevStack.top();
        prevStack.pop();
        if (node->left) {
            pushLeft(node->left, nextStack);
        }
        nextStack.push(node);
        return node->val;
    }
    
    void pushLeft(TreeNode* node, stack<TreeNode*>& stack) {
        while (node) {
            stack.push(node);
            node = node->left;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the BST, because we perform an in-order traversal of the BST and use a stack to store nodes to be visited.
> - **Space Complexity:** $O(h)$, because we use a stack to store nodes to be visited.
> - **Optimality proof:** This approach is optimal because we don't need to store all node values in a list, and we use a stack to store nodes to be visited, which reduces the space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal, stack usage.
- Problem-solving patterns identified: Using a stack to store nodes to be visited.
- Optimization techniques learned: Reducing space complexity by using a stack instead of a list.
- Similar problems to practice: Implementing an iterator for a BST, implementing a stack-based solution for a tree traversal problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for empty stacks, forgetting to push nodes to be visited onto the stack.
- Edge cases to watch for: An empty BST, a BST with a single node.
- Performance pitfalls: Using a list to store all node values, which can lead to high space complexity.
- Testing considerations: Testing the iterator with different BSTs, testing the `next()` and `prev()` functions with different inputs.