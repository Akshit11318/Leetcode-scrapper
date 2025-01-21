## Rolling Average Steps
**Problem Link:** https://leetcode.com/problems/rolling-average-steps/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `nums`, and an integer `k`, calculate the rolling average of the last `k` elements.
- Expected output format: A list of rolling averages.
- Key requirements and edge cases to consider: Handle cases where `k` is larger than the current index, and ensure the average is calculated correctly for all indices.
- Example test cases with explanations:
  - Example 1: `nums = [1, 2, 3, 4, 5], k = 3` should return `[1.0, 1.5, 2.0, 3.0, 4.0]`.
  - Example 2: `nums = [1, 8, 6, 2, 4], k = 5` should return `[1.0, 4.5, 6.0, 5.0, 4.2]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the sum of the last `k` elements for each index, and then divide by `k` to get the average.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the rolling averages.
  2. Iterate through the list of numbers.
  3. For each index, calculate the sum of the last `k` elements.
  4. Calculate the average by dividing the sum by the minimum of `k` and the current index plus one.
  5. Append the average to the list of rolling averages.
- Why this approach comes to mind first: It directly addresses the problem statement and is a straightforward, albeit inefficient, way to solve the problem.

```cpp
class MovingAverage {
public:
    MovingAverage(int k) : k(k) {}
    
    double next(int val) {
        nums.push_back(val);
        double sum = 0;
        int size = nums.size();
        for (int i = max(0, size - k); i < size; i++) {
            sum += nums[i];
        }
        return sum / min(k, size);
    }
private:
    vector<int> nums;
    int k;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the number of elements in the input list. This is because for each element, we potentially iterate over the last `k` elements to calculate the sum.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input list. We store all the elements in the `nums` vector.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loop structure (one loop for iterating through the list and another for calculating the sum of the last `k` elements), and the space complexity is linear because we store all input elements.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Maintain a queue of the last `k` elements and calculate the sum of these elements. When a new element is added, remove the oldest element from the queue if necessary, and update the sum.
- Detailed breakdown of the approach:
  1. Initialize a queue to store the last `k` elements and a variable to store the sum of these elements.
  2. When a new element is added, check if the queue has reached its capacity `k`.
  3. If the queue is full, remove the oldest element from the queue and subtract its value from the sum.
  4. Add the new element to the queue and add its value to the sum.
  5. Calculate the average by dividing the sum by the number of elements in the queue.
- Proof of optimality: This approach ensures that we only iterate through the list once, and for each element, we perform a constant amount of work, resulting in a linear time complexity.

```cpp
class MovingAverage {
public:
    MovingAverage(int k) : k(k) {}
    
    double next(int val) {
        if (window.size() == k) {
            sum -= window.front();
            window.pop_front();
        }
        sum += val;
        window.push_back(val);
        return (double)sum / window.size();
    }
private:
    deque<int> window;
    int k;
    int sum = 0;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for each `next` operation, because we perform a constant amount of work for each new element. The overall time complexity for `n` operations is $O(n)$.
> - **Space Complexity:** $O(k)$, because we store at most `k` elements in the queue.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity for the overall sequence of operations, which is the best possible given that we must process each element at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a queue to maintain a sliding window of elements and updating the sum efficiently.
- Problem-solving patterns identified: Recognizing the need to optimize the calculation of rolling averages by avoiding redundant calculations.
- Optimization techniques learned: Maintaining a running sum and using a queue to efficiently manage the sliding window.
- Similar problems to practice: Other problems involving sliding windows or rolling statistics.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases where `k` is larger than the current index, or not updating the sum correctly when elements are added or removed from the queue.
- Edge cases to watch for: Handling cases where `k` is larger than the input list, or where the input list is empty.
- Performance pitfalls: Using inefficient data structures or algorithms that result in higher than necessary time or space complexities.
- Testing considerations: Thoroughly testing the implementation with various inputs, including edge cases, to ensure correctness and efficiency.