## Find the K Sum of an Array
**Problem Link:** https://leetcode.com/problems/find-the-k-sum-of-an-array/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and an integer `k`, find the sum of the `k` largest numbers in the array.
- Expected output format: The sum of the `k` largest numbers in the array.
- Key requirements and edge cases to consider: The input array `nums` can contain both positive and negative integers, and `k` can range from 1 to the length of the array.
- Example test cases with explanations:
  - Example 1: `nums = [1, 2, 3, 4, 5], k = 3`, Output: `12` (Sum of the 3 largest numbers: `3 + 4 + 5 = 12`)
  - Example 2: `nums = [-1, -2, -3, -4, -5], k = 2`, Output: `-3` (Sum of the 2 largest numbers: `-1 + (-2) = -3`)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the array in descending order and sum up the first `k` elements.
- Step-by-step breakdown of the solution:
  1. Check if `k` is within the valid range (1 to the length of the array).
  2. Sort the array in descending order.
  3. Sum up the first `k` elements of the sorted array.
- Why this approach comes to mind first: It is straightforward and easy to implement.

```cpp
#include <algorithm>
#include <numeric>

int kSum(vector<int>& nums, int k) {
    if (k < 1 || k > nums.size()) {
        throw invalid_argument("k is out of range");
    }
    
    sort(nums.rbegin(), nums.rend()); // Sort in descending order
    return accumulate(nums.begin(), nums.begin() + k, 0); // Sum up the first k elements
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the length of the array.
> - **Space Complexity:** $O(1)$ if the sorting is done in-place, or $O(n)$ if a new sorted array is created.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity depends on the sorting algorithm used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue (or heap) to efficiently find the `k` largest numbers without sorting the entire array.
- Detailed breakdown of the approach:
  1. Create a min-heap and push the first `k` elements into it.
  2. Iterate through the rest of the array, and for each element, if it is larger than the smallest element in the heap, replace the smallest element with the current element and heapify.
  3. After iterating through the entire array, the heap will contain the `k` largest numbers. Sum them up.
- Proof of optimality: This approach has a better time complexity than the brute force approach because it avoids sorting the entire array.

```cpp
#include <queue>

int kSum(vector<int>& nums, int k) {
    if (k < 1 || k > nums.size()) {
        throw invalid_argument("k is out of range");
    }
    
    priority_queue<int, vector<int>, greater<int>> minHeap; // Min-heap
    for (int num : nums) {
        if (minHeap.size() < k) {
            minHeap.push(num);
        } else if (num > minHeap.top()) {
            minHeap.pop();
            minHeap.push(num);
        }
    }
    
    int sum = 0;
    while (!minHeap.empty()) {
        sum += minHeap.top();
        minHeap.pop();
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the length of the array, because each insertion and removal operation in the heap takes $O(\log k)$ time, and we perform these operations $n$ times.
> - **Space Complexity:** $O(k)$ for storing the heap.
> - **Optimality proof:** This is the optimal solution because it minimizes the number of comparisons and operations required to find the `k` largest numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues (heaps) and their application in finding the `k` largest numbers.
- Problem-solving patterns identified: Using data structures to optimize solutions.
- Optimization techniques learned: Minimizing the number of comparisons and operations.
- Similar problems to practice: Finding the `k` smallest numbers, median of an array, etc.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect usage of priority queues, not handling edge cases.
- Edge cases to watch for: `k` being out of range, empty input array.
- Performance pitfalls: Using inefficient sorting algorithms or data structures.
- Testing considerations: Test with different input sizes, `k` values, and edge cases.