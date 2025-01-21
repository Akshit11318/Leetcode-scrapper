## Numbers With Repeated Digits
**Problem Link:** https://leetcode.com/problems/numbers-with-repeated-digits/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, find the number of integers in the range `[1, n]` that contain **at least one repeated digit**.
- Expected output format: Return the count of such integers.
- Key requirements and edge cases to consider: The input `n` will be within the range `[1, 10^9]`.
- Example test cases with explanations:
  - For `n = 20`, the integers with repeated digits are `[11, 22]`. Hence, the output should be `2`.
  - For `n = 100`, the integers with repeated digits are `[11, 22, 33, 44, 55, 66, 77, 88, 99, 10, 11, 12, ..., 99]`. But for this problem, we also need to consider numbers like `10, 20, 30, ...` as they have a repeated digit when considering leading zeros in a certain digit length.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all integers from `1` to `n`, and for each integer, check if it contains any repeated digit.
- Step-by-step breakdown of the solution:
  1. Loop through each integer `i` from `1` to `n`.
  2. For each `i`, convert it to a string to easily check for repeated digits.
  3. Use a set to keep track of the digits seen so far for the current integer.
  4. If a digit is already in the set, it means we've found a repeated digit, and we increment the count of such integers.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
int numDupDigitsAtMostN(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        set<char> seen;
        bool hasDuplicate = false;
        for (char c : str) {
            if (seen.find(c) != seen.end()) {
                hasDuplicate = true;
                break;
            }
            seen.insert(c);
        }
        if (hasDuplicate) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the input number and $m$ is the average number of digits in the numbers from `1` to `n`. This is because we're iterating over each number up to `n` and for each number, we're checking its digits.
> - **Space Complexity:** $O(m)$ for storing the set of seen digits for each number.
> - **Why these complexities occur:** The time complexity is high because we're checking every single number up to `n`, and the space complexity is relatively low because we're only storing a set of digits for each number, which is bounded by the number of possible digits (10 for decimal system).

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every number up to `n`, we can calculate the number of valid numbers (those without repeated digits) for each length up to the length of `n`, and then subtract this total from `n` to find the numbers with repeated digits.
- Detailed breakdown of the approach:
  1. Calculate the number of valid numbers for each digit length up to the length of `n`.
  2. For each length, consider the first digit can't be zero, so there are 9 choices for the first digit and then (9, 8, 7, ...) choices for subsequent digits because we can't repeat digits.
  3. For the numbers of the same length as `n`, we need to consider numbers starting with each digit less than the first digit of `n`, and then for the numbers starting with the same digit as the first digit of `n`, we calculate the valid numbers based on the subsequent digits.
- Proof of optimality: This approach avoids checking every single number up to `n`, instead using combinatorial principles to directly calculate the count of numbers with repeated digits.

```cpp
int numDupDigitsAtMostN(int n) {
    string str = to_string(n);
    int res = n - (int)str.length() * 9;
    for (int i = 0; i < str.length(); i++) {
        int x = str[i] - '0';
        res += (x - 1) * pow(9, str.length() - i - 1);
        if (i < str.length() - 1) {
            res += pow(9, str.length() - i - 1);
        }
    }
    return res;
}
```

However, the optimal code provided above might seem confusing without the detailed explanation of how we calculate the `res`. We actually use the principle of inclusion-exclusion to find the numbers that do not have repeated digits.

To correctly implement this, let's consider how we calculate the number of valid numbers (without repeated digits) for a given length:

```cpp
int numDupDigitsAtMostN(int n) {
    string str = to_string(n);
    int length = str.length();
    int res = 0;
    
    // Calculate the number of valid numbers for lengths less than the length of n
    for (int i = 1; i < length; i++) {
        res += 9 * pow(9, i - 1); // For the first digit, we have 9 choices, for the rest, we have 9 choices for each
    }
    
    // Calculate the number of valid numbers for the length of n
    int firstDigit = str[0] - '0';
    res += (firstDigit - 1) * pow(9, length - 1); // Numbers starting with digits less than the first digit of n
    
    // Calculate the number of valid numbers starting with the first digit of n
    set<int> seen;
    seen.insert(firstDigit);
    for (int i = 1; i < length; i++) {
        int currentDigit = str[i] - '0';
        int choices = 9;
        if (i == 1) {
            choices = 9; // For the second digit onwards, we can choose from the remaining digits
        } else {
            choices = 10 - i; // But we've already chosen i-1 digits, so we have fewer choices
        }
        res += (currentDigit - (seen.size())) * pow(10 - i, length - i - 1); // Adjust choices based on whether we've seen the digit before
        if (currentDigit > 0 && seen.find(currentDigit) == seen.end()) {
            seen.insert(currentDigit);
        } else {
            break;
        }
    }
    
    return n - res;
}
```

However, the explanation of the optimal approach can be simplified and corrected by directly calculating the numbers without repeated digits and then subtracting that count from `n`.

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ because we're only iterating up to the length of `n`, which is logarithmic in `n`.
> - **Space Complexity:** $O(1)$ as we're using a constant amount of space to store the count and the current number being processed.
> - **Optimality proof:** This is optimal because we're using mathematical calculations to directly compute the result without needing to iterate over every number up to `n`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Combinatorics, principle of inclusion-exclusion.
- Problem-solving patterns identified: Calculating the complement (numbers without repeated digits) to find the desired count.
- Optimization techniques learned: Using mathematical formulas to reduce computational complexity.
- Similar problems to practice: Other combinatorial problems, like counting permutations with certain restrictions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the number of valid numbers for each length.
- Edge cases to watch for: Handling numbers with leading zeros, ensuring correct calculation for numbers of different lengths.
- Performance pitfalls: Iterating over every number up to `n` instead of using combinatorial principles.
- Testing considerations: Ensuring the solution works correctly for the full range of possible inputs, including edge cases like `n = 1` or `n = 10^9`.