## Design Circular Deque
**Problem Link:** [https://leetcode.com/problems/design-circular-deque/description](https://leetcode.com/problems/design-circular-deque/description)

**Problem Statement:**
- Input format and constraints: The problem requires designing a circular deque with methods `insertFront`, `insertRear`, `deleteFront`, `deleteRear`, `getFront`, `getRear`, `isEmpty`, and `isFull`. The circular deque has a fixed size `k`.
- Expected output format: The output of each method should be as specified in the problem description.
- Key requirements and edge cases to consider: The circular deque should handle edge cases such as inserting or deleting elements when the deque is empty or full, and getting the front or rear element when the deque is empty.
- Example test cases with explanations:
  - Creating a circular deque with size `k = 3` and inserting elements `1`, `2`, and `3` from the front and rear.
  - Deleting elements from the front and rear and checking if the deque is empty or full.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to use a linear array and shift all elements when inserting or deleting an element from the front or rear.
- Step-by-step breakdown of the solution:
  1. Create a linear array of size `k`.
  2. Implement the `insertFront` method by shifting all elements to the right and inserting the new element at the front.
  3. Implement the `insertRear` method by inserting the new element at the end of the array.
  4. Implement the `deleteFront` method by shifting all elements to the left and removing the front element.
  5. Implement the `deleteRear` method by removing the last element of the array.
  6. Implement the `getFront` and `getRear` methods by returning the first and last elements of the array.
  7. Implement the `isEmpty` and `isFull` methods by checking the size of the array.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the shifting of elements.

```cpp
class MyCircularDeque {
private:
    vector<int> data;
    int k;

public:
    MyCircularDeque(int k) {
        this->k = k;
        data.resize(k);
    }

    bool insertFront(int value) {
        if (isFull()) return false;
        for (int i = k - 2; i >= 0; i--) {
            data[i + 1] = data[i];
        }
        data[0] = value;
        return true;
    }

    bool insertLast(int value) {
        if (isFull()) return false;
        for (int i = 0; i < k - 1; i++) {
            if (data[i] == 0) {
                data[i] = value;
                return true;
            }
        }
        return false;
    }

    bool deleteFront() {
        if (isEmpty()) return false;
        for (int i = 1; i < k; i++) {
            data[i - 1] = data[i];
        }
        data[k - 1] = 0;
        return true;
    }

    bool deleteLast() {
        if (isEmpty()) return false;
        for (int i = 0; i < k - 1; i++) {
            if (data[i] != 0 && data[i + 1] == 0) {
                data[i] = 0;
                return true;
            }
        }
        data[k - 1] = 0;
        return true;
    }

    int getFront() {
        if (isEmpty()) return -1;
        return data[0];
    }

    int getRear() {
        if (isEmpty()) return -1;
        for (int i = k - 1; i >= 0; i--) {
            if (data[i] != 0) return data[i];
        }
        return -1;
    }

    bool isEmpty() {
        for (int i = 0; i < k; i++) {
            if (data[i] != 0) return false;
        }
        return true;
    }

    bool isFull() {
        for (int i = 0; i < k; i++) {
            if (data[i] == 0) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$ for `insertFront` and `deleteFront`, $O(k)$ for `insertLast` and `deleteLast` in the worst case, $O(1)$ for `getFront` and `getRear`, and $O(k)$ for `isEmpty` and `isFull`.
> - **Space Complexity:** $O(k)$ for storing the deque.
> - **Why these complexities occur:** The time complexity is high due to the shifting of elements in the `insertFront` and `deleteFront` methods.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a circular array with two pointers, `head` and `tail`, to keep track of the front and rear of the deque.
- Detailed breakdown of the approach:
  1. Create a circular array of size `k`.
  2. Initialize `head` and `tail` to 0.
  3. Implement the `insertFront` method by inserting the new element at the `head` index and moving `head` to the previous index.
  4. Implement the `insertRear` method by inserting the new element at the `tail` index and moving `tail` to the next index.
  5. Implement the `deleteFront` method by removing the element at the `head` index and moving `head` to the next index.
  6. Implement the `deleteRear` method by removing the element at the `tail` index and moving `tail` to the previous index.
  7. Implement the `getFront` and `getRear` methods by returning the elements at the `head` and `tail` indices.
  8. Implement the `isEmpty` and `isFull` methods by checking the difference between `tail` and `head`.
- Why further optimization is impossible: This approach has a constant time complexity for all operations, which is the best possible complexity.

```cpp
class MyCircularDeque {
private:
    vector<int> data;
    int head;
    int tail;
    int size;

public:
    MyCircularDeque(int k) {
        data.resize(k);
        head = 0;
        tail = 0;
        size = 0;
    }

    bool insertFront(int value) {
        if (isFull()) return false;
        head = (head - 1 + data.size()) % data.size();
        data[head] = value;
        size++;
        return true;
    }

    bool insertLast(int value) {
        if (isFull()) return false;
        data[tail] = value;
        tail = (tail + 1) % data.size();
        size++;
        return true;
    }

    bool deleteFront() {
        if (isEmpty()) return false;
        head = (head + 1) % data.size();
        size--;
        return true;
    }

    bool deleteLast() {
        if (isEmpty()) return false;
        tail = (tail - 1 + data.size()) % data.size();
        size--;
        return true;
    }

    int getFront() {
        if (isEmpty()) return -1;
        return data[head];
    }

    int getRear() {
        if (isEmpty()) return -1;
        return data[(tail - 1 + data.size()) % data.size()];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == data.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations.
> - **Space Complexity:** $O(k)$ for storing the deque.
> - **Optimality proof:** This approach has a constant time complexity for all operations, which is the best possible complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a circular array with two pointers to implement a deque.
- Problem-solving patterns identified: Using a modular arithmetic to handle the circular array.
- Optimization techniques learned: Reducing the time complexity by using a constant-time approach.
- Similar problems to practice: Implementing a queue or a stack using a circular array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the edge cases correctly, such as inserting or deleting elements when the deque is empty or full.
- Edge cases to watch for: Handling the case where the deque is empty or full, and the case where the `head` and `tail` pointers are equal.
- Performance pitfalls: Using a linear array with shifting elements, which has a high time complexity.
- Testing considerations: Testing the deque with different operations and edge cases to ensure correctness.