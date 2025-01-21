## Design Most Recently Used (MRU) Queue

**Problem Link:** https://leetcode.com/problems/design-most-recently-used-queue/description

**Problem Statement:**
- The input format includes a series of operations: `MRUQueue(int k)` initializes the queue with a given `k`, `enqueue(int value)` adds `value` to the queue, and `dequeue()` removes and returns the most recently added element.
- The expected output is the result of each `dequeue()` operation.
- Key requirements include maintaining the order of elements based on their most recent addition and handling edge cases such as an empty queue.
- Example test cases include initializing a queue, enqueuing values, and dequeuing elements to demonstrate the MRU behavior.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves using a simple queue data structure and manually shifting elements upon each `enqueue` operation to maintain the most recently added elements at the front.
- This approach involves checking the queue's size upon each operation and shifting elements accordingly.

```cpp
class MRUQueue {
private:
    queue<int> q;
public:
    MRUQueue(int k) {}
    
    void enqueue(int value) {
        q.push(value);
    }
    
    int dequeue() {
        if (q.empty()) return -1; // Assuming -1 for empty queue
        int front = q.front();
        q.pop();
        return front;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `enqueue` and $O(1)$ for `dequeue`, because both operations are performed at the ends of the queue.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the queue, as we are storing all elements in the queue.
> - **Why these complexities occur:** The queue operations are efficient because they only involve adding or removing elements from the ends.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a data structure that allows for efficient insertion and removal of elements while maintaining their order based on the most recent addition. A `deque` (double-ended queue) is ideal for this purpose.
- The `deque` allows for $O(1)$ insertion and removal at both ends, making it optimal for implementing an MRU queue.

```cpp
#include <deque>

class MRUQueue {
private:
    std::deque<int> dq;
public:
    MRUQueue(int k) {}
    
    void enqueue(int value) {
        dq.push_back(value);
    }
    
    int dequeue() {
        if (dq.empty()) return -1; // Assuming -1 for empty queue
        int front = dq.front();
        dq.pop_front();
        return front;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for both `enqueue` and `dequeue`, because `deque` supports constant time insertion and removal at both ends.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the queue.
> - **Optimality proof:** This is optimal because we are using the most efficient data structure for the problem, allowing for constant time operations for both `enqueue` and `dequeue`.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right data structure for the problem.
- Understanding the trade-offs between different data structures (e.g., `queue` vs. `deque`).
- Recognizing the need for efficient insertion and removal operations.

**Mistakes to Avoid:**
- Not considering the efficiency of operations when selecting a data structure.
- Failing to handle edge cases such as an empty queue.
- Not validating inputs to ensure they are within expected bounds.