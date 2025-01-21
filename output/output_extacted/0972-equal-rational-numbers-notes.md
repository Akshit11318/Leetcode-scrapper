## Equal Rational Numbers
**Problem Link:** https://leetcode.com/problems/equal-rational-numbers/description

**Problem Statement:**
- Input format: Two strings `s` and `t` representing rational numbers in the form `numerator/denominator`.
- Constraints: The input strings are valid rational numbers, and the denominators are non-zero.
- Expected output format: A boolean indicating whether the two rational numbers are equal.
- Key requirements and edge cases to consider: Handle cases where the denominators are different, and consider the possibility of equivalent fractions (e.g., 1/2 = 2/4).

**Example Test Cases:**
- `s = "0.(52)", t = "0.4(2)"` should return `true`.
- `s = "0.(52)", t = "0.4(22)"` should return `false`.
- `s = "0.1666(6)", t = "0.1(6)"` should return `true`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare the two rational numbers by converting them to a common format, such as decimal numbers, and then compare the decimal representations.
- Step-by-step breakdown of the solution:
  1. Parse the input strings to extract the numerator and denominator of each rational number.
  2. Convert each rational number to a decimal number by dividing the numerator by the denominator.
  3. Compare the decimal representations of the two rational numbers.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that leverages familiar arithmetic operations.

```cpp
#include <iostream>
#include <string>

bool isRationalEqual(const std::string& s, const std::string& t) {
    // Parse the input strings to extract the numerator and denominator
    int sNumerator, sDenominator;
    int tNumerator, tDenominator;
    size_t sDotPos = s.find('.');
    size_t tDotPos = t.find('.');
    if (sDotPos != std::string::npos) {
        size_t sParenPos = s.find('(');
        if (sParenPos != std::string::npos) {
            // Handle repeating decimal
            sNumerator = std::stoi(s.substr(0, sDotPos));
            sDenominator = 1;
            for (int i = sDotPos + 1; i < sParenPos; i++) {
                sDenominator *= 10;
            }
            for (int i = sParenPos + 1; i < s.size() - 1; i++) {
                sNumerator = sNumerator * 10 + (s[i] - '0');
                sDenominator *= 10;
            }
        } else {
            // Handle non-repeating decimal
            sNumerator = std::stoi(s.substr(0, sDotPos));
            sDenominator = 1;
            for (int i = sDotPos + 1; i < s.size(); i++) {
                sDenominator *= 10;
            }
            for (int i = sDotPos + 1; i < s.size(); i++) {
                sNumerator = sNumerator * 10 + (s[i] - '0');
            }
        }
    } else {
        sNumerator = std::stoi(s);
        sDenominator = 1;
    }

    if (tDotPos != std::string::npos) {
        size_t tParenPos = t.find('(');
        if (tParenPos != std::string::npos) {
            // Handle repeating decimal
            tNumerator = std::stoi(t.substr(0, tDotPos));
            tDenominator = 1;
            for (int i = tDotPos + 1; i < tParenPos; i++) {
                tDenominator *= 10;
            }
            for (int i = tParenPos + 1; i < t.size() - 1; i++) {
                tNumerator = tNumerator * 10 + (t[i] - '0');
                tDenominator *= 10;
            }
        } else {
            // Handle non-repeating decimal
            tNumerator = std::stoi(t.substr(0, tDotPos));
            tDenominator = 1;
            for (int i = tDotPos + 1; i < t.size(); i++) {
                tDenominator *= 10;
            }
            for (int i = tDotPos + 1; i < t.size(); i++) {
                tNumerator = tNumerator * 10 + (t[i] - '0');
            }
        }
    } else {
        tNumerator = std::stoi(t);
        tDenominator = 1;
    }

    // Compare the decimal representations
    return sNumerator * tDenominator == tNumerator * sDenominator;
}

int main() {
    std::string s = "0.(52)";
    std::string t = "0.4(2)";
    std::cout << std::boolalpha << isRationalEqual(s, t) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(n, m))$, where $n$ and $m$ are the lengths of the input strings. This is because we need to iterate over the input strings to parse and compare the rational numbers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the numerator and denominator of each rational number.
> - **Why these complexities occur:** The time complexity is dominated by the parsing and comparison of the rational numbers, which requires iterating over the input strings. The space complexity is constant because we only use a fixed amount of space to store the numerator and denominator.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Compare the rational numbers by finding the least common multiple (LCM) of the denominators and then comparing the numerators.
- Detailed breakdown of the approach:
  1. Parse the input strings to extract the numerator and denominator of each rational number.
  2. Find the LCM of the denominators.
  3. Multiply the numerator of each rational number by the LCM and divide by the denominator.
  4. Compare the resulting numerators.
- Proof of optimality: This approach is optimal because it minimizes the number of arithmetic operations required to compare the rational numbers.

```cpp
#include <iostream>
#include <string>

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

bool isRationalEqual(const std::string& s, const std::string& t) {
    // Parse the input strings to extract the numerator and denominator
    int sNumerator, sDenominator;
    int tNumerator, tDenominator;
    size_t sDotPos = s.find('.');
    size_t tDotPos = t.find('.');
    if (sDotPos != std::string::npos) {
        size_t sParenPos = s.find('(');
        if (sParenPos != std::string::npos) {
            // Handle repeating decimal
            sNumerator = std::stoi(s.substr(0, sDotPos));
            sDenominator = 1;
            for (int i = sDotPos + 1; i < sParenPos; i++) {
                sDenominator *= 10;
            }
            for (int i = sParenPos + 1; i < s.size() - 1; i++) {
                sNumerator = sNumerator * 10 + (s[i] - '0');
                sDenominator *= 10;
            }
        } else {
            // Handle non-repeating decimal
            sNumerator = std::stoi(s.substr(0, sDotPos));
            sDenominator = 1;
            for (int i = sDotPos + 1; i < s.size(); i++) {
                sDenominator *= 10;
            }
            for (int i = sDotPos + 1; i < s.size(); i++) {
                sNumerator = sNumerator * 10 + (s[i] - '0');
            }
        }
    } else {
        sNumerator = std::stoi(s);
        sDenominator = 1;
    }

    if (tDotPos != std::string::npos) {
        size_t tParenPos = t.find('(');
        if (tParenPos != std::string::npos) {
            // Handle repeating decimal
            tNumerator = std::stoi(t.substr(0, tDotPos));
            tDenominator = 1;
            for (int i = tDotPos + 1; i < tParenPos; i++) {
                tDenominator *= 10;
            }
            for (int i = tParenPos + 1; i < t.size() - 1; i++) {
                tNumerator = tNumerator * 10 + (t[i] - '0');
                tDenominator *= 10;
            }
        } else {
            // Handle non-repeating decimal
            tNumerator = std::stoi(t.substr(0, tDotPos));
            tDenominator = 1;
            for (int i = tDotPos + 1; i < t.size(); i++) {
                tDenominator *= 10;
            }
            for (int i = tDotPos + 1; i < t.size(); i++) {
                tNumerator = tNumerator * 10 + (t[i] - '0');
            }
        }
    } else {
        tNumerator = std::stoi(t);
        tDenominator = 1;
    }

    // Find the LCM of the denominators
    int lcmValue = lcm(sDenominator, tDenominator);

    // Compare the numerators
    return sNumerator * (lcmValue / sDenominator) == tNumerator * (lcmValue / tDenominator);
}

int main() {
    std::string s = "0.(52)";
    std::string t = "0.4(2)";
    std::cout << std::boolalpha << isRationalEqual(s, t) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(n, m))$, where $n$ and $m$ are the lengths of the input strings. This is because we need to iterate over the input strings to parse and compare the rational numbers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the numerator and denominator of each rational number.
> - **Optimality proof:** This approach is optimal because it minimizes the number of arithmetic operations required to compare the rational numbers by finding the LCM of the denominators.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: parsing rational numbers, finding the LCM of denominators, and comparing numerators.
- Problem-solving patterns identified: breaking down complex problems into simpler sub-problems and using mathematical insights to optimize solutions.
- Optimization techniques learned: minimizing arithmetic operations by finding the LCM of denominators.

**Mistakes to Avoid:**
- Common implementation errors: incorrect parsing of input strings, incorrect calculation of LCM, and incorrect comparison of numerators.
- Edge cases to watch for: handling repeating decimals, non-repeating decimals, and integers.
- Performance pitfalls: using inefficient algorithms for finding the LCM or comparing numerators.
- Testing considerations: testing with different input formats, such as repeating decimals, non-repeating decimals, and integers.