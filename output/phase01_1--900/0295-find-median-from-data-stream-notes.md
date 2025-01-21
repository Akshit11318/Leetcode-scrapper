## Find Median from Data Stream
**Problem Link:** https://leetcode.com/problems/find-median-from-data-stream/description

**Problem Statement:**
- Input format and constraints: We need to design a class that supports two operations: `addNum(int num)` to add a number to the data stream and `findMedian()` to return the median of the current data stream. The data stream can contain both positive and negative numbers.
- Expected output format: The median of the current data stream as a double.
- Key requirements and edge cases to consider: Handling an empty data stream, adding duplicate numbers, and finding the median when the data stream has an even or odd number of elements.
- Example test cases with explanations: 
    - Adding 1 and 2 to the data stream and finding the median (should return 1.5).
    - Adding -1 to the data stream and finding the median (should return 1).
    - Adding 3 to the data stream and finding the median (should return 2).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to store all the numbers in a vector and sort it every time we need to find the median.
- Step-by-step breakdown of the solution:
    1. Create a vector to store the numbers.
    2. When `addNum(int num)` is called, add the number to the vector.
    3. When `findMedian()` is called, sort the vector and find the median.
- Why this approach comes to mind first: It is straightforward and easy to implement.

```cpp
class MedianFinder {
public:
    vector<int> nums;

    void addNum(int num) {
        nums.push_back(num);
    }

    double findMedian() {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        if (n % 2 == 0) {
            return (nums[n / 2 - 1] + nums[n / 2]) / 2.0;
        } else {
            return nums[n / 2];
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ for sorting the vector when finding the median, where $n$ is the number of elements in the data stream. The `addNum` operation is $O(1)$.
> - **Space Complexity:** $O(n)$ for storing the numbers in the vector.
> - **Why these complexities occur:** The brute force approach involves sorting the entire vector every time we need to find the median, which leads to a high time complexity. The space complexity is linear because we need to store all the numbers in the vector.

---

### Better Approach

**Explanation:**
- Key insight that leads to improvement: Instead of sorting the entire vector every time, we can use a balanced binary search tree (BST) to store the numbers. This will allow us to find the median in $O(\log n)$ time.
- How it improves upon the brute force: The better approach reduces the time complexity of finding the median from $O(n \log n)$ to $O(\log n)$.
- Why this isn't yet the optimal solution: While the better approach improves the time complexity, it still uses a single data structure to store all the numbers. We can further improve the solution by using two data structures to store the smaller and larger halves of the numbers separately.

```cpp
class MedianFinder {
public:
    set<int> nums;

    void addNum(int num) {
        nums.insert(num);
    }

    double findMedian() {
        vector<int> sorted_nums(nums.begin(), nums.end());
        int n = sorted_nums.size();
        if (n % 2 == 0) {
            return (sorted_nums[n / 2 - 1] + sorted_nums[n / 2]) / 2.0;
        } else {
            return sorted_nums[n / 2];
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ for inserting a number into the set, and $O(n \log n)$ for finding the median (because we need to create a sorted vector). The `addNum` operation is $O(\log n)$.
> - **Space Complexity:** $O(n)$ for storing the numbers in the set.
> - **Improvement over brute force:** The better approach reduces the time complexity of finding the median from $O(n \log n)$ to $O(\log n)$ for the `addNum` operation, but the time complexity of finding the median is still $O(n \log n)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half of the numbers. This will allow us to find the median in $O(1)$ time.
- Detailed breakdown of the approach:
    1. Create a max heap to store the smaller half of the numbers.
    2. Create a min heap to store the larger half of the numbers.
    3. When `addNum(int num)` is called, add the number to the correct heap.
    4. When `findMedian()` is called, find the median using the two heaps.
- Proof of optimality: The optimal approach has a time complexity of $O(\log n)$ for adding a number and $O(1)$ for finding the median, which is the best possible time complexity for this problem.

```cpp
class MedianFinder {
public:
    priority_queue<int> max_heap; // max heap to store the smaller half of the numbers
    priority_queue<int, vector<int>, greater<int>> min_heap; // min heap to store the larger half of the numbers

    void addNum(int num) {
        if (max_heap.empty() || num <= max_heap.top()) {
            max_heap.push(num);
        } else {
            min_heap.push(num);
        }
        // Balance the two heaps
        if (max_heap.size() > min_heap.size() + 1) {
            min_heap.push(max_heap.top());
            max_heap.pop();
        } else if (min_heap.size() > max_heap.size()) {
            max_heap.push(min_heap.top());
            min_heap.pop();
        }
    }

    double findMedian() {
        if (max_heap.size() == min_heap.size()) {
            return (max_heap.top() + min_heap.top()) / 2.0;
        } else {
            return (double)max_heap.top();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ for adding a number to the heaps, and $O(1)$ for finding the median.
> - **Space Complexity:** $O(n)$ for storing the numbers in the heaps.
> - **Optimality proof:** The optimal approach has the best possible time complexity for this problem, and it uses the minimum amount of space necessary to store the numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using heaps to solve problems that require finding the median or other quantiles.
- Problem-solving patterns identified: Balancing two data structures to maintain a certain property (in this case, the balance between the two heaps).
- Optimization techniques learned: Using two heaps to reduce the time complexity of finding the median from $O(n \log n)$ to $O(1)$.
- Similar problems to practice: Finding the k-th smallest element in an unsorted array, finding the median of two sorted arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not balancing the two heaps correctly, not handling the case where the data stream is empty.
- Edge cases to watch for: Handling duplicate numbers, handling the case where the data stream has an even or odd number of elements.
- Performance pitfalls: Using a single data structure to store all the numbers, not using heaps to reduce the time complexity of finding the median.
- Testing considerations: Testing the `addNum` and `findMedian` methods separately, testing the case where the data stream is empty, testing the case where the data stream has an even or odd number of elements.