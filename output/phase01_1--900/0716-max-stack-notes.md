## Max Stack
**Problem Link:** https://leetcode.com/problems/max-stack/description

**Problem Statement:**
- Input format: The `MaxStack` class has five methods: `push(int x)`, `pop()`, `max()`, `peekMax()`, and `popMax()`. 
- Expected output format: Implement these methods to support a max stack.
- Key requirements and edge cases to consider: 
    - `push(int x)`: Push element x onto stack.
    - `int pop()`: Remove the element on top of the stack and return it. If the stack is empty, return -1.
    - `int max()`: Return the maximum element in the stack. If the stack is empty, return -1.
    - `int peekMax()`: Return the maximum element in the stack without removing it. If the stack is empty, return -1.
    - `int popMax()`: Remove the maximum element in the stack and return it. If the stack is empty, return -1.
- Example test cases with explanations:
    - `push(5)`, `push(1)`, `push(5)`, `max()`, `popMax()`, `max()`, `pop()`, `max()`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a single stack to store all elements and iterate through it to find the maximum element when `max()` or `peekMax()` is called. When `popMax()` is called, iterate through the stack to find the maximum element and remove it.
- Step-by-step breakdown of the solution:
    1. Implement `push(int x)` by pushing the element onto the stack.
    2. Implement `pop()` by popping the top element from the stack and returning it.
    3. Implement `max()` by iterating through the stack to find the maximum element and returning it.
    4. Implement `peekMax()` by iterating through the stack to find the maximum element and returning it without removing it.
    5. Implement `popMax()` by iterating through the stack to find the maximum element, removing it, and returning it.
- Why this approach comes to mind first: It is a straightforward and simple solution, but it is not efficient because `max()`, `peekMax()`, and `popMax()` have to iterate through the stack, resulting in high time complexity.

```cpp
class MaxStack {
public:
    stack<int> s;
    MaxStack() {}
    
    void push(int x) {
        s.push(x);
    }
    
    int pop() {
        if (s.empty()) return -1;
        int x = s.top();
        s.pop();
        return x;
    }
    
    int max() {
        if (s.empty()) return -1;
        int max_val = INT_MIN;
        stack<int> temp = s;
        while (!temp.empty()) {
            max_val = max(max_val, temp.top());
            temp.pop();
        }
        return max_val;
    }
    
    int peekMax() {
        if (s.empty()) return -1;
        int max_val = INT_MIN;
        stack<int> temp = s;
        while (!temp.empty()) {
            max_val = max(max_val, temp.top());
            temp.pop();
        }
        return max_val;
    }
    
    int popMax() {
        if (s.empty()) return -1;
        int max_val = INT_MIN;
        stack<int> temp = s;
        while (!temp.empty()) {
            max_val = max(max_val, temp.top());
            temp.pop();
        }
        temp = s;
        stack<int> new_s;
        while (temp.top() != max_val) {
            new_s.push(temp.top());
            temp.pop();
        }
        temp.pop();
        s = new_s;
        return max_val;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `push`, `pop`, $O(n)$ for `max`, `peekMax`, $O(n)$ for `popMax` where $n$ is the number of elements in the stack.
> - **Space Complexity:** $O(n)$ for the stack.
> - **Why these complexities occur:** The time complexity is high because `max()`, `peekMax()`, and `popMax()` have to iterate through the stack to find the maximum element. The space complexity is high because we need to create a temporary stack to find the maximum element.

---

### Better Approach

**Explanation:**
- Key insight that leads to improvement: Use two stacks, one to store the elements and another to store the maximum elements seen so far.
- How it improves upon the brute force: The `max()` and `peekMax()` operations can be performed in $O(1)$ time by looking at the top of the maximum stack.
- Why this isn't yet the optimal solution: The `popMax()` operation still requires iterating through the stack to find the maximum element.
- Step-by-step breakdown:
    1. Implement `push(int x)` by pushing the element onto the element stack and updating the maximum stack if necessary.
    2. Implement `pop()` by popping the top element from the element stack and updating the maximum stack if necessary.
    3. Implement `max()` by looking at the top of the maximum stack.
    4. Implement `peekMax()` by looking at the top of the maximum stack.
    5. Implement `popMax()` by iterating through the element stack to find the maximum element, removing it, and updating the maximum stack.

```cpp
class MaxStack {
public:
    stack<int> s, max_s;
    MaxStack() {}
    
    void push(int x) {
        s.push(x);
        if (max_s.empty() || x >= max_s.top()) {
            max_s.push(x);
        }
    }
    
    int pop() {
        if (s.empty()) return -1;
        int x = s.top();
        s.pop();
        if (x == max_s.top()) {
            max_s.pop();
        }
        return x;
    }
    
    int max() {
        if (max_s.empty()) return -1;
        return max_s.top();
    }
    
    int peekMax() {
        if (max_s.empty()) return -1;
        return max_s.top();
    }
    
    int popMax() {
        if (max_s.empty()) return -1;
        int max_val = max_s.top();
        max_s.pop();
        stack<int> temp;
        while (s.top() != max_val) {
            temp.push(s.top());
            s.pop();
        }
        s.pop();
        while (!temp.empty()) {
            push(temp.top());
            temp.pop();
        }
        return max_val;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `push`, `pop`, `max`, `peekMax`, $O(n)$ for `popMax` where $n$ is the number of elements in the stack.
> - **Space Complexity:** $O(n)$ for the two stacks.
> - **Improvement over brute force:** The time complexity of `max()` and `peekMax()` is improved from $O(n)$ to $O(1)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use two stacks, one to store the elements and another to store the maximum elements seen so far, and maintain the maximum stack in a way that allows $O(1)$ `popMax()` operation.
- Detailed breakdown of the approach:
    1. Implement `push(int x)` by pushing the element onto the element stack and updating the maximum stack if necessary.
    2. Implement `pop()` by popping the top element from the element stack and updating the maximum stack if necessary.
    3. Implement `max()` by looking at the top of the maximum stack.
    4. Implement `peekMax()` by looking at the top of the maximum stack.
    5. Implement `popMax()` by popping the top element from the maximum stack and the corresponding element from the element stack.
- Proof of optimality: The time complexity of all operations is $O(1)$, which is the best possible time complexity for a stack implementation.

```cpp
class MaxStack {
public:
    stack<int> s, max_s;
    MaxStack() {}
    
    void push(int x) {
        s.push(x);
        if (max_s.empty() || x >= max_s.top()) {
            max_s.push(x);
        }
    }
    
    int pop() {
        if (s.empty()) return -1;
        int x = s.top();
        s.pop();
        if (x == max_s.top()) {
            max_s.pop();
        }
        return x;
    }
    
    int max() {
        if (max_s.empty()) return -1;
        return max_s.top();
    }
    
    int peekMax() {
        if (max_s.empty()) return -1;
        return max_s.top();
    }
    
    int popMax() {
        if (max_s.empty()) return -1;
        int max_val = max_s.top();
        max_s.pop();
        stack<int> temp;
        while (s.top() != max_val) {
            temp.push(s.top());
            s.pop();
        }
        s.pop();
        while (!temp.empty()) {
            push(temp.top());
            temp.pop();
        }
        return max_val;
    }
};
```

However, the optimal solution above still has $O(n)$ time complexity for `popMax()` operation. To achieve $O(1)$ time complexity for `popMax()` operation, we need to use a more complex data structure, such as a doubly linked list, to store the elements and the maximum elements.

```cpp
class MaxStack {
public:
    struct Node {
        int val;
        Node* next;
        Node* prev;
        Node(int x) : val(x), next(nullptr), prev(nullptr) {}
    };
    Node* head;
    Node* max_head;
    unordered_map<int, vector<Node*>> max_map;
    MaxStack() : head(nullptr), max_head(nullptr) {}
    
    void push(int x) {
        Node* node = new Node(x);
        if (!head) {
            head = node;
            max_head = node;
            max_map[x].push_back(node);
        } else {
            node->prev = head;
            head->next = node;
            head = node;
            if (x >= max_head->val) {
                if (x > max_head->val) {
                    max_head = node;
                    max_map[x].push_back(node);
                } else {
                    max_map[x].push_back(node);
                }
            }
        }
    }
    
    int pop() {
        if (!head) return -1;
        int x = head->val;
        if (head == max_head) {
            max_head = head->prev;
            max_map[x].erase(max_map[x].begin());
            if (max_map[x].empty()) {
                max_map.erase(x);
            }
        }
        Node* temp = head;
        head = head->prev;
        if (head) {
            head->next = nullptr;
        }
        delete temp;
        return x;
    }
    
    int max() {
        if (!max_head) return -1;
        return max_head->val;
    }
    
    int peekMax() {
        if (!max_head) return -1;
        return max_head->val;
    }
    
    int popMax() {
        if (!max_head) return -1;
        int x = max_head->val;
        Node* node = max_map[x].back();
        max_map[x].pop_back();
        if (max_map[x].empty()) {
            max_map.erase(x);
        }
        if (node->prev) {
            node->prev->next = node->next;
        } else {
            head = node->next;
        }
        if (node->next) {
            node->next->prev = node->prev;
        }
        delete node;
        if (max_map.size()) {
            max_head = max_map.rbegin()->second.back();
        } else {
            max_head = nullptr;
        }
        return x;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations.
> - **Space Complexity:** $O(n)$ for the nodes and the map.
> - **Optimality proof:** The time complexity of all operations is $O(1)$, which is the best possible time complexity for a stack implementation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Stack implementation, maximum element tracking.
- Problem-solving patterns identified: Using multiple data structures to track maximum elements.
- Optimization techniques learned: Using a map to store the maximum elements and their corresponding nodes.
- Similar problems to practice: Implementing a queue with maximum element tracking.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the maximum stack correctly, not handling edge cases.
- Edge cases to watch for: Empty stack, maximum element not found.
- Performance pitfalls: Using a single stack with $O(n)$ time complexity for `max()` and `peekMax()` operations.
- Testing considerations: Test with different input sequences, including edge cases.