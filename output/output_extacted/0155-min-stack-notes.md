## Min Stack

**Problem Link:** https://leetcode.com/problems/min-stack/description

**Problem Statement:**
- Input format and constraints: The problem involves designing a stack that supports two operations: `push` and `pop`, and a `getMin` function to retrieve the minimum element in the stack at any point.
- Expected output format: The stack should return the minimum element in the stack when `getMin` is called.
- Key requirements and edge cases to consider: The stack should handle edge cases such as empty stack, duplicate minimum elements, and the `getMin` function should return the minimum element after each `push` and `pop` operation.
- Example test cases with explanations: 
  - `["MinStack","push","push","push","getMin","pop","top","getMin"]` with inputs `[[],[-2],[0],[-3],[],[],[],[]]`
  - `["MinStack","push","push","getMin","getMin"]` with inputs `[[],[1],[2],[],[]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to create a stack and use a separate data structure (like a vector) to keep track of the minimum elements seen so far.
- Step-by-step breakdown of the solution: 
  1. Create a stack to store the elements.
  2. Create a separate vector to store the minimum elements seen so far.
  3. When `push` is called, add the element to the stack and update the minimum vector if necessary.
  4. When `pop` is called, remove the top element from the stack and update the minimum vector if necessary.
  5. When `getMin` is called, return the last element in the minimum vector.
- Why this approach comes to mind first: This approach seems straightforward because it involves using a separate data structure to keep track of the minimum elements.

```cpp
class MinStack {
private:
    stack<int> s;
    vector<int> minVec;

public:
    MinStack() {}

    void push(int val) {
        s.push(val);
        if (minVec.empty() || val <= minVec.back()) {
            minVec.push_back(val);
        }
    }

    void pop() {
        if (!s.empty()) {
            if (s.top() == minVec.back()) {
                minVec.pop_back();
            }
            s.pop();
        }
    }

    int top() {
        return s.top();
    }

    int getMin() {
        return minVec.back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `push`, `pop`, and `getMin` operations because we're using a stack and a vector, and all operations are constant time.
> - **Space Complexity:** $O(n)$ where $n$ is the number of elements in the stack because we're using a separate vector to store the minimum elements.
> - **Why these complexities occur:** The time complexity is constant because stack and vector operations are $O(1)$, and the space complexity is linear because we're storing the minimum elements in a separate vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using a separate vector to store the minimum elements, we can use a second stack to store the minimum elements seen so far.
- Detailed breakdown of the approach: 
  1. Create two stacks: one for the elements and one for the minimum elements.
  2. When `push` is called, add the element to the element stack and update the minimum stack if necessary.
  3. When `pop` is called, remove the top element from the element stack and update the minimum stack if necessary.
  4. When `getMin` is called, return the top element from the minimum stack.
- Proof of optimality: This approach is optimal because we're using a constant amount of extra space to store the minimum elements, and all operations are constant time.

```cpp
class MinStack {
private:
    stack<int> s;
    stack<int> minStack;

public:
    MinStack() {}

    void push(int val) {
        s.push(val);
        if (minStack.empty() || val <= minStack.top()) {
            minStack.push(val);
        }
    }

    void pop() {
        if (!s.empty()) {
            if (s.top() == minStack.top()) {
                minStack.pop();
            }
            s.pop();
        }
    }

    int top() {
        return s.top();
    }

    int getMin() {
        return minStack.top();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `push`, `pop`, and `getMin` operations because we're using two stacks, and all operations are constant time.
> - **Space Complexity:** $O(n)$ where $n$ is the number of elements in the stack because we're using a second stack to store the minimum elements.
> - **Optimality proof:** This approach is optimal because we're using a constant amount of extra space to store the minimum elements, and all operations are constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a second stack to store the minimum elements seen so far.
- Problem-solving patterns identified: Using a separate data structure to store additional information.
- Optimization techniques learned: Reducing the space complexity by using a second stack instead of a vector.
- Similar problems to practice: Other problems involving stacks and minimum/maximum elements.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the minimum stack when popping an element.
- Edge cases to watch for: Empty stack, duplicate minimum elements.
- Performance pitfalls: Using a vector instead of a stack to store the minimum elements, which can lead to slower performance.
- Testing considerations: Testing the `getMin` function after each `push` and `pop` operation to ensure it returns the correct minimum element.