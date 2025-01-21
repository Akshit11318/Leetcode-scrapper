## Insert into a Sorted Circular Linked List
**Problem Link:** [https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description)

**Problem Statement:**
- Input: A `Node` object representing the head of a sorted circular linked list and an integer `insertVal` representing the value to be inserted.
- Constraints: The linked list is sorted in ascending order, and the `insertVal` will be inserted into the correct position to maintain the sorted order.
- Expected Output: The head of the modified linked list with `insertVal` inserted.
- Key Requirements: 
  - Maintain the sorted order of the linked list.
  - Handle edge cases such as an empty linked list or a linked list with a single node.
- Example Test Cases:
  - Inserting into an empty linked list.
  - Inserting into a linked list with a single node.
  - Inserting into a linked list with multiple nodes.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the linked list to find the correct position for `insertVal`.
- Step-by-step breakdown:
  1. Start at the head of the linked list.
  2. Compare `insertVal` with the current node's value.
  3. If `insertVal` is less than the current node's value, move to the next node.
  4. Repeat steps 2-3 until we find the correct position for `insertVal`.
  5. Insert a new node with `insertVal` at the correct position.
- Why this approach comes to mind first: It's a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        // Handle edge case: empty linked list
        if (!head) {
            Node* newNode = new Node(insertVal);
            newNode->next = newNode;
            return newNode;
        }

        // Handle edge case: linked list with a single node
        if (head->next == head) {
            Node* newNode = new Node(insertVal);
            if (insertVal >= head->val) {
                head->next = newNode;
                newNode->next = head;
            } else {
                newNode->next = head;
                head = newNode;
            }
            return head;
        }

        // Find the correct position for insertVal
        Node* curr = head;
        do {
            if (curr->val <= insertVal && insertVal <= curr->next->val) {
                Node* newNode = new Node(insertVal);
                newNode->next = curr->next;
                curr->next = newNode;
                return head;
            }
            curr = curr->next;
        } while (curr != head);

        // If insertVal is less than the smallest value or greater than the largest value
        Node* newNode = new Node(insertVal);
        newNode->next = head;
        curr->next = newNode;
        return newNode;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because we may need to traverse the entire linked list to find the correct position for `insertVal`.
> - **Space Complexity:** $O(1)$, because we only create a new node to insert into the linked list.
> - **Why these complexities occur:** The time complexity is linear because we may need to traverse the entire linked list, and the space complexity is constant because we only create a single new node.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can simplify the solution by handling the edge cases separately and then finding the correct position for `insertVal` in a single pass through the linked list.
- Detailed breakdown:
  1. Handle the edge case where the linked list is empty.
  2. Handle the edge case where the linked list has a single node.
  3. Find the correct position for `insertVal` by iterating through the linked list.
- Proof of optimality: This solution has the same time complexity as the brute force approach but is more efficient in practice because it reduces the number of iterations through the linked list.

```cpp
class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        // Handle edge case: empty linked list
        if (!head) {
            Node* newNode = new Node(insertVal);
            newNode->next = newNode;
            return newNode;
        }

        // Handle edge case: linked list with a single node
        if (head->next == head) {
            Node* newNode = new Node(insertVal);
            if (insertVal >= head->val) {
                head->next = newNode;
                newNode->next = head;
            } else {
                newNode->next = head;
                head = newNode;
            }
            return head;
        }

        // Find the correct position for insertVal
        Node* prev = head;
        Node* curr = head->next;
        while (curr != head && curr->val < insertVal) {
            prev = curr;
            curr = curr->next;
        }

        // Insert the new node
        Node* newNode = new Node(insertVal);
        newNode->next = curr;
        prev->next = newNode;

        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because we may need to traverse the entire linked list to find the correct position for `insertVal`.
> - **Space Complexity:** $O(1)$, because we only create a new node to insert into the linked list.
> - **Optimality proof:** This solution is optimal because it has the same time complexity as the brute force approach but is more efficient in practice due to reduced iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration through a linked list, edge case handling, and node insertion.
- Problem-solving patterns identified: Handling edge cases separately and finding the correct position for `insertVal` in a single pass through the linked list.
- Optimization techniques learned: Reducing the number of iterations through the linked list by handling edge cases separately.
- Similar problems to practice: Insertion into a sorted linked list, deletion from a sorted linked list, and searching in a sorted linked list.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not updating the `next` pointers correctly, and not checking for the correct position for `insertVal`.
- Edge cases to watch for: Empty linked list, linked list with a single node, and `insertVal` being less than the smallest value or greater than the largest value.
- Performance pitfalls: Not optimizing the solution to reduce the number of iterations through the linked list.
- Testing considerations: Testing the solution with different edge cases and input values to ensure correctness.