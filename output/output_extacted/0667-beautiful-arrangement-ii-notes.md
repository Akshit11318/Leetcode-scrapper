## Beautiful Arrangement II
**Problem Link:** https://leetcode.com/problems/beautiful-arrangement-ii/description

**Problem Statement:**
- Input format and constraints: Given two integers `n` and `k`, construct a `n`-element array `arr` where `arr[i]` is between 1 and `n` (inclusive), and `|arr[i] - arr[i - 1]| = k` for `1 <= i <= n - 1`.
- Expected output format: Return a `vector` containing the constructed array `arr`.
- Key requirements and edge cases to consider: 
  - `1 <= n <= 1000`
  - `1 <= k <= 20`
  - `n` is greater than or equal to `2 * k`
- Example test cases with explanations: For example, given `n = 3` and `k = 1`, a possible output is `[1, 2, 3]` or `[3, 2, 1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by checking all possible permutations of numbers from `1` to `n` and validate if the difference between consecutive elements is `k`.
- Step-by-step breakdown of the solution: 
  1. Generate all permutations of numbers from `1` to `n`.
  2. For each permutation, check if the absolute difference between consecutive elements is `k`.
  3. If such a permutation exists, return it.
- Why this approach comes to mind first: This is a straightforward approach that checks all possibilities, but it's inefficient due to the large number of permutations.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> constructArray(int n, int k) {
        std::vector<int> result(n);
        for (int i = 1; i <= n; i++) {
            result[i - 1] = i;
        }
        std::sort(result.begin(), result.end());
        do {
            bool isValid = true;
            for (int i = 1; i < n; i++) {
                if (abs(result[i] - result[i - 1]) != k) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                return result;
            }
        } while (std::next_permutation(result.begin(), result.end()));
        return {};
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, because we are generating all permutations of `n` numbers.
> - **Space Complexity:** $O(n)$, for storing the permutation.
> - **Why these complexities occur:** Generating all permutations and checking each one leads to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can construct the array by iterating from `1` to `n` and placing the numbers in a way that satisfies the condition `|arr[i] - arr[i - 1]| = k`.
- Detailed breakdown of the approach:
  1. Initialize an empty vector `result` to store the constructed array.
  2. Initialize two pointers, `left` and `right`, to `1` and `n`, respectively.
  3. Alternate between adding `left` and `right` to the `result` vector, decrementing `left` and incrementing `right` after each addition.
  4. Once `left` exceeds `right`, start adding the remaining numbers in ascending order.
- Proof of optimality: This approach ensures that the difference between consecutive elements is always `k`, and it constructs the array in linear time.

```cpp
class Solution {
public:
    std::vector<int> constructArray(int n, int k) {
        std::vector<int> result;
        int left = 1, right = n;
        for (int i = 0; i < n - k; i++) {
            result.push_back(left++);
        }
        for (int i = 0; i < k; i++) {
            if (i % 2 == 0) {
                result.push_back(right--);
            } else {
                result.push_back(left++);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we are iterating from `1` to `n` once.
> - **Space Complexity:** $O(n)$, for storing the constructed array.
> - **Optimality proof:** This approach constructs the array in linear time and ensures that the difference between consecutive elements is always `k`, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Constructing an array that satisfies a specific condition, using two pointers to iterate from both ends.
- Problem-solving patterns identified: Alternating between two pointers to construct the array.
- Optimization techniques learned: Using a linear approach to construct the array instead of generating all permutations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the base case, not initializing the pointers correctly.
- Edge cases to watch for: When `n` is less than `2 * k`, there is no valid solution.
- Performance pitfalls: Generating all permutations, which leads to high time complexity.
- Testing considerations: Test the function with different values of `n` and `k` to ensure it works correctly.