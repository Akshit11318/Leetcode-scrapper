## Find Peak Element
**Problem Link:** [https://leetcode.com/problems/find-peak-element/description](https://leetcode.com/problems/find-peak-element/description)

**Problem Statement:**
- Input format: An integer array `nums` of size `n`.
- Constraints: `1 <= nums.length <= 10^4`, `nums[i] != nums[i + 1]`.
- Expected output format: The index of a peak element in the array.
- Key requirements and edge cases to consider: A peak element is an element which is not smaller than its neighbors. If there are multiple peak elements, any of them can be returned. The array may contain duplicate elements.
- Example test cases with explanations: 
    - Example 1: Input: `nums = [1,2,3,1]`, Output: `2`, Explanation: `3` is a peak element and your function should return the index number `2`.
    - Example 2: Input: `nums = [1,2,1,3,5,6,4]`, Output: `1` or `5`, Explanation: Your function can return either index number `1` where the peak element is `2`, or index number `5` where the peak element is `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find a peak element, we need to check each element in the array and compare it with its neighbors.
- Step-by-step breakdown of the solution: 
    1. Iterate through the array from the second element to the second last element (inclusive).
    2. For each element, check if it is greater than its previous and next element.
    3. If an element satisfies the condition, return its index.
    4. If no such element is found after iterating through the entire array, check the first and last elements separately.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that checks every possible peak element.

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        // Check the first element
        if (n == 1 || nums[0] > nums[1]) {
            return 0;
        }
        // Check the middle elements
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
                return i;
            }
        }
        // Check the last element
        if (nums[n - 1] > nums[n - 2]) {
            return n - 1;
        }
        // If no peak element is found
        return -1; // This line will never be reached due to the problem constraints
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are potentially checking every element in the array.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is linear because we are iterating through the array once, and the space complexity is constant because we are only using a constant amount of space to store the index of the peak element.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the peak element. The idea is to divide the array into two halves and determine which half contains a peak element.
- Detailed breakdown of the approach: 
    1. Start by considering the middle element of the array.
    2. If the middle element is a peak element, return its index.
    3. If the middle element is smaller than the next element, then there must be a peak element in the right half of the array.
    4. If the middle element is greater than the next element, then there must be a peak element in the left half of the array.
    5. Repeat the process until a peak element is found.
- Proof of optimality: This approach is optimal because it reduces the search space by half at each step, resulting in a logarithmic time complexity.

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[mid + 1]) {
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
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the array. This is because we are dividing the search space in half at each step.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it has a logarithmic time complexity, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, peak element detection.
- Problem-solving patterns identified: Reducing the search space by dividing it into smaller sub-problems.
- Optimization techniques learned: Using a binary search approach to achieve a logarithmic time complexity.
- Similar problems to practice: Finding the first bad version, searching for a range in a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not checking for the base case in the recursive approach.
- Edge cases to watch for: Empty array, array with a single element, array with duplicate elements.
- Performance pitfalls: Using a linear search approach, not optimizing the search space.
- Testing considerations: Testing with different input sizes, testing with edge cases, testing with duplicate elements.