## Vowels Game in a String

**Problem Link:** https://leetcode.com/problems/vowels-game-in-a-string/description

**Problem Statement:**
- Input: A string `s` containing lowercase English letters.
- Constraints: `1 <= s.length <= 1000`.
- Expected Output: The string `s` with the vowels ('a', 'e', 'i', 'o', 'u') removed.
- Key Requirements: The solution should efficiently remove all vowels from the given string.
- Edge Cases: Consider strings with no vowels, strings consisting entirely of vowels, and strings with a mix of vowels and consonants.

**Example Test Cases:**
- Input: `s = "aeiou"`; Output: `""`.
- Input: `s = "bcdfg"`; Output: `"bcdfg"`.
- Input: `s = "hello"`; Output: `"hll"`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through each character in the string and checking if it is a vowel.
- If a character is a vowel, it is skipped; otherwise, it is included in the resulting string.
- This approach comes to mind first because it directly addresses the problem statement by examining each character.

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
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are iterating through the string once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might end up with a new string of the same length as the original string if it contains no vowels.
> - **Why these complexities occur:** The time complexity is linear because we are scanning the string once, and the space complexity is also linear due to the potential creation of a new string of the same length.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a similar iteration approach but optimize the vowel check by using a `std::string` of vowels for lookup, which is more readable and maintainable than a series of `if` conditions.
- The approach involves iterating through the string `s`, checking each character against the set of vowels, and appending it to the result if it's not a vowel.
- This is the optimal solution because it achieves the goal with minimal overhead, maintaining a linear time complexity.

```cpp
string removeVowels(string s) {
    string vowels = "aeiou";
    string result = "";
    for (char c : s) {
        if (vowels.find(c) == std::string::npos) {
            result += c;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are still iterating through the string once, and the `find` operation within the loop does not change the overall time complexity.
> - **Space Complexity:** $O(n)$, as we are potentially creating a new string of the same length as the input string.
> - **Optimality proof:** This is optimal because we must examine each character at least once to determine if it's a vowel or not, and our approach does this with a constant factor overhead per character.

---

### Final Notes

**Learning Points:**
- The importance of iterating through strings to examine each character.
- How to optimize simple checks (like checking for vowels) using `std::string` methods.
- Understanding that sometimes, the most straightforward approach is also the most efficient, especially for linear scans of data.

**Mistakes to Avoid:**
- Overcomplicating the solution by using more complex data structures or algorithms than necessary.
- Not considering the potential size of the input and how it affects space complexity.
- Failing to validate inputs or handle edge cases properly.