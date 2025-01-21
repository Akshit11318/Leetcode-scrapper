## Bounded Blocking Queue

**Problem Link:** https://leetcode.com/problems/design-bounded-blocking-queue/description

**Problem Statement:**
- Design a `BoundedBlockingQueue` class that implements a queue with a given capacity.
- The class should have two methods: `enqueue` and `dequeue`.
- The `enqueue` method should add an element to the queue if it's not full. If the queue is full, it should block until space becomes available.
- The `dequeue` method should remove an element from the queue if it's not empty. If the queue is empty, it should block until an element becomes available.
- The class should handle multiple threads concurrently.

**Input format and constraints:**
- The class constructor takes an integer `capacity` as input, which represents the maximum number of elements the queue can hold.
- The `enqueue` method takes an integer `element` as input, which represents the element to be added to the queue.
- The `dequeue` method returns an integer, which represents the removed element.

**Expected output format:**
- The `dequeue` method should return the removed element.

**Key requirements and edge cases to consider:**
- The queue should be thread-safe.
- The `enqueue` method should block until space becomes available if the queue is full.
- The `dequeue` method should block until an element becomes available if the queue is empty.
- The class should handle multiple threads concurrently.

**Example test cases with explanations:**
- Creating a `BoundedBlockingQueue` with a capacity of 3 and adding 3 elements to it using `enqueue`.
- Dequeueing an element from the queue using `dequeue`.
- Trying to add an element to a full queue using `enqueue` and verifying that it blocks until space becomes available.
- Trying to remove an element from an empty queue using `dequeue` and verifying that it blocks until an element becomes available.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to use a simple queue data structure and implement the `enqueue` and `dequeue` methods.
- However, this approach does not handle the blocking behavior required by the problem.
- To implement the blocking behavior, we can use a `while` loop to continuously check if the queue is full or empty.

```cpp
class BoundedBlockingQueue {
private:
    queue<int> q;
    int capacity;
    mutex mtx;
    condition_variable cv;

public:
    BoundedBlockingQueue(int capacity) {
        this->capacity = capacity;
    }

    void enqueue(int element) {
        unique_lock<mutex> lock(mtx);
        while (q.size() == capacity) {
            cv.wait(lock);
        }
        q.push(element);
        cv.notify_all();
    }

    int dequeue() {
        unique_lock<mutex> lock(mtx);
        while (q.empty()) {
            cv.wait(lock);
        }
        int element = q.front();
        q.pop();
        cv.notify_all();
        return element;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for both `enqueue` and `dequeue` methods, assuming that the `wait` and `notify_all` operations take constant time.
> - **Space Complexity:** $O(n)$, where $n$ is the capacity of the queue.
> - **Why these complexities occur:** The time complexity is constant because the `enqueue` and `dequeue` methods only perform a constant amount of work. The space complexity is linear because we need to store all the elements in the queue.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is to use a condition variable to signal when the queue is not full or not empty.
- This approach is more efficient than the brute force approach because it avoids busy-waiting.
- We can use a `unique_lock` to lock the mutex and a `condition_variable` to signal when the queue is not full or not empty.

```cpp
class BoundedBlockingQueue {
private:
    queue<int> q;
    int capacity;
    mutex mtx;
    condition_variable notFull;
    condition_variable notEmpty;

public:
    BoundedBlockingQueue(int capacity) {
        this->capacity = capacity;
    }

    void enqueue(int element) {
        unique_lock<mutex> lock(mtx);
        notFull.wait(lock, [this]{ return q.size() < capacity; });
        q.push(element);
        notEmpty.notify_one();
    }

    int dequeue() {
        unique_lock<mutex> lock(mtx);
        notEmpty.wait(lock, [this]{ return !q.empty(); });
        int element = q.front();
        q.pop();
        notFull.notify_one();
        return element;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for both `enqueue` and `dequeue` methods, assuming that the `wait` and `notify_one` operations take constant time.
> - **Space Complexity:** $O(n)$, where $n$ is the capacity of the queue.
> - **Optimality proof:** This approach is optimal because it avoids busy-waiting and uses a condition variable to signal when the queue is not full or not empty.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: condition variables, mutexes, and queues.
- Problem-solving patterns identified: using condition variables to signal when a queue is not full or not empty.
- Optimization techniques learned: avoiding busy-waiting and using condition variables to signal when a queue is not full or not empty.
- Similar problems to practice: implementing a bounded blocking stack or a concurrent hash table.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to lock the mutex or not using a condition variable to signal when the queue is not full or not empty.
- Edge cases to watch for: handling multiple threads concurrently and avoiding busy-waiting.
- Performance pitfalls: using a busy-waiting approach instead of a condition variable.
- Testing considerations: testing the implementation with multiple threads and different scenarios.