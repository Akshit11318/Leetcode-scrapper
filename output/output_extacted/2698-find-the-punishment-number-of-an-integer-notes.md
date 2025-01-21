## Find the Punishment Number of an Integer
**Problem Link:** https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input and requires finding the punishment number of `n`, which is defined as the sum of all numbers `i` in the range `[1, n]` such that the sum of the digits of `i` is equal to `i`.
- Expected output format: The punishment number of `n`.
- Key requirements and edge cases to consider: The input `n` is a positive integer, and the output should be a non-negative integer.
- Example test cases with explanations:
  - For `n = 1`, the punishment number is `1` because the sum of the digits of `1` is `1`.
  - For `n = 10`, the punishment number is `1 + 10 = 11` because the sum of the digits of `1` is `1` and the sum of the digits of `10` is `1 + 0 = 1`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves iterating over all numbers in the range `[1, n]` and checking if the sum of the digits of each number is equal to the number itself.
- Step-by-step breakdown of the solution:
  1. Iterate over all numbers `i` in the range `[1, n]`.
  2. For each number `i`, calculate the sum of its digits.
  3. If the sum of the digits of `i` is equal to `i`, add `i` to the punishment number.
- Why this approach comes to mind first: This approach is straightforward and directly implements the problem definition.

```cpp
int punishmentNumber(int n) {
    int punishment = 0;
    for (int i = 1; i <= n; i++) {
        int sum = 0;
        int num = i;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        if (sum == i) {
            punishment += i;
        }
    }
    return punishment;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the input number. The reason is that we iterate over all numbers up to $n$, and for each number, we calculate the sum of its digits, which takes $O(\log n)$ time because the number of digits in a number is proportional to the logarithm of the number.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the punishment number and other variables.
> - **Why these complexities occur:** The time complexity is due to the iteration over all numbers up to $n$ and the calculation of the sum of digits for each number. The space complexity is low because we do not use any data structures that grow with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, because the problem requires checking all numbers up to $n$ to calculate the punishment number. However, we can optimize the calculation of the sum of digits by using a more efficient algorithm.
- Detailed breakdown of the approach:
  1. Iterate over all numbers `i` in the range `[1, n]`.
  2. For each number `i`, calculate the sum of its digits using a more efficient algorithm, such as using a string representation of the number and iterating over its characters.
  3. If the sum of the digits of `i` is equal to `i`, add `i` to the punishment number.
- Proof of optimality: The optimal solution has the same time complexity as the brute force approach, which is $O(n \log n)$. However, the optimal solution uses a more efficient algorithm to calculate the sum of digits, which can reduce the constant factor in the time complexity.

```cpp
int punishmentNumber(int n) {
    int punishment = 0;
    for (int i = 1; i <= n; i++) {
        int sum = 0;
        string str = to_string(i);
        for (char c : str) {
            sum += c - '0';
        }
        if (sum == i) {
            punishment += i;
        }
    }
    return punishment;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the input number. The reason is that we iterate over all numbers up to $n$, and for each number, we calculate the sum of its digits, which takes $O(\log n)$ time because the number of digits in a number is proportional to the logarithm of the number.
> - **Space Complexity:** $O(\log n)$, because we use a string representation of the number to calculate the sum of its digits, and the length of the string is proportional to the logarithm of the number.
> - **Optimality proof:** The time complexity is optimal because we must check all numbers up to $n$ to calculate the punishment number. The space complexity is also optimal because we only use a small amount of extra space to store the string representation of the number.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, calculation of sum of digits, and conditional addition to the punishment number.
- Problem-solving patterns identified: the problem requires checking all numbers up to $n$ and using a efficient algorithm to calculate the sum of digits.
- Optimization techniques learned: using a more efficient algorithm to calculate the sum of digits can reduce the constant factor in the time complexity.
- Similar problems to practice: problems that require checking all numbers up to a certain limit and using efficient algorithms to calculate properties of numbers.

**Mistakes to Avoid:**
- Common implementation errors: not checking all numbers up to $n$, using an inefficient algorithm to calculate the sum of digits, and not handling edge cases correctly.
- Edge cases to watch for: the input $n$ is a positive integer, and the output should be a non-negative integer.
- Performance pitfalls: using an inefficient algorithm to calculate the sum of digits can increase the time complexity.
- Testing considerations: test the solution with different inputs, including edge cases, to ensure that it produces the correct output.