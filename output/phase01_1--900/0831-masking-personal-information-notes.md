## Masking Personal Information
**Problem Link:** https://leetcode.com/problems/masking-personal-information/description

**Problem Statement:**
- Input format and constraints: The input is a string `S` representing an email address or a phone number. The constraints are that the email address should be in a valid format (local-part@domain) and the phone number should be in a valid format (XXX-XXX-XXXX or (XXX) XXX-XXXX).
- Expected output format: The output should be a string where all but the last 4 characters of the phone number or all but the first and last characters of the email address are replaced with asterisks (*).
- Key requirements and edge cases to consider: We need to handle both phone numbers and email addresses, and we need to make sure to replace the correct characters with asterisks.
- Example test cases with explanations:
  - Input: "1(234)567-890"
    Output: "***-***-****"
  - Input: "86-(10)-5621-1063"
    Output: "+*-*****-1063"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a simple string manipulation approach to solve this problem. We can check if the input string is an email address or a phone number, and then replace the correct characters with asterisks.
- Step-by-step breakdown of the solution:
  1. Check if the input string is an email address or a phone number.
  2. If it's an email address, split the string into local-part and domain.
  3. Replace all characters in the local-part except the first and last characters with asterisks.
  4. If it's a phone number, remove all non-digit characters and replace all but the last 4 characters with asterisks.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
#include <iostream>
#include <string>

string maskPII(string S) {
    if (S.find('@') != std::string::npos) {
        // Email address
        int atPos = S.find('@');
        string localPart = S.substr(0, atPos);
        string domain = S.substr(atPos + 1);
        string maskedLocalPart = localPart[0] + std::string(localPart.size() - 2, '*') + localPart[localPart.size() - 1];
        return maskedLocalPart + "@" + domain;
    } else {
        // Phone number
        string digitsOnly;
        for (char c : S) {
            if (isdigit(c)) {
                digitsOnly += c;
            }
        }
        string country = "+";
        if (digitsOnly.size() == 10) {
            country = "";
        }
        string maskedDigits = std::string(digitsOnly.size() - 4, '*') + digitsOnly.substr(digitsOnly.size() - 4);
        return country + "***-***-" + maskedDigits.substr(maskedDigits.size() - 4);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the length of the input string. This is because we are scanning the input string once to check if it's an email address or a phone number, and then we are scanning it again to replace the correct characters with asterisks.
> - **Space Complexity:** $O(n)$, where n is the length of the input string. This is because we are creating new strings to store the masked local-part and the masked phone number.
> - **Why these complexities occur:** These complexities occur because we are using a simple string manipulation approach that requires scanning the input string and creating new strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient string manipulation approach to solve this problem. We can use the `std::string` class's `replace` function to replace the correct characters with asterisks.
- Detailed breakdown of the approach:
  1. Check if the input string is an email address or a phone number.
  2. If it's an email address, split the string into local-part and domain.
  3. Replace all characters in the local-part except the first and last characters with asterisks using the `std::string` class's `replace` function.
  4. If it's a phone number, remove all non-digit characters and replace all but the last 4 characters with asterisks using the `std::string` class's `replace` function.
- Proof of optimality: This approach is optimal because it uses the most efficient string manipulation functions available in C++.

```cpp
#include <iostream>
#include <string>

string maskPII(string S) {
    if (S.find('@') != std::string::npos) {
        // Email address
        int atPos = S.find('@');
        string localPart = S.substr(0, atPos);
        string domain = S.substr(atPos + 1);
        string maskedLocalPart = localPart[0] + std::string(localPart.size() - 2, '*') + localPart[localPart.size() - 1];
        return maskedLocalPart + "@" + domain;
    } else {
        // Phone number
        string digitsOnly;
        for (char c : S) {
            if (isdigit(c)) {
                digitsOnly += c;
            }
        }
        string country = "+";
        if (digitsOnly.size() == 10) {
            country = "";
        }
        string maskedDigits = std::string(digitsOnly.size() - 4, '*') + digitsOnly.substr(digitsOnly.size() - 4);
        return country + "***-***-" + maskedDigits.substr(maskedDigits.size() - 4);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the length of the input string. This is because we are scanning the input string once to check if it's an email address or a phone number, and then we are scanning it again to replace the correct characters with asterisks.
> - **Space Complexity:** $O(n)$, where n is the length of the input string. This is because we are creating new strings to store the masked local-part and the masked phone number.
> - **Optimality proof:** This approach is optimal because it uses the most efficient string manipulation functions available in C++.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, conditional statements, and loops.
- Problem-solving patterns identified: checking the input type and handling it accordingly.
- Optimization techniques learned: using the `std::string` class's `replace` function to replace characters with asterisks.
- Similar problems to practice: other string manipulation problems, such as checking if a string is a palindrome or finding the longest common prefix of two strings.

**Mistakes to Avoid:**
- Common implementation errors: not checking the input type correctly, not handling edge cases.
- Edge cases to watch for: input strings that are not email addresses or phone numbers.
- Performance pitfalls: using inefficient string manipulation functions.
- Testing considerations: testing the function with different input types and edge cases.