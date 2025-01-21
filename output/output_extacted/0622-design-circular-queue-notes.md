## Design Circular Queue

**Problem Link:** https://leetcode.com/problems/design-circular-queue/description

**Problem Statement:**
- Input format and constraints: The problem asks us to design a circular queue with a given capacity. The queue should support the following operations: `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.
- Expected output format: The output of each operation should be a boolean value indicating whether the operation was successful or not, or the value of the front or rear element.
- Key requirements and edge cases to consider: We need to handle edge cases such as an empty queue, a full queue, and when the queue is not empty but the front and rear pointers are at the same position.
- Example test cases with explanations: For example, if we have a queue with a capacity of 3, we can perform the following operations: `enQueue(1)`, `enQueue(2)`, `enQueue(3)`, `deQueue()`, `enQueue(4)`, and then check the front and rear elements.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use a linear array to implement the queue and handle the circularity manually.
- Step-by-step breakdown of the solution: We can use two pointers, `front` and `rear`, to keep track of the front and rear elements of the queue. When the `rear` pointer reaches the end of the array, we can reset it to the beginning of the array.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
class MyCircularQueue {
private:
    int* data;
    int front, rear, size, capacity;

public:
    MyCircularQueue(int k) {
        capacity = k;
        data = new int[k];
        front = rear = size = 0;
    }

    ~MyCircularQueue() {
        delete[] data;
    }

    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        data[rear] = value;
        rear = (rear + 1) % capacity;
        size++;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) {
            return false;
        }
        front = (front + 1) % capacity;
        size--;
        return true;
    }

    int Front() {
        if (isEmpty()) {
            return -1;
        }
        return data[front];
    }

    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return data[(rear - 1 + capacity) % capacity];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations, since we only need to update the pointers and check the size of the queue.
> - **Space Complexity:** $O(k)$, where $k$ is the capacity of the queue, since we need to store the data in the array.
> - **Why these complexities occur:** The time complexity is constant because we only need to perform a constant number of operations for each method call. The space complexity is linear because we need to store the data in the array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, since we can't do better than $O(1)$ time complexity for all operations.
- Detailed breakdown of the approach: We use two pointers, `front` and `rear`, to keep track of the front and rear elements of the queue. When the `rear` pointer reaches the end of the array, we reset it to the beginning of the array.
- Proof of optimality: This solution is optimal because we can't do better than $O(1)$ time complexity for all operations.
- Why further optimization is impossible: Further optimization is impossible because we already have the optimal time complexity for all operations.

```cpp
class MyCircularQueue {
private:
    int* data;
    int front, rear, size, capacity;

public:
    MyCircularQueue(int k) {
        capacity = k;
        data = new int[k];
        front = rear = size = 0;
    }

    ~MyCircularQueue() {
        delete[] data;
    }

    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        data[rear] = value;
        rear = (rear + 1) % capacity;
        size++;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) {
            return false;
        }
        front = (front + 1) % capacity;
        size--;
        return true;
    }

    int Front() {
        if (isEmpty()) {
            return -1;
        }
        return data[front];
    }

    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return data[(rear - 1 + capacity) % capacity];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations, since we only need to update the pointers and check the size of the queue.
> - **Space Complexity:** $O(k)$, where $k$ is the capacity of the queue, since we need to store the data in the array.
> - **Optimality proof:** This solution is optimal because we can't do better than $O(1)$ time complexity for all operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of circular arrays and how to implement a queue using a circular array.
- Problem-solving patterns identified: The problem requires us to think about how to handle edge cases and how to optimize the solution.
- Optimization techniques learned: We learned how to optimize the solution by using two pointers to keep track of the front and rear elements of the queue.
- Similar problems to practice: Similar problems to practice include implementing a stack using a circular array and implementing a queue using a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Common implementation errors include not handling edge cases correctly and not optimizing the solution.
- Edge cases to watch for: Edge cases to watch for include an empty queue, a full queue, and when the queue is not empty but the front and rear pointers are at the same position.
- Performance pitfalls: Performance pitfalls include using a linear array to implement the queue without handling the circularity manually.
- Testing considerations: Testing considerations include testing the solution with different input sizes and testing the solution with different sequences of operations.