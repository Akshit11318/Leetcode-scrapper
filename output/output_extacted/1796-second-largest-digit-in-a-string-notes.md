## Second Largest Digit in a String

**Problem Link:** https://leetcode.com/problems/second-largest-digit-in-a-string/description

**Problem Statement:**
- Input format: A string `s` containing digits and non-digit characters.
- Constraints: The length of `s` is between 1 and 1000.
- Expected output format: The second largest digit in the string. If there is no second largest digit, return `-1`.
- Key requirements and edge cases to consider: 
  - Handling strings with no digits or only one unique digit.
  - Ignoring non-digit characters.
  - Dealing with an empty string or a string with only non-digit characters.

**Example Test Cases:**
- Input: `s = "dfa123bf45a"` Output: `4`
- Input: `s = "abc1111"` Output: `-1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the string to find all digits, store them in a list or set, and then sort them to find the second largest.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set to store unique digits.
  2. Iterate through each character in the string.
  3. Check if the character is a digit.
  4. If it's a digit, add it to the set.
  5. After iterating through all characters, check if the set has less than two unique digits. If so, return `-1`.
  6. Otherwise, sort the set in descending order and return the second element (which is the second largest digit).

```cpp
#include <iostream>
#include <set>
#include <string>
using namespace std;

int secondHighest(string s) {
    set<int> digits;
    for (char c : s) {
        if (isdigit(c)) {
            digits.insert(c - '0'); // Convert char to int
        }
    }
    if (digits.size() < 2) return -1;
    auto it = digits.begin();
    it++; // Move to the second element (second largest)
    return *it;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of the set, where $n$ is the number of unique digits found in the string.
> - **Space Complexity:** $O(n)$ for storing the unique digits in the set.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which in the case of a set in C++, is typically a balanced binary search tree, thus the $\log n$ factor. The space complexity is linear with respect to the number of unique digits because each digit is stored in the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting all unique digits, keep track of the maximum and second maximum digits encountered so far.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the maximum and second maximum digits.
  2. Iterate through each character in the string.
  3. If the character is a digit, compare it with the current maximum and second maximum.
  4. Update the maximum and second maximum as necessary.
  5. After iterating through all characters, return the second maximum digit if it exists, otherwise return `-1`.

```cpp
int secondHighest(string s) {
    int maxDigit = -1, secondMax = -1;
    for (char c : s) {
        if (isdigit(c)) {
            int digit = c - '0';
            if (digit > maxDigit) {
                secondMax = maxDigit;
                maxDigit = digit;
            } else if (digit < maxDigit && digit > secondMax) {
                secondMax = digit;
            }
        }
    }
    return secondMax;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the maximum and second maximum digits.
> - **Optimality proof:** This is the optimal solution because we only need to make one pass through the string to find the second largest digit, and we use a constant amount of space, making it both time and space efficient.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and variable updates.
- Problem-solving patterns identified: Keeping track of maximum and second maximum values.
- Optimization techniques learned: Avoiding unnecessary sorting and using constant space.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables, incorrect conditional checks.
- Edge cases to watch for: Strings with no digits, strings with only one unique digit.
- Performance pitfalls: Using inefficient data structures or algorithms.
- Testing considerations: Test with various inputs, including edge cases and large inputs.