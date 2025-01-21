## Check if the Number is Fascinating
**Problem Link:** [https://leetcode.com/problems/check-if-the-number-is-fascinating/description](https://leetcode.com/problems/check-if-the-number-is-fascinating/description)

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `1 <= n <= 2^31 - 1`.
- Expected output: Return `true` if `n` is a fascinating number, otherwise return `false`.
- Key requirements and edge cases to consider: A fascinating number is a number that, when concatenated with its multiples (`2n`, `3n`), contains all digits from 1 to 9 at least once.

### Example Test Cases:
- Input: `n = 192`
Output: `true`
Explanation: Concatenating `n`, `2n`, and `3n` results in `192192576`, which contains all digits from 1 to 9 at least once.

- Input: `n = 1`
Output: `false`
Explanation: Concatenating `n`, `2n`, and `3n` results in `123`, which does not contain all digits from 1 to 9.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking all possible numbers and their multiples to see if they contain all digits from 1 to 9.
- Step-by-step breakdown:
  1. Convert the input number and its multiples to strings.
  2. Concatenate these strings.
  3. Check if the concatenated string contains all digits from 1 to 9.

```cpp
class Solution {
public:
    bool isFascinating(int n) {
        string concat = to_string(n) + to_string(2 * n) + to_string(3 * n);
        bool seen[10] = {false};
        for (char c : concat) {
            int digit = c - '0';
            if (digit >= 1 && digit <= 9) {
                seen[digit] = true;
            }
        }
        for (int i = 1; i <= 9; i++) {
            if (!seen[i]) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, as converting a number to a string takes time proportional to the number of digits in the number, which is $log(n)$ for base 10.
> - **Space Complexity:** $O(log(n))$, as we need to store the concatenated string.
> - **Why these complexities occur:** The time complexity is due to the string operations, and the space complexity is due to storing the concatenated string.

---

### Optimal Approach (Required)
The brute force approach is already quite efficient for this problem and can be considered optimal. However, we can slightly optimize the code for better readability and maintainability.

```cpp
class Solution {
public:
    bool isFascinating(int n) {
        string concat = to_string(n) + to_string(2 * n) + to_string(3 * n);
        unordered_set<char> seen;
        for (char c : concat) {
            if (c >= '1' && c <= '9') {
                seen.insert(c);
            }
        }
        return seen.size() == 9;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, as converting a number to a string and iterating over the characters takes time proportional to the number of digits in the number.
> - **Space Complexity:** $O(log(n))$, as we need to store the unique characters in the set.
> - **Optimality proof:** This approach is optimal because we must at least read the input and its multiples, which already takes $O(log(n))$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, set operations.
- Problem-solving patterns identified: checking for the presence of all digits in a concatenated string.
- Optimization techniques learned: using `unordered_set` for efficient lookup of unique characters.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the presence of all digits from 1 to 9.
- Edge cases to watch for: numbers that do not contain all digits from 1 to 9 when concatenated with their multiples.
- Performance pitfalls: using inefficient data structures or algorithms for string manipulation.
- Testing considerations: testing with a variety of inputs, including edge cases.