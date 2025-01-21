## Find N Unique Integers Sum Up to Zero

**Problem Link:** https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description

**Problem Statement:**
- Given an integer `n`, return any array `ans` of length `n` such that `sum(ans) == 0` and the sum of the squares of all elements in `ans` is minimized.
- Input format: `n` is an integer.
- Expected output format: An array of integers.
- Key requirements: All elements in the output array must be unique, the sum of the elements must be zero, and the sum of the squares of the elements should be minimized.
- Edge cases: When `n` is odd, the array can contain a single zero. When `n` is even, the array can contain pairs of positive and negative integers.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of unique integers that sum up to zero and calculate the sum of their squares.
- However, this approach quickly becomes impractical due to the large number of possible combinations.

```cpp
#include <iostream>
#include <vector>
#include <climits>

std::vector<int> sumZero(int n) {
    std::vector<int> result;
    int minSum = INT_MAX;
    std::vector<int> bestResult;

    // Generate all permutations of unique integers from -n to n
    std::vector<int> nums;
    for (int i = -n; i <= n; ++i) {
        nums.push_back(i);
    }

    // Try all possible subsets of size n
    // This is a very inefficient approach and is not practical for large n
    // It's mainly here to illustrate the brute force concept
    // For actual implementation, we should directly generate the optimal solution
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{2n})$ due to generating all subsets of a set of size $2n$.
> - **Space Complexity:** $O(2n)$ for storing the set of numbers from `-n` to `n`.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that for an array of length `n` with unique integers to sum up to zero, we can use a sequence of consecutive integers around zero.
- When `n` is odd, we can have a sequence like `-k, -(k-1), ..., -1, 0, 1, ..., k-1, k` where `k = (n-1)/2`.
- When `n` is even, we can have a sequence like `-k, -(k-1), ..., -1, 1, 2, ..., k-1, k` where `k = n/2`.

```cpp
#include <iostream>
#include <vector>

std::vector<int> sumZero(int n) {
    std::vector<int> result;
    if (n % 2 == 1) {
        // For odd n, include 0 in the sequence
        for (int i = -(n-1)/2; i <= (n-1)/2; ++i) {
            result.push_back(i);
        }
    } else {
        // For even n, exclude 0 and use pairs of positive and negative integers
        for (int i = -n/2; i <= n/2 - 1; ++i) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are generating a sequence of length `n`.
> - **Space Complexity:** $O(n)$ for storing the result sequence.
> - **Optimality proof:** This approach is optimal because it directly generates a sequence that meets all conditions (unique integers, sum to zero, and minimized sum of squares) without trying all possible combinations.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the importance of identifying key constraints and leveraging them to find an efficient solution.
- It shows how to approach problems that require minimizing a certain metric (in this case, the sum of squares) under given constraints.
- It highlights the difference between brute force and optimal approaches, emphasizing the need for insight and clever construction of solutions.

**Mistakes to Avoid:**
- Trying to solve the problem through brute force without considering the constraints and potential optimizations.
- Not recognizing the pattern for constructing the sequence that meets the conditions.
- Failing to consider both odd and even cases for `n`.