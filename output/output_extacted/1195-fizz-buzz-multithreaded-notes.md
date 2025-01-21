## Fizz Buzz Multithreaded

**Problem Link:** [https://leetcode.com/problems/fizz-buzz-multithreaded/description](https://leetcode.com/problems/fizz-buzz-multithreaded/description)

**Problem Statement:**
- Input format and constraints: The problem requires writing a multithreaded program that prints numbers from 1 to `n`. For multiples of 3, it should print "Fizz" instead of the number, for multiples of 5, it should print "Buzz", and for numbers that are multiples of both 3 and 5, it should print "FizzBuzz". 
- Expected output format: The output should be a sequence of numbers and/or "Fizz", "Buzz", or "FizzBuzz" printed to the console, one per line, with each line corresponding to a number from 1 to `n`.
- Key requirements and edge cases to consider: The program should handle any positive integer `n` and should be multithreaded.
- Example test cases with explanations: For example, if `n = 15`, the output should be the sequence of numbers and/or "Fizz", "Buzz", or "FizzBuzz" from 1 to 15.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might initially think of a simple loop that checks each number from 1 to `n` and prints the appropriate output.
- Step-by-step breakdown of the solution: However, to make it multithreaded, we would need to synchronize threads to ensure that the numbers are printed in the correct order.
- Why this approach comes to mind first: This approach is straightforward but lacks efficiency due to the synchronization overhead.

```cpp
#include <iostream>
#include <mutex>

class FizzBuzz {
public:
    FizzBuzz(int n) : n_(n) {}

    void fizzbuzz(int n) {
        std::mutex mtx;
        for (int i = 1; i <= n; ++i) {
            std::lock_guard<std::mutex> lock(mtx);
            if (i % 15 == 0) {
                std::cout << "FizzBuzz" << std::endl;
            } else if (i % 3 == 0) {
                std::cout << "Fizz" << std::endl;
            } else if (i % 5 == 0) {
                std::cout << "Buzz" << std::endl;
            } else {
                std::cout << i << std::endl;
            }
        }
    }

private:
    int n_;
};

int main() {
    FizzBuzz fizzBuzz(15);
    fizzBuzz.fizzbuzz(15);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number, because we are iterating over all numbers from 1 to $n$.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the mutex and other variables.
> - **Why these complexities occur:** The time complexity is linear because we are checking each number once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: To make the program multithreaded efficiently, we can use four threads: one for numbers that are multiples of 3 and 5, one for multiples of 3, one for multiples of 5, and one for numbers that are not multiples of either.
- Detailed breakdown of the approach: Each thread will be responsible for checking its respective condition and printing the corresponding output. We can use a `std::condition_variable` to synchronize the threads.
- Proof of optimality: This approach is optimal because it minimizes the synchronization overhead by only requiring threads to wait when they need to print a number that is also a multiple of another thread's condition.
- Why further optimization is impossible: This approach is already optimal because it uses the minimum number of threads necessary to solve the problem and minimizes the synchronization overhead.

```cpp
#include <iostream>
#include <mutex>
#include <condition_variable>

class FizzBuzz {
public:
    FizzBuzz(int n) : n_(n), current_(1) {}

    void fizz() {
        for (int i = 1; i <= n_; ++i) {
            if (i % 3 == 0 && i % 5 != 0) {
                std::unique_lock<std::mutex> lock(mtx_);
                while (current_ != i) {
                    cond_.wait(lock);
                }
                std::cout << "Fizz" << std::endl;
                current_++;
                cond_.notify_all();
            }
        }
    }

    void buzz() {
        for (int i = 1; i <= n_; ++i) {
            if (i % 5 == 0 && i % 3 != 0) {
                std::unique_lock<std::mutex> lock(mtx_);
                while (current_ != i) {
                    cond_.wait(lock);
                }
                std::cout << "Buzz" << std::endl;
                current_++;
                cond_.notify_all();
            }
        }
    }

    void fizzbuzz() {
        for (int i = 1; i <= n_; ++i) {
            if (i % 15 == 0) {
                std::unique_lock<std::mutex> lock(mtx_);
                while (current_ != i) {
                    cond_.wait(lock);
                }
                std::cout << "FizzBuzz" << std::endl;
                current_++;
                cond_.notify_all();
            }
        }
    }

    void number() {
        for (int i = 1; i <= n_; ++i) {
            if (i % 3 != 0 && i % 5 != 0) {
                std::unique_lock<std::mutex> lock(mtx_);
                while (current_ != i) {
                    cond_.wait(lock);
                }
                std::cout << i << std::endl;
                current_++;
                cond_.notify_all();
            }
        }
    }

private:
    int n_;
    int current_;
    std::mutex mtx_;
    std::condition_variable cond_;
};

int main() {
    FizzBuzz fizzBuzz(15);
    std::thread t1(&FizzBuzz::fizz, &fizzBuzz);
    std::thread t2(&FizzBuzz::buzz, &fizzBuzz);
    std::thread t3(&FizzBuzz::fizzbuzz, &fizzBuzz);
    std::thread t4(&FizzBuzz::number, &fizzBuzz);
    t1.join();
    t2.join();
    t3.join();
    t4.join();
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number, because we are iterating over all numbers from 1 to $n$.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the mutex, condition variable, and other variables.
> - **Optimality proof:** This approach is optimal because it minimizes the synchronization overhead by only requiring threads to wait when they need to print a number that is also a multiple of another thread's condition.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Multithreading, synchronization, and condition variables.
- Problem-solving patterns identified: Breaking down a problem into smaller sub-problems and solving them concurrently.
- Optimization techniques learned: Minimizing synchronization overhead by using condition variables.
- Similar problems to practice: Other multithreading problems that require synchronization and condition variables.

**Mistakes to Avoid:**
- Common implementation errors: Not using `std::unique_lock` with `std::condition_variable`, not checking the condition before waiting, and not notifying all threads after changing the condition.
- Edge cases to watch for: Handling the case where `n` is 0 or negative, and handling the case where the threads are not properly synchronized.
- Performance pitfalls: Using too much synchronization, which can lead to performance bottlenecks, and not using condition variables, which can lead to busy-waiting.
- Testing considerations: Testing the program with different values of `n`, testing the program with different numbers of threads, and testing the program for correctness and performance.