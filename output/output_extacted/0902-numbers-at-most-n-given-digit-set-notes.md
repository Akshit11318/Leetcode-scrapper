## Numbers at Most N Given Digit Set
**Problem Link:** https://leetcode.com/problems/numbers-at-most-n-given-digit-set/description

**Problem Statement:**
- Input format and constraints: The problem takes in an array of digits and a number `n`. The array of digits represents the allowed digits to form numbers, and `n` is the upper limit of the numbers we are counting.
- Expected output format: The function should return the number of integers that can be formed using the digits in the array that are less than or equal to `n`.
- Key requirements and edge cases to consider: We need to consider the cases where the number `n` has more digits than the allowed digits, and the cases where the digits in `n` are not in the allowed digits.
- Example test cases with explanations: For example, if the allowed digits are `[1, 3, 5, 7]` and `n` is `100`, we need to count all numbers that can be formed using the digits `[1, 3, 5, 7]` and are less than or equal to `100`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible numbers using the allowed digits and count the numbers that are less than or equal to `n`.
- Step-by-step breakdown of the solution:
  1. Generate all possible numbers using the allowed digits.
  2. Check each generated number to see if it is less than or equal to `n`.
  3. Count the numbers that meet the condition.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs because it generates all possible numbers.

```cpp
int atMostNGivenDigitSet(vector<string>& digits, int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        string num = to_string(i);
        bool isValid = true;
        for (char c : num) {
            bool found = false;
            for (string d : digits) {
                if (d == string(1, c)) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the input number, $m$ is the number of digits in the input number, and $k$ is the number of allowed digits. This is because we are iterating over all numbers up to $n$, and for each number, we are checking each digit against the allowed digits.
> - **Space Complexity:** $O(1)$, because we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** These complexities occur because we are generating all possible numbers up to $n$ and checking each digit of each number against the allowed digits.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible numbers, we can use a dynamic programming approach to count the numbers that can be formed using the allowed digits.
- Detailed breakdown of the approach:
  1. Calculate the number of possible numbers for each length up to the length of `n`.
  2. For each length, calculate the number of possible numbers that can be formed using the allowed digits.
  3. Add up the counts for each length to get the total count.
- Proof of optimality: This approach is optimal because it only considers the numbers that can be formed using the allowed digits and does not generate any unnecessary numbers.

```cpp
int atMostNGivenDigitSet(vector<string>& digits, int n) {
    string str = to_string(n);
    int k = digits.size();
    vector<int> dp(str.size() + 1);
    dp[0] = 1;
    for (int i = 1; i <= str.size(); i++) {
        for (string d : digits) {
            if (d <= str.substr(i - 1, 1)) {
                dp[i] += dp[i - 1];
            }
        }
    }
    for (int i = 1; i < str.size(); i++) {
        dp[i] += dp[i - 1] * (k - 1);
    }
    return dp[str.size()] - 1 + (find(digits.begin(), digits.end(), to_string(n)) != digits.end());
}
```

However, the above solution can be simplified by using the concept of combinatorics.

```cpp
int atMostNGivenDigitSet(vector<string>& digits, int n) {
    string str = to_string(n);
    int k = digits.size();
    int res = 0;
    for (int i = 1; i < str.size(); i++) {
        res += pow(k, i);
    }
    int i = 0;
    while (i < str.size()) {
        bool found = false;
        for (string d : digits) {
            if (d <= str.substr(i, 1)) {
                res += (d < str.substr(i, 1)) * pow(k, str.size() - i - 1);
                if (d == str.substr(i, 1)) {
                    i++;
                    found = true;
                    break;
                }
            }
        }
        if (!found) break;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot k)$, where $m$ is the number of digits in the input number and $k$ is the number of allowed digits. This is because we are iterating over each digit of the input number and checking each allowed digit.
> - **Space Complexity:** $O(1)$, because we are not using any extra space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it only considers the numbers that can be formed using the allowed digits and does not generate any unnecessary numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, combinatorics.
- Problem-solving patterns identified: counting problems, digit manipulation.
- Optimization techniques learned: avoiding unnecessary computation, using mathematical formulas.
- Similar problems to practice: counting problems, digit manipulation problems.

**Mistakes to Avoid:**
- Common implementation errors: off-by-one errors, incorrect indexing.
- Edge cases to watch for: empty input, invalid input.
- Performance pitfalls: generating unnecessary numbers, using inefficient algorithms.
- Testing considerations: testing with different input sizes, testing with edge cases.