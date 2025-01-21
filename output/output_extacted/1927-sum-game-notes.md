## Sum Game

**Problem Link:** https://leetcode.com/problems/sum-game/description

**Problem Statement:**
- Input: A string `num` consisting of digits.
- Constraints: `1 <= num.length <= 10^4`, `num` consists of digits.
- Expected output: Return the difference between the sum of the numbers on the left side of the `|` and the sum of the numbers on the right side.
- Key requirements: The input string can be split into two parts at any index.
- Edge cases: The input string may contain only one digit.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible splits of the input string and calculate the difference between the sums of the two parts for each split.
- Step-by-step breakdown:
  1. Iterate over each possible split index in the input string.
  2. For each split, calculate the sum of the numbers on the left and right sides.
  3. Calculate the difference between the sums of the two parts for each split.
  4. Return the maximum difference found.

```cpp
int sumGame(string num) {
    int n = num.size();
    int maxDiff = 0;
    for (int i = 0; i < n; i++) {
        int leftSum = 0, rightSum = 0;
        for (int j = 0; j < i; j++) {
            leftSum += num[j] - '0';
        }
        for (int j = i; j < n; j++) {
            rightSum += num[j] - '0';
        }
        maxDiff = max(maxDiff, abs(leftSum - rightSum));
    }
    return maxDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string, because we iterate over each character in the string and for each character, we iterate over the characters on the left and right sides.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the sums and the maximum difference.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, and the constant space usage is because we only need a few variables to store the sums and the maximum difference.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can calculate the sum of the numbers on the left and right sides in a single pass, without needing to iterate over the characters multiple times.
- Detailed breakdown:
  1. Initialize variables to store the sum of the numbers on the left and right sides.
  2. Iterate over the input string from left to right.
  3. For each character, add its value to the sum of the numbers on the left side if we are on the left side of the split, or add its value to the sum of the numbers on the right side if we are on the right side of the split.
  4. Calculate the difference between the sums of the two parts for each split.
  5. Return the maximum difference found.

```cpp
int sumGame(string num) {
    int n = num.size();
    int result = 0;
    int rightSum = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (i < n / 2) {
            rightSum += (num[i] == '0') ? 0 : (num[i] - '0' - 9);
        } else {
            result += num[i] - '0';
        }
    }
    return result + rightSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we only need to iterate over the characters once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the sums and the result.
> - **Optimality proof:** This is the optimal solution because we only need to iterate over the characters once, and we use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Iteration, sum calculation, and difference calculation.
- Problem-solving patterns: Single-pass iteration and constant space usage.
- Optimization techniques: Avoiding nested loops and using a single pass to calculate sums.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input string.
- Edge cases to watch for: Input strings with only one digit.
- Performance pitfalls: Using nested loops, which can lead to quadratic time complexity.
- Testing considerations: Test with input strings of varying lengths and containing different digits.