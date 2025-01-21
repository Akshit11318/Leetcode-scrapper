## CamelCase Matching

**Problem Link:** https://leetcode.com/problems/camelcase-matching/description

**Problem Statement:**
- Input format and constraints: The problem takes in a string `pattern` and an array of strings `strings`. The goal is to determine which strings in the array match the given `pattern`.
- Expected output format: A vector of strings that match the `pattern`.
- Key requirements and edge cases to consider: A string matches the pattern if it is in CamelCase and the lowercase version of the string matches the lowercase version of the pattern.
- Example test cases with explanations:
  - `pattern = "a", strings = ["Foo", "Bar", "a", "An"]`, the output should be `["a", "An"]`.
  - `pattern = "z", strings = ["def", "de", "f"]`, the output should be `["z"]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate over each string in the array and check if it matches the pattern.
- Step-by-step breakdown of the solution:
  1. Convert the pattern to lowercase.
  2. Iterate over each string in the array.
  3. Convert the string to lowercase and check if it matches the lowercase pattern.
  4. If the string matches the pattern, check if it is in CamelCase.
- Why this approach comes to mind first: It is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
class Solution {
public:
    vector<string> camelMatch(vector<string>& strings, string pattern) {
        vector<string> result;
        string lowerPattern = pattern;
        transform(lowerPattern.begin(), lowerPattern.end(), lowerPattern.begin(), ::tolower);
        
        for (const auto& str : strings) {
            string lowerStr = str;
            transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);
            if (lowerStr == lowerPattern) {
                bool isCamelCase = true;
                for (int i = 0; i < str.size(); ++i) {
                    if (isupper(str[i]) && (i == 0 || islower(str[i - 1]))) {
                        continue;
                    }
                    if (isupper(str[i])) {
                        isCamelCase = false;
                        break;
                    }
                }
                if (isCamelCase) {
                    result.push_back(str);
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we iterate over each string and each character in the string.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we store the result and the lowercase version of each string.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each string and each character in the string. The space complexity occurs because we store the result and the lowercase version of each string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking if a string is in CamelCase after we know it matches the pattern, we can do both checks simultaneously.
- Detailed breakdown of the approach:
  1. Convert the pattern to lowercase.
  2. Iterate over each string in the array.
  3. Use two pointers, one for the string and one for the pattern, to check if the string matches the pattern and is in CamelCase.
- Proof of optimality: This solution has the same time complexity as the brute force approach, but it reduces the number of operations and is more efficient in practice.

```cpp
class Solution {
public:
    vector<string> camelMatch(vector<string>& strings, string pattern) {
        vector<string> result;
        string lowerPattern = pattern;
        transform(lowerPattern.begin(), lowerPattern.end(), lowerPattern.begin(), ::tolower);
        
        for (const auto& str : strings) {
            string lowerStr = str;
            transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);
            int patternIndex = 0;
            bool isMatch = true;
            for (int i = 0; i < str.size(); ++i) {
                if (patternIndex < lowerPattern.size() && lowerStr[i] == lowerPattern[patternIndex]) {
                    patternIndex++;
                } else if (isupper(str[i])) {
                    isMatch = false;
                    break;
                }
            }
            if (isMatch && patternIndex == lowerPattern.size()) {
                result.push_back(str);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string.
> - **Optimality proof:** This solution is optimal because it has the same time complexity as the brute force approach, but it reduces the number of operations and is more efficient in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique and string manipulation.
- Problem-solving patterns identified: Checking if a string matches a pattern and is in CamelCase.
- Optimization techniques learned: Reducing the number of operations by combining checks.
- Similar problems to practice: Other string manipulation problems, such as checking if a string is a substring of another string.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a string is in CamelCase correctly.
- Edge cases to watch for: Empty strings and strings with only uppercase or lowercase characters.
- Performance pitfalls: Using inefficient algorithms or data structures.
- Testing considerations: Testing with different inputs, including edge cases.