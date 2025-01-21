## UTF-8 Validation

**Problem Link:** https://leetcode.com/problems/utf-8-validation/description

**Problem Statement:**
- Input format and constraints: Given an integer array `data` representing the bytes of a UTF-8 encoded string, return `true` if it is a valid UTF-8 encoding, and `false` otherwise.
- Expected output format: A boolean indicating whether the input is a valid UTF-8 encoding.
- Key requirements and edge cases to consider: 
  - Understanding UTF-8 encoding rules, including the number of bytes required for each character (1-4 bytes).
  - Handling cases where the input array does not represent a valid UTF-8 encoded string.
- Example test cases with explanations: 
  - `[197,130,1]` represents a valid UTF-8 encoding.
  - `[235,140,4]` does not represent a valid UTF-8 encoding.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To validate a UTF-8 encoding, we need to check each sequence of bytes to ensure it follows the UTF-8 encoding rules.
- Step-by-step breakdown of the solution:
  1. Iterate over the input array `data`.
  2. For each byte, determine if it is a single-byte character (0xxxxxxx), a two-byte sequence start (110xxxxx), a three-byte sequence start (1110xxxx), or a four-byte sequence start (11110xxx).
  3. For multi-byte sequences, verify that the subsequent bytes are valid continuation bytes (10xxxxxx).
- Why this approach comes to mind first: It directly follows the definition of UTF-8 encoding rules.

```cpp
bool validUtf8(vector<int>& data) {
    int bytesLeft = 0;
    for (int i = 0; i < data.size(); ++i) {
        // Convert integer to binary string for easier manipulation
        string byteStr = bitset<8>(data[i]).to_string();
        
        if (bytesLeft == 0) {
            // Check for single-byte character
            if (byteStr[0] == '0') {
                continue;
            }
            // Check for multi-byte sequence start
            else if (byteStr[0] == '1' && byteStr[1] == '1' && byteStr[2] == '0') {
                bytesLeft = 1;
            }
            else if (byteStr[0] == '1' && byteStr[1] == '1' && byteStr[2] == '1' && byteStr[3] == '0') {
                bytesLeft = 2;
            }
            else if (byteStr[0] == '1' && byteStr[1] == '1' && byteStr[2] == '1' && byteStr[3] == '1' && byteStr[4] == '0') {
                bytesLeft = 3;
            }
            else {
                return false; // Invalid start byte
            }
        } else {
            // Check for valid continuation byte
            if (byteStr[0] != '1' || byteStr[1] != '0') {
                return false; // Invalid continuation byte
            }
            bytesLeft--;
        }
    }
    return bytesLeft == 0; // All bytes were part of a valid sequence
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bytes in the input array, since we potentially check every byte once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, as we only use a constant amount of space to store the current state (`bytesLeft`).
> - **Why these complexities occur:** The algorithm iterates through the input array once, and the space usage does not grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of converting integers to binary strings, we can directly manipulate the bits using bitwise operations, which is more efficient.
- Detailed breakdown of the approach:
  1. Use bitwise operations to check the first few bits of each byte to determine if it's a single-byte character or the start of a multi-byte sequence.
  2. For multi-byte sequences, use bitwise operations to verify that subsequent bytes are valid continuation bytes.
- Proof of optimality: This approach still checks every byte once but does so more efficiently by avoiding string conversions.

```cpp
bool validUtf8(vector<int>& data) {
    int bytesLeft = 0;
    for (int byte : data) {
        if (bytesLeft == 0) {
            // Check for single-byte character
            if ((byte >> 7) == 0) {
                continue;
            }
            // Check for multi-byte sequence start
            else if ((byte >> 5) == 0b110) {
                bytesLeft = 1;
            }
            else if ((byte >> 4) == 0b1110) {
                bytesLeft = 2;
            }
            else if ((byte >> 3) == 0b11110) {
                bytesLeft = 3;
            }
            else {
                return false; // Invalid start byte
            }
        } else {
            // Check for valid continuation byte
            if ((byte >> 6) != 0b10) {
                return false; // Invalid continuation byte
            }
            bytesLeft--;
        }
    }
    return bytesLeft == 0; // All bytes were part of a valid sequence
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bytes in the input array, since we potentially check every byte once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, as we only use a constant amount of space to store the current state (`bytesLeft`).
> - **Optimality proof:** This is the most efficient algorithm because it checks every byte exactly once and uses bitwise operations, which are faster than converting integers to strings and manipulating them as such.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation and understanding of UTF-8 encoding rules.
- Problem-solving patterns identified: Direct application of encoding rules and efficient use of bitwise operations.
- Optimization techniques learned: Avoiding unnecessary string conversions and using bitwise operations for efficiency.
- Similar problems to practice: Other encoding and decoding problems, such as URL encoding or base64 encoding.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly applying UTF-8 encoding rules or misunderstanding how bitwise operations work.
- Edge cases to watch for: Sequences that are too long (more than 4 bytes), sequences that are incomplete at the end of the input, and invalid start or continuation bytes.
- Performance pitfalls: Using inefficient methods for checking byte values, such as converting them to strings.
- Testing considerations: Ensure to test with a variety of inputs, including valid and invalid UTF-8 encodings, and edge cases like incomplete sequences or sequences with more than 4 bytes.