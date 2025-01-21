## Implement Stack Using Queues
**Problem Link:** https://leetcode.com/problems/implement-stack-using-queues/description

**Problem Statement:**
- Input format: `MyStack()`, `void push(int x)`, `int pop()`, `int top()`, `boolean empty()`
- Constraints: $0 \leq x \leq 100$, $0 \leq \text{Number of operations} \leq 100$
- Expected output format: Stack operations result
- Key requirements and edge cases to consider: Handling multiple `push`, `pop`, `top`, and `empty` operations, ensuring LIFO order
- Example test cases with explanations:
  - `["MyStack", "push", "push", "top", "pop", "empty"]`, `[[], [1], [2], [], [], []]`
  - `["MyStack", "push", "push", "pop", "empty"]`, `[[], [1], [2], [], []]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use two queues to implement a stack, with one queue storing the elements and the other queue helping to maintain the LIFO order
- Step-by-step breakdown of the solution:
  1. Create two queues, `q1` and `q2`, to store the elements
  2. When pushing an element, add it to the end of `q1`
  3. When popping an element, move all elements from `q1` to `q2` except the last one, which is the top element
  4. When getting the top element, move all elements from `q1` to `q2` except the last one, which is the top element
  5. When checking if the stack is empty, check if `q1` is empty
- Why this approach comes to mind first: It's a straightforward way to implement a stack using queues, but it's not efficient

```cpp
class MyStack {
public:
    queue<int> q1, q2;
    MyStack() {}
    void push(int x) {
        q1.push(x);
    }
    int pop() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int top = q1.front();
        q1.pop();
        q1.swap(q2);
        return top;
    }
    int top() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int top = q1.front();
        q2.push(top);
        q1.pop();
        q1.swap(q2);
        return top;
    }
    bool empty() {
        return q1.empty();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `push`, $O(n)$ for `pop`, $O(n)$ for `top`, $O(1)$ for `empty`
> - **Space Complexity:** $O(n)$
> - **Why these complexities occur:** The `push` operation is efficient because we simply add the element to the end of the queue. However, the `pop` and `top` operations are inefficient because we need to move all elements from one queue to another to maintain the LIFO order.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of moving all elements from one queue to another for `pop` and `top` operations, we can maintain the LIFO order by always adding new elements to the front of the queue
- Detailed breakdown of the approach:
  1. Create a queue `q` to store the elements
  2. When pushing an element, add it to the front of `q` by moving all existing elements to a temporary queue, adding the new element, and then moving the elements back to `q`
  3. When popping an element, simply remove the front element from `q`
  4. When getting the top element, simply return the front element from `q`
  5. When checking if the stack is empty, check if `q` is empty
- Proof of optimality: This approach is optimal because we only need to move elements when pushing a new element, and we can do this in $O(n)$ time. The `pop` and `top` operations are now $O(1)$.

```cpp
class MyStack {
public:
    queue<int> q;
    MyStack() {}
    void push(int x) {
        queue<int> temp;
        temp.push(x);
        while (!q.empty()) {
            temp.push(q.front());
            q.pop();
        }
        q = temp;
    }
    int pop() {
        int top = q.front();
        q.pop();
        return top;
    }
    int top() {
        return q.front();
    }
    bool empty() {
        return q.empty();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `push`, $O(1)$ for `pop`, $O(1)$ for `top`, $O(1)$ for `empty`
> - **Space Complexity:** $O(n)$
> - **Optimality proof:** This approach is optimal because we minimize the number of operations required to maintain the LIFO order. We only need to move elements when pushing a new element, and we can do this in $O(n)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Implementing a stack using queues, maintaining LIFO order
- Problem-solving patterns identified: Using temporary queues to maintain order
- Optimization techniques learned: Minimizing the number of operations required to maintain order
- Similar problems to practice: Implementing a queue using stacks, implementing a priority queue using a binary heap

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for empty queues
- Edge cases to watch for: Empty queues, single-element queues
- Performance pitfalls: Not minimizing the number of operations required to maintain order
- Testing considerations: Testing with different input sizes, testing with different operations (push, pop, top, empty)