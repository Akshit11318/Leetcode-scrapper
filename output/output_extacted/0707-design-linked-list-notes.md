## Design Linked List
**Problem Link:** https://leetcode.com/problems/design-linked-list/description

**Problem Statement:**
- Design a singly linked list with the following methods:
  - `get(index)`: Returns the value at the given index.
  - `addAtHead(val)`: Adds a new node with the given value at the head of the list.
  - `addAtTail(val)`: Adds a new node with the given value at the tail of the list.
  - `addAtIndex(index, val)`: Adds a new node with the given value at the specified index.
  - `deleteAtIndex(index)`: Deletes the node at the specified index.
- Input format and constraints:
  - The index is 0-based.
  - The index is guaranteed to be valid.
  - The value is guaranteed to be valid.
- Expected output format:
  - The `get` method returns an integer.
  - The `addAtHead`, `addAtTail`, `addAtIndex`, and `deleteAtIndex` methods do not return anything.
- Key requirements and edge cases to consider:
  - The linked list is initially empty.
  - The linked list can grow and shrink dynamically.
- Example test cases with explanations:
  - `MyLinkedList myLinkedList = new MyLinkedList();`
  - `myLinkedList.addAtHead(1);`
  - `myLinkedList.addAtTail(3);`
  - `myLinkedList.addAtIndex(1, 2);`
  - `myLinkedList.get(1); // returns 2`
  - `myLinkedList.deleteAtIndex(1);`
  - `myLinkedList.get(1); // returns 3`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to implement a basic linked list with the required methods.
- We can use a `struct` to represent a node in the linked list, containing an integer value and a pointer to the next node.
- We can use a `class` to represent the linked list itself, containing a pointer to the head node and a pointer to the tail node.

```cpp
class MyLinkedList {
public:
    struct Node {
        int val;
        Node* next;
        Node(int x) : val(x), next(NULL) {}
    };

    MyLinkedList() : head(NULL), tail(NULL), size(0) {}

    int get(int index) {
        if (index < 0 || index >= size) {
            return -1; // or throw an exception
        }
        Node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }

    void addAtHead(int val) {
        Node* newNode = new Node(val);
        if (head == NULL) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head = newNode;
        }
        size++;
    }

    void addAtTail(int val) {
        Node* newNode = new Node(val);
        if (tail == NULL) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        size++;
    }

    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) {
            return; // or throw an exception
        }
        if (index == 0) {
            addAtHead(val);
            return;
        }
        if (index == size) {
            addAtTail(val);
            return;
        }
        Node* curr = head;
        for (int i = 0; i < index - 1; i++) {
            curr = curr->next;
        }
        Node* newNode = new Node(val);
        newNode->next = curr->next;
        curr->next = newNode;
        size++;
    }

    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return; // or throw an exception
        }
        if (index == 0) {
            Node* temp = head;
            head = head->next;
            if (head == NULL) {
                tail = NULL;
            }
            delete temp;
        } else {
            Node* curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr->next;
            }
            Node* temp = curr->next;
            curr->next = curr->next->next;
            if (temp == tail) {
                tail = curr;
            }
            delete temp;
        }
        size--;
    }

private:
    Node* head;
    Node* tail;
    int size;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `get`, `addAtIndex`, and `deleteAtIndex` methods, where $n$ is the size of the linked list. $O(1)$ for `addAtHead` and `addAtTail` methods.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the linked list.
> - **Why these complexities occur:** The time complexity is $O(n)$ for `get`, `addAtIndex`, and `deleteAtIndex` methods because we need to traverse the linked list to find the desired node. The space complexity is $O(n)$ because we need to store all the nodes in the linked list.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is similar to the brute force approach, but we can improve the implementation by using a dummy node to simplify the code.
- We can use a `struct` to represent a node in the linked list, containing an integer value and a pointer to the next node.
- We can use a `class` to represent the linked list itself, containing a pointer to the dummy node and a pointer to the tail node.

```cpp
class MyLinkedList {
public:
    struct Node {
        int val;
        Node* next;
        Node(int x) : val(x), next(NULL) {}
    };

    MyLinkedList() : dummy(new Node(0)), tail(NULL), size(0) {}

    int get(int index) {
        if (index < 0 || index >= size) {
            return -1; // or throw an exception
        }
        Node* curr = dummy->next;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }

    void addAtHead(int val) {
        Node* newNode = new Node(val);
        newNode->next = dummy->next;
        dummy->next = newNode;
        if (tail == NULL) {
            tail = newNode;
        }
        size++;
    }

    void addAtTail(int val) {
        Node* newNode = new Node(val);
        if (tail == NULL) {
            dummy->next = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        size++;
    }

    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) {
            return; // or throw an exception
        }
        if (index == 0) {
            addAtHead(val);
            return;
        }
        if (index == size) {
            addAtTail(val);
            return;
        }
        Node* curr = dummy;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        Node* newNode = new Node(val);
        newNode->next = curr->next;
        curr->next = newNode;
        size++;
    }

    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return; // or throw an exception
        }
        Node* curr = dummy;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        Node* temp = curr->next;
        curr->next = curr->next->next;
        if (temp == tail) {
            tail = curr;
        }
        delete temp;
        size--;
    }

private:
    Node* dummy;
    Node* tail;
    int size;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `get`, `addAtIndex`, and `deleteAtIndex` methods, where $n$ is the size of the linked list. $O(1)$ for `addAtHead` and `addAtTail` methods.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the linked list.
> - **Optimality proof:** The time complexity is $O(n)$ for `get`, `addAtIndex`, and `deleteAtIndex` methods because we need to traverse the linked list to find the desired node. The space complexity is $O(n)$ because we need to store all the nodes in the linked list. The use of a dummy node simplifies the implementation and reduces the number of edge cases.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: linked lists, node insertion, node deletion.
- Problem-solving patterns identified: using a dummy node to simplify the implementation.
- Optimization techniques learned: reducing the number of edge cases by using a dummy node.
- Similar problems to practice: implementing a doubly linked list, implementing a stack or queue using a linked list.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to update the `tail` pointer when adding or deleting nodes.
- Edge cases to watch for: handling empty linked lists, handling linked lists with a single node.
- Performance pitfalls: using a brute force approach without considering the time complexity.
- Testing considerations: testing the implementation with different input scenarios, testing the implementation with edge cases.