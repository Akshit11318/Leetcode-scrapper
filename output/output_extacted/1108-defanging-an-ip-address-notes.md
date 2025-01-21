## Defanging an IP Address
**Problem Link:** https://leetcode.com/problems/defanging-an-ip-address/description

**Problem Statement:**
- Input format and constraints: The input is a string representing an IP address.
- Expected output format: The output should be a string where every period (`.`) in the IP address is replaced with `[.]`.
- Key requirements and edge cases to consider: The input string will only contain valid IP addresses.
- Example test cases with explanations: 
    - Input: `address = "1.1.1.1"`
      Output: `"1[.]1[.]1[.]1"`
    - Input: `address = "255.100.100.0"`
      Output: `"255[.]100[.]100[.]0"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to iterate over each character in the input string. When a period is encountered, replace it with `[.]`.
- Step-by-step breakdown of the solution: 
  1. Initialize an empty string to store the result.
  2. Iterate over each character in the input string.
  3. If the character is a period, append `[.]` to the result string. Otherwise, append the character itself.
- Why this approach comes to mind first: It's a simple, intuitive method that directly addresses the requirement without needing complex data structures or algorithms.

```cpp
string defangIPaddr(string address) {
    string result = "";
    for (char c : address) {
        if (c == '.') {
            result += "[.]";
        } else {
            result += c;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we're doing a constant amount of work for each character.
> - **Space Complexity:** $O(n)$, because in the worst case, we're creating a new string that's the same length as the input string plus the additional characters for each period.
> - **Why these complexities occur:** The iteration over the input string causes the time complexity, and the creation of a new string with potentially more characters causes the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is essentially the same as the brute force approach, as the problem requires iterating over each character in the input string to replace periods with `[.]`. However, a slightly more efficient way to implement this is to use the `std::string::replace` method or string concatenation more efficiently.
- Detailed breakdown of the approach: 
  1. Use a loop to iterate over the input string, checking each character.
  2. If a period is found, replace it with `[.]`.
- Proof of optimality: This solution is optimal because it only requires a single pass through the input string, resulting in a linear time complexity. Further optimization is impossible without changing the fundamental requirement of examining each character.

```cpp
string defangIPaddr(string address) {
    string result = "";
    for (char c : address) {
        result += (c == '.') ? "[.]" : c;
    }
    return result;
}
```

Alternatively, for a more concise solution:

```cpp
string defangIPaddr(string address) {
    string result = address;
    replace(result.begin(), result.end(), '.', "[.]");
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we're still doing a constant amount of work for each character.
> - **Space Complexity:** $O(n)$, because we're either creating a new string or modifying the existing one, which could require additional space for the `[.]` replacements.
> - **Optimality proof:** This is the most efficient solution because it only requires a single pass through the input string, and any solution must at least examine each character once to perform the required replacements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, character replacement.
- Problem-solving patterns identified: Iterating over input data to perform transformations.
- Optimization techniques learned: While the optimal solution is straightforward, recognizing the necessity of examining each character helps in understanding why further optimization is not possible.
- Similar problems to practice: Other string manipulation problems, such as removing duplicates or finding substrings.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (e.g., an empty string), incorrectly replacing characters.
- Edge cases to watch for: Very long input strings, strings with many periods.
- Performance pitfalls: Using inefficient string concatenation methods in loops.
- Testing considerations: Ensure to test with a variety of input strings, including those with multiple periods and those without any.