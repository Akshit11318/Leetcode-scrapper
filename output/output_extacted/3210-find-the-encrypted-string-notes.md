## Find the Encrypted String
**Problem Link:** https://leetcode.com/problems/find-the-encrypted-string/description

**Problem Statement:**
- Input format: The function takes a string `s` as input.
- Constraints: The string `s` consists of lowercase letters.
- Expected output format: The function returns the encrypted string.
- Key requirements and edge cases to consider: The string `s` can be empty, and the function should handle this case correctly.
- Example test cases with explanations:
  - Input: `s = "abc"` Output: `"aabbcc"`
  - Input: `s = "abcdef"` Output: `"aabbccddeeff"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem asks to encrypt the string by repeating each character twice.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string `encrypted` to store the encrypted string.
  2. Iterate through each character `c` in the input string `s`.
  3. For each character, append the character twice to the `encrypted` string.
- Why this approach comes to mind first: This approach is straightforward and directly implements the problem statement.

```cpp
string encryptString(string s) {
    string encrypted = "";
    for (char c : s) {
        encrypted += c;
        encrypted += c;
    }
    return encrypted;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we iterate through each character in the string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we create a new string `encrypted` that has twice the length of the input string.
> - **Why these complexities occur:** The time complexity occurs because we iterate through each character in the string once, and the space complexity occurs because we create a new string that has twice the length of the input string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `StringBuilder` or a `stringstream` to efficiently build the encrypted string.
- Detailed breakdown of the approach:
  1. Initialize a `StringBuilder` or a `stringstream` to store the encrypted string.
  2. Iterate through each character `c` in the input string `s`.
  3. For each character, append the character twice to the `StringBuilder` or `stringstream`.
  4. Return the encrypted string as a string.
- Proof of optimality: This approach is optimal because it has the same time complexity as the brute force approach, but it uses less memory because it avoids creating intermediate strings.
- Why further optimization is impossible: This approach is already optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve the problem.

```cpp
string encryptString(string s) {
    stringstream ss;
    for (char c : s) {
        ss << c << c;
    }
    return ss.str();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we iterate through each character in the string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we create a new string that has twice the length of the input string.
> - **Optimality proof:** This approach is optimal because it has the same time complexity as the brute force approach, but it uses less memory because it avoids creating intermediate strings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, iteration, and memory efficiency.
- Problem-solving patterns identified: Using `StringBuilder` or `stringstream` to efficiently build strings.
- Optimization techniques learned: Avoiding intermediate strings and using efficient data structures.
- Similar problems to practice: Other string manipulation problems, such as reversing strings or finding substrings.

**Mistakes to Avoid:**
- Common implementation errors: Creating intermediate strings or using inefficient data structures.
- Edge cases to watch for: Handling empty strings or strings with special characters.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Testing with different input sizes and edge cases to ensure the solution is correct and efficient.