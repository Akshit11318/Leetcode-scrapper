## Design a Stack with Increment Operation

**Problem Link:** https://leetcode.com/problems/design-a-stack-with-increment-operation/description

**Problem Statement:**
- The problem requires designing a stack that supports two operations: `push(x)`, which pushes an element `x` onto the stack, and `pop()`, which removes the element on top of the stack and returns it. Additionally, there's an `increment(k, val)` operation, which increments the bottom `k` elements of the stack by a value `val`.
- The input format consists of a series of these operations.
- The expected output is the result of each `pop()` operation.
- Key requirements include handling edge cases such as attempting to pop from an empty stack or incrementing more elements than are present in the stack.
- Example test cases include pushing elements, popping elements, and incrementing elements to demonstrate the functionality of the stack.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves using a standard stack data structure and implementing the `increment(k, val)` operation by popping elements from the stack, incrementing them, and then pushing them back onto the stack.
- This approach comes to mind first because it directly addresses the problem statement without considering optimization.

```cpp
class CustomStack {
private:
    vector<int> stack;
    int maxSize;

public:
    CustomStack(int maxSize) {
        this->maxSize = maxSize;
    }

    void push(int x) {
        if (stack.size() < maxSize) {
            stack.push_back(x);
        }
    }

    int pop() {
        if (stack.empty()) {
            return -1;
        }
        int top = stack.back();
        stack.pop_back();
        return top;
    }

    void increment(int k, int val) {
        for (int i = 0; i < min(k, (int)stack.size()); i++) {
            stack[i] += val;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$ for the `increment(k, val)` operation in the worst case, where $k$ is the number of elements to increment. The `push(x)` and `pop()` operations are $O(1)$.
> - **Space Complexity:** $O(n)$, where $n$ is the maximum size of the stack.
> - **Why these complexities occur:** The time complexity of $O(k)$ for `increment(k, val)` occurs because in the worst case, we might need to iterate through all elements up to $k$. The space complexity is $O(n)$ because we need to store all elements in the stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is realizing that we don't need to actually increment the elements in the stack when the `increment(k, val)` operation is called. Instead, we can store the increments separately and apply them when elements are popped from the stack.
- This approach avoids the need to iterate through the stack for each `increment(k, val)` operation, reducing the time complexity.

```cpp
class CustomStack {
private:
    vector<int> stack;
    vector<int> increments;
    int maxSize;

public:
    CustomStack(int maxSize) {
        this->maxSize = maxSize;
        increments.resize(maxSize, 0);
    }

    void push(int x) {
        if (stack.size() < maxSize) {
            stack.push_back(x);
            increments.push_back(0);
        }
    }

    int pop() {
        if (stack.empty()) {
            return -1;
        }
        int top = stack.back() + increments.back();
        stack.pop_back();
        increments.pop_back();
        return top;
    }

    void increment(int k, int val) {
        if (!stack.empty()) {
            int index = min(k, (int)stack.size()) - 1;
            if (index >= 0) {
                increments[index] += val;
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations (`push(x)`, `pop()`, and `increment(k, val)`), because we only manipulate the top element or the last increment value.
> - **Space Complexity:** $O(n)$, where $n$ is the maximum size of the stack, because we store the increments separately.
> - **Optimality proof:** This is the optimal solution because we've reduced the time complexity of all operations to constant time, and the space complexity remains linear with respect to the maximum stack size.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a separate data structure (the `increments` vector) to store and manage increments to the stack elements, allowing for efficient application of these increments when elements are popped.
- The problem-solving pattern identified is the avoidance of unnecessary work (in this case, iterating through the stack for each increment operation) by delaying the application of increments until necessary.
- The optimization technique learned is to consider alternative representations of the problem data that can reduce computational complexity.

**Mistakes to Avoid:**
- A common implementation error is forgetting to handle edge cases such as an empty stack or attempting to increment more elements than are present in the stack.
- Performance pitfalls include using inefficient data structures or algorithms for the operations, leading to higher than necessary time complexities.