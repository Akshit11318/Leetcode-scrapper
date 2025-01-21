## Moving Average from Data Stream
**Problem Link:** https://leetcode.com/problems/moving-average-from-data-stream/description

**Problem Statement:**
- Given a stream of integers and an integer `size`, implement a `MovingAverage` class that calculates the moving average of the last `size` numbers in the stream.
- Input format and constraints:
  - `size` is a positive integer.
  - The stream of integers can be any sequence of integers.
- Expected output format:
  - The moving average of the last `size` numbers in the stream.
- Key requirements and edge cases to consider:
  - Handle the case where the stream has fewer than `size` numbers.
  - Handle the case where `size` is 1.
- Example test cases with explanations:
  - Example 1: `MovingAverage ma = new MovingAverage(3); ma.next(1); ma.next(10); ma.next(3); ma.next(5);`
  - Expected output: `1.0, 5.5, 4.66667, 6.0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Store all the numbers in the stream and calculate the average of the last `size` numbers every time a new number is added.
- Step-by-step breakdown of the solution:
  1. Store all the numbers in a vector.
  2. When a new number is added, calculate the sum of the last `size` numbers.
  3. Calculate the average by dividing the sum by `size`.
- Why this approach comes to mind first: It is straightforward to implement and easy to understand.

```cpp
class MovingAverage {
public:
    MovingAverage(int size) : size(size) {}
    
    double next(int val) {
        stream.push_back(val);
        double sum = 0.0;
        int start = max(0, (int)stream.size() - size);
        for (int i = start; i < stream.size(); i++) {
            sum += stream[i];
        }
        return sum / min(size, (int)stream.size());
    }
private:
    int size;
    vector<int> stream;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the stream. This is because we are iterating over the last `size` numbers in the stream every time a new number is added.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the stream. This is because we are storing all the numbers in the stream.
> - **Why these complexities occur:** The brute force approach has high time and space complexities because it involves iterating over the entire stream and storing all the numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all the numbers in the stream, we can store the sum of the last `size` numbers and update it every time a new number is added.
- Detailed breakdown of the approach:
  1. Initialize the sum of the last `size` numbers to 0.
  2. When a new number is added, subtract the oldest number from the sum and add the new number.
  3. Calculate the average by dividing the sum by the minimum of `size` and the current size of the stream.
- Proof of optimality: This approach has a time complexity of $O(1)$ and a space complexity of $O(size)$, which is optimal because we only need to store the last `size` numbers.

```cpp
class MovingAverage {
public:
    MovingAverage(int size) : size(size), sum(0.0) {}
    
    double next(int val) {
        queue.push(val);
        sum += val;
        if (queue.size() > size) {
            sum -= queue.front();
            queue.pop();
        }
        return sum / min(size, (int)queue.size());
    }
private:
    int size;
    double sum;
    queue<int> queue;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are only updating the sum and the queue every time a new number is added.
> - **Space Complexity:** $O(size)$, because we are storing the last `size` numbers in the queue.
> - **Optimality proof:** This approach is optimal because we are only storing the necessary information (the sum of the last `size` numbers and the last `size` numbers themselves) and updating it in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a queue to store the last `size` numbers and updating the sum in constant time.
- Problem-solving patterns identified: Using a data structure to store the necessary information and updating it in constant time.
- Optimization techniques learned: Avoiding unnecessary iterations and storing only the necessary information.
- Similar problems to practice: Problems involving sliding windows and queues.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the sum correctly when a new number is added.
- Edge cases to watch for: Handling the case where the stream has fewer than `size` numbers.
- Performance pitfalls: Using a brute force approach that has high time and space complexities.
- Testing considerations: Testing the implementation with different inputs and edge cases to ensure correctness.