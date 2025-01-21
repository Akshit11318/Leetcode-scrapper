## Throttle
**Problem Link:** https://leetcode.com/problems/throttle/description

**Problem Statement:**
- Input format and constraints: The function takes a timestamp as an input and returns a boolean indicating whether the function can be executed at that time.
- Expected output format: A boolean value.
- Key requirements and edge cases to consider: The function can only be executed at most once every `n` milliseconds, where `n` is the given time interval.
- Example test cases with explanations: 
    - throttle(1000) - The function can be executed at most once every 1000 milliseconds.
    - throttle(1000)(1) - Returns true because it's the first call.
    - throttle(1000)(1001) - Returns true because 1001 milliseconds have passed since the last call.
    - throttle(1000)(1000) - Returns false because less than 1000 milliseconds have passed since the last call.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a global variable to keep track of the last execution time.
- Step-by-step breakdown of the solution: 
    1. Initialize a global variable `last_execution_time` to 0.
    2. When the function is called, check if the difference between the current time and `last_execution_time` is greater than or equal to the given time interval `n`.
    3. If it is, update `last_execution_time` to the current time and return true. Otherwise, return false.
- Why this approach comes to mind first: It's a straightforward solution that meets the requirements.

```cpp
class Throttle {
private:
    long last_execution_time;
    int n;

public:
    Throttle(int n) : n(n), last_execution_time(0) {}

    bool is_allowed(int timestamp) {
        if (timestamp - last_execution_time >= n) {
            last_execution_time = timestamp;
            return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we're only performing constant-time operations.
> - **Space Complexity:** $O(1)$ because we're only using a constant amount of space to store the `last_execution_time` and `n`.
> - **Why these complexities occur:** These complexities occur because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach. We need to keep track of the last execution time and compare it with the current time.
- Detailed breakdown of the approach: 
    1. Initialize a variable `last_execution_time` to 0.
    2. When the function is called, check if the difference between the current time and `last_execution_time` is greater than or equal to the given time interval `n`.
    3. If it is, update `last_execution_time` to the current time and return true. Otherwise, return false.
- Proof of optimality: This solution is optimal because it meets the requirements with the minimum possible time and space complexity.
- Why further optimization is impossible: Further optimization is impossible because we need to perform at least one comparison to determine if the function can be executed.

```cpp
class Throttle {
private:
    long last_execution_time;
    int n;

public:
    Throttle(int n) : n(n), last_execution_time(0) {}

    bool is_allowed(int timestamp) {
        if (timestamp - last_execution_time >= n) {
            last_execution_time = timestamp;
            return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we're only performing constant-time operations.
> - **Space Complexity:** $O(1)$ because we're only using a constant amount of space to store the `last_execution_time` and `n`.
> - **Optimality proof:** This solution is optimal because it meets the requirements with the minimum possible time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of keeping track of state in a class.
- Problem-solving patterns identified: Using a variable to keep track of the last execution time.
- Optimization techniques learned: None, because the brute force approach is already optimal.
- Similar problems to practice: Other problems that involve keeping track of state, such as the `LRUCache` problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the `last_execution_time` when the function is allowed to execute.
- Edge cases to watch for: The case where the input time is less than the `last_execution_time`.
- Performance pitfalls: Using a data structure with a higher time complexity than necessary.
- Testing considerations: Testing the function with different input times to ensure it works correctly.