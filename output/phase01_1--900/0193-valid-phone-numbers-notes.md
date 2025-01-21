## Valid Phone Numbers
**Problem Link:** https://leetcode.com/problems/valid-phone-numbers/description

**Problem Statement:**
- Input format and constraints: The input is a list of phone numbers in the format of a string.
- Expected output format: Return the phone numbers that are valid according to the specified rules.
- Key requirements and edge cases to consider: A phone number is valid if it starts with a `(`, followed by exactly three digits, a `)`, a space, and then exactly three more digits, a `-`, and finally four more digits.
- Example test cases with explanations: 
    - Example 1: Input: ["(123) 456-7890","123-456-7890","(123) 456-7890"] Output: ["(123) 456-7890","(123) 456-7890"]
    - Example 2: Input: ["123-456-7890"] Output: []

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each character of the phone number string to see if it matches the required format.
- Step-by-step breakdown of the solution: 
    1. Check if the string length is 14.
    2. Check the first character is `(`.
    3. Check the next three characters are digits.
    4. Check the fifth character is `)`.
    5. Check the sixth character is a space.
    6. Check the next three characters are digits.
    7. Check the tenth character is `-`.
    8. Check the last four characters are digits.
- Why this approach comes to mind first: This approach is straightforward and checks each character individually.

```cpp
#include <vector>
#include <string>

std::vector<std::string> validPhoneNumbers(const std::vector<std::string>& nums) {
    std::vector<std::string> result;
    for (const auto& num : nums) {
        if (num.length() != 14) continue;
        if (num[0] != '(' || num[4] != ')' || num[5] != ' ' || num[9] != '-') continue;
        bool isValid = true;
        for (int i = 1; i <= 3; i++) {
            if (!isdigit(num[i])) {
                isValid = false;
                break;
            }
        }
        for (int i = 6; i <= 8; i++) {
            if (!isdigit(num[i])) {
                isValid = false;
                break;
            }
        }
        for (int i = 10; i <= 13; i++) {
            if (!isdigit(num[i])) {
                isValid = false;
                break;
            }
        }
        if (isValid) result.push_back(num);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of phone numbers and $m$ is the length of each phone number (which is 14 in this case). This is because we are iterating over each character in each phone number.
> - **Space Complexity:** $O(n)$ where $n$ is the number of valid phone numbers. This is because we are storing the valid phone numbers in a new vector.
> - **Why these complexities occur:** These complexities occur because we are checking each character in each phone number individually.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a regular expression to match the phone number pattern.
- Detailed breakdown of the approach: 
    1. Define a regular expression pattern that matches the required phone number format.
    2. Use this pattern to check each phone number in the input list.
- Proof of optimality: This approach is optimal because it directly checks the phone number against the required pattern, without needing to check each character individually.
- Why further optimization is impossible: This approach is already optimal because it uses a regular expression, which is a concise and efficient way to match patterns in strings.

```cpp
#include <vector>
#include <string>
#include <regex>

std::vector<std::string> validPhoneNumbers(const std::vector<std::string>& nums) {
    std::vector<std::string> result;
    std::regex pattern("^\\(\\d{3}\\) \\d{3}-\\d{4}$");
    for (const auto& num : nums) {
        if (std::regex_match(num, pattern)) result.push_back(num);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of phone numbers and $m$ is the length of each phone number (which is 14 in this case). This is because we are using a regular expression to match the phone number pattern.
> - **Space Complexity:** $O(n)$ where $n$ is the number of valid phone numbers. This is because we are storing the valid phone numbers in a new vector.
> - **Optimality proof:** This approach is optimal because it uses a regular expression to match the phone number pattern, which is a concise and efficient way to match patterns in strings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Regular expressions, pattern matching.
- Problem-solving patterns identified: Using regular expressions to match patterns in strings.
- Optimization techniques learned: Using regular expressions to match patterns in strings can be more efficient than checking each character individually.
- Similar problems to practice: Other problems that involve matching patterns in strings.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the input phone numbers for validity before trying to match them against the pattern.
- Edge cases to watch for: Phone numbers that are not in the correct format.
- Performance pitfalls: Using a brute force approach to match the phone number pattern, which can be slower than using a regular expression.
- Testing considerations: Testing the function with a variety of input phone numbers to ensure it works correctly.