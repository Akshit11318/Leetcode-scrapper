## Count Numbers with Unique Digits
**Problem Link:** https://leetcode.com/problems/count-numbers-with-unique-digits/description

**Problem Statement:**
- Input: An integer `n` representing the maximum number of digits.
- Output: The count of numbers with unique digits.
- Key requirements: The numbers should have unique digits, and the count should be calculated up to `n` digits.
- Example test cases:
  - Input: `n = 2`
  - Output: `91`
  - Explanation: The numbers with unique digits up to 2 digits are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all numbers up to `n` digits and check each number for unique digits.
- Step-by-step breakdown:
  1. Generate all numbers up to `n` digits.
  2. For each number, check if all digits are unique.
  3. Count the numbers with unique digits.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int count = 0;
        for (int i = 0; i <= pow(10, n) - 1; i++) {
            if (hasUniqueDigits(i)) {
                count++;
            }
        }
        return count;
    }
    
    bool hasUniqueDigits(int num) {
        unordered_set<int> digits;
        while (num > 0) {
            int digit = num % 10;
            if (digits.find(digit) != digits.end()) {
                return false;
            }
            digits.insert(digit);
            num /= 10;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^n \cdot n)$, where $n$ is the input number. The reason is that we generate all numbers up to `n` digits, and for each number, we check its digits.
> - **Space Complexity:** $O(n)$, as we use a set to store the digits of each number.
> - **Why these complexities occur:** The time complexity occurs because we generate all numbers up to `n` digits and check each number's digits. The space complexity occurs because we use a set to store the digits of each number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a mathematical approach to calculate the count of numbers with unique digits.
- Detailed breakdown:
  1. For the first digit, we have 9 choices (1-9) because 0 cannot be the first digit.
  2. For the second digit, we have 9 choices (0-9 excluding the first digit).
  3. For the third digit, we have 8 choices (0-9 excluding the first two digits).
  4. We continue this process until we reach `n` digits.
  5. We calculate the count of numbers with unique digits for each number of digits from 1 to `n`.
- Proof of optimality: This approach is optimal because it directly calculates the count of numbers with unique digits without generating all numbers.

```cpp
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        if (n == 1) return 10;
        
        int count = 10;
        int uniqueDigits = 9;
        int availableDigits = 9;
        
        for (int i = 2; i <= n && availableDigits > 0; i++) {
            uniqueDigits *= availableDigits;
            count += uniqueDigits;
            availableDigits--;
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number. The reason is that we calculate the count of numbers with unique digits for each number of digits from 1 to `n`.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it directly calculates the count of numbers with unique digits without generating all numbers, resulting in a significant reduction in time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Using a mathematical approach to calculate the count of numbers with unique digits.
- Problem-solving pattern: Breaking down the problem into smaller sub-problems and solving each sub-problem recursively.
- Optimization technique: Reducing the time complexity by avoiding the generation of all numbers and instead calculating the count directly.

**Mistakes to Avoid:**
- Common implementation error: Not handling the edge case where `n` is 0 or 1.
- Performance pitfall: Generating all numbers up to `n` digits, resulting in a high time complexity.
- Testing consideration: Testing the function with different values of `n` to ensure it returns the correct count.