## Design Front Middle Back Queue
**Problem Link:** https://leetcode.com/problems/design-front-middle-back-queue/description

**Problem Statement:**
- Input format and constraints: The problem asks to design a queue with three operations: `pushFront`, `pushMiddle`, and `pushBack` to add elements to the front, middle, and back of the queue respectively, and two operations: `popFront` and `popBack` to remove elements from the front and back of the queue respectively.
- Expected output format: The queue should support the above operations and return the removed element when `popFront` or `popBack` is called.
- Key requirements and edge cases to consider: The queue should handle cases where the queue is empty, and the `pushMiddle` operation should insert the element at the middle index of the queue.
- Example test cases with explanations:
  - `FrontMiddleBackQueue q; q.pushFront(1); q.pushBack(2); q.pushMiddle(3); q.pushMiddle(4); q.popFront(); q.popMiddle(); q.popBack();`
  - The queue should handle cases where the queue is empty and return -1 when `popFront` or `popBack` is called on an empty queue.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use a linked list to implement the queue. This is because linked lists allow for efficient insertion and deletion of elements at any position.
- Step-by-step breakdown of the solution:
  1. Create a linked list with a `head` and `tail` pointer.
  2. Implement the `pushFront` operation by inserting a new node at the beginning of the linked list.
  3. Implement the `pushBack` operation by inserting a new node at the end of the linked list.
  4. Implement the `pushMiddle` operation by finding the middle node of the linked list and inserting a new node after it.
  5. Implement the `popFront` operation by removing the first node from the linked list.
  6. Implement the `popBack` operation by removing the last node from the linked list.
- Why this approach comes to mind first: This approach is intuitive because linked lists are a natural fit for implementing queues with insertion and deletion operations at arbitrary positions.

```cpp
class FrontMiddleBackQueue {
public:
    FrontMiddleBackQueue() {}
    
    void pushFront(int val) {
        head = new ListNode(val, head);
    }
    
    void pushMiddle(int val) {
        if (!head || !head->next) {
            pushFront(val);
            return;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* newNode = new ListNode(val, slow->next);
        slow->next = newNode;
    }
    
    void pushBack(int val) {
        if (!head) {
            pushFront(val);
            return;
        }
        ListNode* curr = head;
        while (curr->next) {
            curr = curr->next;
        }
        curr->next = new ListNode(val);
    }
    
    int popFront() {
        if (!head) return -1;
        int val = head->val;
        head = head->next;
        return val;
    }
    
    int popMiddle() {
        if (!head) return -1;
        if (!head->next) return popFront();
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        int val = slow->next->val;
        slow->next = slow->next->next;
        return val;
    }
    
    int popBack() {
        if (!head) return -1;
        if (!head->next) return popFront();
        ListNode* curr = head;
        while (curr->next->next) {
            curr = curr->next;
        }
        int val = curr->next->val;
        curr->next = nullptr;
        return val;
    }
private:
    struct ListNode {
        int val;
        ListNode* next;
        ListNode(int x, ListNode* next = nullptr) : val(x), next(next) {}
    };
    ListNode* head;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `pushMiddle`, `popMiddle` operations, where $n$ is the number of elements in the queue. $O(1)$ for `pushFront`, `pushBack`, `popFront`, `popBack` operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the queue.
> - **Why these complexities occur:** The time complexity for `pushMiddle` and `popMiddle` operations is $O(n)$ because we need to find the middle node of the linked list, which takes linear time. The space complexity is $O(n)$ because we need to store $n$ elements in the linked list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using two deques to store the front and back halves of the queue. This allows for efficient insertion and deletion of elements at the front, middle, and back of the queue.
- Detailed breakdown of the approach:
  1. Create two deques `front` and `back` to store the front and back halves of the queue.
  2. Implement the `pushFront` operation by pushing the element to the front of the `front` deque.
  3. Implement the `pushBack` operation by pushing the element to the back of the `back` deque.
  4. Implement the `pushMiddle` operation by checking if the `front` deque has more elements than the `back` deque. If so, pop the last element from the `front` deque and push it to the front of the `back` deque. Then, push the new element to the back of the `front` deque.
  5. Implement the `popFront` operation by popping the front element from the `front` deque. If the `front` deque is empty, pop the front element from the `back` deque and move all elements from the `back` deque to the `front` deque.
  6. Implement the `popBack` operation by popping the back element from the `back` deque. If the `back` deque is empty, pop the back element from the `front` deque and move all elements from the `front` deque to the `back` deque.
- Proof of optimality: This approach is optimal because it allows for efficient insertion and deletion of elements at the front, middle, and back of the queue, with an average time complexity of $O(1)$ for all operations.

```cpp
class FrontMiddleBackQueue {
public:
    FrontMiddleBackQueue() {}
    
    void pushFront(int val) {
        front.push_front(val);
        balance();
    }
    
    void pushMiddle(int val) {
        if (front.size() > back.size()) {
            back.push_front(front.back());
            front.pop_back();
        }
        front.push_back(val);
        balance();
    }
    
    void pushBack(int val) {
        back.push_back(val);
        balance();
    }
    
    int popFront() {
        if (front.empty()) {
            if (back.empty()) return -1;
            front = back;
            back.clear();
            balance();
        }
        int val = front.front();
        front.pop_front();
        return val;
    }
    
    int popMiddle() {
        if (front.empty()) {
            if (back.empty()) return -1;
            front = back;
            back.clear();
            balance();
        }
        int val = front.back();
        front.pop_back();
        return val;
    }
    
    int popBack() {
        if (back.empty()) {
            if (front.empty()) return -1;
            back = front;
            front.clear();
            balance();
        }
        int val = back.back();
        back.pop_back();
        return val;
    }
private:
    deque<int> front;
    deque<int> back;
    
    void balance() {
        if (front.size() > back.size() + 1) {
            back.push_front(front.back());
            front.pop_back();
        } else if (back.size() > front.size()) {
            front.push_back(back.front());
            back.pop_front();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the queue.
> - **Optimality proof:** This approach is optimal because it allows for efficient insertion and deletion of elements at the front, middle, and back of the queue, with an average time complexity of $O(1)$ for all operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using two deques to implement a queue with efficient insertion and deletion of elements at the front, middle, and back.
- Problem-solving patterns identified: Balancing the size of the two deques to ensure efficient operations.
- Optimization techniques learned: Using two deques to reduce the time complexity of operations.
- Similar problems to practice: Implementing a queue with a similar set of operations using a different data structure, such as a linked list or a vector.

**Mistakes to Avoid:**
- Common implementation errors: Not balancing the size of the two deques, which can lead to inefficient operations.
- Edge cases to watch for: Handling the case where one of the deques is empty, and ensuring that the queue is properly initialized.
- Performance pitfalls: Not using the correct data structure for the problem, which can lead to inefficient operations.
- Testing considerations: Thoroughly testing the queue with a variety of operations and edge cases to ensure correctness and efficiency.