## Implement Queue Using Stacks

**Problem Link:** https://leetcode.com/problems/implement-queue-using-stacks/description

**Problem Statement:**
- Input format and constraints: The problem requires implementing a queue using two stacks. The queue should support `push(x)`, `pop()`, and `empty()` operations, where `x` is the element to be pushed into the queue.
- Expected output format: The output of `pop()` should be the element that was added to the queue first, and `empty()` should return `true` if the queue is empty, `false` otherwise.
- Key requirements and edge cases to consider: The queue should follow the First-In-First-Out (FIFO) principle, and the `pop()` operation should remove and return the front element of the queue.
- Example test cases with explanations:
    - `MyQueue queue = new MyQueue()`: Initializes the queue.
    - `queue.push(1)`: Pushes the element `1` into the queue.
    - `queue.push(2)`: Pushes the element `2` into the queue.
    - `queue.peek()`: Returns `1`, which is the front element of the queue.
    - `queue.pop()`: Removes and returns `1`, which is the front element of the queue.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use one stack to store the elements and another stack to keep track of the order of elements.
- Step-by-step breakdown of the solution: 
    1. When `push(x)` is called, push the element `x` onto the first stack.
    2. When `pop()` is called, pop all elements from the first stack and push them onto the second stack, except for the last element, which is the front element of the queue. Then, pop this element from the first stack and return it.
    3. When `empty()` is called, check if the first stack is empty. If it is, return `true`, indicating that the queue is empty. Otherwise, return `false`.
- Why this approach comes to mind first: This approach seems straightforward because it uses two stacks to implement the queue, but it is inefficient because it requires popping all elements from one stack and pushing them onto another stack for each `pop()` operation.

```cpp
class MyQueue {
private:
    stack<int> stack1;
    stack<int> stack2;

public:
    MyQueue() {}

    void push(int x) {
        stack1.push(x);
    }

    int pop() {
        while (stack1.size() > 1) {
            stack2.push(stack1.top());
            stack1.pop();
        }
        int front = stack1.top();
        stack1.pop();
        while (!stack2.empty()) {
            stack1.push(stack2.top());
            stack2.pop();
        }
        return front;
    }

    int peek() {
        while (stack1.size() > 1) {
            stack2.push(stack1.top());
            stack1.pop();
        }
        int front = stack1.top();
        while (!stack2.empty()) {
            stack1.push(stack2.top());
            stack2.pop();
        }
        return front;
    }

    bool empty() {
        return stack1.empty();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `push(x)`, $O(n)$ for `pop()`, $O(n)$ for `peek()`, and $O(1)$ for `empty()`, where $n$ is the number of elements in the queue. The `pop()` and `peek()` operations have a high time complexity because they require popping all elements from one stack and pushing them onto another stack.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the queue. This is because we use two stacks to store the elements.
> - **Why these complexities occur:** The high time complexity of the `pop()` and `peek()` operations occurs because we need to pop all elements from one stack and push them onto another stack to maintain the correct order of elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using two stacks to store the elements and keep track of the order, we can use two stacks to implement the queue directly. One stack will be used to store the new elements, and the other stack will be used to store the elements in the correct order.
- Detailed breakdown of the approach:
    1. When `push(x)` is called, push the element `x` onto the first stack.
    2. When `pop()` is called, if the second stack is empty, pop all elements from the first stack and push them onto the second stack. Then, pop the top element from the second stack and return it.
    3. When `empty()` is called, check if both stacks are empty. If they are, return `true`, indicating that the queue is empty. Otherwise, return `false`.
- Proof of optimality: This approach is optimal because it uses two stacks to implement the queue directly, without requiring any additional data structures. The time complexity of the `push(x)` operation is $O(1)$, and the time complexity of the `pop()` operation is amortized $O(1)$, because we only need to pop all elements from one stack and push them onto another stack when the second stack is empty.

```cpp
class MyQueue {
private:
    stack<int> stack1;
    stack<int> stack2;

public:
    MyQueue() {}

    void push(int x) {
        stack1.push(x);
    }

    int pop() {
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        int front = stack2.top();
        stack2.pop();
        return front;
    }

    int peek() {
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        return stack2.top();
    }

    bool empty() {
        return stack1.empty() && stack2.empty();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `push(x)`, $O(1)$ for `pop()`, $O(1)$ for `peek()`, and $O(1)$ for `empty()$. The `pop()` operation has an amortized time complexity of $O(1)$ because we only need to pop all elements from one stack and push them onto another stack when the second stack is empty.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the queue. This is because we use two stacks to store the elements.
> - **Optimality proof:** This approach is optimal because it uses two stacks to implement the queue directly, without requiring any additional data structures. The time complexity of the `push(x)` operation is $O(1)$, and the time complexity of the `pop()` operation is amortized $O(1)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of stacks to implement a queue, and the importance of considering the order of elements when implementing a queue.
- Problem-solving patterns identified: The problem requires identifying the key insight that leads to the optimal solution, which is using two stacks to implement the queue directly.
- Optimization techniques learned: The problem demonstrates the use of amortized analysis to optimize the time complexity of the `pop()` operation.
- Similar problems to practice: Other problems that involve implementing data structures using other data structures, such as implementing a stack using a queue.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is to use a single stack to implement the queue, which can lead to incorrect results because the order of elements is not maintained.
- Edge cases to watch for: One edge case to watch for is when the queue is empty, and the `pop()` operation is called. In this case, the implementation should return an error or throw an exception.
- Performance pitfalls: One performance pitfall is to use a naive implementation that requires popping all elements from one stack and pushing them onto another stack for each `pop()` operation, which can lead to a high time complexity.
- Testing considerations: The implementation should be tested with various input scenarios, including empty queues, queues with a single element, and queues with multiple elements.