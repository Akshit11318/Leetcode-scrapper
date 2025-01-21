## Find Pivot Index
**Problem Link:** https://leetcode.com/problems/find-pivot-index/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `-1000 <= nums[i] <= 1000`.
- Expected output format: The pivot index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index. If no such index exists, return -1.
- Key requirements and edge cases to consider: 
  - Handling arrays with a single element.
  - Handling arrays where no pivot index exists.
  - Handling arrays where the pivot index is at the start or end.
- Example test cases with explanations:
  - Input: `nums = [1,7,3,6,5,6]`, Output: `3`.
  - Input: `nums = [1,2,3]`, Output: `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the sum of all elements to the left and right of each index and compare them.
- Step-by-step breakdown of the solution:
  1. Iterate over each index in the array.
  2. For each index, calculate the sum of all elements to the left and right.
  3. Compare the sums. If they are equal, return the current index.
- Why this approach comes to mind first: It directly follows from the problem statement, checking each index as a potential pivot.

```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int leftSum = 0;
            for (int j = 0; j < i; j++) {
                leftSum += nums[j];
            }
            int rightSum = 0;
            for (int j = i + 1; j < n; j++) {
                rightSum += nums[j];
            }
            if (leftSum == rightSum) {
                return i;
            }
        }
        return -1; // No pivot index found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we are potentially summing up all other elements.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array. This is because we only use a constant amount of space to store the sums and the current index.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to only using a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Calculate the total sum of the array once and then adjust the sum as we iterate through the array.
- Detailed breakdown of the approach:
  1. Calculate the total sum of the array.
  2. Initialize a variable to keep track of the sum of elements to the left of the current index.
  3. Iterate through the array. For each index, check if the sum of elements to the left equals the total sum minus the sum of elements to the left and the current element.
  4. If a match is found, return the current index.
- Proof of optimality: This approach only requires a single pass through the array, making it more efficient than the brute force approach.

```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        int leftSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1; // No pivot index found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make two passes through the array: one to calculate the total sum and another to find the pivot index.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array. This is because we only use a constant amount of space to store the sums and the current index.
> - **Optimality proof:** This is the best possible time complexity because we must at least look at each element once to determine if it could be the pivot index.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Summation, iteration, and optimization through reducing redundant calculations.
- Problem-solving patterns identified: Breaking down problems into smaller, more manageable parts, and looking for ways to avoid redundant calculations.
- Optimization techniques learned: Calculating totals or sums once and then adjusting them as needed, rather than recalculating for each iteration.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables properly, not handling edge cases (like empty arrays or arrays with a single element).
- Edge cases to watch for: Arrays with negative numbers, arrays with all elements being the same, arrays with a large range of values.
- Performance pitfalls: Using nested loops when a single pass can suffice, not optimizing calculations to reduce time complexity.