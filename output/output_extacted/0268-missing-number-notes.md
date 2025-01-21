## Missing Number

**Problem Link:** https://leetcode.com/problems/missing-number/description

**Problem Statement:**
- Given an array `nums` containing `n` distinct non-negative integers in the range `[0, n]`, where `n` is the length of the array, return the missing number.
- Input format and constraints: `1 <= nums.length <= 10^4`, `0 <= nums[i] <= 10^4`.
- Expected output format: The missing number in the range `[0, n]`.
- Key requirements and edge cases to consider: The input array may contain duplicates, but the missing number is unique.
- Example test cases with explanations:
  - `nums = [3,0,1]`: The missing number is `2`, which is the length of the array minus one.
  - `nums = [0,1]`: The missing number is `2`, which is the length of the array.
  - `nums = [9,6,4,2,3,5,7,0,1]`: The missing number is `8`, which is the missing number in the range `[0, 9]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through the range `[0, n]` and check if each number exists in the input array.
- Step-by-step breakdown of the solution:
  1. Create a set from the input array for efficient lookups.
  2. Iterate through the range `[0, n]` and check if each number exists in the set.
  3. Return the first missing number found.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i <= n; i++) {
            if (numSet.find(i) == numSet.end()) {
                return i;
            }
        }
        return -1; // Should not reach here
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate through the range `[0, n]` once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we create a set to store the input array elements.
> - **Why these complexities occur:** The time complexity occurs because we perform a constant amount of work for each element in the input array. The space complexity occurs because we store all elements of the input array in the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the mathematical formula for the sum of an arithmetic series to calculate the expected sum of numbers in the range `[0, n]`. Then, we can subtract the actual sum of the input array elements to find the missing number.
- Detailed breakdown of the approach:
  1. Calculate the expected sum of numbers in the range `[0, n]` using the formula `n * (n + 1) / 2`.
  2. Calculate the actual sum of the input array elements.
  3. Subtract the actual sum from the expected sum to find the missing number.
- Proof of optimality: This approach has a time complexity of $O(n)$ and a space complexity of $O(1)$, making it optimal.
- Why further optimization is impossible: We must iterate through the input array at least once to find the missing number, so the time complexity cannot be improved.

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;
        for (int num : nums) {
            actualSum += num;
        }
        return expectedSum - actualSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate through the input array once to calculate the actual sum.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we only use a constant amount of space to store the expected sum, actual sum, and missing number.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(1)$, which is the best possible complexity for this problem.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: We can use bitwise operations to find the missing number.
- Unique trade-offs: This approach has the same time and space complexity as the optimal approach but uses bitwise operations instead of arithmetic operations.
- Scenarios where this approach might be preferred: This approach might be preferred in situations where bitwise operations are faster than arithmetic operations.
- Comparison with optimal approach: This approach has the same time and space complexity as the optimal approach but uses a different technique.

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int result = n;
        for (int i = 0; i < n; i++) {
            result = result ^ i ^ nums[i];
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate through the input array once.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we only use a constant amount of space to store the result.
> - **Trade-off analysis:** This approach has the same time and space complexity as the optimal approach but uses bitwise operations instead of arithmetic operations. This might be preferred in situations where bitwise operations are faster than arithmetic operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Arithmetic series formula, bitwise operations.
- Problem-solving patterns identified: Using mathematical formulas to simplify problems, using bitwise operations to improve performance.
- Optimization techniques learned: Reducing time and space complexity by using efficient algorithms and data structures.
- Similar problems to practice: Finding the duplicate number in an array, finding the first missing positive integer in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not validating input.
- Edge cases to watch for: Empty input array, input array with duplicate elements.
- Performance pitfalls: Using inefficient algorithms or data structures, not optimizing for time and space complexity.
- Testing considerations: Testing with different input sizes, testing with edge cases.