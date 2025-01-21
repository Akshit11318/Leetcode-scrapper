## Partition Array into Three Parts with Equal Sum

**Problem Link:** https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers as input and requires partitioning it into three parts with equal sums. The input array is guaranteed to have at least three elements.
- Expected output format: The function should return `true` if the array can be partitioned into three parts with equal sums and `false` otherwise.
- Key requirements and edge cases to consider: The sum of the three parts must be equal, and the parts must be contiguous subarrays.
- Example test cases with explanations:
  - `[0,2,1,-6,6,-7,9,1,2,0,1]`: The array can be partitioned into three parts with equal sums as `0, 2, 1` (sum = 3), `-6, 6` (sum = 0), and `-7, 9, 1, 2, 0, 1` (sum = 6). However, the sums of these parts are not equal, so the function should return `false`.
  - `[1,1,1]`: The array can be partitioned into three parts with equal sums as `1`, `1`, and `1`, so the function should return `true`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible ways to partition the array into three parts.
- Step-by-step breakdown of the solution:
  1. Calculate the total sum of the array.
  2. Check if the total sum is divisible by 3. If not, return `false`.
  3. Calculate the target sum for each part.
  4. Iterate over all possible partition points to divide the array into three parts.
  5. Check if the sums of the three parts are equal to the target sum.
- Why this approach comes to mind first: It is a straightforward approach to try all possible partitions and check if any of them satisfy the condition.

```cpp
class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& A) {
        int n = A.size();
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += A[i];
        }
        
        if (totalSum % 3 != 0) {
            return false;
        }
        
        int targetSum = totalSum / 3;
        int count = 0;
        int currentSum = 0;
        
        for (int i = 0; i < n; i++) {
            currentSum += A[i];
            if (currentSum == targetSum) {
                count++;
                currentSum = 0;
            }
        }
        
        return count >= 3;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are iterating over the array twice: once to calculate the total sum and once to find the partition points.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the total sum, target sum, and other variables.
> - **Why these complexities occur:** The time complexity is linear because we are scanning the array a constant number of times, and the space complexity is constant because we are not using any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the total sum and target sum in a single pass, and then iterate over the array to find the partition points.
- Detailed breakdown of the approach:
  1. Calculate the total sum of the array and check if it is divisible by 3.
  2. Calculate the target sum for each part.
  3. Initialize a variable to keep track of the current sum and a counter for the number of parts.
  4. Iterate over the array, adding each element to the current sum.
  5. If the current sum equals the target sum, increment the counter and reset the current sum.
  6. If the counter reaches 3, return `true`.
- Proof of optimality: This approach is optimal because it only requires a single pass over the array, resulting in a linear time complexity.
- Why further optimization is impossible: We must iterate over the array at least once to calculate the total sum and find the partition points, so the time complexity cannot be improved.

```cpp
class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& A) {
        int n = A.size();
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += A[i];
        }
        
        if (totalSum % 3 != 0) {
            return false;
        }
        
        int targetSum = totalSum / 3;
        int count = 0;
        int currentSum = 0;
        
        for (int i = 0; i < n; i++) {
            currentSum += A[i];
            if (currentSum == targetSum) {
                count++;
                currentSum = 0;
            }
        }
        
        return count >= 3;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the total sum, target sum, and other variables.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the array, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear scanning, divisibility checks, and partitioning.
- Problem-solving patterns identified: Checking for divisibility and using counters to track the number of parts.
- Optimization techniques learned: Reducing the number of passes over the array to achieve linear time complexity.
- Similar problems to practice: Partitioning arrays into equal sums, finding maximum or minimum values in arrays, and checking for divisibility.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for divisibility before attempting to partition the array.
- Edge cases to watch for: Empty arrays, arrays with a single element, and arrays with negative numbers.
- Performance pitfalls: Using nested loops or recursive functions, which can result in quadratic or exponential time complexities.
- Testing considerations: Test the function with arrays of different sizes, including edge cases, to ensure it works correctly.