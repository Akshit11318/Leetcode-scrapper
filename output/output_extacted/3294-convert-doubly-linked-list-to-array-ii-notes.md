## Convert Doubly Linked List to Array II

**Problem Link:** https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/description

**Problem Statement:**
- Input format and constraints: Given a doubly linked list, convert it to an array. The doubly linked list is defined by a `Node` class with `val`, `prev`, and `next` attributes.
- Expected output format: Return an array of integers where each integer represents the value of a node in the linked list.
- Key requirements and edge cases to consider: Handle cases where the linked list is empty or has only one node.
- Example test cases with explanations: For example, given the linked list `1 <-> 2 <-> 3`, the output should be `[1, 2, 3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To convert the doubly linked list to an array, we can start at the head of the list and traverse each node, appending its value to the array.
- Step-by-step breakdown of the solution: 
  1. Initialize an empty array to store the node values.
  2. Start at the head of the linked list.
  3. Traverse the linked list, appending each node's value to the array.
  4. Continue until the end of the linked list is reached.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
class Solution {
public:
    vector<int> vectorFromList(Node* head) {
        vector<int> result;
        Node* current = head;
        while (current != nullptr) {
            result.push_back(current->val);
            current = current->next;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, we store every node's value in the array.
> - **Why these complexities occur:** The time complexity is linear because we only traverse the linked list once. The space complexity is also linear because we store the values of all nodes in the array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must visit each node at least once to include its value in the array.
- Detailed breakdown of the approach: The same steps as the brute force approach apply.
- Proof of optimality: Since we must visit each node at least once, any solution must have a time complexity of at least $O(n)$. Thus, the brute force approach is optimal.
- Why further optimization is impossible: We cannot reduce the time complexity below $O(n)$ because we must examine each node's value to include it in the output array.

```cpp
class Solution {
public:
    vector<int> vectorFromList(Node* head) {
        vector<int> result;
        Node* current = head;
        while (current != nullptr) {
            result.push_back(current->val);
            current = current->next;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list.
> - **Space Complexity:** $O(n)$, because we store the values of all nodes in the array.
> - **Optimality proof:** The solution is optimal because it visits each node exactly once, which is necessary to include all node values in the output array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list traversal and array construction.
- Problem-solving patterns identified: The need to visit each element in a data structure to perform a transformation.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the inherent requirements of the problem.
- Similar problems to practice: Converting other data structures (like trees or graphs) into arrays or lists.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for `nullptr` before accessing node attributes.
- Edge cases to watch for: Handling empty linked lists or linked lists with a single node.
- Performance pitfalls: Using inefficient data structures or algorithms that have higher time complexities than necessary.
- Testing considerations: Ensure that the solution works correctly for linked lists of varying lengths and with different values.