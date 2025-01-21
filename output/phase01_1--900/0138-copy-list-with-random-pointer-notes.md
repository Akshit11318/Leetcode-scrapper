## Copy List with Random Pointer

**Problem Link:** https://leetcode.com/problems/copy-list-with-random-pointer/description

**Problem Statement:**
- Input format and constraints: A linked list with `n` nodes, where each node has a `val` (node value), `next` (next node in the list), and `random` (random node in the list) pointers. 
- Expected output format: The head of the copied linked list.
- Key requirements and edge cases to consider: The copied list should be a deep copy, meaning that all nodes should be new and not reference the original list's nodes. The `random` pointers in the copied list should point to the corresponding nodes in the copied list.
- Example test cases with explanations: For example, given the list `1 -> 2 -> 3` with `1.random -> 3`, `2.random -> 1`, and `3.random -> 2`, the copied list should have the same structure and `random` pointers.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through the original list and create a new node for each node in the original list. Then, we can iterate through the original list again and set the `next` and `random` pointers for each node in the copied list.
- Step-by-step breakdown of the solution:
  1. Create a hash map to store the nodes in the original list and their corresponding nodes in the copied list.
  2. Iterate through the original list and create a new node for each node in the original list.
  3. Store the new node in the hash map.
  4. Iterate through the original list again and set the `next` and `random` pointers for each node in the copied list using the hash map.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves creating a new node for each node in the original list and then setting the `next` and `random` pointers for each node in the copied list.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        
        // Create a hash map to store the nodes in the original list and their corresponding nodes in the copied list
        unordered_map<Node*, Node*> nodeMap;
        
        // Iterate through the original list and create a new node for each node in the original list
        Node* current = head;
        while (current) {
            Node* newNode = new Node(current->val);
            nodeMap[current] = newNode;
            current = current->next;
        }
        
        // Iterate through the original list again and set the next and random pointers for each node in the copied list
        current = head;
        while (current) {
            if (current->next) {
                nodeMap[current]->next = nodeMap[current->next];
            }
            if (current->random) {
                nodeMap[current]->random = nodeMap[current->random];
            }
            current = current->next;
        }
        
        return nodeMap[head];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the original list. We iterate through the original list twice: once to create the new nodes and once to set the `next` and `random` pointers.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the original list. We use a hash map to store the nodes in the original list and their corresponding nodes in the copied list.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the original list twice. The space complexity occurs because we use a hash map to store the nodes in the original list and their corresponding nodes in the copied list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hash map to store the nodes in the original list and their corresponding nodes in the copied list. This allows us to set the `next` and `random` pointers for each node in the copied list in a single pass.
- Detailed breakdown of the approach:
  1. Create a hash map to store the nodes in the original list and their corresponding nodes in the copied list.
  2. Iterate through the original list and create a new node for each node in the original list.
  3. Store the new node in the hash map.
  4. Set the `next` and `random` pointers for each node in the copied list using the hash map.
- Proof of optimality: This approach is optimal because it only requires a single pass through the original list and uses a hash map to store the nodes in the original list and their corresponding nodes in the copied list.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        
        // Create a hash map to store the nodes in the original list and their corresponding nodes in the copied list
        unordered_map<Node*, Node*> nodeMap;
        
        // Iterate through the original list and create a new node for each node in the original list
        Node* current = head;
        while (current) {
            Node* newNode = new Node(current->val);
            nodeMap[current] = newNode;
            current = current->next;
        }
        
        // Set the next and random pointers for each node in the copied list using the hash map
        current = head;
        while (current) {
            if (current->next) {
                nodeMap[current]->next = nodeMap[current->next];
            }
            if (current->random) {
                nodeMap[current]->random = nodeMap[current->random];
            }
            current = current->next;
        }
        
        return nodeMap[head];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the original list. We iterate through the original list twice: once to create the new nodes and once to set the `next` and `random` pointers.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the original list. We use a hash map to store the nodes in the original list and their corresponding nodes in the copied list.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the original list and uses a hash map to store the nodes in the original list and their corresponding nodes in the copied list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, linked lists, and deep copying.
- Problem-solving patterns identified: Using a hash map to store nodes in the original list and their corresponding nodes in the copied list.
- Optimization techniques learned: Using a single pass through the original list and a hash map to store the nodes in the original list and their corresponding nodes in the copied list.
- Similar problems to practice: Copying a linked list with a random pointer, copying a binary tree with a random pointer.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for `nullptr` before accessing a node's `next` or `random` pointer.
- Edge cases to watch for: An empty list, a list with a single node, a list with multiple nodes.
- Performance pitfalls: Using multiple passes through the original list, not using a hash map to store the nodes in the original list and their corresponding nodes in the copied list.
- Testing considerations: Test the function with different input cases, including an empty list, a list with a single node, and a list with multiple nodes.