## Kth Largest Element in a Stream
**Problem Link:** https://leetcode.com/problems/kth-largest-element-in-a-stream/description

**Problem Statement:**
- Input format and constraints: The input is a stream of integers and an integer `k`, where `1 <= k <= 10^4`. The integers in the stream can range from `10^4` to `10^9`.
- Expected output format: Design a class to add the given integers to a data structure and return the `kth` largest element in the current stream.
- Key requirements and edge cases to consider: 
    - The class should support the `add` and `getKthLargest` methods.
    - The `add` method adds an integer to the stream.
    - The `getKthLargest` method returns the `kth` largest element in the current stream.
- Example test cases with explanations: 
    - Example 1: `["KthLargest", "add", "add", "add", "getKthLargest", "add", "getKthLargest"]`, `[[3, [4, 5, 8, 2]], [3], [5], [10], [], [9], []]`. 
      - The output should be `[null, null, null, 4, null, 5]`.
    - Example 2: `["KthLargest", "add", "add", "add", "getKthLargest", "add", "getKthLargest"]`, `[[1, [2, 1]], [2], [1], [], [2], []]`. 
      - The output should be `[null, null, null, 2, null, 1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Store all the integers in a vector and sort the vector in descending order whenever the `getKthLargest` method is called.
- Step-by-step breakdown of the solution: 
    1. Create a class `KthLargest` with a vector `nums` to store the integers and an integer `k` to store the value of `k`.
    2. In the `add` method, add the integer to the vector `nums`.
    3. In the `getKthLargest` method, sort the vector `nums` in descending order and return the `kth` largest element.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has high time complexity due to the sorting operation.

```cpp
class KthLargest {
public:
    vector<int> nums;
    int k;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        this->nums = nums;
    }
    
    int add(int val) {
        nums.push_back(val);
        sort(nums.rbegin(), nums.rend());
        return nums[k-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of integers in the stream. This is because the `sort` method is called in the `getKthLargest` method, and it has a time complexity of $O(n \log n)$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of integers in the stream. This is because all the integers are stored in the vector `nums`.
> - **Why these complexities occur:** The time complexity is high because of the sorting operation, and the space complexity is high because all the integers are stored in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to store the `k` largest elements in the stream.
- Detailed breakdown of the approach: 
    1. Create a class `KthLargest` with a priority queue `pq` to store the `k` largest elements and an integer `k` to store the value of `k`.
    2. In the `add` method, add the integer to the priority queue `pq` if its size is less than `k`, or if the integer is greater than the smallest element in the priority queue.
    3. In the `getKthLargest` method, return the smallest element in the priority queue `pq`.
- Why further optimization is impossible: This approach has the optimal time complexity because it only requires a constant amount of work to add an integer to the priority queue and to get the `kth` largest element.

```cpp
class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        if (pq.size() < k) {
            pq.push(val);
        } else if (val > pq.top()) {
            pq.pop();
            pq.push(val);
        }
        return pq.top();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log k)$, where $k$ is the value of `k`. This is because the `push` and `pop` operations on the priority queue have a time complexity of $O(\log k)$.
> - **Space Complexity:** $O(k)$, where $k$ is the value of `k`. This is because the priority queue stores at most $k$ elements.
> - **Optimality proof:** This approach is optimal because it only requires a constant amount of work to add an integer to the priority queue and to get the `kth` largest element. The time complexity is $O(\log k)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues and sorting.
- Problem-solving patterns identified: Using a priority queue to store the `k` largest elements in a stream.
- Optimization techniques learned: Using a priority queue to reduce the time complexity of the `add` and `getKthLargest` methods.
- Similar problems to practice: Problems involving priority queues and sorting, such as finding the `kth` smallest element in a stream.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the priority queue is empty before calling `top` or `pop`.
- Edge cases to watch for: The case where `k` is 1, and the case where the stream is empty.
- Performance pitfalls: Using a sorting algorithm with high time complexity, such as bubble sort or insertion sort.
- Testing considerations: Testing the `add` and `getKthLargest` methods with different inputs and edge cases.