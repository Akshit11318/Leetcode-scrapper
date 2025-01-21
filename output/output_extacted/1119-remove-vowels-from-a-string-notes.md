## Remove Vowels from a String
**Problem Link:** https://leetcode.com/problems/remove-vowels-from-a-string/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing only lowercase English letters. The length of `s` is not specified, but it is guaranteed to be a valid string.
- Expected output format: The output should be a string with all vowels removed from the input string `s`.
- Key requirements and edge cases to consider: 
  - The input string `s` may be empty.
  - The input string `s` may contain only vowels.
  - The input string `s` may contain a mix of vowels and consonants.
- Example test cases with explanations:
  - Input: `"leetcodeisacommunityresource"` 
    - Expected output: `"ltcdscmmntyrsrcc"`
  - Input: `"aeiou"`
    - Expected output: `""`
  - Input: `"bcdfg"`
    - Expected output: `"bcdfg"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each character in the string, check if it is a vowel, and if not, append it to a new string.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string to store the result.
  2. Iterate over each character in the input string.
  3. Check if the current character is a vowel.
  4. If the character is not a vowel, append it to the result string.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it directly checks each character and includes it in the output if it is not a vowel.

```cpp
string removeVowels(string s) {
    string vowels = "aeiou";
    string result = "";
    
    for (char c : s) {
        if (vowels.find(c) == string::npos) {
            result += c;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the length of the string and $m$ is the number of vowels (5 in this case), because we are iterating over each character in the string and for each character, we are searching for it in the string of vowels.
> - **Space Complexity:** $O(n)$, because we are storing the result in a new string, which in the worst case could be as large as the input string.
> - **Why these complexities occur:** The time complexity is due to the nested operations of iterating over the string and searching for vowels. The space complexity is due to the storage of the result string.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of using the `find` method to search for vowels in a string, we can directly check if a character is a vowel by comparing it with the vowel characters.
- Detailed breakdown of the approach:
  1. Initialize an empty string to store the result.
  2. Iterate over each character in the input string.
  3. Check if the current character is a vowel by directly comparing it with the vowel characters.
  4. If the character is not a vowel, append it to the result string.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input string, resulting in a linear time complexity.
- Why further optimization is impossible: We must examine each character at least once to determine if it is a vowel or not, so any algorithm must have at least a linear time complexity.

```cpp
string removeVowels(string s) {
    string result = "";
    
    for (char c : s) {
        if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
            result += c;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we are making a constant number of comparisons for each character in the string.
> - **Space Complexity:** $O(n)$, because we are storing the result in a new string, which in the worst case could be as large as the input string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
  - Iteration over a string.
  - Conditional checks for vowel characters.
- Problem-solving patterns identified: 
  - The importance of directly checking conditions instead of using methods that may have higher complexities.
- Optimization techniques learned: 
  - Reducing the number of operations by directly comparing characters instead of searching in a string.

**Mistakes to Avoid:**
- Common implementation errors: 
  - Not checking for edge cases, such as an empty input string.
  - Using inefficient methods, such as the `find` method in a string, for conditional checks.
- Edge cases to watch for: 
  - Empty input string.
  - Input string containing only vowels.
  - Input string containing a mix of vowels and consonants.
- Performance pitfalls: 
  - Using methods with higher time complexities than necessary.
- Testing considerations: 
  - Test the function with various input strings, including edge cases.