## Print FooBar Alternately
**Problem Link:** https://leetcode.com/problems/print-foobar-alternately/description

**Problem Statement:**
- Input format and constraints: The problem involves two threads, one printing "Foo" and the other printing "Bar". The threads are required to print "FooBar" alternately.
- Expected output format: The output should be a sequence of "FooBar" printed alternately by the two threads.
- Key requirements and edge cases to consider: The threads should print "FooBar" alternately, and the solution should ensure that the threads are properly synchronized to avoid any conflicts or deadlocks.
- Example test cases with explanations: For example, if the input is `n = 5`, the output should be "FooBarFooBarFooBarFooBarFooBar".

### Brute Force Approach
**Explanation:**
- Initial thought process: The initial thought process involves using a shared variable to synchronize the threads. One thread prints "Foo" and then sets the shared variable to indicate that it's the other thread's turn. The other thread waits until the shared variable is set and then prints "Bar".
- Step-by-step breakdown of the solution:
  1. Create a shared variable to indicate whose turn it is.
  2. The "Foo" thread prints "Foo" and then sets the shared variable to indicate that it's the "Bar" thread's turn.
  3. The "Bar" thread waits until the shared variable is set and then prints "Bar".
  4. The "Bar" thread resets the shared variable to indicate that it's the "Foo" thread's turn.
- Why this approach comes to mind first: This approach comes to mind first because it's a simple and straightforward way to synchronize the threads. However, it may not be the most efficient solution.

```cpp
class FooBar {
private:
    int n;
    mutex mtx;
    condition_variable cv;
    bool foo_turn;

public:
    FooBar(int n) {
        this->n = n;
        foo_turn = true;
    }

    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [this] { return foo_turn; });
            printFoo();
            foo_turn = false;
            cv.notify_one();
        }
    }

    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [this] { return !foo_turn; });
            printBar();
            foo_turn = true;
            cv.notify_one();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of times "FooBar" is printed.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the shared variable and the mutex.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we have a loop that runs $n$ times, and each iteration involves a constant amount of work. The space complexity is $O(1)$ because we only use a constant amount of space to store the shared variable and the mutex.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a `std::condition_variable` to synchronize the threads. This allows us to avoid busy-waiting and reduce the overhead of context switching.
- Detailed breakdown of the approach:
  1. Create a `std::condition_variable` to synchronize the threads.
  2. The "Foo" thread prints "Foo" and then notifies the "Bar" thread using the `std::condition_variable`.
  3. The "Bar" thread waits until it's notified by the "Foo" thread and then prints "Bar".
  4. The "Bar" thread notifies the "Foo" thread using the `std::condition_variable`.
- Proof of optimality: This solution is optimal because it minimizes the overhead of context switching and avoids busy-waiting.

```cpp
class FooBar {
private:
    int n;
    mutex mtx;
    condition_variable cv;
    bool foo_turn;

public:
    FooBar(int n) {
        this->n = n;
        foo_turn = true;
    }

    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [this] { return foo_turn; });
            printFoo();
            foo_turn = false;
            cv.notify_one();
        }
    }

    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [this] { return !foo_turn; });
            printBar();
            foo_turn = true;
            cv.notify_one();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of times "FooBar" is printed.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the shared variable and the mutex.
> - **Optimality proof:** This solution is optimal because it minimizes the overhead of context switching and avoids busy-waiting.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Synchronization using `std::condition_variable`.
- Problem-solving patterns identified: Using a shared variable to synchronize threads.
- Optimization techniques learned: Minimizing context switching and avoiding busy-waiting.
- Similar problems to practice: Other synchronization problems, such as the "Dining Philosophers" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not using a `std::condition_variable` to synchronize threads.
- Edge cases to watch for: Not handling the case where one thread is waiting for the other thread to finish.
- Performance pitfalls: Busy-waiting and excessive context switching.
- Testing considerations: Testing the solution with different inputs and thread schedules.