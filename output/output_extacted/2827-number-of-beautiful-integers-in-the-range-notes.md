## Number of Beautiful Integers in the Range

**Problem Link:** https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/description

**Problem Statement:**
- Given an integer `n`, find the number of beautiful integers in the range `[1, n]`.
- A beautiful integer is an integer whose digits are all the same, for example, `111`, `222`, etc.
- The input is an integer `n`, and the output should be the count of beautiful integers in the range `[1, n]`.
- Key requirements and edge cases to consider: handle cases where `n` is less than 10, and cases where `n` is greater than or equal to 10.

**Example Test Cases:**
- Input: `n = 10`
  Output: `9`
  Explanation: The beautiful integers in the range `[1, 10]` are `[1, 2, 3, 4, 5, 6, 7, 8, 9]`.
- Input: `n = 100`
  Output: `18`
  Explanation: The beautiful integers in the range `[1, 100]` are `[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through all integers in the range `[1, n]` and check if each integer is beautiful.
- We can convert each integer to a string and check if all characters are the same.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
int beautifulIntegers(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        bool isBeautiful = true;
        for (int j = 1; j < str.size(); j++) {
            if (str[j] != str[0]) {
                isBeautiful = false;
                break;
            }
        }
        if (isBeautiful) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \log n)$, where $n$ is the input integer. The outer loop runs in $O(n)$ time, and the inner loop runs in $O(\log n)$ time because the maximum number of digits in an integer is $\log n$.
> - **Space Complexity:** $O(\log n)$, because we need to convert each integer to a string, which takes $O(\log n)$ space.
> - **Why these complexities occur:** The time complexity is high because we are iterating through all integers in the range `[1, n]`, and the space complexity is moderate because we need to store the string representation of each integer.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to generate all beautiful integers instead of checking each integer.
- We can generate all beautiful integers by iterating through all possible digits and creating integers with the same digit repeated.
- This approach is optimal because it avoids unnecessary iterations and directly generates the beautiful integers.

```cpp
int beautifulIntegers(int n) {
    int count = 0;
    for (int digit = 1; digit <= 9; digit++) {
        for (int numDigits = 1; numDigits <= 10; numDigits++) {
            int beautifulInt = 0;
            for (int i = 0; i < numDigits; i++) {
                beautifulInt = beautifulInt * 10 + digit;
            }
            if (beautifulInt <= n) {
                count++;
            } else {
                break;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input integer. The outer loop runs in $O(1)$ time, and the middle loop runs in $O(\log n)$ time because the maximum number of digits in a beautiful integer is $\log n$.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the beautiful integers.
> - **Optimality proof:** This solution is optimal because it generates all beautiful integers in the range `[1, n]` with the minimum number of iterations, avoiding unnecessary checks and iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, string manipulation, and beautiful integer generation.
- Problem-solving patterns identified: generating solutions instead of checking each possibility.
- Optimization techniques learned: avoiding unnecessary iterations and using optimal data structures.

**Mistakes to Avoid:**
- Common implementation errors: incorrect loop conditions, missing edge cases, and inefficient string manipulation.
- Edge cases to watch for: handling cases where `n` is less than 10, and cases where `n` is greater than or equal to 10.
- Performance pitfalls: using inefficient algorithms or data structures, and not optimizing the solution for the given constraints.