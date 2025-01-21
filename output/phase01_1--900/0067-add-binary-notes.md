## Add Binary
**Problem Link:** [https://leetcode.com/problems/add-binary/description](https://leetcode.com/problems/add-binary/description)

**Problem Statement:**
- Input format: Two binary strings `a` and `b`.
- Constraints: `1 <= a.length, b.length <= 104`, `a` and `b` consist only of `0`s and `1`s.
- Expected output format: A binary string representing the sum of `a` and `b`.
- Key requirements and edge cases to consider:
  - Handling carry from one bit position to the next.
  - Ensuring the output string is a valid binary representation.
- Example test cases with explanations:
  - `a = "11", b = "1"`: Output should be `"100"`.
  - `a = "1010", b = "1011"`: Output should be `"10101"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert binary strings to integers, add them, and then convert the result back to a binary string.
- Step-by-step breakdown of the solution:
  1. Convert each binary string to an integer.
  2. Add the two integers together.
  3. Convert the sum back to a binary string.
- Why this approach comes to mind first: It directly leverages the built-in integer addition capabilities of the programming language and the straightforward conversion between binary strings and integers.

```cpp
string addBinary(string a, string b) {
    // Convert binary strings to integers
    int sum = stoi(a, 0, 2) + stoi(b, 0, 2);
    
    // Convert the sum back to a binary string
    if (sum == 0) return "0";
    string result;
    while (sum > 0) {
        result = to_string(sum % 2) + result;
        sum /= 2;
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(log(a), log(b)))$, where $log(a)$ and $log(b)$ are the number of bits in $a$ and $b$, respectively. This is because we're converting each binary string to an integer and then back to a binary string.
> - **Space Complexity:** $O(max(log(a), log(b)))$, as we need to store the result string.
> - **Why these complexities occur:** The conversion between binary strings and integers, as well as the iteration to build the result string, are linear in the length of the input strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can simulate the process of adding two binary numbers bit by bit from right to left, just like we do in decimal addition, but without converting the entire numbers to integers first.
- Detailed breakdown of the approach:
  1. Initialize two pointers at the end of both strings.
  2. Initialize a carry variable to 0.
  3. Iterate through the strings from right to left. At each position, calculate the sum of the current bits and the carry.
  4. Update the carry for the next iteration based on the sum.
  5. Append the least significant bit of the sum to the result string.
- Proof of optimality: This approach has a linear time complexity with respect to the length of the input strings, which is optimal since we must at least read the input once.

```cpp
string addBinary(string a, string b) {
    string result;
    int carry = 0, i = a.size() - 1, j = b.size() - 1;
    
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        
        result = to_string(sum % 2) + result;
        carry = sum / 2;
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(a.length, b.length))$, where $a.length$ and $b.length$ are the lengths of the input strings. This is because we're iterating through the strings once.
> - **Space Complexity:** $O(max(a.length, b.length))$, as we need to store the result string.
> - **Optimality proof:** This approach directly constructs the result string without unnecessary conversions, making it optimal in terms of time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, string iteration, and carry propagation in binary addition.
- Problem-solving patterns identified: Simulating manual addition processes in code, handling carry in binary arithmetic.
- Optimization techniques learned: Avoiding unnecessary conversions between data types, using iterative approaches instead of recursive ones when possible.
- Similar problems to practice: Adding numbers represented as linked lists, multiplying binary numbers.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the carry, not checking for the case where one string is longer than the other.
- Edge cases to watch for: When one or both input strings are empty, when the sum of two bits and the carry results in a carry for the next iteration.
- Performance pitfalls: Using inefficient data structures or algorithms that scale poorly with input size.
- Testing considerations: Ensure to test with a variety of input lengths and combinations of bits to cover all possible scenarios.