## Reformat The String
**Problem Link:** https://leetcode.com/problems/reformat-the-string/description

**Problem Statement:**
- Input: A string `s` containing only lowercase letters and digits.
- Constraints: `1 <= s.length <= 500`.
- Expected Output: If we can reformat the string such that no two adjacent characters are the same type (both letters or both digits), return the reformatted string; otherwise, return an empty string.
- Key Requirements: The input string can be a mix of letters and digits, and we need to reformat it to meet the condition.
- Edge Cases:
  - If the difference in the count of letters and digits is more than 1, it's impossible to reformat the string.
  - If the input string is already reformatted, the function should return the string as it is.

**Example Test Cases:**
- `s = "a0b1c2"`: The output should be `"0a1b2c"`, `"0a1b2c"`, `"2c1b0a"`, etc.
- `s = "leetcode"`: The output should be an empty string because it's impossible to reformat the string to meet the condition.
- `s = "1229857369"`: The output should be an empty string because it's impossible to reformat the string to meet the condition.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of the characters in the string and check if the condition is met.
- We can use a recursive approach or backtracking to generate all permutations of the string.
- However, this approach is inefficient because it has an exponential time complexity.

```cpp
#include <iostream>
#include <string>
using namespace std;

string reformatString(string s) {
    int n = s.length();
    // Generate all permutations of the string
    string result = "";
    // Check each permutation to see if it meets the condition
    return result;
}

// However, implementing this approach is complex and inefficient, so let's consider a better approach.
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ because we are generating all permutations of the string.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible combinations of the characters in the string.

---

### Optimal Approach (Required)

**Explanation:**
- We can solve this problem by using two pointers, one for letters and one for digits.
- We count the number of letters and digits in the string and check if the difference is more than 1.
- If the difference is not more than 1, we can reformat the string by alternating between letters and digits.
- We can use two separate lists to store the letters and digits, and then iterate through the lists to construct the result string.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string reformat(string s) {
    vector<char> letters, digits;
    for (char c : s) {
        if (isalpha(c)) {
            letters.push_back(c);
        } else {
            digits.push_back(c);
        }
    }
    if (abs((int)letters.size() - (int)digits.size()) > 1) {
        return "";
    }
    string result = "";
    if (letters.size() > digits.size()) {
        for (int i = 0; i < digits.size(); i++) {
            result += letters[i];
            result += digits[i];
        }
        result += letters.back();
    } else if (digits.size() > letters.size()) {
        for (int i = 0; i < letters.size(); i++) {
            result += digits[i];
            result += letters[i];
        }
        result += digits.back();
    } else {
        for (int i = 0; i < letters.size(); i++) {
            result += letters[i];
            result += digits[i];
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are iterating through the string twice.
> - **Space Complexity:** $O(n)$ for storing the letters and digits.
> - **Optimality proof:** This is the optimal solution because we are only iterating through the string twice, and we are not using any unnecessary data structures.

---

### Final Notes

**Learning Points:**
- We learned how to solve a string reformatting problem using two pointers.
- We identified the key insight that the difference in the count of letters and digits should not be more than 1.
- We practiced using separate lists to store different types of characters and then constructing the result string.

**Mistakes to Avoid:**
- Not checking the difference in the count of letters and digits before attempting to reformat the string.
- Not using separate lists to store letters and digits, which can lead to incorrect results.
- Not handling edge cases, such as when the input string is already reformatted or when the difference in the count of letters and digits is more than 1.