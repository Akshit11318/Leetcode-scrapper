## Strobogrammatic Number III
**Problem Link:** https://leetcode.com/problems/strobogrammatic-number-iii/description

**Problem Statement:**
- Input format: A string `low` and a string `high` where `low` and `high` are both non-empty and consist only of digits.
- Constraints: $1 \leq low.length \leq high.length \leq 4$, $low$ and $high` are both valid numbers, and $low$ is less than or equal to $high`.
- Expected output format: The number of strobogrammatic numbers in the range `[low, high]`.
- Key requirements and edge cases to consider: A strobogrammatic number is a number whose numeral is rotationally symmetric, so it appears the same when its digits are rotated by 180 degrees. We need to count all such numbers within the given range.
- Example test cases with explanations:
  - Example 1: Input: `low = "50", high = "100"`. Output: `3`. Explanation: The strobogrammatic numbers in the range are `69`, `88`, and `96`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible numbers within the range and check each one to see if it's strobogrammatic.
- Step-by-step breakdown of the solution:
  1. Generate all numbers from `low` to `high`.
  2. For each number, check if it's strobogrammatic.
  3. Count all strobogrammatic numbers.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
#include <iostream>
#include <string>

bool isStrobogrammatic(const std::string& num) {
    std::string rotated = "";
    for (int i = num.size() - 1; i >= 0; --i) {
        char c = num[i];
        if (c == '0') rotated += '0';
        else if (c == '1') rotated += '1';
        else if (c == '6') rotated += '9';
        else if (c == '8') rotated += '8';
        else if (c == '9') rotated += '6';
        else return false; // If any digit is not strobogrammatic, return false
    }
    return num == rotated; // Check if original number equals its rotation
}

int strobogrammaticInRange(const std::string& low, const std::string& high) {
    int count = 0;
    for (long long num = std::stoll(low); num <= std::stoll(high); ++num) {
        std::string numStr = std::to_string(num);
        if (isStrobogrammatic(numStr)) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of integers in the range $[low, high]$ and $m$ is the average number of digits in these integers. The reason is we're generating each number and checking if it's strobogrammatic, which involves string manipulation.
> - **Space Complexity:** $O(m)$ for storing the string representation of each number and its rotation. 
> - **Why these complexities occur:** The brute force approach involves iterating over all numbers in the range and performing a strobogrammatic check on each, leading to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every number in the range, generate only strobogrammatic numbers of the appropriate length and check if they fall within the range.
- Detailed breakdown of the approach:
  1. Determine the lengths of `low` and `high`.
  2. For each length from `low.length()` to `high.length()`, generate all possible strobogrammatic numbers.
  3. For each generated strobogrammatic number, check if it falls within the range `[low, high]`.
  4. Count all strobogrammatic numbers within the range.

```cpp
#include <iostream>
#include <string>

void generateStrobogrammatic(std::string& current, int length, int pos, std::string& low, std::string& high, int& count) {
    if (pos == length) {
        if (length == low.size() && current < low) return;
        if (length == high.size() && current > high) return;
        count++;
        return;
    }

    if (pos == 0) {
        if (length == 1) {
            current += '0';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
            current += '1';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
            current += '8';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
        } else {
            current += '0';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
            current += '1';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
            current += '8';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
        }
    } else {
        if (pos == length - 1) {
            if (current[0] == '0') {
                current += '0';
                generateStrobogrammatic(current, length, pos + 1, low, high, count);
                current.pop_back();
            } else if (current[0] == '1') {
                current += '1';
                generateStrobogrammatic(current, length, pos + 1, low, high, count);
                current.pop_back();
            } else if (current[0] == '6') {
                current += '9';
                generateStrobogrammatic(current, length, pos + 1, low, high, count);
                current.pop_back();
            } else if (current[0] == '8') {
                current += '8';
                generateStrobogrammatic(current, length, pos + 1, low, high, count);
                current.pop_back();
            } else if (current[0] == '9') {
                current += '6';
                generateStrobogrammatic(current, length, pos + 1, low, high, count);
                current.pop_back();
            }
        } else {
            current += '0';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
            current += '1';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
            current += '6';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
            current += '8';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
            current += '9';
            generateStrobogrammatic(current, length, pos + 1, low, high, count);
            current.pop_back();
        }
    }
}

int strobogrammaticInRange(const std::string& low, const std::string& high) {
    int count = 0;
    for (int length = low.size(); length <= high.size(); length++) {
        std::string current = "";
        generateStrobogrammatic(current, length, 0, low, high, count);
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(5^{\frac{n}{2}})$ where $n$ is the number of digits in the larger number (`high`). This is because for each digit position (except the middle one for odd lengths), we have up to 5 choices (0, 1, 6, 8, 9) that can be mirrored.
> - **Space Complexity:** $O(n)$ for the recursion stack and storing the current number being generated.
> - **Optimality proof:** This approach is optimal because it directly generates only the strobogrammatic numbers, avoiding the need to check every number in the range. It also prunes branches that would result in numbers outside the specified range, further optimizing the process.