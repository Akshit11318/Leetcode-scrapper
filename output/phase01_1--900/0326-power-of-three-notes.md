## Power of Three
**Problem Link:** https://leetcode.com/problems/power-of-three/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, return `true` if it is a power of three, and `false` otherwise.
- Expected output format: A boolean value indicating whether the input is a power of three.
- Key requirements and edge cases to consider: The input `n` can be any integer, including negative numbers and zero. We need to handle these edge cases correctly.
- Example test cases with explanations:
  - Input: `n = 27`, Output: `true`, Explanation: 27 is 3^3, which is a power of three.
  - Input: `n = 12`, Output: `false`, Explanation: 12 is not a power of three.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by checking if the number `n` is a power of three by repeatedly dividing it by three and checking if the result is an integer.
- Step-by-step breakdown of the solution:
  1. Start with the number `n`.
  2. If `n` is less than or equal to zero, return `false` because negative numbers and zero are not powers of three.
  3. Repeatedly divide `n` by three as long as `n` is divisible by three (i.e., `n % 3 == 0`).
  4. After the loop, if `n` is equal to one, then the original number was a power of three.
- Why this approach comes to mind first: It's a straightforward way to check if a number is a power of three by using the definition of a power of three.

```cpp
bool isPowerOfThree(int n) {
    if (n <= 0) {
        return false;
    }
    while (n % 3 == 0) {
        n /= 3;
    }
    return n == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ because in the worst case, we divide `n` by three until it reaches one, which takes logarithmic time.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the input and temporary results.
> - **Why these complexities occur:** The time complexity is logarithmic because we're reducing the size of the input by a constant factor (three) in each iteration. The space complexity is constant because we're not using any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of repeatedly dividing the number by three, we can use the property of logarithms to directly check if a number is a power of three.
- Detailed breakdown of the approach:
  1. Import the `cmath` library to use the `log` function.
  2. Calculate the base-3 logarithm of the absolute value of `n` using `log(abs(n)) / log(3)`.
  3. Check if the result is an integer by comparing it to its rounded value. If they are equal, then `n` is a power of three.
- Proof of optimality: This approach is optimal because it directly checks if a number is a power of three without requiring any loops or recursive function calls.
- Why further optimization is impossible: This approach has a constant time complexity, which is the best possible time complexity for this problem.

```cpp
#include <cmath>
bool isPowerOfThree(int n) {
    if (n <= 0) {
        return false;
    }
    double logResult = log(abs(n)) / log(3);
    return floor(logResult) == ceil(logResult);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the logarithm calculation and comparison operations take constant time.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the input and temporary results.
> - **Optimality proof:** The time complexity is constant because we're only performing a constant number of operations, regardless of the size of the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of logarithms to solve problems involving powers of numbers.
- Problem-solving patterns identified: The importance of considering different approaches to a problem, including using mathematical properties to simplify the solution.
- Optimization techniques learned: The use of logarithms to reduce the time complexity of a solution.
- Similar problems to practice: Other problems involving powers of numbers, such as checking if a number is a power of two or four.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as negative numbers or zero.
- Edge cases to watch for: The input `n` can be any integer, including negative numbers and zero.
- Performance pitfalls: Using a brute-force approach that has a high time complexity.
- Testing considerations: Make sure to test the solution with a variety of inputs, including edge cases and large numbers.