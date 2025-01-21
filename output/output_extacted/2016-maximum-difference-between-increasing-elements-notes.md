## Maximum Difference Between Increasing Elements
**Problem Link:** https://leetcode.com/problems/maximum-difference-between-increasing-elements/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums`, find the maximum difference between two elements in the array such that the larger element appears after the smaller element in the array.
- Expected output format: The function should return the maximum difference.
- Key requirements and edge cases to consider: The array may contain duplicate elements, and the function should handle this case correctly. If no such pair of elements exists, the function should return `-1`.
- Example test cases with explanations:
  - Input: `nums = [7,1,5,4]`
    - Output: `4`
    - Explanation: The maximum difference between two elements in the array such that the larger element appears after the smaller element is `5 - 1 = 4`.
  - Input: `nums = [9,4,3,2]`
    - Output: `-1`
    - Explanation: No such pair of elements exists in the array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every pair of elements in the array to find the maximum difference between two elements such that the larger element appears after the smaller element.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum difference to `-1`.
  2. Iterate over the array using two nested loops to consider every pair of elements.
  3. For each pair of elements, check if the larger element appears after the smaller element.
  4. If it does, calculate the difference between the two elements and update the maximum difference if necessary.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution to a problem, and it can be a good starting point for developing more efficient solutions.

```cpp
class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int max_diff = -1;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] > nums[i]) {
                    max_diff = max(max_diff, nums[j] - nums[i]);
                }
            }
        }
        return max_diff;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because the brute force approach involves iterating over the array using two nested loops.
> - **Space Complexity:** $O(1)$, because the brute force approach only uses a constant amount of space to store the maximum difference.
> - **Why these complexities occur:** The time complexity is quadratic because the brute force approach checks every pair of elements in the array. The space complexity is constant because the brute force approach only uses a small amount of space to store the maximum difference.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach involves iterating over the array only once and keeping track of the minimum element seen so far.
- Detailed breakdown of the approach:
  1. Initialize the minimum element to the first element of the array.
  2. Initialize the maximum difference to `-1`.
  3. Iterate over the array starting from the second element.
  4. For each element, check if it is greater than the minimum element seen so far.
  5. If it is, calculate the difference between the current element and the minimum element, and update the maximum difference if necessary.
  6. Update the minimum element if the current element is smaller.
- Proof of optimality: The optimal approach is optimal because it only requires iterating over the array once, resulting in a linear time complexity.
- Why further optimization is impossible: The optimal approach is already optimal because it only requires a single pass over the array, and any further optimization would not be possible without changing the problem constraints.

```cpp
class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int min_val = nums[0];
        int max_diff = -1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > min_val) {
                max_diff = max(max_diff, nums[i] - min_val);
            }
            min_val = min(min_val, nums[i]);
        }
        return max_diff;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because the optimal approach involves iterating over the array only once.
> - **Space Complexity:** $O(1)$, because the optimal approach only uses a constant amount of space to store the minimum element and the maximum difference.
> - **Optimality proof:** The optimal approach is optimal because it only requires iterating over the array once, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of iterating over an array and keeping track of the minimum element seen so far.
- Problem-solving patterns identified: The problem requires identifying the minimum element seen so far and updating the maximum difference accordingly.
- Optimization techniques learned: The problem demonstrates the importance of optimizing the time complexity by reducing the number of iterations over the array.
- Similar problems to practice: Other problems that involve iterating over an array and keeping track of the minimum or maximum element seen so far, such as finding the maximum subarray sum or the minimum window that contains all elements of a given array.

**Mistakes to Avoid:**
- Common implementation errors: One common mistake is to forget to update the minimum element when a smaller element is encountered.
- Edge cases to watch for: The problem requires handling the case where no such pair of elements exists in the array, in which case the function should return `-1`.
- Performance pitfalls: The brute force approach can result in a high time complexity, which can be avoided by using the optimal approach.
- Testing considerations: The problem requires testing the function with different input arrays, including arrays with duplicate elements and arrays with no pairs of elements that satisfy the condition.