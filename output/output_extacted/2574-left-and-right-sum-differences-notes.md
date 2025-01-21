## Left and Right Sum Differences
**Problem Link:** https://leetcode.com/problems/left-and-right-sum-differences/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The length of `nums` is between 2 and 1000, and each element in `nums` is between 1 and 1000.
- Expected Output: An array of integers where the `i-th` element is the difference between the sum of the elements to the right of `i` and the sum of the elements to the left of `i`.
- Key Requirements and Edge Cases: Handle arrays with varying lengths and element values, ensuring the solution is efficient for large inputs.

**Example Test Cases:**
- For `nums = [10,4,8,3]`, the expected output is `[15,1,11,22]`.
- For `nums = [1,2,3,4,5,6]`, the expected output is `[21,15,9,3,-3,-9]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the sum of elements to the left and right of each index `i` and then finding the difference between these two sums.
- Step-by-step breakdown:
  1. Iterate through the array for each element `i`.
  2. For each `i`, iterate through the array again to calculate the sum of elements to the left and right of `i`.
  3. Calculate the difference between the right sum and the left sum for each `i`.
- This approach comes to mind first because it directly addresses the problem statement without requiring any additional insights.

```cpp
#include <vector>

std::vector<int> leftRigthDifference(std::vector<int>& nums) {
    std::vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        int leftSum = 0, rightSum = 0;
        for (int j = 0; j < i; j++) {
            leftSum += nums[j];
        }
        for (int j = i + 1; j < nums.size(); j++) {
            rightSum += nums[j];
        }
        result.push_back(rightSum - leftSum);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`. This is because for each element, we are potentially iterating through the entire array again.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is for storing the result.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, while the space complexity is linear due to the output vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of recalculating the sum of elements to the left and right of each index `i` from scratch, we can calculate the total sum of the array once and then iteratively update the left and right sums as we move through the array.
- Detailed breakdown:
  1. Calculate the total sum of the array `nums`.
  2. Initialize variables to keep track of the left sum (initially 0) and the result vector.
  3. Iterate through `nums`, updating the left sum and calculating the right sum as the difference between the total sum and the left sum plus the current element.
  4. Calculate the difference between the right sum and the left sum for each element and store it in the result vector.
- Proof of optimality: This approach is optimal because it reduces the time complexity from quadratic to linear by avoiding redundant calculations.

```cpp
std::vector<int> leftRigthDifference(std::vector<int>& nums) {
    int totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }
    
    int leftSum = 0;
    std::vector<int> result;
    for (int num : nums) {
        int rightSum = totalSum - leftSum - num;
        result.push_back(rightSum - leftSum);
        leftSum += num;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we make two passes through the array: one to calculate the total sum and another to calculate the differences.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is for storing the result.
> - **Optimality proof:** The linear time complexity is optimal because we must at least read the input once, and our solution does this in two linear passes, avoiding any unnecessary redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include avoiding redundant calculations and using iterative approaches to update sums.
- Problem-solving patterns identified include the importance of understanding the problem constraints and looking for ways to reduce computational complexity.
- Optimization techniques learned include calculating total sums beforehand and iteratively updating relevant variables.

**Mistakes to Avoid:**
- Common implementation errors include not handling edge cases properly (e.g., arrays of length 2) and not optimizing for performance.
- Performance pitfalls include using nested loops when a linear solution is possible.
- Testing considerations include ensuring that the solution works correctly for arrays of varying lengths and with different element values.