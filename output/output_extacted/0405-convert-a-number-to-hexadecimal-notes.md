## Convert a Number to Hexadecimal

**Problem Link:** https://leetcode.com/problems/convert-a-number-to-hexadecimal/description

**Problem Statement:**
- Input: An integer `num`.
- Output: The hexadecimal representation of `num`.
- Constraints: `-2^31 <= num <= 2^31 - 1`.
- Key requirements: Handle negative numbers, zero, and the maximum integer value.
- Example test cases:
  - `num = 26`, output: `"1a"`.
  - `num = -1`, output: `"ffffffff"`.

---

### Brute Force Approach

**Explanation:**
- Convert the integer to a string and then replace each digit with its hexadecimal equivalent.
- Handle negative numbers by converting the absolute value and then adding a minus sign if necessary.
- Use a dictionary or a switch statement to map decimal digits to hexadecimal.

```cpp
string toHex(int num) {
    if (num == 0) return "0";
    string hex = "";
    while (num != 0) {
        int remainder = num % 16;
        if (remainder < 10) {
            hex = to_string(remainder) + hex;
        } else {
            hex = char('a' + remainder - 10) + hex;
        }
        num /= 16;
    }
    return hex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the absolute value of `num`, since we divide `num` by 16 in each iteration.
> - **Space Complexity:** $O(log(n))$, since we store the hexadecimal representation as a string.
> - **Why these complexities occur:** The number of iterations depends on the number of hexadecimal digits in `num`, which is proportional to the logarithm of `num`.

---

### Optimal Approach (Required)

**Explanation:**
- Use bitwise operations to extract the last 4 bits of `num` in each iteration.
- Use a lookup table to map the extracted bits to the corresponding hexadecimal digit.
- Handle negative numbers by converting them to positive and then applying the same logic.

```cpp
string toHex(int num) {
    if (num == 0) return "0";
    string hex = "";
    char map[] = "0123456789abcdef";
    while (num != 0 && hex.length() < 8) {
        hex = map[(num & 15)] + hex;
        num >>= 4;
    }
    return hex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the absolute value of `num`.
> - **Space Complexity:** $O(log(n))$, since we store the hexadecimal representation as a string.
> - **Optimality proof:** This approach is optimal because it uses bitwise operations to extract the hexadecimal digits, which is more efficient than using division and modulus operations.

---

### Final Notes

**Learning Points:**
- Bitwise operations can be used to extract and manipulate bits in an integer.
- Lookup tables can be used to map bits to their corresponding hexadecimal digits.
- Handling negative numbers requires converting them to positive and then applying the same logic.

**Mistakes to Avoid:**
- Not handling negative numbers correctly.
- Not using bitwise operations to extract the hexadecimal digits.
- Not using a lookup table to map the extracted bits to their corresponding hexadecimal digits.