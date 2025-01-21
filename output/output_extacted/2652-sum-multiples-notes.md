## Sum Multiples

**Problem Link:** https://leetcode.com/problems/sum-multiples/description

**Problem Statement:**
- Input: `n` - the upper limit of the range.
- Constraints: `1 <= n <= 10^5`.
- Expected Output: The sum of all the multiples of `3` or `5` below `n`.
- Key Requirements: Calculate the sum of multiples of `3` and `5` up to but not including `n`.
- Edge Cases: Handle the case when `n` is less than `3` or `5`.
- Example Test Cases:
  - For `n = 10`, the output should be `23` because the sum of all multiples of `3` or `5` below `10` is `3 + 5 + 6 + 9 = 23`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through all numbers from `1` to `n-1` and check if each number is a multiple of `3` or `5`.
- If a number is a multiple, add it to the sum.
- This approach comes to mind first because it directly addresses the problem statement without considering optimization.

```cpp
int sumMultiples(int n) {
    int sum = 0;
    for (int i = 1; i < n; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we potentially check every number up to `n-1`.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the sum and the loop variable.
> - **Why these complexities occur:** The time complexity is linear because of the loop that iterates up to `n-1`, and the space complexity is constant because we don't use any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the formula for the sum of an arithmetic series to calculate the sum of multiples of `3` and `5` separately and then subtract the sum of multiples of `15` (since multiples of `15` are counted twice).
- The formula for the sum of an arithmetic series is `n * (a1 + an) / 2`, where `n` is the number of terms, `a1` is the first term, and `an` is the last term.
- For multiples of `3`, the number of terms is `(n-1)/3`, the first term is `3`, and the last term is `3 * ((n-1)/3)`.
- Similarly, for multiples of `5`, the number of terms is `(n-1)/5`, the first term is `5`, and the last term is `5 * ((n-1)/5)`.
- For multiples of `15`, the number of terms is `(n-1)/15`, the first term is `15`, and the last term is `15 * ((n-1)/15)`.

```cpp
int sumMultiples(int n) {
    int sum3 = 3 * ((n-1)/3) * (((n-1)/3) + 1) / 2;
    int sum5 = 5 * ((n-1)/5) * (((n-1)/5) + 1) / 2;
    int sum15 = 15 * ((n-1)/15) * (((n-1)/15) + 1) / 2;
    return sum3 + sum5 - sum15;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we only perform a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the sums and the intermediate calculations.
> - **Optimality proof:** This is optimal because we directly calculate the sum without iterating through the numbers, making it a constant time operation.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of the formula for the sum of an arithmetic series to avoid iteration.
- The problem-solving pattern identified is looking for mathematical formulas or properties that can simplify the problem.
- The optimization technique learned is to avoid iteration when possible by using direct calculations.
- Similar problems to practice include finding the sum of multiples of other numbers or ranges.

**Mistakes to Avoid:**
- A common implementation error is forgetting to subtract the sum of multiples of `15` to avoid double-counting.
- An edge case to watch for is when `n` is less than `3` or `5`, but the given constraints ensure `n` is within the valid range.
- A performance pitfall is using the brute force approach for large inputs, which can be very slow.
- A testing consideration is to ensure the function works correctly for small inputs and edge cases.