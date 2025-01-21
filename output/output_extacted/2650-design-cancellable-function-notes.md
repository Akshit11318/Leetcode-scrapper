## Design Cancellable Function
**Problem Link:** https://leetcode.com/problems/design-cancellable-function/description

**Problem Statement:**
- Input format and constraints: The function should take a function `func` and its arguments `args`, and return a cancellable function.
- Expected output format: The returned function should be cancellable and should return the result of the original function when called.
- Key requirements and edge cases to consider: The function should be able to handle asynchronous functions and should be cancellable.
- Example test cases with explanations:
  - Test case 1: Test with a simple synchronous function.
  - Test case 2: Test with an asynchronous function.
  - Test case 3: Test with a function that throws an error.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a cancellable function by using a boolean flag to indicate whether the function should be cancelled.
- Step-by-step breakdown of the solution:
  1. Create a boolean flag `cancelled` and initialize it to `false`.
  2. Create a new function `cancellableFunc` that checks the `cancelled` flag before calling the original function.
  3. If the `cancelled` flag is `true`, throw an error indicating that the function was cancelled.
  4. Otherwise, call the original function with the provided arguments.
- Why this approach comes to mind first: It is a simple and straightforward approach to creating a cancellable function.

```cpp
class CancellableFunction {
public:
    CancellableFunction(function<void()> func) : func_(func), cancelled_(false) {}

    void cancel() {
        cancelled_ = true;
    }

    void call() {
        if (cancelled_) {
            throw runtime_error("Function was cancelled");
        }
        func_();
    }

private:
    function<void()> func_;
    bool cancelled_;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are simply checking a boolean flag and calling a function.
> - **Space Complexity:** $O(1)$ because we are only storing a boolean flag and a function pointer.
> - **Why these complexities occur:** The time complexity is constant because we are not performing any loops or recursive calls. The space complexity is constant because we are not using any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `std::atomic<bool>` to make the `cancelled` flag thread-safe.
- Detailed breakdown of the approach:
  1. Create a `std::atomic<bool>` `cancelled` and initialize it to `false`.
  2. Create a new function `cancellableFunc` that checks the `cancelled` flag before calling the original function.
  3. If the `cancelled` flag is `true`, throw an error indicating that the function was cancelled.
  4. Otherwise, call the original function with the provided arguments.
- Proof of optimality: This approach is optimal because it provides a thread-safe way to cancel the function and does not introduce any unnecessary overhead.

```cpp
#include <atomic>
#include <functional>

class CancellableFunction {
public:
    CancellableFunction(function<void()> func) : func_(func), cancelled_(false) {}

    void cancel() {
        cancelled_.store(true);
    }

    void call() {
        if (cancelled_.load()) {
            throw runtime_error("Function was cancelled");
        }
        func_();
    }

private:
    function<void()> func_;
    std::atomic<bool> cancelled_;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are simply checking a boolean flag and calling a function.
> - **Space Complexity:** $O(1)$ because we are only storing a boolean flag and a function pointer.
> - **Optimality proof:** This approach is optimal because it provides a thread-safe way to cancel the function and does not introduce any unnecessary overhead.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a boolean flag to indicate whether a function should be cancelled.
- Problem-solving patterns identified: Creating a cancellable function by checking a boolean flag before calling the original function.
- Optimization techniques learned: Using `std::atomic<bool>` to make the `cancelled` flag thread-safe.
- Similar problems to practice: Creating a retryable function, creating a function that can be paused and resumed.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the `cancelled` flag before calling the original function.
- Edge cases to watch for: The function being cancelled while it is being called.
- Performance pitfalls: Introducing unnecessary overhead when checking the `cancelled` flag.
- Testing considerations: Testing the function with different scenarios, such as cancelling the function before it is called, while it is being called, and after it has been called.