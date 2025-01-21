## Fraction Addition and Subtraction
**Problem Link:** https://leetcode.com/problems/fraction-addition-and-subtraction/description

**Problem Statement:**
- Input format: a string `equation` containing fractions with `+` and `-` signs.
- Constraints: $1 \leq \text{length of equation} \leq 10^5$, the input string only contains digits, `+`, `-`, `/`, and `(`, `)`.
- Expected output format: the result of the addition and subtraction as a string in the format `"-x/y"` or `"x/y"` where `x` is the numerator and `y` is the denominator.
- Key requirements: calculate the result of the given equation, handle edge cases such as division by zero, and simplify the fraction.
- Example test cases:
  - Input: `"1/2+1/2+1/3"`
    - Output: `"7/6"`
  - Input: `"1/3-1/2"`
    - Output: `"-1/6"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: parse the input string to extract the fractions, then calculate the least common multiple (LCM) of all denominators.
- Step-by-step breakdown:
  1. Extract the fractions from the input string.
  2. Calculate the LCM of all denominators.
  3. Convert each fraction to have the LCM as the denominator.
  4. Add or subtract the numerators based on the signs.
  5. Simplify the resulting fraction if possible.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <numeric>

// Function to calculate the greatest common divisor (GCD)
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

// Function to calculate the LCM
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

string fractionAddition(string equation) {
    vector<int> numerators, denominators;
    bool isPositive = true;
    int numerator = 0, denominator = 1;

    for (int i = 0; i < equation.size(); ++i) {
        if (equation[i] == '+' || equation[i] == '-') {
            numerators.push_back(isPositive ? numerator : -numerator);
            denominators.push_back(denominator);
            isPositive = equation[i] == '+';
            numerator = 0;
            denominator = 1;
        } else if (equation[i] == '/') {
            denominator = 0;
            for (int j = i + 1; j < equation.size(); ++j) {
                if (equation[j] == '+' || equation[j] == '-' || equation[j] == '\0') {
                    break;
                }
                denominator = denominator * 10 + (equation[j] - '0');
            }
            i = j - 1;
        } else {
            numerator = numerator * 10 + (equation[i] - '0');
        }
    }

    numerators.push_back(isPositive ? numerator : -numerator);
    denominators.push_back(denominator);

    int lcmValue = 1;
    for (int denominator : denominators) {
        lcmValue = lcm(lcmValue, denominator);
    }

    int sum = 0;
    for (int i = 0; i < numerators.size(); ++i) {
        sum += (lcmValue / denominators[i]) * numerators[i];
    }

    int gcdValue = gcd(sum, lcmValue);
    sum /= gcdValue;
    lcmValue /= gcdValue;

    string result = to_string(sum) + "/" + to_string(lcmValue);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of fractions and $m$ is the maximum number of digits in a fraction.
> - **Space Complexity:** $O(n)$, where $n$ is the number of fractions.
> - **Why these complexities occur:** The time complexity is due to the iteration over the input string and the calculation of the LCM and GCD. The space complexity is due to the storage of the fractions.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: instead of calculating the LCM of all denominators, we can calculate the LCM on the fly as we process the fractions.
- Detailed breakdown:
  1. Initialize the result numerator and denominator to 0 and 1, respectively.
  2. Iterate over the input string, extracting the fractions and signs.
  3. For each fraction, calculate the LCM of the current denominator and the fraction's denominator.
  4. Update the result numerator and denominator based on the sign and the LCM.
  5. Simplify the resulting fraction if possible.

```cpp
string fractionAddition(string equation) {
    int A = 0, B = 1;
    int i = 0, n = equation.size();
    while (i < n) {
        int sign = 1;
        if (equation[i] == '-' || equation[i] == '+') {
            if (equation[i] == '-') sign = -1;
            i++;
        }
        int numerator = 0;
        while (i < n && equation[i] != '/') {
            numerator = numerator * 10 + equation[i++] - '0';
        }
        i++;
        int denominator = 0;
        while (i < n && equation[i] != '+' && equation[i] != '-' && i < n) {
            denominator = denominator * 10 + equation[i++] - '0';
        }
        int gcdValue = gcd(B, denominator);
        A = A * (denominator / gcdValue) + sign * numerator * (B / gcdValue);
        B = B * (denominator / gcdValue);
        gcdValue = gcd(A, B);
        A /= gcdValue;
        B /= gcdValue;
    }
    if (A == 0) return "0/1";
    return to_string(A) + "/" + to_string(B);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input string and uses a constant amount of extra space. The calculation of the LCM and GCD is done on the fly, avoiding the need for extra storage.