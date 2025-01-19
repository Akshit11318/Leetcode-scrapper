## Copy List with Random Pointer

**Problem Link:** https://leetcode.com/problems/copy-list-with-random-pointer/description

**Problem Statement:**

The problem requires creating a deep copy of a given linked list where each node has a random pointer that can point to any other node in the list, including itself. The task is to create a copy of the list such that the random pointers in the copied list point to the corresponding nodes in the copied list, not the original list.

---

### Brute Force Approach

**Explanation:**

1. Create a hashmap to store the mapping between the original nodes and their corresponding copies.
2. Traverse the original list and create a copy of each node.
3. Store the mapping between the original node and its copy in the hashmap.
4. Traverse the original list again and update the random pointers of the copied nodes based on the hashmap.

```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return NULL;
        
        unordered_map<Node*, Node*> map;
        Node* curr = head;
        
        // Create a copy of each node and store in hashmap
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        curr = head;
        Node* copy = map[curr];
        
        // Update next and random pointers
        while (curr) {
            copy->next = map[curr->next];
            copy->random = map[curr->random];
            curr = curr->next;
            copy = copy->next;
        }
        
        return map[head];
    }
};
```

> Complexity Analysis:
> 
> **Time Complexity:** O(N), where N is the number of nodes in the linked list, because we are traversing the list twice. The reason is 2 * N where N is the number of nodes, but we ignore constants in Big O notation.
> 
> **Space Complexity:** O(N), where N is the number of nodes in the linked list, because we are storing all the nodes in the hashmap.

---

### Optimal Approach

**Explanation:**

The optimal approach is similar to the brute force approach, but it uses a more efficient way to update the random pointers.

```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return NULL;
        
        unordered_map<Node*, Node*> map;
        Node* curr = head;
        
        // Create a copy of each node and store in hashmap
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        curr = head;
        
        // Update next and random pointers
        while (curr) {
            map[curr]->next = curr->next ? map[curr->next] : NULL;
            map[curr]->random = curr->random ? map[curr->random] : NULL;
            curr = curr->next;
        }
        
        return map[head];
    }
};
```

> Complexity Analysis:
> 
> **Time Complexity:** O(N), where N is the number of nodes in the linked list, because we are traversing the list twice.
> 
> **Space Complexity:** O(N), where N is the number of nodes in the linked list, because we are storing all the nodes in the hashmap.

---

### Final Notes

**Learning Points:**

*   We can use a hashmap to store the mapping between the original nodes and their copies.
*   We need to traverse the list twice to create a copy of each node and update the next and random pointers.
*   The time and space complexity of the solution is O(N), where N is the number of nodes in the linked list.

**Mistakes to Avoid:**

*   Not handling the case where the random pointer points to NULL.
*   Not updating the next and random pointers correctly.
*   Not using a hashmap to store the mapping between the original nodes and their copies, which can lead to incorrect results.