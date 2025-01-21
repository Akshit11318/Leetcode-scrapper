## Factorial Generator
**Problem Link:** https://leetcode.com/problems/factorial-generator/description

**Problem Statement:**
- Input format: The problem asks to write a function that generates the factorial of a given number `n`.
- Constraints: The input `n` is a non-negative integer.
- Expected output format: The function should return the factorial of `n`.
- Key requirements and edge cases to consider:
  - The input `n` is a non-negative integer.
  - The function should handle large inputs and avoid overflow.
- Example test cases with explanations:
  - For `n = 0`, the function should return `1` because the factorial of 0 is 1.
  - For `n = 1`, the function should return `1` because the factorial of 1 is 1.
  - For `n = 2`, the function should return `2` because the factorial of 2 is 2.
  - For `n = 5`, the function should return `120` because the factorial of 5 is 120.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves calculating the factorial of `n` by multiplying all integers from 1 to `n`.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `result` to 1.
  2. Iterate from 1 to `n` (inclusive) and multiply `result` by the current integer.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a natural first thought.

```cpp
class FactorialGenerator {
public:
    int factorial(int n) {
        // Initialize result to 1
        long long result = 1;
        
        // Iterate from 1 to n and multiply result by the current integer
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        
        // Return the result
        return (int)result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we iterate from 1 to `n` once.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the result.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each integer from 1 to `n`. The space complexity is constant because we only use a fixed amount of space to store the result, regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use memoization to store the factorial of previously calculated numbers to avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Create a map to store the factorial of previously calculated numbers.
  2. Check if the factorial of `n` is already in the map. If it is, return the stored value.
  3. If not, calculate the factorial of `n` using the brute force approach and store it in the map.
- Proof of optimality: This approach is optimal because it avoids redundant calculations by storing the factorial of previously calculated numbers.

```cpp
class FactorialGenerator {
private:
    unordered_map<int, long long> memo;
public:
    int factorial(int n) {
        // Check if the factorial of n is already in the memo
        if (memo.find(n) != memo.end()) {
            return (int)memo[n];
        }
        
        // If n is 0 or 1, return 1
        if (n == 0 || n == 1) {
            memo[n] = 1;
            return 1;
        }
        
        // Calculate the factorial of n using the brute force approach
        long long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        
        // Store the result in the memo
        memo[n] = result;
        
        // Return the result
        return (int)result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we iterate from 1 to `n` once in the worst case.
> - **Space Complexity:** $O(n)$ because we store the factorial of previously calculated numbers in the memo.
> - **Optimality proof:** This approach is optimal because it avoids redundant calculations by storing the factorial of previously calculated numbers, reducing the time complexity to linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Memoization, iteration, and calculation of factorials.
- Problem-solving patterns identified: Using memoization to avoid redundant calculations.
- Optimization techniques learned: Storing previously calculated values to avoid redundant calculations.
- Similar problems to practice: Calculating the Fibonacci sequence, calculating the greatest common divisor (GCD) of two numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for overflow when calculating the factorial, not handling edge cases correctly.
- Edge cases to watch for: Handling `n = 0` and `n = 1` correctly, handling large inputs and avoiding overflow.
- Performance pitfalls: Not using memoization to avoid redundant calculations, not optimizing the calculation of factorials.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs, to ensure correctness and performance.