## Decrypt String from Alphabet to Integer Mapping
**Problem Link:** https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description

**Problem Statement:**
- Input: A string `s` containing alphanumeric characters and `#`.
- Constraints: The input string will only contain lowercase letters, digits, and `#`.
- Expected output: The decrypted string where each sequence of three digits corresponds to the ASCII value of a character.
- Key requirements and edge cases: The input string may contain sequences of three digits that do not correspond to valid ASCII values for lowercase letters. The `#` symbol indicates the start of a three-digit sequence.

**Example Test Cases:**
- Input: "10#11#12"
- Output: "jk"
- Explanation: The sequences "10#", "11#", and "12#" correspond to the characters 'j', 'k', and 'l', respectively.

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves iterating through the input string and checking for each character if it's a digit or the `#` symbol.
- When a `#` symbol is encountered, the previous three characters (which are digits) are used to form a number that corresponds to the ASCII value of a character.

```cpp
string freqAlphabets(string s) {
    string res = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '#') {
            int val = (s[i-3] - '0') * 100 + (s[i-2] - '0') * 10 + (s[i-1] - '0');
            res += (char)(96 + val);
            i += 2; // Skip the next two characters
        } else {
            res += (char)(s[i] - '0' + 96);
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, since we are scanning the string once.
> - **Space Complexity:** $O(n)$, as in the worst-case scenario, we might end up with a string of the same length as the input.
> - **Why these complexities occur:** The time complexity is linear because we are iterating through the string once. The space complexity is also linear because we are building a new string that could potentially be as large as the input string.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is similar to the brute force approach but involves iterating through the string from right to left to avoid skipping characters when a `#` symbol is encountered.
- This approach ensures that we correctly handle sequences of three digits and single digits.

```cpp
string freqAlphabets(string s) {
    string res = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        if (s[i] == '#') {
            int val = (s[i-3] - '0') * 100 + (s[i-2] - '0') * 10 + (s[i-1] - '0');
            res = (char)(96 + val) + res;
            i -= 3; // Move back three steps
        } else {
            res = (char)(s[i] - '0' + 96) + res;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, as we are still scanning the string once, just from right to left.
> - **Space Complexity:** $O(n)$, as we are building a new string that could potentially be as large as the input string.
> - **Optimality proof:** This approach is optimal because it processes each character in the input string exactly once, resulting in a linear time complexity. The space complexity is also optimal since we must store the output string.

---

### Final Notes

**Learning Points:**
- **Character encoding and decoding**: Understanding how characters are represented as ASCII values and how to convert between them.
- **String manipulation**: Techniques for iterating through strings, handling different cases (like `#` symbols), and building new strings.
- **Optimization techniques**: Approaches for improving the efficiency of algorithms, such as iterating from right to left to avoid skipping characters.

**Mistakes to Avoid:**
- Not handling edge cases correctly, such as when the input string contains invalid sequences of digits.
- Not considering the direction of iteration and how it affects the handling of `#` symbols and digit sequences.
- Failing to validate the input and output strings for correctness and handling any potential errors.