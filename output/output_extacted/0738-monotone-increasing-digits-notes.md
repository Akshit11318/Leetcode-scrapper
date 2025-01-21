## Monotone Increasing Digits
**Problem Link:** https://leetcode.com/problems/monotone-increasing-digits/description

**Problem Statement:**
- Input format and constraints: The input is a non-negative integer `N`.
- Expected output format: The output should be the largest number that is less than or equal to `N` and has monotone increasing digits.
- Key requirements and edge cases to consider: The number should be non-negative and have monotone increasing digits.
- Example test cases with explanations: 
  - Input: `N = 10`, Output: `9` (Explanation: The largest number less than or equal to 10 with monotone increasing digits is 9).
  - Input: `N = 1234`, Output: `1234` (Explanation: The number 1234 already has monotone increasing digits).
  - Input: `N = 332`, Output: `299` (Explanation: The largest number less than or equal to 332 with monotone increasing digits is 299).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by checking all numbers less than or equal to `N` and checking if they have monotone increasing digits.
- Step-by-step breakdown of the solution:
  1. Iterate over all numbers from `N` down to 0.
  2. For each number, convert it to a string to easily access each digit.
  3. Check if the digits are monotone increasing by comparing each digit with the next one.
  4. If a number with monotone increasing digits is found, return it immediately.
- Why this approach comes to mind first: It's a straightforward approach that checks all possible numbers, but it's not efficient for large inputs.

```cpp
class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        for (int i = N; i >= 0; i--) {
            if (isMonotoneIncreasing(i)) {
                return i;
            }
        }
        return 0;
    }
    
    bool isMonotoneIncreasing(int num) {
        string str = to_string(num);
        for (int i = 0; i < str.size() - 1; i++) {
            if (str[i] > str[i + 1]) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \times logN)$, where $N$ is the input number. The reason is that we iterate over all numbers from `N` down to 0, and for each number, we convert it to a string and check if it's monotone increasing, which takes $O(logN)$ time.
> - **Space Complexity:** $O(logN)$, where $N$ is the input number. The reason is that we convert each number to a string, which takes $O(logN)$ space.
> - **Why these complexities occur:** These complexities occur because we're checking all possible numbers and converting each number to a string, which takes time and space proportional to the number of digits in the number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all numbers, we can construct the largest number with monotone increasing digits that is less than or equal to `N`.
- Detailed breakdown of the approach:
  1. Convert `N` to a string to easily access each digit.
  2. Initialize an empty string `result` to store the result.
  3. Iterate over each digit in `N`.
  4. For each digit, find the largest digit that is less than or equal to the current digit and can be appended to `result` without violating the monotone increasing property.
  5. Append the found digit to `result`.
- Proof of optimality: This approach is optimal because it constructs the largest number with monotone increasing digits that is less than or equal to `N` in a single pass.

```cpp
class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        string str = to_string(N);
        string result = "";
        for (int i = 0; i < str.size(); i++) {
            int maxDigit = str[i] - '0';
            for (int j = maxDigit; j >= 0; j--) {
                string temp = result + to_string(j);
                if (isValid(temp, str, i + 1)) {
                    result += to_string(j);
                    break;
                }
            }
        }
        return stoi(result);
    }
    
    bool isValid(string temp, string str, int index) {
        for (int i = index; i < str.size(); i++) {
            if (str[i] - '0' < 9) {
                return true;
            }
        }
        return temp.size() + (str.size() - index) <= str.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(logN)$, where $N$ is the input number. The reason is that we iterate over each digit in `N` and perform a constant amount of work for each digit.
> - **Space Complexity:** $O(logN)$, where $N` is the input number. The reason is that we convert `N` to a string and store the result as a string, which takes $O(logN)$ space.
> - **Optimality proof:** This approach is optimal because it constructs the largest number with monotone increasing digits that is less than or equal to `N` in a single pass, without checking all possible numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, string manipulation.
- Problem-solving patterns identified: Constructing the optimal solution by iterating over the input and making greedy choices.
- Optimization techniques learned: Avoiding unnecessary work by constructing the optimal solution directly.
- Similar problems to practice: Other problems that involve constructing the optimal solution by iterating over the input and making greedy choices.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not checking for invalid input.
- Edge cases to watch for: Handling numbers with leading zeros, handling numbers with all digits being the same.
- Performance pitfalls: Checking all possible numbers instead of constructing the optimal solution directly.
- Testing considerations: Testing with different inputs, including edge cases and large inputs.