## Super Pow

**Problem Link:** [https://leetcode.com/problems/super-pow/description](https://leetcode.com/problems/super-pow/description)

**Problem Statement:**
- Input format and constraints: The function `superPow` takes two parameters, `a` and `b`, where `a` is an integer and `b` is a vector of integers representing the exponent. The function should return the result of `a` to the power of `b` modulo `1337`.
- Expected output format: An integer representing the result of `a` to the power of `b` modulo `1337`.
- Key requirements and edge cases to consider: The input `a` can be any integer between `1` and `2,147,483,647`, and `b` is a vector of integers. The result should be calculated modulo `1337`.
- Example test cases with explanations:
  - `superPow(2, [3])` should return `8` because `2` to the power of `3` is `8`.
  - `superPow(2, [1,0])` should return `1024` because `2` to the power of `10` is `1024`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to calculate `a` to the power of `b` directly and then take the result modulo `1337`.
- Step-by-step breakdown of the solution:
  1. Convert the vector `b` into a single integer by iterating through the vector and multiplying each digit by `10` raised to the power of its position.
  2. Calculate `a` to the power of the resulting integer using a loop or the `pow` function.
  3. Take the result modulo `1337`.
- Why this approach comes to mind first: It directly implements the mathematical operation described in the problem.

```cpp
int superPow(int a, vector<int>& b) {
    long long result = 1;
    for (int i = 0; i < b.size(); i++) {
        result = result * 10 + b[i];
    }
    return pow(a, result) % 1337;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the size of the vector `b` and $m$ is the number of bits in the resulting exponent. The `pow` function has a time complexity that depends on the size of the exponent.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the result and temporary variables.
> - **Why these complexities occur:** The brute force approach involves iterating through the vector `b` to construct the exponent and then using a loop or the `pow` function to calculate the power, which leads to the time complexity. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the property of modular arithmetic that $(a \cdot b) \mod n = ((a \mod n) \cdot (b \mod n)) \mod n$ to avoid large intermediate results. Additionally, we can use the property of exponentiation that $a^{b+c} = a^b \cdot a^c$ to reduce the exponentiation into smaller parts.
- Detailed breakdown of the approach:
  1. Define a helper function `powMod` that calculates `a` to the power of `b` modulo `1337` efficiently using the property of modular arithmetic.
  2. Iterate through the vector `b` from right to left, for each digit, calculate `a` to the power of `10` raised to the power of the current position, and multiply the result with the current `a` to the power of the digit.
  3. Use the `powMod` function to calculate the power efficiently.
- Proof of optimality: This approach avoids large intermediate results by using modular arithmetic and reduces the exponentiation into smaller parts, making it more efficient than the brute force approach.

```cpp
int superPow(int a, vector<int>& b) {
    int mod = 1337;
    int result = 1;
    for (int i = b.size() - 1; i >= 0; i--) {
        result = powMod(result, 10, mod) * powMod(a, b[i], mod) % mod;
    }
    return result;
}

int powMod(int a, int b, int mod) {
    int result = 1;
    a = a % mod;
    while (b > 0) {
        if (b & 1) {
            result = (result * a) % mod;
        }
        b = b >> 1;
        a = (a * a) % mod;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(m))$ where $n$ is the size of the vector `b` and $m$ is the maximum value in the vector `b`. The `powMod` function has a time complexity of $O(log(m))$.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the result and temporary variables.
> - **Optimality proof:** This approach is optimal because it uses the properties of modular arithmetic and exponentiation to reduce the problem into smaller parts, avoiding large intermediate results and achieving the best possible time complexity.