## Make Array Zero by Subtracting Equal Amounts

**Problem Link:** https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 1000`, `-1000 <= nums[i] <= 1000`.
- Expected Output: Return the minimum number of operations required to make all elements in the array zero.
- Key Requirements: We can subtract the same non-zero integer from each element in the array in one operation.
- Edge Cases: The input array may contain zeros or all elements may be the same.

**Example Test Cases:**
- Input: `nums = [1,5,10,10]`
  - Output: `4`
  - Explanation: We can subtract `1` from each element in `4` operations.
- Input: `nums = [0,0,0]`
  - Output: `0`
  - Explanation: The array already contains all zeros, so no operations are needed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible values that can be subtracted from each element.
- Step-by-step breakdown:
  1. Generate all possible values that can be subtracted.
  2. For each value, subtract it from each element in the array and count the number of operations required to make all elements zero.
  3. Keep track of the minimum number of operations.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by trying all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <climits>

int minimumOperations(std::vector<int>& nums) {
    int minOps = INT_MAX;
    for (int val = -1000; val <= 1000; val++) {
        if (val == 0) continue; // Skip zero since it doesn't change the array
        int ops = 0;
        bool allZero = true;
        for (int num : nums) {
            int currOps = (num - val) / val;
            if (currOps < 0) {
                currOps = -currOps;
            }
            ops = std::max(ops, currOps);
            if (num % val != 0) {
                allZero = false;
                break;
            }
        }
        if (allZero) {
            minOps = std::min(minOps, ops);
        }
    }
    return minOps == INT_MAX ? -1 : minOps; // If no valid operations, return -1
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2001)$ where $n$ is the length of the input array. This is because we try all possible values (`-1000` to `1000`) and for each value, we iterate over the array.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array, since we use a constant amount of space.
> - **Why these complexities occur:** The brute force approach tries all possible values and for each value, it iterates over the array to calculate the number of operations required.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The minimum number of operations is determined by the greatest common divisor (GCD) of all the numbers in the array.
- Detailed breakdown:
  1. Calculate the GCD of all numbers in the array.
  2. If the GCD is zero, it means all numbers are zero, so return `0`.
  3. Otherwise, return the maximum number of operations required to make each number zero, which is the absolute value of the number divided by the GCD.
- Proof of optimality: This approach is optimal because the GCD represents the largest number that can be subtracted from all elements in the array in one operation.

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int minimumOperations(std::vector<int>& nums) {
    int g = 0;
    for (int num : nums) {
        if (num != 0) {
            g = gcd(g, abs(num));
            if (g == 1) break;
        }
    }
    if (g == 0) return 0; // All numbers are zero
    int maxOps = 0;
    for (int num : nums) {
        if (num != 0) {
            maxOps = std::max(maxOps, abs(num) / g);
        }
    }
    return maxOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(m))$ where $n$ is the length of the input array and $m$ is the maximum absolute value in the array. This is because we calculate the GCD of all numbers in the array.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array, since we use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it uses the GCD to minimize the number of operations required to make all elements in the array zero.

---

### Final Notes

**Learning Points:**
- The key to solving this problem is to understand that the minimum number of operations is determined by the GCD of all the numbers in the array.
- We can use the Euclidean algorithm to calculate the GCD of two numbers.
- This problem demonstrates the importance of understanding the properties of GCD and how it can be used to optimize solutions.

**Mistakes to Avoid:**
- Not considering the case where all numbers in the array are zero.
- Not using the GCD to minimize the number of operations.
- Not handling the case where the GCD is zero correctly.
- Not optimizing the solution by using the GCD to reduce the number of operations.