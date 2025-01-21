## Convert to Base 2
**Problem Link:** https://leetcode.com/problems/convert-to-base-2/description

**Problem Statement:**
- Input format and constraints: The function takes an integer `n` as input and should return its binary representation as a string. `n` is a non-negative integer.
- Expected output format: The binary representation of `n` as a string.
- Key requirements and edge cases to consider: The function should handle `n = 0` correctly and return `"0"`. For all other non-negative integers, it should return the binary representation as a string without any prefix.
- Example test cases with explanations: 
    - Input: `n = 1`, Output: `"1"`. 
    - Input: `n = 2`, Output: `"10"`.
    - Input: `n = 3`, Output: `"11"`.
    - Input: `n = 4`, Output: `"100"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to convert a decimal number to binary is by continuously dividing the number by 2 and appending the remainder to the binary representation.
- Step-by-step breakdown of the solution:
    1. Start with an empty string `binary` to store the binary representation.
    2. If `n` is 0, return `"0"`.
    3. While `n` is greater than 0, perform the following steps:
        - Append the remainder of `n` divided by 2 to the beginning of `binary`.
        - Update `n` to be the integer division of `n` by 2.
    4. Return `binary`.

```cpp
string toBinary(int n) {
    if (n == 0) return "0";
    string binary = "";
    while (n > 0) {
        binary = to_string(n % 2) + binary;
        n /= 2;
    }
    return binary;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ because we divide `n` by 2 in each iteration until `n` becomes 0. The number of iterations is proportional to the number of bits in the binary representation of `n`, which is $log_2(n)$.
> - **Space Complexity:** $O(log(n))$ because in the worst case, the length of the binary string is $log_2(n)$.
> - **Why these complexities occur:** These complexities occur because the number of operations (divisions and appends) and the amount of space used (for storing the binary string) are directly related to the number of bits in the binary representation of `n`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach is to use bitwise operations to extract the least significant bit of `n` in each iteration and prepend it to the binary string. This approach avoids the overhead of division and modulo operations.
- Detailed breakdown of the approach:
    1. If `n` is 0, return `"0"`.
    2. Initialize an empty string `binary` to store the binary representation.
    3. While `n` is greater than 0, perform the following steps:
        - Prepend the least significant bit of `n` (extracted using `n & 1`) to `binary`.
        - Right shift `n` by 1 bit to remove the least significant bit.
    4. Return `binary`.

```cpp
string toBinary(int n) {
    if (n == 0) return "0";
    string binary = "";
    while (n > 0) {
        binary = to_string(n & 1) + binary;
        n >>= 1;
    }
    return binary;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ because we perform a constant amount of work for each bit in the binary representation of `n`.
> - **Space Complexity:** $O(log(n))$ because the length of the binary string is proportional to the number of bits in `n`.
> - **Optimality proof:** This is the optimal solution because we minimize the number of operations required to convert `n` to binary by using bitwise operations, which are typically faster than division and modulo operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, binary representation, and efficient conversion from decimal to binary.
- Problem-solving patterns identified: Using bitwise operations to solve problems involving binary numbers.
- Optimization techniques learned: Avoiding division and modulo operations in favor of bitwise operations when working with binary numbers.
- Similar problems to practice: Converting binary to decimal, finding the binary representation of a negative number, etc.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where `n` is 0, incorrectly appending or prepending bits to the binary string.
- Edge cases to watch for: `n = 0`, `n = 1`, and large values of `n` that may cause overflow.
- Performance pitfalls: Using division and modulo operations instead of bitwise operations.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases and large numbers.