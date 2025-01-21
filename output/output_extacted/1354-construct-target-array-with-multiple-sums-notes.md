## Construct Target Array With Multiple Sums
**Problem Link:** [https://leetcode.com/problems/construct-target-array-with-multiple-sums/description](https://leetcode.com/problems/construct-target-array-with-multiple-sums/description)

**Problem Statement:**
- Input format: An array of integers `target`.
- Constraints: The length of `target` is in the range `[1, 5 * 10^4]`, and each integer in `target` is in the range `[1, 10^9]`.
- Expected output format: Return `true` if it is possible to construct the `target` array from the array `[1]` using the operation of adding all elements in the array to the largest element, `false` otherwise.
- Key requirements and edge cases to consider: The sum of the elements in the `target` array must not exceed `10^12`, and the length of the `target` array must be at least 1.

**Example Test Cases:**
- `target = [9,3,5]`: The array can be constructed as follows: `[1] -> [1,1] -> [1,2] -> [3,3] -> [6,3] -> [9,3]`.
- `target = [8,2]`: The array cannot be constructed because the largest element must be increased by the sum of all other elements, and the only way to increase the largest element by 7 is to add 1 seven times.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try to construct the `target` array by repeatedly adding the sum of all elements to the largest element.
- Step-by-step breakdown of the solution:
  1. Initialize the array with `[1]`.
  2. While the array is not equal to the `target` array:
    a. Find the index of the largest element in the array.
    b. Calculate the sum of all elements in the array.
    c. Add the sum to the largest element.
    d. If the resulting array is equal to the `target` array, return `true`.
    e. If the largest element in the resulting array exceeds the largest element in the `target` array, return `false`.

```cpp
bool isPossible(vector<int>& target) {
    // Initialize the array with [1]
    vector<int> arr(1, 1);
    while (arr != target) {
        // Find the index of the largest element in the array
        int maxIndex = max_element(arr.begin(), arr.end()) - arr.begin();
        // Calculate the sum of all elements in the array
        int sum = accumulate(arr.begin(), arr.end(), 0);
        // Add the sum to the largest element
        arr[maxIndex] += sum;
        // If the resulting array is equal to the target array, return true
        if (arr == target) return true;
        // If the largest element in the resulting array exceeds the largest element in the target array, return false
        if (arr[maxIndex] > target[maxIndex]) return false;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the `target` array, because in the worst case, we need to iterate over the array $n$ times.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `target` array, because we need to store the array.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over the array in each iteration of the while loop, and the space complexity occurs because we need to store the array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to store the elements of the array, and in each iteration, we can add the sum of all elements to the largest element.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the elements of the `target` array.
  2. While the priority queue is not empty:
    a. Dequeue the largest element from the priority queue.
    b. Calculate the sum of all elements in the priority queue.
    c. If the largest element is greater than the sum, return `false`.
    d. If the largest element is equal to the sum, continue to the next iteration.
    e. Otherwise, subtract the sum from the largest element and enqueue the result.
  3. If the priority queue is empty and the largest element is 1, return `true`. Otherwise, return `false`.

```cpp
bool isPossible(vector<int>& target) {
    // Initialize a priority queue with the elements of the target array
    priority_queue<long long> pq;
    long long sum = 0;
    for (int num : target) {
        pq.push(num);
        sum += num;
    }
    while (pq.top() != 1) {
        // Dequeue the largest element from the priority queue
        long long maxNum = pq.top();
        pq.pop();
        // Calculate the sum of all elements in the priority queue
        sum -= maxNum;
        // If the largest element is greater than the sum, return false
        if (maxNum <= sum || sum == 0) return false;
        // Subtract the sum from the largest element and enqueue the result
        maxNum %= sum;
        sum += maxNum;
        pq.push(maxNum);
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the `target` array, because we use a priority queue to store the elements.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `target` array, because we need to store the priority queue.
> - **Optimality proof:** The time complexity is optimal because we need to iterate over the array at least once, and the space complexity is optimal because we need to store the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, greedy algorithm.
- Problem-solving patterns identified: Using a priority queue to store the elements of the array and iterating over the array to find the solution.
- Optimization techniques learned: Using a priority queue to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the base case, not handling the case where the largest element is greater than the sum.
- Edge cases to watch for: The case where the `target` array has only one element, the case where the largest element is equal to the sum.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.