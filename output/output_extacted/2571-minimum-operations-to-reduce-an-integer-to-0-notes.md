## Minimum Operations to Reduce an Integer to 0

**Problem Link:** https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `1 <= n <= 10^6`.
- Expected Output: The minimum number of operations required to reduce `n` to 0.
- Key Requirements: The operations allowed are subtracting 1 or dividing by 2 (if `n` is even).
- Edge Cases: `n` could be an odd or even number, and could be close to the maximum limit or minimum limit of the given constraints.

**Example Test Cases:**
- For `n = 3`, the minimum operations would be 2 (subtract 1 to get 2, then divide by 2 to get 1, then subtract 1 to get 0).
- For `n = 6`, the minimum operations would be 3 (divide by 2 to get 3, then divide by 2 to get 1.5 which is not allowed, so instead, subtract 1 to get 5, then subtract 1 to get 4, then divide by 2 to get 2, then divide by 2 to get 1, then subtract 1 to get 0. However, a more optimal approach is to subtract 1 to get 5, then divide by 2 and get a non-integer result which is not allowed, so we actually follow the sequence: divide by 2 to get 3, then divide by 2 to get 1.5 which is not allowed, so instead we do: subtract 1 to get 5, then divide by 2 and get a non-integer result which is not allowed, so we do: divide by 2 to get 3, then subtract 1 to get 2, then divide by 2 to get 1, then subtract 1 to get 0).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of subtracting 1 and dividing by 2 to reach 0 and keep track of the minimum number of operations.
- However, due to the nature of the problem, a brute force approach would be highly inefficient, especially for larger inputs, because it would involve trying all possible sequences of operations, which grows exponentially with the size of the input.

```cpp
int minOperations(int n) {
    if (n == 0) return 0;
    int minOps = n; // Substracting 1 n times
    for (int ops = 0; n > 0; ops++) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n -= 1;
        }
        if (ops > minOps) break;
    }
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because in the worst case, we might have to perform operations `n` times.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is linear because we are essentially counting down from `n` to 0, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that the optimal strategy involves always dividing by 2 when possible (since it reduces the number of operations more significantly than subtracting 1) and only subtracting 1 when `n` is odd.
- We can implement this strategy using a simple loop that continues until `n` reaches 0, keeping track of the number of operations performed.
- This approach is optimal because it minimizes the number of operations by maximizing the use of division by 2, which reduces the value of `n` more efficiently than subtracting 1.

```cpp
int minOperations(int n) {
    int operations = 0;
    while (n > 0) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n -= 1;
        }
        operations++;
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ because we are effectively reducing the size of `n` by half in each step when `n` is even, which leads to a logarithmic number of operations.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the number of operations and the current value of `n`.
> - **Optimality proof:** This approach is optimal because it always chooses the operation that reduces the value of `n` the most (division by 2 when `n` is even) and only resorts to subtracting 1 when `n` is odd, ensuring the minimum number of operations to reach 0.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a greedy strategy to minimize the number of operations.
- The problem-solving pattern identified is the importance of choosing the operation that maximizes the reduction in the problem size at each step.
- The optimization technique learned is the use of division to reduce the problem size more efficiently than subtraction.

**Mistakes to Avoid:**
- A common mistake is to overlook the importance of always dividing by 2 when possible, leading to suboptimal solutions.
- Another mistake is to not consider the base case where `n` is 0, which requires handling to avoid infinite loops.
- Testing considerations include ensuring the function works correctly for both even and odd inputs, as well as for the boundary cases (e.g., `n = 1`, `n = 2`).