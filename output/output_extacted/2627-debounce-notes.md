## Debounce
**Problem Link:** https://leetcode.com/problems/debounce/description

**Problem Statement:**
- Input format: A `function` to be debounced, and a `delay` in milliseconds.
- Expected output format: A new function that wraps the original function with debouncing logic.
- Key requirements and edge cases to consider:
  - The debounced function should not be called more than once within the specified delay.
  - If the debounced function is called again within the delay, the previous call should be cancelled.
  - Example test cases:
    - Calling the debounced function multiple times within the delay should only result in one actual call to the original function.
    - Calling the debounced function after the delay has passed should result in an actual call to the original function.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a simple timer to track when the debounced function was last called.
- Step-by-step breakdown of the solution:
  1. Create a timer variable to store the last call time.
  2. When the debounced function is called, check if the delay has passed since the last call.
  3. If the delay has passed, call the original function and update the last call time.
  4. If the delay has not passed, do nothing.
- Why this approach comes to mind first: It's a straightforward way to implement debouncing using a simple timer.

```cpp
class Debounce {
public:
    Debounce(int delay) : delay_(delay), last_call_time_(0) {}

    void operator()(function<void()> func) {
        int current_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
        if (current_time - last_call_time_ >= delay_) {
            func();
            last_call_time_ = current_time;
        }
    }

private:
    int delay_;
    int last_call_time_;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're only performing a constant amount of work to check the timer and call the original function.
> - **Space Complexity:** $O(1)$, because we're only storing a constant amount of data (the timer variable).
> - **Why these complexities occur:** These complexities occur because we're using a simple timer variable to track when the debounced function was last called, and we're only performing a constant amount of work to check the timer and call the original function.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `std::thread` to implement the debouncing logic, and a `std::mutex` to protect access to the timer variable.
- Detailed breakdown of the approach:
  1. Create a `std::thread` to run the debouncing logic.
  2. Use a `std::mutex` to protect access to the timer variable.
  3. When the debounced function is called, lock the mutex and check if the delay has passed since the last call.
  4. If the delay has passed, call the original function and update the last call time.
  5. If the delay has not passed, do nothing.
- Proof of optimality: This approach is optimal because it uses a `std::thread` to run the debouncing logic, which allows it to handle multiple calls to the debounced function concurrently.

```cpp
class Debounce {
public:
    Debounce(int delay) : delay_(delay), last_call_time_(0), running_(false) {}

    void operator()(function<void()> func) {
        std::lock_guard<std::mutex> lock(mutex_);
        if (running_) return;
        running_ = true;
        std::thread([this, func]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(delay_));
            std::lock_guard<std::mutex> lock(mutex_);
            if (last_call_time_ != 0 && chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count() - last_call_time_ >= delay_) {
                func();
                last_call_time_ = 0;
            }
            running_ = false;
        }).detach();
        last_call_time_ = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
    }

private:
    int delay_;
    int last_call_time_;
    std::mutex mutex_;
    bool running_;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're only performing a constant amount of work to check the timer and call the original function.
> - **Space Complexity:** $O(1)$, because we're only storing a constant amount of data (the timer variable and the mutex).
> - **Optimality proof:** This approach is optimal because it uses a `std::thread` to run the debouncing logic, which allows it to handle multiple calls to the debounced function concurrently.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Debouncing, threading, mutexes.
- Problem-solving patterns identified: Using a timer to track when a function was last called, using a mutex to protect access to shared data.
- Optimization techniques learned: Using a `std::thread` to run the debouncing logic, using a `std::mutex` to protect access to shared data.
- Similar problems to practice: Implementing rate limiting, implementing a retry mechanism.

**Mistakes to Avoid:**
- Common implementation errors: Not using a mutex to protect access to shared data, not handling the case where the debounced function is called multiple times within the delay.
- Edge cases to watch for: The debounced function being called multiple times within the delay, the debounced function being called after the delay has passed.
- Performance pitfalls: Not using a `std::thread` to run the debouncing logic, not using a `std::mutex` to protect access to shared data.
- Testing considerations: Testing the debounced function with multiple calls within the delay, testing the debounced function after the delay has passed.