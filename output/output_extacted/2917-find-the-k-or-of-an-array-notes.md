## Find the Kth Largest Element in an Array
**Problem Link:** https://leetcode.com/problems/find-the-k-or-of-an-array/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= k <= nums.size()`.
- Expected output format: The kth largest element in the array.
- Key requirements and edge cases to consider: Handling duplicates, edge cases where `k` is 1 or the size of the array.
- Example test cases with explanations:
  - Input: `nums = [3,2,1,5,6,4]`, `k = 2`
    Output: `5`
  - Input: `nums = [3,2,3]`, `k = 1`
    Output: `3`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the array in descending order and select the kth element.
- Step-by-step breakdown of the solution:
  1. Validate the input array and `k`.
  2. Sort the array in descending order.
  3. Return the kth element.
- Why this approach comes to mind first: It's straightforward and easy to implement.

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Validate input
        if (k < 1 || k > nums.size()) {
            throw invalid_argument("k is out of range");
        }
        
        // Sort the array in descending order
        sort(nums.rbegin(), nums.rend());
        
        // Return the kth element
        return nums[k - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the size of the input array.
> - **Space Complexity:** $O(1)$ if we ignore the space required for sorting, or $O(n)$ if we consider the space required for sorting in the worst case.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity depends on the sorting algorithm used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a heap data structure to find the kth largest element.
- Detailed breakdown of the approach:
  1. Create a min-heap and insert the first `k` elements of the array.
  2. Iterate through the rest of the array, and for each element, if it's larger than the root of the heap, remove the root and insert the new element.
  3. The root of the heap will be the kth largest element.
- Proof of optimality: This approach has a time complexity of $O(n \log k)$, which is optimal because we need to at least read the input array once.

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a min-heap
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        // Insert the first k elements into the heap
        for (int i = 0; i < k; i++) {
            minHeap.push(nums[i]);
        }
        
        // Iterate through the rest of the array
        for (int i = k; i < nums.size(); i++) {
            // If the current element is larger than the root of the heap
            if (nums[i] > minHeap.top()) {
                // Remove the root and insert the new element
                minHeap.pop();
                minHeap.push(nums[i]);
            }
        }
        
        // The root of the heap is the kth largest element
        return minHeap.top();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the size of the input array.
> - **Space Complexity:** $O(k)$ for the heap.
> - **Optimality proof:** This approach is optimal because we need to at least read the input array once, and the heap operations take $O(\log k)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Heap data structure, sorting, and iteration.
- Problem-solving patterns identified: Using a min-heap to find the kth largest element.
- Optimization techniques learned: Reducing the time complexity by using a heap instead of sorting the entire array.
- Similar problems to practice: Finding the kth smallest element, finding the median of an array.

**Mistakes to Avoid:**
- Common implementation errors: Not validating the input, not handling edge cases.
- Edge cases to watch for: Handling duplicates, edge cases where `k` is 1 or the size of the array.
- Performance pitfalls: Using a sorting algorithm with a high time complexity.
- Testing considerations: Testing with different input sizes, testing with edge cases.