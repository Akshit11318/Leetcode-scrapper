## Number of Digit One

**Problem Link:** https://leetcode.com/problems/number-of-digit-one/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `1 <= n <= 10^9`.
- Expected output: The number of times digit 1 appears in the integers from 1 to `n`.
- Key requirements: Count the occurrences of digit 1 in all numbers up to `n`.
- Example test cases:
  - Input: `n = 13`
  - Output: `6` (1 appears in 1, 10, 11, 12, 13, and there are other numbers with 1 in them)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over all numbers from 1 to `n` and count the occurrences of digit 1 in each number.
- Step-by-step breakdown:
  1. Iterate over all numbers from 1 to `n`.
  2. Convert each number to a string to easily access each digit.
  3. Iterate over each character (digit) in the string.
  4. If the character is '1', increment the count.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, but it's not efficient for large inputs.

```cpp
int countDigitOne(int n) {
    int count = 0;
    for (int i = 1; i <= n; ++i) {
        string str = to_string(i);
        for (char c : str) {
            if (c == '1') {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(n))$ where $n$ is the input number. The reason is we iterate over all numbers up to $n$, and for each number, we iterate over its digits, which is proportional to $log(n)$.
> - **Space Complexity:** $O(log(n))$ for storing the string representation of each number.
> - **Why these complexities occur:** The brute force approach involves iterating over all numbers and their digits, leading to the $O(n \cdot log(n))$ time complexity. The space complexity is due to the need to store the string representation of each number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of counting the occurrences of digit 1 in each number, we can calculate the number of times digit 1 appears in each place value (ones, tens, hundreds, etc.) up to `n`.
- Detailed breakdown:
  1. For each place value (starting from the ones place), calculate how many times digit 1 appears in that place.
  2. To do this, consider the numbers from 1 to `n` and how they contribute to the count for each place value.
  3. For the ones place, every 10 numbers contribute 1 occurrence of digit 1 (in the numbers 1, 11, 21, ...).
  4. Generalize this logic for tens, hundreds, etc., places.
- Proof of optimality: This approach avoids the need to iterate over all numbers, reducing the time complexity significantly.

```cpp
int countDigitOne(int n) {
    int count = 0;
    long long i = 1;
    while (i <= n) {
        long long divider = i * 10;
        count += (n / divider) * i + min(max(n % divider - i + 1, 0LL), i);
        i *= 10;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ because we iterate over each place value (ones, tens, hundreds, etc.), which is proportional to the number of digits in `n`.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space.
> - **Optimality proof:** The optimal approach has a time complexity of $O(log(n))$ because it only needs to consider each place value once, making it much more efficient than the brute force approach for large inputs.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the ability to think about the problem at a higher level, focusing on patterns and place values rather than individual numbers.
- Problem-solving patterns identified include breaking down complex problems into simpler, more manageable parts (in this case, considering each place value separately).
- Optimization techniques learned include avoiding unnecessary iterations and using mathematical insights to calculate results directly.

**Mistakes to Avoid:**
- Common implementation errors include off-by-one errors when calculating the occurrences of digit 1 in each place value.
- Edge cases to watch for include handling the case when `n` is 0 or a negative number (though the problem statement specifies `n` is positive).
- Performance pitfalls include using the brute force approach for large inputs, which can lead to very slow execution times.