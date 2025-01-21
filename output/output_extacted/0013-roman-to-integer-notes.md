## Roman to Integer
**Problem Link:** https://leetcode.com/problems/roman-to-integer/description

**Problem Statement:**
- Input: A string `s` containing a valid Roman numeral.
- Constraints: `1 <= s.length <= 15`, `s` contains only the characters `I`, `V`, `X`, `L`, `C`, `D`, and `M`.
- Expected Output: An integer representing the integer value of the Roman numeral.
- Key Requirements: Convert the Roman numeral to an integer, considering the subtractive notation in Roman numerals (e.g., `IV` equals 4, not 6).
- Example Test Cases:
  - Input: `s = "III"`
    - Output: `3`
    - Explanation: `III` represents 3 in Roman numerals.
  - Input: `s = "IV"`
    - Output: `4`
    - Explanation: `IV` represents 4 in Roman numerals due to the subtractive notation.
  - Input: `s = "IX"`
    - Output: `9`
    - Explanation: `IX` represents 9 in Roman numerals due to the subtractive notation.
  - Input: `s = "LVIII"`
    - Output: `58`
    - Explanation: `L` equals 50, `V` equals 5, `III` equals 3, adding these gives 58.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves directly translating each Roman numeral character into its integer equivalent and summing them up. However, this approach doesn't account for the subtractive notation in Roman numerals (like `IV` or `IX`).
- To handle the subtractive notation, we could check each character and the one following it to see if the current character's value is less than the next one. If so, we subtract its value; otherwise, we add it.
- This approach comes to mind first because it directly addresses the problem's requirements without considering the efficiency of the solution.

```cpp
int romanToInt(string s) {
    // Define a map to store the values of Roman numerals
    map<char, int> romanValues = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int result = 0;
    for (int i = 0; i < s.length(); i++) {
        // Check if the current character's value is less than the next one
        if (i + 1 < s.length() && romanValues[s[i]] < romanValues[s[i + 1]]) {
            // Subtract the current character's value
            result -= romanValues[s[i]];
        } else {
            // Add the current character's value
            result += romanValues[s[i]];
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we are iterating over the string once.
> - **Space Complexity:** $O(1)$, because the space used does not grow with the size of the input string, given that the map of Roman numeral values is constant.
> - **Why these complexities occur:** The time complexity is linear due to the single pass through the input string, and the space complexity is constant because we use a fixed-size map to store the values of the Roman numerals.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is recognizing that we only need to consider the subtractive notation for certain pairs of Roman numerals (`IV`, `IX`, `XL`, `XC`, `CD`, `CM`).
- The detailed breakdown involves initializing a result variable to 0 and then iterating over the input string. For each character, we check if it's part of a subtractive pair with the next character. If it is, we subtract its value; otherwise, we add it.
- The proof of optimality lies in the fact that we make a single pass through the input string and use constant additional space, which is the most efficient way to solve this problem given the constraints.
- Further optimization is impossible because we must at least read the input string once to determine its integer value.

```cpp
int romanToInt(string s) {
    map<char, int> romanValues = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int result = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i + 1 < s.length() && romanValues[s[i]] < romanValues[s[i + 1]]) {
            result -= romanValues[s[i]];
        } else {
            result += romanValues[s[i]];
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we make a single pass through the input.
> - **Space Complexity:** $O(1)$, because the space used does not grow with the size of the input string.
> - **Optimality proof:** This solution is optimal because it achieves the minimum possible time complexity ($O(n)$) and space complexity ($O(1)$) for the problem.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated include the use of a map for constant-time lookups and a single pass through the input string for linear time complexity.
- Problem-solving patterns identified include handling special cases (like subtractive notation) and optimizing the solution by minimizing the number of operations.
- Optimization techniques learned include reducing the number of iterations and using constant additional space.
- Similar problems to practice include other string manipulation and conversion problems, such as converting integers to Roman numerals or parsing dates.

**Mistakes to Avoid:**
- Common implementation errors include forgetting to handle edge cases (like an empty input string) and not validating the input.
- Edge cases to watch for include strings containing invalid Roman numerals or strings that are too long.
- Performance pitfalls include using unnecessary data structures or algorithms that have higher time or space complexities than needed.
- Testing considerations include ensuring that the solution works correctly for a variety of inputs, including edge cases and large inputs.