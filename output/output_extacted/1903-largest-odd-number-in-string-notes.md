## Largest Odd Number in String
**Problem Link:** https://leetcode.com/problems/largest-odd-number-in-string/description

**Problem Statement:**
- Input: A string `num` consisting of digits.
- Constraints: `1 <= num.length <= 10^5`.
- Expected Output: The largest odd number that can be formed by removing at most one digit from `num`. If no such number exists, return an empty string.
- Key Requirements: Identify the largest odd number by possibly removing one digit.
- Edge Cases: Consider strings that do not contain any odd digits, or strings where removing one digit can result in a larger odd number.

### Brute Force Approach

**Explanation:**
- Start by checking if the number is already odd. If it is, return the number as it is.
- Otherwise, iterate through each digit in the string. For each digit, create a new string by removing that digit and check if the resulting number is odd.
- Keep track of the largest odd number found.

```cpp
#include <iostream>
#include <string>

std::string largestOddNumber(std::string num) {
    // Check if the number is already odd
    int lastDigit = num[num.size() - 1] - '0';
    if (lastDigit % 2 != 0) {
        return num;
    }

    std::string largestOdd;
    for (int i = 0; i < num.size(); i++) {
        std::string newNum = num.substr(0, i) + num.substr(i + 1);
        lastDigit = newNum[newNum.size() - 1] - '0';
        if (lastDigit % 2 != 0 && (largestOdd.empty() || newNum > largestOdd)) {
            largestOdd = newNum;
        }
    }
    return largestOdd;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because in the worst case, we are creating a new string of length $n-1$ for each digit in the string, and then comparing this new string with the current largest odd string.
> - **Space Complexity:** $O(n)$, as we are creating a new string of length $n-1$ in each iteration.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach, checking every possible removal of a digit and then comparing the resulting strings.

### Optimal Approach (Required)

**Explanation:**
- Start from the end of the string and check if the last digit is odd. If it is, return the string as it is.
- If the last digit is even, move towards the start of the string to find the first even digit. Remove this digit and return the resulting string if it is not empty.
- If no even digit is found, return an empty string.

```cpp
std::string largestOddNumber(std::string num) {
    int n = num.size();
    for (int i = n - 1; i >= 0; i--) {
        if ((num[i] - '0') % 2 != 0) {
            if (i == n - 1) return num;
            for (int j = n - 1; j > i; j--) {
                if ((num[j] - '0') % 2 == 0) {
                    num.erase(j, 1);
                    return num;
                }
            }
        }
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because in the worst case, we are scanning the string once.
> - **Space Complexity:** $O(n)$, as we are modifying the input string in the worst case.
> - **Optimality proof:** This approach is optimal because we are scanning the string only once and making a single modification if necessary, resulting in the largest odd number possible.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: scanning the string from the end, checking for odd and even digits, and making a single modification to achieve the optimal result.
- Problem-solving patterns identified: starting from the end of the string and moving towards the start, and making use of the properties of odd and even numbers.
- Optimization techniques learned: reducing the time complexity by scanning the string only once and making a single modification.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the edge case where the input string is empty, or not handling the case where no odd digit is found.
- Edge cases to watch for: strings with only even digits, or strings with only one digit.
- Performance pitfalls: using a brute force approach that results in a high time complexity.
- Testing considerations: testing the function with different input strings, including edge cases and large inputs.