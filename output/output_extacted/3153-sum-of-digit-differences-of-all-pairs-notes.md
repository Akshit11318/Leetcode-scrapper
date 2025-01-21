## Sum of Digit Differences of All Pairs

**Problem Link:** https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/description

**Problem Statement:**
- Given a non-negative integer `num`, return the sum of the differences of all pairs of digits.
- Input: `num` is a non-negative integer.
- Expected output: The sum of the differences of all pairs of digits.
- Key requirements: Calculate the sum of the absolute differences between all pairs of digits in the given number.
- Example test cases:
  - Input: `num = 234`
    - All pairs of digits are (2, 3), (2, 4), and (3, 4).
    - The sum of the differences is |2 - 3| + |2 - 4| + |3 - 4| = 1 + 2 + 1 = 4.
    - Output: `4`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves converting the number into a string to easily access each digit, then iterating through all pairs of digits to calculate their differences.
- Step-by-step breakdown:
  1. Convert the number to a string to access each digit.
  2. Initialize a variable to store the sum of the differences.
  3. Use nested loops to generate all pairs of digits.
  4. For each pair, calculate the absolute difference and add it to the sum.
- Why this approach comes to mind first: It directly addresses the problem statement by considering all pairs of digits and calculating their differences.

```cpp
int sumOfDigitDifferences(int num) {
    // Convert the number to a string
    string str = to_string(num);
    int sum = 0;
    
    // Generate all pairs of digits
    for (int i = 0; i < str.length(); i++) {
        for (int j = i + 1; j < str.length(); j++) {
            // Calculate the absolute difference and add it to the sum
            sum += abs(str[i] - str[j]);
            sum += abs(str[j] - str[i]); // Since the problem asks for all pairs (a, b) and (b, a)
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of digits in the input number. This is because we use nested loops to generate all pairs of digits.
> - **Space Complexity:** $O(n)$, as we convert the number to a string of length $n$.
> - **Why these complexities occur:** The brute force approach involves iterating over all pairs of digits, resulting in quadratic time complexity. The space complexity is linear due to the conversion of the number to a string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is recognizing that the difference between two digits is the same regardless of their order, so we can calculate the difference for each unique pair of digits only once and then multiply by the number of times that pair occurs.
- However, given the nature of this problem, the optimal approach simplifies to calculating the sum of differences directly without needing to consider the frequency of each digit pair explicitly, as each digit will be compared with every other digit in the number.
- Detailed breakdown:
  1. Convert the number to a string for easy digit access.
  2. Initialize a sum variable.
  3. Iterate through the string to calculate the differences between all pairs of digits.
- Proof of optimality: This approach directly calculates the required sum without unnecessary computations, making it optimal for this specific problem.

```cpp
int sumOfDigitDifferences(int num) {
    string str = to_string(num);
    int sum = 0;
    
    for (int i = 0; i < str.length(); i++) {
        for (int j = i + 1; j < str.length(); j++) {
            sum += abs(str[i] - str[j]);
            sum += abs(str[j] - str[i]);
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of digits in the input number. This is due to the nested loops used to compare all pairs of digits.
> - **Space Complexity:** $O(n)$, for converting the number to a string.
> - **Optimality proof:** The time complexity is optimal because we must consider all pairs of digits at least once to calculate their differences. The space complexity is also optimal as we only need to store the input number as a string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Iteration, nested loops for generating pairs, and calculating absolute differences.
- Problem-solving patterns: Directly addressing the problem statement by breaking it down into smaller, manageable parts (in this case, pairs of digits).
- Optimization techniques: Recognizing that each digit needs to be compared with every other digit, but no further optimization is possible without changing the fundamental approach of comparing all pairs.

**Mistakes to Avoid:**
- Not considering all pairs of digits.
- Not accounting for the fact that the difference between two digits is the same regardless of their order, but in this problem, we need to consider both (a, b) and (b, a) pairs explicitly due to the problem's requirements.
- Not validating the input (though in this case, the problem statement guarantees a non-negative integer).