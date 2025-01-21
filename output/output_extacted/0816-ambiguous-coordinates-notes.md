## Ambiguous Coordinates
**Problem Link:** https://leetcode.com/problems/ambiguous-coordinates/description

**Problem Statement:**
- Input format and constraints: Given a string `s` representing a valid number, return all possible ambiguous coordinates that can be generated from `s`. The valid number should have a maximum of 5 digits and should not start with `0` unless it's a single digit number.
- Expected output format: Return a list of all possible ambiguous coordinates that can be generated from `s`.
- Key requirements and edge cases to consider: 
  - A valid number can have a maximum of 5 digits and should not start with `0` unless it's a single digit number.
  - For each number, we can insert a decimal point anywhere between the digits to form different coordinates.
- Example test cases with explanations:
  - Input: `s = "123"`
    - Output: `["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]`
  - Input: `s = "0000"`
    - Output: `["(0, 0)"]`
  - Input: `s = "0123"`
    - Output: `["(0, 123)", "(0, 1.23)"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by generating all possible combinations of coordinates that can be formed by inserting a decimal point at different positions in the string `s`.
- Step-by-step breakdown of the solution:
  1. Check if the string `s` is valid (does not start with `0` unless it's a single digit number).
  2. Generate all possible combinations of coordinates by inserting a decimal point at different positions in the string `s`.
  3. For each combination, check if the numbers before and after the decimal point are valid (do not start with `0` unless they are single digit numbers).
  4. If both numbers are valid, add the combination to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. It involves generating all possible combinations of coordinates and checking their validity.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> ambiguousCoordinates(std::string s) {
    std::vector<std::string> result;
    if (s[0] == '0' && s.size() > 1) return result;

    for (int i = 1; i < s.size(); i++) {
        std::string left = s.substr(0, i);
        std::string right = s.substr(i);

        // Check if the left number is valid
        if (left[0] == '0' && left.size() > 1) continue;
        if (right[0] == '0' && right.size() > 1) continue;

        // Generate all possible combinations of coordinates
        for (int j = 0; j < left.size(); j++) {
            for (int k = 0; k < right.size(); k++) {
                std::string leftStr = left;
                std::string rightStr = right;

                if (j > 0) leftStr.insert(j, ".");
                if (k > 0) rightStr.insert(k, ".");

                // Check if the numbers before and after the decimal point are valid
                if (leftStr[0] == '0' && leftStr.size() > 1 && leftStr.find(".") == std::string::npos) continue;
                if (rightStr[0] == '0' && rightStr.size() > 1 && rightStr.find(".") == std::string::npos) continue;

                result.push_back("(" + leftStr + ", " + rightStr + ")");
            }
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string `s`. This is because we have two nested loops that iterate over the string `s`.
> - **Space Complexity:** $O(n)$ where $n$ is the length of the string `s`. This is because we need to store the result list which can have up to $n^2$ elements.
> - **Why these complexities occur:** The time complexity occurs because we have two nested loops that iterate over the string `s`. The space complexity occurs because we need to store the result list which can have up to $n^2$ elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations of coordinates and checking their validity, we can generate the combinations only when the numbers before and after the decimal point are valid.
- Detailed breakdown of the approach:
  1. Check if the string `s` is valid (does not start with `0` unless it's a single digit number).
  2. Generate all possible combinations of coordinates by inserting a decimal point at different positions in the string `s`.
  3. For each combination, check if the numbers before and after the decimal point are valid (do not start with `0` unless they are single digit numbers).
  4. If both numbers are valid, add the combination to the result list.
- Why further optimization is impossible: This approach is already optimal because it generates the combinations only when the numbers before and after the decimal point are valid.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> ambiguousCoordinates(std::string s) {
    std::vector<std::string> result;
    if (s[0] == '0' && s.size() > 1) return result;

    for (int i = 1; i < s.size(); i++) {
        std::string left = s.substr(0, i);
        std::string right = s.substr(i);

        std::vector<std::string> leftList = generateNumbers(left);
        std::vector<std::string> rightList = generateNumbers(right);

        for (const auto& leftStr : leftList) {
            for (const auto& rightStr : rightList) {
                result.push_back("(" + leftStr + ", " + rightStr + ")");
            }
        }
    }

    return result;
}

std::vector<std::string> generateNumbers(std::string num) {
    std::vector<std::string> result;
    if (num[0] == '0' && num.size() > 1) {
        if (num.find('0', 1) == std::string::npos) {
            result.push_back(num);
        }
        return result;
    }

    result.push_back(num);
    for (int i = 1; i < num.size(); i++) {
        std::string numStr = num;
        numStr.insert(i, ".");
        result.push_back(numStr);
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string `s`. This is because we have two nested loops that iterate over the string `s`.
> - **Space Complexity:** $O(n)$ where $n$ is the length of the string `s`. This is because we need to store the result list which can have up to $n^2$ elements.
> - **Optimality proof:** This approach is optimal because it generates the combinations only when the numbers before and after the decimal point are valid. This reduces the number of combinations that need to be generated and checked.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Generating all possible combinations of coordinates and checking their validity.
- Problem-solving patterns identified: Using a brute force approach and then optimizing it to reduce the number of combinations that need to be generated and checked.
- Optimization techniques learned: Generating the combinations only when the numbers before and after the decimal point are valid.
- Similar problems to practice: Generating all possible combinations of a given string, checking the validity of numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the numbers before and after the decimal point are valid.
- Edge cases to watch for: When the string `s` starts with `0` or has a length of 1.
- Performance pitfalls: Generating all possible combinations of coordinates and checking their validity without optimizing the approach.
- Testing considerations: Testing the approach with different input strings to ensure that it generates all possible ambiguous coordinates correctly.