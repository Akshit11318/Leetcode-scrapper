## Counter

**Problem Link:** https://leetcode.com/problems/counter/description

**Problem Statement:**
- Input format and constraints: None
- Expected output format: Implement a counter class
- Key requirements and edge cases to consider: Implement `getCount`, `increment`, and `decrement` methods
- Example test cases with explanations: `Counter counter; counter.increment(); counter.increment(); counter.decrement(); counter.getCount();`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a simple class to keep track of a count variable.
- Step-by-step breakdown of the solution: 
    1. Create a class `Counter`.
    2. Initialize a private variable `count` to 0.
    3. Implement `getCount` method to return the current count.
    4. Implement `increment` method to increment the count.
    5. Implement `decrement` method to decrement the count.

```cpp
class Counter {
private:
    int count;
public:
    Counter() : count(0) {}

    int getCount() {
        return count;
    }

    void increment() {
        count++;
    }

    void decrement() {
        count--;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all methods, since they involve constant time operations.
> - **Space Complexity:** $O(1)$, as the space used does not change with the size of the input, it only uses a fixed amount of space to store the `count` variable.
> - **Why these complexities occur:** These complexities occur because the operations are simple and do not depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal, as it uses the minimum amount of space and time required to implement the counter class.
- Detailed breakdown of the approach: 
    1. Create a class `Counter`.
    2. Initialize a private variable `count` to 0.
    3. Implement `getCount` method to return the current count.
    4. Implement `increment` method to increment the count.
    5. Implement `decrement` method to decrement the count.

```cpp
class Counter {
private:
    int count;
public:
    Counter() : count(0) {}

    int getCount() {
        return count;
    }

    void increment() {
        count++;
    }

    void decrement() {
        count--;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all methods, since they involve constant time operations.
> - **Space Complexity:** $O(1)$, as the space used does not change with the size of the input, it only uses a fixed amount of space to store the `count` variable.
> - **Optimality proof:** This is the optimal solution because it uses the minimum amount of space and time required to implement the counter class.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Encapsulation and abstraction in object-oriented programming.
- Problem-solving patterns identified: Using classes to encapsulate data and behavior.
- Optimization techniques learned: Using the minimum amount of space and time required to solve a problem.
- Similar problems to practice: Implementing other simple classes, such as a stack or a queue.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `count` variable, or not implementing the methods correctly.
- Edge cases to watch for: Negative counts, or very large counts.
- Performance pitfalls: Using more space or time than necessary to solve the problem.
- Testing considerations: Testing the class with different sequences of `increment`, `decrement`, and `getCount` calls.