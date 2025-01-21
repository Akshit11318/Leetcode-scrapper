## Print Zero Even Odd
**Problem Link:** https://leetcode.com/problems/print-zero-even-odd/description

**Problem Statement:**
- Input format and constraints: The problem involves printing numbers from 1 to `n` in three threads - one printing zeros, one printing even numbers, and one printing odd numbers. Each number should be printed in the correct order.
- Expected output format: The output should be a sequence of numbers where zeros are printed after every number, and the numbers are printed in ascending order.
- Key requirements and edge cases to consider: The key requirement is to ensure that the numbers are printed in the correct order, with zeros printed after every number. The edge case is when `n` is 1, in which case only one number should be printed.
- Example test cases with explanations: For example, if `n` is 5, the output should be "zero, 1, zero, 2, zero, 3, zero, 4, zero, 5".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to use a simple loop to print the numbers from 1 to `n`, with a separate thread printing zeros after every number.
- Step-by-step breakdown of the solution: The brute force approach involves using a shared variable to keep track of the current number being printed, and using a lock to synchronize access to this variable.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward way to solve the problem, but it is not efficient because it involves a lot of overhead due to the use of locks.

```cpp
class ZeroEvenOdd {
public:
    ZeroEvenOdd(int n) {
        this->n = n;
    }

    void zero(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i++) {
            printNumber(0);
        }
    }

    void even(function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            printNumber(i);
        }
    }

    void odd(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            printNumber(i);
        }
    }

private:
    int n;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$
> - **Space Complexity:** $O(1)$
> - **Why these complexities occur:** The time complexity is $O(n)$ because we are printing $n$ numbers, and the space complexity is $O(1)$ because we are not using any extra space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a `std::condition_variable` to synchronize the threads, and to use a shared variable to keep track of the current state of the threads.
- Detailed breakdown of the approach: The optimal approach involves using a `std::mutex` to protect access to the shared variable, and using a `std::condition_variable` to signal when a thread should print a number.
- Proof of optimality: This approach is optimal because it minimizes the overhead of synchronization, and it ensures that the numbers are printed in the correct order.

```cpp
class ZeroEvenOdd {
public:
    ZeroEvenOdd(int n) {
        this->n = n;
        state = 0;
    }

    void zero(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i++) {
            std::unique_lock<std::mutex> lock(mutex);
            cond.wait(lock, [this]{ return state == 0; });
            printNumber(0);
            state = (i % 2 == 0) ? 2 : 1;
            cond.notify_all();
        }
    }

    void even(function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            std::unique_lock<std::mutex> lock(mutex);
            cond.wait(lock, [this]{ return state == 2; });
            printNumber(i);
            state = 0;
            cond.notify_all();
        }
    }

    void odd(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            std::unique_lock<std::mutex> lock(mutex);
            cond.wait(lock, [this]{ return state == 1; });
            printNumber(i);
            state = 0;
            cond.notify_all();
        }
    }

private:
    int n;
    int state;
    std::mutex mutex;
    std::condition_variable cond;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$
> - **Space Complexity:** $O(1)$
> - **Optimality proof:** This approach is optimal because it minimizes the overhead of synchronization, and it ensures that the numbers are printed in the correct order.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concepts demonstrated in this solution are the use of `std::mutex` and `std::condition_variable` to synchronize threads.
- Problem-solving patterns identified: The problem-solving pattern identified in this solution is the use of a shared variable to keep track of the current state of the threads.
- Optimization techniques learned: The optimization technique learned in this solution is the use of `std::condition_variable` to minimize the overhead of synchronization.
- Similar problems to practice: Similar problems to practice include the "FizzBuzz" problem and the "Producer-Consumer" problem.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a `std::mutex` without a `std::condition_variable`, which can lead to busy-waiting.
- Edge cases to watch for: An edge case to watch for is when `n` is 1, in which case only one number should be printed.
- Performance pitfalls: A performance pitfall is to use a `std::mutex` with a `std::condition_variable` without using a `std::unique_lock`, which can lead to deadlocks.
- Testing considerations: A testing consideration is to test the solution with different values of `n` to ensure that it works correctly in all cases.