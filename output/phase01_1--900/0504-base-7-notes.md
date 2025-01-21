## Base 7
**Problem Link:** https://leetcode.com/problems/base-7/description

**Problem Statement:**
- Input format: The input is a signed integer `num`.
- Constraints: `-7^31 <= num <= 7^31 - 1`.
- Expected output format: A string representing the input number in base 7.
- Key requirements: Handle negative numbers, zero, and the base conversion process.
- Example test cases:
  - Input: `100`
    - Output: `"202"`
  - Input: `-7`
    - Output: `"-10"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the number to base 7 by continuously dividing by 7 and appending the remainder to the result string.
- Step-by-step breakdown:
  1. Check if the number is negative. If so, store the sign and make the number positive for further calculations.
  2. Initialize an empty string to store the base 7 representation.
  3. If the number is 0, return "0" as it's the base case.
  4. While the number is greater than 0, divide it by 7 and append the remainder to the front of the string.
  5. If the original number was negative, prepend a "-" to the result string.
- Why this approach comes to mind first: It's a straightforward method that directly applies the concept of base conversion.

```cpp
string convertToBase7(int num) {
    if (num == 0) return "0";
    string result = "";
    bool isNegative = false;
    
    if (num < 0) {
        isNegative = true;
        num = -num; // Make the number positive for calculation
    }
    
    while (num > 0) {
        int remainder = num % 7;
        result = to_string(remainder) + result; // Append remainder to the front
        num /= 7;
    }
    
    if (isNegative) {
        result = "-" + result; // Prepend the negative sign
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log_{7}N)$, where $N$ is the absolute value of the input number. This is because in the worst case, we divide the number by 7 until it becomes 0.
> - **Space Complexity:** $O(\log_{7}N)$, as we store the result string which can be at most $\log_{7}N$ digits long.
> - **Why these complexities occur:** The time complexity is due to the division operation in the while loop, and the space complexity is due to storing the result string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The brute force approach is already quite efficient and straightforward for this problem. However, we can slightly optimize the code by reducing the number of string concatenations, which can be expensive operations in some programming languages.
- Detailed breakdown:
  1. Use a `stringstream` to build the result string instead of concatenating strings in each iteration.
  2. The logic remains the same as the brute force approach.
- Proof of optimality: This approach is optimal because it still has the same time complexity as the brute force approach but reduces the overhead of string operations.

```cpp
string convertToBase7(int num) {
    if (num == 0) return "0";
    stringstream ss;
    bool isNegative = false;
    
    if (num < 0) {
        isNegative = true;
        num = -num; // Make the number positive for calculation
    }
    
    while (num > 0) {
        int remainder = num % 7;
        ss << remainder; // Append remainder to the stream
        num /= 7;
    }
    
    string result = ss.str();
    reverse(result.begin(), result.end()); // Reverse the string
    
    if (isNegative) {
        result = "-" + result; // Prepend the negative sign
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log_{7}N)$, where $N$ is the absolute value of the input number.
> - **Space Complexity:** $O(\log_{7}N)$, for storing the result string.
> - **Optimality proof:** This is the best possible complexity for this problem since we must perform at least $\log_{7}N$ operations to convert the number to base 7.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Base conversion, handling negative numbers, and efficient string manipulation.
- Problem-solving patterns: Direct application of mathematical concepts to solve the problem efficiently.
- Optimization techniques: Using `stringstream` for efficient string building.

**Mistakes to Avoid:**
- Not handling the case where the input number is 0.
- Not correctly handling negative numbers.
- Inefficient string concatenation in loops.
- Not considering the constraints of the problem (e.g., the range of the input number).