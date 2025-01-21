## Minimum Operations to Make Array Equal

**Problem Link:** https://leetcode.com/problems/minimum-operations-to-make-array-equal/description

**Problem Statement:**
- Input format: An integer `n`.
- Constraints: `1 <= n <= 10^5`.
- Expected output format: The minimum number of operations required to make all elements in the array equal.
- Key requirements and edge cases to consider: The array is initially empty, and we can add or remove elements to make all elements equal.
- Example test cases with explanations:
  - Input: `n = 3`
  - Output: `2`
  - Explanation: We can create the array `[1, 2, 3]`, then change the 2nd and 3rd elements to 1 to make all elements equal.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible arrays of length `n` and calculate the minimum number of operations required to make all elements equal.
- Step-by-step breakdown of the solution:
  1. Generate all possible arrays of length `n`.
  2. For each array, calculate the minimum number of operations required to make all elements equal.
  3. Return the minimum number of operations among all arrays.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
int minOperations(int n) {
    int minOps = INT_MAX;
    // Generate all possible arrays of length n
    for (int i = 0; i < (1 << n); i++) {
        int ops = 0;
        int arr[n];
        // Create the array
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                arr[j] = 1;
            } else {
                arr[j] = 0;
            }
        }
        // Calculate the minimum number of operations required to make all elements equal
        for (int j = 0; j < n; j++) {
            if (arr[j] != arr[0]) {
                ops++;
            }
        }
        // Update the minimum number of operations
        minOps = min(minOps, ops);
    }
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the input integer. The time complexity comes from generating all possible arrays of length `n` and calculating the minimum number of operations for each array.
> - **Space Complexity:** $O(n)$, where $n$ is the input integer. The space complexity comes from storing the array of length `n`.
> - **Why these complexities occur:** The brute force approach tries all possible arrays of length `n`, which results in exponential time complexity. The space complexity comes from storing the array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The minimum number of operations required to make all elements equal is equal to the minimum between `n/2` and `(n+1)/2`.
- Detailed breakdown of the approach:
  1. Calculate `n/2` and `(n+1)/2`.
  2. Return the minimum between `n/2` and `(n+1)/2`.
- Proof of optimality: The minimum number of operations required to make all elements equal is equal to the minimum between `n/2` and `(n+1)/2`, because we can always make the first `n/2` elements equal to the last `(n+1)/2` elements.
- Why further optimization is impossible: The optimal approach already has a time complexity of $O(1)$, which is the best possible time complexity.

```cpp
int minOperations(int n) {
    return n / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $n$ is the input integer. The time complexity comes from calculating `n/2`.
> - **Space Complexity:** $O(1)$, where $n$ is the input integer. The space complexity comes from storing the result.
> - **Optimality proof:** The optimal approach already has a time complexity of $O(1)$, which is the best possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The optimal approach demonstrates the concept of finding the minimum number of operations required to make all elements equal in an array.
- Problem-solving patterns identified: The problem-solving pattern identified is to find the minimum between `n/2` and `(n+1)/2`.
- Optimization techniques learned: The optimization technique learned is to simplify the problem by finding a pattern or a formula that can be used to calculate the result directly.
- Similar problems to practice: Similar problems to practice include finding the minimum number of operations required to make all elements equal in a linked list or a tree.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a brute force approach that tries all possible arrays of length `n`.
- Edge cases to watch for: An edge case to watch for is when `n` is 1, in which case the minimum number of operations required is 0.
- Performance pitfalls: A performance pitfall is to use a brute force approach that has exponential time complexity.
- Testing considerations: A testing consideration is to test the optimal approach with different values of `n` to ensure that it produces the correct result.