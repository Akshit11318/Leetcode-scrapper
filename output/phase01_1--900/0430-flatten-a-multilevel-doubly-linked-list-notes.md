## Flatten a Multilevel Doubly Linked List

**Problem Link:** https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description

**Problem Statement:**
- Input: A `Node` object representing the head of a multilevel doubly linked list.
- Output: The head of the flattened doubly linked list.
- Key requirements: The list should be flattened in-place, and each node should have a `child` pointer to another list or `NULL`.
- Edge cases: An empty list, a list with a single node, a list with multiple levels.

Example test cases:
- A list with a single node: The output should be the same node.
- A list with multiple nodes but no children: The output should be the same list.
- A list with multiple levels: The output should be a flattened list.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the list, and for each node, if it has a child, recursively flatten the child list and append it to the current node.
- Step-by-step breakdown:
  1. Create a recursive function to flatten a list.
  2. In the function, iterate through the list, and for each node, check if it has a child.
  3. If a node has a child, recursively call the function on the child list.
  4. After the recursive call, append the flattened child list to the current node.
- Why this approach comes to mind first: It directly addresses the problem statement and seems straightforward.

```cpp
// Definition for a Node.
struct Node {
    int val;
    Node *next;
    Node *prev;
    Node *child;
};

Node* flatten(Node* head) {
    if (!head) return head;
    Node* current = head;
    while (current) {
        if (current->child) {
            Node* child = current->child;
            Node* next = current->next;
            current->next = child;
            child->prev = current;
            current->child = NULL;
            Node* tail = child;
            while (tail->next) {
                tail = tail->next;
            }
            tail->next = next;
            if (next) next->prev = tail;
            current = child;
        } else {
            current = current->next;
        }
    }
    return head;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the total number of nodes in the multilevel list, because we visit each node once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the current node and do not use any additional data structures that scale with the input size.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the list once, and the space complexity is constant because we do not use any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of using recursion, we can iterate through the list and directly append child lists to their parent nodes.
- Detailed breakdown: We maintain a pointer to the current node and iterate through the list. If a node has a child, we append the child list to the current node and update the `next` and `prev` pointers accordingly.
- Proof of optimality: This approach is optimal because it visits each node exactly once and uses a constant amount of extra space.

```cpp
Node* flatten(Node* head) {
    if (!head) return head;
    Node* current = head;
    while (current) {
        if (current->child) {
            Node* child = current->child;
            Node* next = current->next;
            current->next = child;
            child->prev = current;
            current->child = NULL;
            Node* tail = child;
            while (tail->next) {
                tail = tail->next;
            }
            tail->next = next;
            if (next) next->prev = tail;
            current = child;
        } else {
            current = current->next;
        }
    }
    return head;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the total number of nodes in the multilevel list.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This is the optimal solution because it visits each node once and uses constant space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Iteration, pointer manipulation, and in-place modification.
- Problem-solving patterns: Identifying the need to iterate through a data structure and update pointers accordingly.
- Optimization techniques: Avoiding recursion when possible and using iteration instead.
- Similar problems to practice: Other problems involving linked lists and tree traversals.

**Mistakes to Avoid:**
- Common implementation errors: Failing to update `next` and `prev` pointers correctly.
- Edge cases: Forgetting to handle the case where a node has no child or the list is empty.
- Performance pitfalls: Using recursion when iteration is more efficient.
- Testing considerations: Thoroughly testing the function with different inputs, including edge cases.