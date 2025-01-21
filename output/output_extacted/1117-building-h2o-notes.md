## Building H2O
**Problem Link:** https://leetcode.com/problems/building-h2o/description

**Problem Statement:**
- Input format and constraints: The problem involves two types of threads: hydrogen (`H`) and oxygen (`O`). Hydrogen threads are generated in a 2:1 ratio with oxygen threads. 
- Expected output format: The goal is to synchronize these threads to form water molecules (`H2O`).
- Key requirements and edge cases to consider: 
    * Two hydrogen atoms and one oxygen atom are required to form one water molecule.
    * The `releaseHydrogen` and `releaseOxygen` functions should be called in a way that ensures the correct formation of water molecules.
- Example test cases with explanations:
    * If there are two hydrogen threads and one oxygen thread, they should form one water molecule.
    * If there are three hydrogen threads and no oxygen threads, only one water molecule can be formed when an oxygen thread is available.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach to solving this problem is to use a simple locking mechanism. We can use a `std::mutex` to protect the critical section of code where the water molecules are formed.
- Step-by-step breakdown of the solution:
    1. Create a `std::mutex` to protect the critical section.
    2. Create two `std::condition_variable` objects, one for hydrogen threads and one for oxygen threads.
    3. In the `releaseHydrogen` function, lock the mutex and wait until there are at least two hydrogen atoms available.
    4. In the `releaseOxygen` function, lock the mutex and wait until there is at least one oxygen atom available.
    5. Once the required atoms are available, form a water molecule and notify the other threads.
- Why this approach comes to mind first: This approach is straightforward and uses basic synchronization primitives.

```cpp
class H2O {
private:
    std::mutex mtx;
    std::condition_variable cv_h;
    std::condition_variable cv_o;
    int h_count = 0;
    int o_count = 0;

public:
    void hydrogen(function<void()> releaseHydrogen) {
        std::unique_lock<std::mutex> lock(mtx);
        cv_h.wait(lock, [this] { return h_count < 2; });
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        h_count++;
        if (h_count == 2 && o_count == 1) {
            cv_o.notify_one();
        }
    }

    void oxygen(function<void()> releaseOxygen) {
        std::unique_lock<std::mutex> lock(mtx);
        cv_o.wait(lock, [this] { return h_count == 2 && o_count < 1; });
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        o_count++;
        h_count = 0;
        o_count = 0;
        cv_h.notify_all();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of threads.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the mutex, condition variables, and counters.
> - **Why these complexities occur:** The time complexity is linear because each thread has to wait for the required atoms to be available. The space complexity is constant because we are using a fixed amount of space to store the synchronization primitives and counters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `std::atomic` variable to keep track of the number of hydrogen atoms and oxygen atoms. We can also use a `std::mutex` to protect the critical section of code where the water molecules are formed.
- Detailed breakdown of the approach:
    1. Create a `std::mutex` to protect the critical section.
    2. Create two `std::condition_variable` objects, one for hydrogen threads and one for oxygen threads.
    3. Create two `std::atomic` variables to keep track of the number of hydrogen atoms and oxygen atoms.
    4. In the `releaseHydrogen` function, lock the mutex and wait until there are less than two hydrogen atoms available.
    5. In the `releaseOxygen` function, lock the mutex and wait until there are at least two hydrogen atoms available.
    6. Once the required atoms are available, form a water molecule and notify the other threads.
- Proof of optimality: This approach is optimal because it uses the minimum amount of synchronization primitives required to solve the problem.

```cpp
class H2O {
private:
    std::mutex mtx;
    std::condition_variable cv_h;
    std::condition_variable cv_o;
    std::atomic<int> h_count(0);
    std::atomic<int> o_count(0);

public:
    void hydrogen(function<void()> releaseHydrogen) {
        std::unique_lock<std::mutex> lock(mtx);
        cv_h.wait(lock, [this] { return h_count.load() < 2; });
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        h_count++;
        if (h_count.load() == 2) {
            cv_o.notify_one();
        }
    }

    void oxygen(function<void()> releaseOxygen) {
        std::unique_lock<std::mutex> lock(mtx);
        cv_o.wait(lock, [this] { return h_count.load() == 2; });
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        h_count = 0;
        cv_h.notify_all();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of threads.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the mutex, condition variables, and counters.
> - **Optimality proof:** This approach is optimal because it uses the minimum amount of synchronization primitives required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Synchronization primitives, condition variables, and atomic variables.
- Problem-solving patterns identified: Using synchronization primitives to solve concurrent programming problems.
- Optimization techniques learned: Minimizing the use of synchronization primitives to improve performance.
- Similar problems to practice: Other concurrent programming problems that involve synchronization primitives.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of synchronization primitives, condition variables, and atomic variables.
- Edge cases to watch for: Handling the case where there are multiple hydrogen threads and no oxygen threads.
- Performance pitfalls: Using too many synchronization primitives, which can lead to performance degradation.
- Testing considerations: Testing the code with multiple threads and edge cases to ensure correctness.