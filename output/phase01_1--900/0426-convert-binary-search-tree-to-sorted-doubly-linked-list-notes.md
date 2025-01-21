## Convert Binary Search Tree to Sorted Doubly Linked List

**Problem Link:** https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description

**Problem Statement:**
- Input: The root of a binary search tree (`BST`).
- Output: Convert the `BST` into a sorted doubly linked list (`DLL`) in-place.
- Key requirements and edge cases:
  - The left child of a node in the `DLL` should be the previous node in the sorted order.
  - The right child of a node in the `DLL` should be the next node in the sorted order.
  - The `DLL` should be sorted in ascending order.
- Example test cases:
  - A `BST` with a single node should be converted into a `DLL` with a single node.
  - An empty `BST` should result in an empty `DLL`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the `BST` in-order to get the nodes in ascending order, then create a `DLL` by linking these nodes.
- Step-by-step breakdown:
  1. Perform an in-order traversal of the `BST` to get the nodes in ascending order.
  2. Store the nodes in a vector or array.
  3. Create a `DLL` by linking the nodes in the vector or array.
- Why this approach comes to mind first: It's a straightforward way to get the nodes in the correct order and then create the `DLL`.

```cpp
// Brute Force Approach
Node* prev = nullptr;
void inorder(Node* node) {
    if (node) {
        inorder(node->left);
        if (prev) {
            prev->right = node;
            node->left = prev;
        }
        prev = node;
        inorder(node->right);
    }
}
Node* treeToDoublyList(Node* root) {
    if (!root) return nullptr;
    Node dummy;
    prev = &dummy;
    inorder(root);
    Node* head = dummy.right;
    head->left = prev;
    prev->right = head;
    return head;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the `BST`, because we visit each node once during the in-order traversal.
> - **Space Complexity:** $O(n)$, because we store all nodes in the vector or array.
> - **Why these complexities occur:** The in-order traversal and storing nodes in a data structure cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Perform an in-order traversal of the `BST` and create the `DLL` on the fly without storing nodes in a data structure.
- Detailed breakdown:
  1. Initialize a `dummy` node to simplify the process of finding the head and tail of the `DLL`.
  2. Initialize a `prev` pointer to keep track of the previous node in the `DLL`.
  3. Perform an in-order traversal of the `BST`.
  4. During the traversal, link each node to the previous node and update the `prev` pointer.
- Proof of optimality: This approach has the same time complexity as the brute force approach but reduces the space complexity to $O(1)$, excluding the space needed for the output.

```cpp
// Optimal Approach
Node* prev = nullptr;
Node* treeToDoublyList(Node* root) {
    if (!root) return nullptr;
    Node dummy;
    prev = &dummy;
    inorder(root);
    Node* head = dummy.right;
    head->left = prev;
    prev->right = head;
    return head;
}
void inorder(Node* node) {
    if (node) {
        inorder(node->left);
        node->left = prev;
        if (prev) prev->right = node;
        prev = node;
        inorder(node->right);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the `BST`.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output, because we only use a constant amount of space to store the `dummy` node and the `prev` pointer.
> - **Optimality proof:** This is the optimal solution because we cannot reduce the time complexity further without changing the data structure, and we have minimized the space complexity by avoiding the storage of nodes in a data structure.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal of a `BST`, creation of a `DLL`, and optimization of space complexity.
- Problem-solving patterns identified: Using a `dummy` node to simplify the process of finding the head and tail of the `DLL`, and performing operations on the fly during the traversal.
- Optimization techniques learned: Reducing space complexity by avoiding the storage of nodes in a data structure.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the `prev` pointer during the traversal, or not correctly linking the nodes in the `DLL`.
- Edge cases to watch for: Handling an empty `BST` or a `BST` with a single node.
- Performance pitfalls: Using a data structure to store nodes, which increases the space complexity.
- Testing considerations: Verifying that the `DLL` is correctly sorted and linked.