## Monotonic Array
**Problem Link:** https://leetcode.com/problems/monotonic-array/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10000`.
- Expected output format: A boolean indicating whether the array is monotonic.
- Key requirements and edge cases to consider:
  - An array is monotonic if it is either monotonically increasing or monotonically decreasing.
  - An array `A` is monotonically increasing if for all `i <= j`, `A[i] <= A[j]`.
  - An array `A` is monotonically decreasing if for all `i <= j`, `A[i] >= A[j]`.
- Example test cases with explanations:
  - `[1, 2, 2, 3]` is monotonic because it is monotonically increasing.
  - `[6, 5, 4, 4]` is monotonic because it is monotonically decreasing.
  - `[1, 3, 2]` is not monotonic.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if the array is monotonic, we can compare each element with its next element to determine if the array is increasing or decreasing.
- Step-by-step breakdown of the solution:
  1. Initialize two flags, `increasing` and `decreasing`, to `true`.
  2. Iterate through the array, comparing each element with its next element.
  3. If we find an element that is greater than its next element, set `increasing` to `false`.
  4. If we find an element that is less than its next element, set `decreasing` to `false`.
  5. After iterating through the entire array, check the values of `increasing` and `decreasing`. If either is `true`, the array is monotonic.

```cpp
class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool increasing = true;
        bool decreasing = true;
        
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                increasing = false;
            }
            if (nums[i] < nums[i + 1]) {
                decreasing = false;
            }
        }
        
        return increasing || decreasing;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the flags.
> - **Why these complexities occur:** The time complexity is linear because we are performing a single pass through the array, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same approach as the brute force can be considered optimal because we must examine each element at least once to determine if the array is monotonic.
- Detailed breakdown of the approach:
  1. Initialize two flags, `increasing` and `decreasing`, to `true`.
  2. Iterate through the array, comparing each element with its next element.
  3. If we find an element that is greater than its next element, set `increasing` to `false`.
  4. If we find an element that is less than its next element, set `decreasing` to `false`.
  5. After iterating through the entire array, check the values of `increasing` and `decreasing`. If either is `true`, the array is monotonic.
- Proof of optimality: This approach is optimal because we must examine each element at least once to determine if the array is monotonic, resulting in a time complexity of $O(n)$.

```cpp
class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool increasing = true;
        bool decreasing = true;
        
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                increasing = false;
            }
            if (nums[i] < nums[i + 1]) {
                decreasing = false;
            }
            if (!increasing && !decreasing) {
                return false;
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the flags.
> - **Optimality proof:** This approach is optimal because we must examine each element at least once to determine if the array is monotonic.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and flagging.
- Problem-solving patterns identified: Checking for monotonicity in an array.
- Optimization techniques learned: Reducing unnecessary comparisons by returning early when both flags are false.
- Similar problems to practice: Checking for sorted arrays, finding the longest increasing subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: Arrays with duplicate elements, arrays with a mix of increasing and decreasing sequences.
- Performance pitfalls: Using unnecessary data structures or algorithms that have higher time complexities.
- Testing considerations: Testing with arrays of different sizes, testing with arrays that are already sorted, testing with arrays that are not sorted.