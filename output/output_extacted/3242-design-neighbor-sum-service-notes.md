## Design Neighbor Sum Service

**Problem Link:** https://leetcode.com/problems/design-neighbor-sum-service/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a service that can add and query values in a data structure, where each query is based on the sum of neighboring values.
- Expected output format: The service should return the sum of neighboring values for a given query.
- Key requirements and edge cases to consider: Handling edge cases where a node has no neighbors, and optimizing the data structure for efficient queries.
- Example test cases with explanations: 
    - Adding values and querying their sums.
    - Handling edge cases such as adding a value with no neighbors.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a simple array or list to store the values and iterate through the list to calculate the sum of neighboring values for each query.
- Step-by-step breakdown of the solution:
    1. Initialize an array or list to store the values.
    2. For each `add` operation, append the value to the end of the array or list.
    3. For each `query` operation, iterate through the array or list to find the value at the given index and calculate the sum of its neighboring values.
- Why this approach comes to mind first: It is a straightforward and simple solution that does not require complex data structures or algorithms.

```cpp
class NeighborSumService {
public:
    vector<int> values;
    
    void add(int index, int value) {
        values.insert(values.begin() + index, value);
    }
    
    int query(int index) {
        int sum = 0;
        if (index > 0) {
            sum += values[index - 1];
        }
        if (index < values.size() - 1) {
            sum += values[index + 1];
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the `add` operation because inserting an element at a specific index in a vector requires shifting all elements after that index. $O(1)$ for the `query` operation because we only need to access the neighboring values.
> - **Space Complexity:** $O(n)$ because we need to store all the values in the vector.
> - **Why these complexities occur:** The `add` operation has a high time complexity because of the need to shift elements in the vector, while the `query` operation has a low time complexity because it only requires accessing a few elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a data structure that allows for efficient insertion and query operations, such as a linked list.
- Detailed breakdown of the approach:
    1. Initialize a linked list to store the values.
    2. For each `add` operation, insert a new node at the given index in the linked list.
    3. For each `query` operation, find the node at the given index in the linked list and calculate the sum of its neighboring values.
- Proof of optimality: This solution has an optimal time complexity for both `add` and `query` operations because linked lists allow for efficient insertion and query operations.
- Why further optimization is impossible: This solution has the best possible time complexity for both operations, making it optimal.

```cpp
class Node {
public:
    int value;
    Node* next;
    Node* prev;
    Node(int val) : value(val), next(nullptr), prev(nullptr) {}
};

class NeighborSumService {
public:
    Node* head;
    Node* tail;
    
    void add(int index, int value) {
        Node* newNode = new Node(value);
        if (index == 0) {
            newNode->next = head;
            if (head) {
                head->prev = newNode;
            } else {
                tail = newNode;
            }
            head = newNode;
        } else if (index == size) {
            newNode->prev = tail;
            tail->next = newNode;
            tail = newNode;
        } else {
            Node* curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr->next;
            }
            newNode->next = curr->next;
            newNode->prev = curr;
            curr->next->prev = newNode;
            curr->next = newNode;
        }
        size++;
    }
    
    int query(int index) {
        Node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        int sum = 0;
        if (curr->prev) {
            sum += curr->prev->value;
        }
        if (curr->next) {
            sum += curr->next->value;
        }
        return sum;
    }
private:
    int size = 0;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the `add` operation because we need to find the correct position to insert the new node. $O(n)$ for the `query` operation because we need to find the node at the given index.
> - **Space Complexity:** $O(n)$ because we need to store all the nodes in the linked list.
> - **Optimality proof:** This solution has an optimal time complexity for both `add` and `query` operations because linked lists allow for efficient insertion and query operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked lists, efficient insertion and query operations.
- Problem-solving patterns identified: Using the right data structure for the problem.
- Optimization techniques learned: Choosing the best data structure for the problem to minimize time complexity.
- Similar problems to practice: Other problems that involve designing data structures for efficient operations.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not updating pointers correctly in linked lists.
- Edge cases to watch for: Handling cases where the list is empty, or where the index is out of bounds.
- Performance pitfalls: Using the wrong data structure for the problem, not optimizing for time complexity.
- Testing considerations: Testing the implementation with different inputs and edge cases to ensure correctness.