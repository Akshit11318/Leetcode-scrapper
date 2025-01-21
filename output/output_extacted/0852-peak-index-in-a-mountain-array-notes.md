## Peak Index in a Mountain Array

**Problem Link:** https://leetcode.com/problems/peak-index-in-a-mountain-array/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `arr`, where `arr` is a mountain array, find the index of the peak element.
- Expected output format: Return the index of the peak element.
- Key requirements and edge cases to consider: 
  - The input array is guaranteed to be a mountain array, meaning it will have a single peak element.
  - The array will have at least 3 elements.
  - The peak element is the element which is not smaller than its neighbors.
- Example test cases with explanations:
  - Example 1: `arr = [0,1,0]`, Output: `1`. Explanation: The peak element is `1`.
  - Example 2: `arr = [0,2,1,0]`, Output: `1`. Explanation: The peak element is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to find the index of the peak element in the mountain array.
- Step-by-step breakdown of the solution:
  1. Iterate through the array.
  2. For each element, check if it is not smaller than its neighbors.
  3. If it is not smaller than its neighbors, return its index.
- Why this approach comes to mind first: It is a straightforward solution that checks every element in the array.

```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        for (int i = 1; i < arr.size() - 1; i++) {
            if (arr[i] >= arr[i - 1] && arr[i] >= arr[i + 1]) {
                return i;
            }
        }
        return -1; // This line will never be reached
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the index of the peak element.
> - **Why these complexities occur:** The time complexity is linear because we are checking every element in the array, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the peak element in the mountain array.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one at the start of the array and one at the end.
  2. While the pointers have not crossed each other, calculate the middle index.
  3. If the middle element is smaller than the next element, move the left pointer to the middle index + 1.
  4. Otherwise, move the right pointer to the middle index.
- Proof of optimality: This approach has a time complexity of $O(\log n)$, which is optimal for this problem because we are using a binary search approach.
- Why further optimization is impossible: The time complexity of $O(\log n)$ is optimal because we need to check at least $\log n$ elements to find the peak element in the worst case.

```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int left = 0;
        int right = arr.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < arr[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the array, because we are using a binary search approach.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the pointers.
> - **Optimality proof:** The time complexity is optimal because we are using a binary search approach, which reduces the search space by half at each step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, mountain array properties.
- Problem-solving patterns identified: Using a binary search approach to find the peak element in a mountain array.
- Optimization techniques learned: Reducing the search space by half at each step using a binary search approach.
- Similar problems to practice: Finding the peak element in a unimodal array, finding the minimum element in a rotated sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the base cases, not updating the pointers correctly.
- Edge cases to watch for: The input array may have a single element, the input array may not be a mountain array.
- Performance pitfalls: Using a brute force approach, not using a binary search approach.
- Testing considerations: Test the function with different input arrays, including edge cases.