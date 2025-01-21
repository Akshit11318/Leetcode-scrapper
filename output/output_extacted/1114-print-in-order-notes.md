## Print in Order
**Problem Link:** https://leetcode.com/problems/print-in-order/description

**Problem Statement:**
- Input format and constraints: The problem requires writing a program that prints numbers from 1 to `n` in order, with `n` being the input. The catch is that the program must use three threads to print these numbers: one thread for printing numbers from 1 to `n` (except for multiples of 3), another for printing multiples of 3 (but not multiples of 2), and the last for printing multiples of 2 (but not multiples of 3).
- Expected output format: The numbers should be printed in ascending order, each on a new line.
- Key requirements and edge cases to consider: Synchronization between threads is crucial to maintain the correct order. The program must also handle cases where `n` is small (e.g., 1, 2) and where `n` is large.
- Example test cases with explanations:
    - For `n = 5`, the output should be `1, 2, 3, 4, 5` printed in order.
    - For `n = 6`, the output should be `1, 2, 3, 4, 5, 6` printed in order.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is using a shared variable to keep track of the current number being printed and using synchronization primitives (like mutexes and condition variables) to ensure that the threads print numbers in the correct order.
- Step-by-step breakdown of the solution:
    1. Initialize a shared variable `currentNumber` to 1.
    2. Create three threads: one for printing numbers that are not multiples of 3 or 2, one for printing multiples of 3 that are not multiples of 2, and one for printing multiples of 2 that are not multiples of 3.
    3. Use a mutex to protect access to `currentNumber`.
    4. Each thread checks if `currentNumber` meets its condition (e.g., the first thread checks if `currentNumber` is not a multiple of 3 or 2). If it does, the thread prints `currentNumber` and increments it. If not, the thread waits until `currentNumber` meets its condition.
- Why this approach comes to mind first: It's a straightforward way to divide the work among threads based on the problem's requirements.

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv;
int currentNumber = 1;
int n;

void printNotMultipleOf3Or2() {
    while (currentNumber <= n) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, []{ return currentNumber <= n && currentNumber % 3 != 0 && currentNumber % 2 != 0; });
        if (currentNumber > n) break;
        std::cout << currentNumber << std::endl;
        currentNumber++;
        cv.notify_all();
    }
}

void printMultipleOf3NotMultipleOf2() {
    while (currentNumber <= n) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, []{ return currentNumber <= n && currentNumber % 3 == 0 && currentNumber % 2 != 0; });
        if (currentNumber > n) break;
        std::cout << currentNumber << std::endl;
        currentNumber++;
        cv.notify_all();
    }
}

void printMultipleOf2NotMultipleOf3() {
    while (currentNumber <= n) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, []{ return currentNumber <= n && currentNumber % 2 == 0 && currentNumber % 3 != 0; });
        if (currentNumber > n) break;
        std::cout << currentNumber << std::endl;
        currentNumber++;
        cv.notify_all();
    }
}

int main() {
    n = 10; // Example value for n
    std::thread t1(printNotMultipleOf3Or2);
    std::thread t2(printMultipleOf3NotMultipleOf2);
    std::thread t3(printMultipleOf2NotMultipleOf3);
    t1.join();
    t2.join();
    t3.join();
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as each number up to `n` is printed once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the threads, as only a constant amount of space is used.
> - **Why these complexities occur:** The time complexity is linear because each number is processed once. The space complexity is constant because only a fixed amount of extra memory is used, regardless of `n`.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a `std::condition_variable` to signal between threads when it's their turn to print. This approach minimizes overhead and ensures correct ordering.
- Detailed breakdown of the approach:
    1. Initialize a shared variable `currentNumber` to 1 and a shared `std::mutex` for synchronization.
    2. Create three threads as before, but now each thread waits on a condition variable until it's its turn to print.
    3. After printing, each thread increments `currentNumber` and notifies the next thread that it's its turn.
- Proof of optimality: This solution is optimal because it minimizes synchronization overhead by only waking up the thread that needs to run next, avoiding unnecessary wake-ups and context switches.
- Why further optimization is impossible: Further optimization is not possible because the problem inherently requires synchronization between threads to maintain the correct order, and this solution achieves that with minimal overhead.

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv;
int currentNumber = 1;
int n;

void printNotMultipleOf3Or2() {
    while (currentNumber <= n) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, []{ return currentNumber <= n && (currentNumber % 3 != 0 && currentNumber % 2 != 0); });
        if (currentNumber > n) break;
        std::cout << currentNumber << std::endl;
        currentNumber++;
        cv.notify_all();
    }
}

void printMultipleOf3NotMultipleOf2() {
    while (currentNumber <= n) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, []{ return currentNumber <= n && (currentNumber % 3 == 0 && currentNumber % 2 != 0); });
        if (currentNumber > n) break;
        std::cout << currentNumber << std::endl;
        currentNumber++;
        cv.notify_all();
    }
}

void printMultipleOf2NotMultipleOf3() {
    while (currentNumber <= n) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, []{ return currentNumber <= n && (currentNumber % 2 == 0 && currentNumber % 3 != 0); });
        if (currentNumber > n) break;
        std::cout << currentNumber << std::endl;
        currentNumber++;
        cv.notify_all();
    }
}

int main() {
    n = 10; // Example value for n
    std::thread t1(printNotMultipleOf3Or2);
    std::thread t2(printMultipleOf3NotMultipleOf2);
    std::thread t3(printMultipleOf2NotMultipleOf3);
    t1.join();
    t2.join();
    t3.join();
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as each number up to `n` is printed once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the threads, as only a constant amount of space is used.
> - **Optimality proof:** This solution is optimal because it minimizes the overhead of synchronization by only notifying the next thread that needs to run, thus avoiding unnecessary wake-ups and context switches.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Synchronization between threads, use of condition variables for signaling between threads.
- Problem-solving patterns identified: Dividing work among threads based on specific conditions, minimizing synchronization overhead.
- Optimization techniques learned: Using condition variables to minimize wake-ups and context switches.
- Similar problems to practice: Other problems involving synchronization and division of work among threads.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of synchronization primitives, failing to handle edge cases (e.g., small `n`).
- Edge cases to watch for: Handling cases where `n` is small or large, ensuring correct ordering in all scenarios.
- Performance pitfalls: Using synchronization primitives inefficiently, leading to high overhead and slow performance.
- Testing considerations: Thoroughly testing the program with different values of `n`, including edge cases, to ensure correct behavior.