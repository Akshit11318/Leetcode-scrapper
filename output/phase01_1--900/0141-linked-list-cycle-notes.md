## Linked List Cycle

**Problem Link:** [https://leetcode.com/problems/linked-list-cycle/description](https://leetcode.com/problems/linked-list-cycle/description)

**Problem Statement:**
- Input format: A linked list represented as a sequence of nodes, where each node contains an integer value and a pointer to the next node.
- Constraints: The linked list may or may not contain a cycle.
- Expected output format: A boolean indicating whether a cycle exists in the linked list.
- Key requirements and edge cases to consider: Handling of empty linked lists, linked lists with a single node, and linked lists with multiple nodes and a cycle.
- Example test cases with explanations:
  - Example 1: `[3, 2, 0, -4]` with a cycle at the node with value 0.
  - Example 2: `[1, 2]` with no cycle.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One approach to detect a cycle is to keep track of all the nodes we have visited. If we encounter a node that we have already visited, then a cycle exists.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set to store the nodes we have visited.
  2. Traverse the linked list, starting from the head node.
  3. For each node, check if it is already in the set. If it is, return true (cycle exists). Otherwise, add it to the set.
  4. If we reach the end of the linked list (i.e., we encounter a null node), return false (no cycle exists).

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> visited;
        while (head) {
            if (visited.find(head) != visited.end()) {
                return true; // Cycle exists
            }
            visited.insert(head);
            head = head->next;
        }
        return false; // No cycle exists
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because in the worst case, we need to traverse the entire linked list.
> - **Space Complexity:** $O(n)$, because in the worst case, we need to store all nodes in the set.
> - **Why these complexities occur:** The brute force approach requires storing all nodes in the set, resulting in high space complexity. The time complexity is linear because we only traverse the linked list once.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the Floyd's Tortoise and Hare (Cycle Detection) algorithm, which uses two pointers that move at different speeds to detect a cycle. If a cycle exists, the faster pointer will eventually catch up to the slower pointer.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `slow` and `fast`, both pointing to the head node.
  2. Move `slow` one step at a time and `fast` two steps at a time.
  3. If `fast` reaches the end of the linked list, return false (no cycle exists).
  4. If `fast` catches up to `slow`, return true (cycle exists).

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head || !head->next) {
            return false; // No cycle exists
        }
        ListNode *slow = head;
        ListNode *fast = head->next;
        while (slow != fast) {
            if (!fast || !fast->next) {
                return false; // No cycle exists
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        return true; // Cycle exists
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because in the worst case, we need to traverse the entire linked list.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the two pointers.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity and constant space complexity, which is the best possible for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Cycle detection, Floyd's Tortoise and Hare algorithm.
- Problem-solving patterns identified: Using two pointers to detect a cycle, handling edge cases such as empty linked lists.
- Optimization techniques learned: Reducing space complexity by using a constant amount of space, improving time complexity by using a more efficient algorithm.
- Similar problems to practice: Detecting a cycle in a graph, finding the start of a cycle in a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases such as empty linked lists, not checking for null nodes when traversing the linked list.
- Edge cases to watch for: Linked lists with a single node, linked lists with multiple nodes and a cycle.
- Performance pitfalls: Using a brute force approach that results in high space complexity, not optimizing the algorithm for large inputs.
- Testing considerations: Testing the solution with different types of linked lists, including empty linked lists, linked lists with a single node, and linked lists with multiple nodes and a cycle.