## Nth Digit
**Problem Link:** https://leetcode.com/problems/nth-digit/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, find the `n`th digit of the infinite sequence `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...`.
- Expected output format: The `n`th digit of the sequence.
- Key requirements and edge cases to consider: The sequence is infinite, and `n` can be any positive integer. We need to consider the case where `n` falls within a number that has multiple digits.
- Example test cases with explanations: 
    - For `n = 3`, the sequence starts as `1, 2, 3`, so the `3`rd digit is `3`.
    - For `n = 11`, the sequence starts as `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11`, so the `11`th digit is `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate the sequence up to the `n`th digit and return the `n`th digit.
- Step-by-step breakdown of the solution: 
    1. Initialize an empty string to store the sequence.
    2. Initialize a counter `i` to `1`.
    3. While the length of the sequence is less than `n`, append the string representation of `i` to the sequence and increment `i`.
    4. Return the `n`th character of the sequence.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, as it directly generates the sequence and returns the desired digit.

```cpp
string findNthDigit(int n) {
    string sequence = "";
    int i = 1;
    while (sequence.length() < n) {
        sequence += to_string(i);
        i++;
    }
    return sequence.substr(n-1, 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because in the worst case, we need to generate the entire sequence up to the `n`th digit.
> - **Space Complexity:** $O(n)$, because we store the entire sequence in memory.
> - **Why these complexities occur:** The brute force approach requires generating the entire sequence, which leads to linear time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the `n`th digit without generating the entire sequence. We can do this by considering the number of digits in each range of numbers (1-9, 10-99, 100-999, etc.).
- Detailed breakdown of the approach: 
    1. Calculate the number of digits in each range until we find the range that contains the `n`th digit.
    2. Determine which number in the range contains the `n`th digit.
    3. Determine which digit of the number is the `n`th digit.
- Proof of optimality: This approach is optimal because it only requires calculating the number of digits in each range and determining which number and digit contain the `n`th digit, resulting in a logarithmic time complexity.

```cpp
string findNthDigit(int n) {
    int length = 1;
    long long count = 9;
    int start = 1;
    while (n > length * count) {
        n -= length * count;
        length++;
        count *= 10;
        start *= 10;
    }
    start += (n - 1) / length;
    string s = to_string(start);
    return string(1, s[(n - 1) % length]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, because we only need to calculate the number of digits in each range until we find the range that contains the `n`th digit.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it has a logarithmic time complexity, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The optimal approach demonstrates the concept of calculating the `n`th digit without generating the entire sequence.
- Problem-solving patterns identified: The problem requires breaking down the sequence into ranges and calculating the number of digits in each range.
- Optimization techniques learned: The optimal approach uses a logarithmic time complexity, which is a significant improvement over the brute force approach.
- Similar problems to practice: Other problems that involve calculating the `n`th term of a sequence or finding a specific digit in a sequence.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the case where `n` falls within a number that has multiple digits.
- Edge cases to watch for: The case where `n` is 1, and the case where `n` is a large number that requires calculating the number of digits in many ranges.
- Performance pitfalls: Using the brute force approach for large values of `n`, which can result in a significant performance degradation.
- Testing considerations: Testing the function with a variety of inputs, including small and large values of `n`, to ensure that it works correctly in all cases.