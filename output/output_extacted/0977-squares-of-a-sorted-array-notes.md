## Squares of a Sorted Array

**Problem Link:** https://leetcode.com/problems/squares-of-a-sorted-array/description

**Problem Statement:**
- Input: A sorted array `nums` containing `n` integers.
- Constraints: `1 <= n <= 10^4`, `-10^4 <= nums[i] <= 10^4`.
- Expected output: A new sorted array containing the squares of all numbers in `nums`.
- Key requirements: The output array should be sorted in non-decreasing order.
- Example test cases:
  - `nums = [-4, -1, 0, 3, 10]`, expected output: `[0, 1, 9, 16, 100]`.
  - `nums = [-7, -3, 2, 3, 11]`, expected output: `[4, 9, 9, 49, 121]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves squaring each number in the array and then sorting the resulting array.
- Step-by-step breakdown:
  1. Square each number in the input array.
  2. Sort the resulting array in non-decreasing order.
- Why this approach comes to mind first: It directly addresses the problem statement without requiring additional insight into the properties of the input array.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> sortedSquares(std::vector<int>& nums) {
    std::vector<int> result;
    for (int num : nums) {
        result.push_back(num * num);
    }
    std::sort(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the input array. This is because we are sorting the array, which takes $O(n \log n)$ time using the `std::sort` algorithm in C++.
> - **Space Complexity:** $O(n)$, as we create a new array to store the squared numbers.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is due to the creation of a new array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Since the input array is already sorted, we can utilize this property to avoid the need for sorting the squared array.
- Detailed breakdown:
  1. Initialize two pointers, one at the beginning and one at the end of the array.
  2. Compare the absolute values of the numbers at these positions, square the larger one, and place it at the end of the result array.
  3. Move the corresponding pointer towards the center of the array.
  4. Repeat steps 2-3 until all numbers have been processed.
- Proof of optimality: This approach takes advantage of the sorted nature of the input array, allowing us to construct the sorted array of squares in a single pass, thus achieving the optimal time complexity.

```cpp
#include <vector>

std::vector<int> sortedSquares(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> result(n);
    int left = 0, right = n - 1;
    for (int i = n - 1; i >= 0; --i) {
        if (abs(nums[left]) < abs(nums[right])) {
            result[i] = nums[right] * nums[right];
            --right;
        } else {
            result[i] = nums[left] * nums[left];
            ++left;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we process each element exactly once.
> - **Space Complexity:** $O(n)$, as we create a new array to store the squared numbers.
> - **Optimality proof:** The linear time complexity is optimal because we must at least read the input array once, which takes $O(n)$ time.

---

### Final Notes

**Learning Points:**
- Utilizing the properties of the input data to avoid unnecessary operations.
- The importance of understanding the problem constraints and how they can be leveraged to improve efficiency.
- Two-pointer techniques can be very effective in solving problems that involve sorted arrays or sequences.

**Mistakes to Avoid:**
- Overlooking the sorted nature of the input array and thus not taking advantage of it.
- Not considering the absolute values of the numbers when comparing them, which is crucial for correctly placing the squared numbers in the result array.
- Failing to test the solution with edge cases, such as arrays containing negative numbers, zero, or duplicate values.