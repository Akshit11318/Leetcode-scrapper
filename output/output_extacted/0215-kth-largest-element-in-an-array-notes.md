## Kth Largest Element in an Array

**Problem Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.
- Expected output format: The `k`th largest element in the array.
- Key requirements and edge cases to consider: 
  - `1 <= k <= nums.length`
  - `-10^4 <= nums[i] <= 10^4`
- Example test cases with explanations: 
  - Example 1: Input: `nums = [3,2,1,5,6,4]`, `k = 2`, Output: `5`
  - Example 2: Input: `nums = [3,2,3,1,2,4,5,5,6]`, `k = 4`, Output: `4`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to sort the array in descending order and then select the `k`th element.
- Step-by-step breakdown of the solution: 
  1. Sort the array in descending order using a sorting algorithm like bubble sort, selection sort, or quicksort.
  2. Select the `k`th element from the sorted array.
- Why this approach comes to mind first: It is a simple and intuitive solution that directly addresses the problem statement.

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Sort the array in descending order
        sort(nums.rbegin(), nums.rend());
        
        // Select the kth element
        return nums[k-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$ if the sorting algorithm is in-place, or $O(n)$ if the sorting algorithm requires additional space.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity depends on the specific sorting algorithm used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the entire array, we can use a priority queue (or heap) to keep track of the `k` largest elements.
- Detailed breakdown of the approach: 
  1. Create a min-heap and insert the first `k` elements into the heap.
  2. Iterate through the remaining elements in the array. For each element, if it is larger than the smallest element in the heap, remove the smallest element from the heap and insert the current element.
  3. After iterating through the entire array, the smallest element in the heap is the `k`th largest element.
- Proof of optimality: This approach has a time complexity of $O(n \log k)$, which is optimal because we only need to consider the `k` largest elements.

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a min-heap and insert the first k elements
        priority_queue<int, vector<int>, greater<int>> minHeap;
        for (int i = 0; i < k; i++) {
            minHeap.push(nums[i]);
        }
        
        // Iterate through the remaining elements
        for (int i = k; i < nums.size(); i++) {
            if (nums[i] > minHeap.top()) {
                minHeap.pop();
                minHeap.push(nums[i]);
            }
        }
        
        // The smallest element in the heap is the kth largest
        return minHeap.top();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of elements in the array and $k$ is the number of largest elements to consider.
> - **Space Complexity:** $O(k)$ for the min-heap.
> - **Optimality proof:** This approach is optimal because it only considers the `k` largest elements and uses a min-heap to efficiently keep track of the smallest element among them.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: We can use the `nth_element` function in C++ to find the `k`th largest element in the array.
- Unique trade-offs: This approach is more concise and easier to implement, but it may not be as efficient as the optimal approach for large arrays.
- Scenarios where this approach might be preferred: When code readability and simplicity are more important than performance.
- Comparison with optimal approach: This approach has a time complexity of $O(n)$ on average, but it may not be as efficient as the optimal approach for large arrays.

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Use nth_element to find the kth largest element
        nth_element(nums.begin(), nums.begin() + k, nums.end(), greater<int>());
        
        // Return the kth largest element
        return nums[k-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ on average, but may be $O(n^2)$ in the worst case.
> - **Space Complexity:** $O(1)$ if the `nth_element` function is in-place, or $O(n)$ if it requires additional space.
> - **Trade-off analysis:** This approach is more concise and easier to implement, but it may not be as efficient as the optimal approach for large arrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, priority queues, and the `nth_element` function.
- Problem-solving patterns identified: Using a min-heap to keep track of the `k` largest elements and using the `nth_element` function to find the `k`th largest element.
- Optimization techniques learned: Using a min-heap to reduce the time complexity and using the `nth_element` function to simplify the code.
- Similar problems to practice: Finding the `k`th smallest element, finding the median of an array, and finding the `k`th largest element in a stream of data.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty array or `k` being larger than the array size.
- Edge cases to watch for: Handling duplicate elements and handling the case where `k` is equal to the array size.
- Performance pitfalls: Using a sorting algorithm with a high time complexity, such as bubble sort or insertion sort, and not using a min-heap to reduce the time complexity.
- Testing considerations: Testing the code with different input sizes, testing the code with duplicate elements, and testing the code with edge cases.