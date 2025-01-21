## Reformat Phone Number

**Problem Link:** https://leetcode.com/problems/reformat-phone-number/description

**Problem Statement:**
- Input: A string `s` representing a phone number.
- Constraints: The length of `s` is between 2 and 13 digits (inclusive).
- Expected output: The phone number in a formatted string.
- Key requirements: The phone number should be formatted as XXX-XXX-XXXX if it has 10 digits, or XXX-XXX-XXX if it has 9 digits, or XXX-XX-XX if it has 8 digits, or XXX-XX-XX-XX if it has 11 digits, or XXX-XX-XX-XX-XX if it has 12 digits, or XXX-XX-XX-XX-XX-XX if it has 13 digits.
- Edge cases: Handle phone numbers of varying lengths.

**Example Test Cases:**
- Input: `s = "1234567890"`
  Output: `"123-456-7890"`
- Input: `s = "1234"`
  Output: `"1234"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to manually check the length of the string and then format it accordingly.
- Step-by-step breakdown:
  1. Check the length of the string.
  2. Based on the length, apply the corresponding formatting rules.

```cpp
string reformatNumber(string s) {
    // Remove all non-digit characters
    string digits;
    for (char c : s) {
        if (isdigit(c)) {
            digits += c;
        }
    }
    
    if (digits.length() == 2) {
        return digits;
    } else if (digits.length() == 3) {
        return digits;
    } else if (digits.length() == 10) {
        return digits.substr(0, 3) + "-" + digits.substr(3, 3) + "-" + digits.substr(6);
    } else {
        int groups = (digits.length() - 1) / 3;
        string result;
        for (int i = 0; i < groups; i++) {
            result += digits.substr(i * 3, 3) + "-";
        }
        result += digits.substr(groups * 3);
        if (result.back() == '-') {
            result.pop_back();
        }
        return result;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we iterate over the string to remove non-digit characters and then format the digits.
> - **Space Complexity:** $O(n)$, because we create a new string to store the digits and the formatted result.
> - **Why these complexities occur:** The time complexity occurs because we perform a constant amount of work for each character in the string. The space complexity occurs because we create new strings to store the digits and the formatted result.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to remove all non-digit characters and then format the digits based on their length.
- Step-by-step breakdown:
  1. Remove all non-digit characters from the string.
  2. Determine the length of the resulting string.
  3. Apply the corresponding formatting rules based on the length.

```cpp
string reformatNumber(string s) {
    string digits;
    for (char c : s) {
        if (isdigit(c)) {
            digits += c;
        }
    }
    
    if (digits.length() <= 3) {
        return digits;
    } else if (digits.length() == 4) {
        return digits.substr(0, 2) + "-" + digits.substr(2);
    }
    
    string result;
    while (digits.length() > 4) {
        result += digits.substr(0, 3) + "-";
        digits = digits.substr(3);
    }
    
    if (digits.length() == 2) {
        result += "-" + digits;
    } else {
        result += "-" + digits.substr(0, 2) + "-" + digits.substr(2);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we iterate over the string to remove non-digit characters and then format the digits.
> - **Space Complexity:** $O(n)$, because we create new strings to store the digits and the formatted result.
> - **Optimality proof:** This is the optimal solution because we only iterate over the string once to remove non-digit characters and then format the digits in a single pass. We also avoid unnecessary string concatenations by building the result string incrementally.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, formatting, and iteration.
- Problem-solving patterns identified: handling edge cases, iterating over strings, and formatting output.
- Optimization techniques learned: avoiding unnecessary string concatenations and iterating over strings in a single pass.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, incorrect string indexing, and inefficient string concatenations.
- Edge cases to watch for: phone numbers of varying lengths and non-digit characters in the input string.
- Performance pitfalls: using inefficient string concatenation methods and iterating over strings multiple times.
- Testing considerations: test the function with phone numbers of different lengths and containing non-digit characters.